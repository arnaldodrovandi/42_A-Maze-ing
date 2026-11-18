Here is a complete comparison of the 5 algorithms you researched, plus **1 additional important algorithm (Hunt-and-Kill)**, evaluated specifically against the requirements of **A-Maze-ing** (where $V = \text{WIDTH} \times \text{HEIGHT}$ is the total number of cells in the grid).

---

### 1. Side-by-Side Comparison Table

| Algorithm | 1. Number of Dead Ends | 2. Length of Solution Path | 3. Time Complexity (Big-O) | 4. Programming Complexity | 5. Fit with `A-Maze-ing` (especially the `"42"` obstacle!) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Randomized DFS (Recursive / Iterative Backtracker)** | **Low** (~10% of cells). Creates long corridors with few branches. | **Very Long** & winding. High "river" factor. | **$O(V)$** (Visits each cell & edge a constant number of times) | **Easy** (~25 lines using a `while stack:` loop) | **Excellent (10/10).** Naturally routes around the closed `"42"` cells just by marking them as already visited. |
| **2. Randomized Kruskal’s** | **High** (~30% of cells). Lots of short, stubby branches. | **Medium / Short.** More direct paths. | **$O(V \log V)$** or **$O(V \alpha(V))$** (Sorting edges + Union-Find) | **Medium** (Requires a Disjoint-Set / Union-Find structure) | **Very Good (8.5/10).** Easy to exclude `"42"` walls, and great if you want to remove extra walls for `PERFECT=False`. |
| **3. Randomized Prim’s** | **Very High** (~35% of cells). Radiates outward like a bush. | **Short / Direct.** Easy for a human to solve visually. | **$O(V \log V)$** or **$O(V)$** (with random list swap-and-pop) | **Easy–Medium** (Requires tracking a frontier wall list) | **Very Good (8.5/10).** Routes around `"42"` cleanly, though high dead-end count means more walls to knock down in `PERFECT=False`. |
| **4. Wilson’s Algorithm** | **Moderate** (~28% of cells). Truly unbiased uniform spanning tree. | **Medium.** Completely unbiased random walk. | **$O(V)$** average, but **$O(V^3)$ / Unbounded** worst-case | **Hard** (Requires loop-erased random walks) | **Poor–Medium (5/10).** Random walks can bounce off the `"42"` obstacle and take a long time to hit the first target cell on large grids. |
| **5. Binary Tree** | **Moderate** (~25% of cells), strongly biased diagonally. | **Very Short** along two borders (trivial to solve). | **$O(V)$** (Single pass over grid) | **Trivial** (~10 lines, no state needed) | **BAD — Avoid (1/10).** Cannot route around the `"42"` pattern without disconnecting cells or creating forbidden open corridors along borders! |
| **6. Hunt-and-Kill** *(Added Option)* | **Low** (~12% of cells). Very similar look to Backtracker. | **Long** & winding. | **$O(V^2)$** worst-case (due to grid scans), **$O(V)$** with row tracking | **Easy** (No stack needed — uses `O(1)` extra memory) | **Good (8/10).** Works just like Backtracker without needing a stack, though slightly slower on huge grids. |

---

### 2. Deep Dive into How Each Fits `A-Maze-ing`

#### 1. Randomized Depth-First Search (Backtracker)
* **How it behaves:** It carves a single tunnel as far as it can go before backing up.
* **Why it shines in `A-Maze-ing`:**
  1. **The `"42"` pattern:** Before starting, you just put the coordinates of the `"42"` cells into your `visited` set. The algorithm automatically treats them like solid rock and carves around them with zero extra logic.
  2. **`PERFECT=False` (Pac-Man mode):** Because Backtracker produces **very few dead-ends (~10%)**, converting a `PERFECT=True` Backtracker maze into a `PERFECT=False` braided Pac-Man board requires knocking down very few walls, making it much easier to avoid accidentally creating forbidden `3x3` open areas!
  3. **Important Warning:** In Python, use a `while stack:` loop (**Iterative Backtracker**) instead of a function calling itself (`def dfs()`), because Python crashes with `RecursionError` on grids larger than ~`30x30`.

#### 2. Randomized Kruskal’s Algorithm
* **How it behaves:** Treats every cell as its own separate island, shuffles all internal walls, and knocks down a wall whenever it separates two different islands.
* **Why it's a great Bonus #2 candidate:** If you want to implement the **"Support multiple maze generation algorithms"** bonus (Chapter VIII), Kruskal's is the best second algorithm because its visual style (lots of short branches) contrasts noticeably with Backtracker's long winding corridors.

#### 3. Randomized Prim’s Algorithm
* **How it behaves:** Starts at `ENTRY` and grows outward like mold, picking random walls on the frontier.
* **Pros/Cons for `A-Maze-ing`:** Very easy to understand and naturally avoids the `"42"` cells. The only downside is that it creates **3x more dead-ends** than Backtracker, so in `PERFECT=False` mode your braiding step has to remove many more walls, which increases the chance of running into the `3x3` open-area limit.

#### 4. Wilson’s Algorithm
* **How it behaves:** Uses "Loop-Erased Random Walks". A walker wanders randomly until it touches the existing maze, erasing any loops it makes along the way.
* **Pros/Cons for `A-Maze-ing`:** Mathematically famous because every possible spanning tree has an equal probability of being generated. However, with the `"42"` obstacle sitting in the middle of the grid, random walks can take thousands of wasted steps on large grids, and it is harder to explain and modify live during a 42 evaluation defense.

#### 5. Binary Tree *(Do NOT use as your main algorithm!)*
* **How it behaves:** For every cell, flip a coin to open either the **North** wall or the **East** wall.
* **Why it breaks `A-Maze-ing`:**
  1. It always leaves the entire top row and rightmost column as two completely straight, empty corridors.
  2. **It breaks around the `"42"` pattern!** If a cell is directly south and west of `"42"` cells, neither North nor East can be opened, leaving the cell completely trapped and violating the **full connectivity** rule (Section IV.4).

#### 6. Hunt-and-Kill *(Bonus Alternative)*
* **How it behaves:** Carves a random walk just like Backtracker until it gets stuck in a dead-end. Instead of using a stack to backtrack, it scans the grid row-by-row ("hunts") for an unvisited cell next to a visited cell and starts carving from there.
* **Fit:** Produces long, winding mazes nearly identical to Backtracker while using zero stack memory.

---

### 3. Final Recommendation & Why (What to Put in Your `README.md`)

**Primary Choice: Iterative Randomized Depth-First Search (Backtracker)**
*(Optional Bonus Choice: Add **Randomized Prim's** or **Randomized Kruskal's** as a second selectable algorithm in `config.txt` for Bonus points!)*

**4 Reasons Why Iterative Backtracker is the Best Choice for Your Project (and for your `README.md` justification required in Chapter VII):**
1. **Optimal `O(V)` Time Complexity & Zero Recursion Risk:** Using an explicit Python `list` as a stack visits every cell in linear time $O(\text{WIDTH} \times \text{HEIGHT})$ and never hits Python's recursion limit.
2. **Seamless Obstacle Handling (`"42"` Pattern):** Pre-marking the `"42"` cells as visited allows the algorithm to naturally wrap around the central `"42"` logo while guaranteeing 100% connectivity of all remaining cells.
3. **Aesthetically Challenging Solutions (`PERFECT=True`):** Its high "river" factor produces long, twisting solution paths between `ENTRY` and `EXIT` rather than short, trivial diagonal paths.
4. **Ideal Foundation for Pac-Man Mode (`PERFECT=False`):** Because it generates ~65% fewer dead-ends than Prim's or Kruskal's, braiding the dead-ends into loops for `PERFECT=False` requires minimal wall removals — making it easy to achieve **0 dead-ends** while strictly respecting the **max 2-cell corridor width (`no 3x3 open areas`)** rule.