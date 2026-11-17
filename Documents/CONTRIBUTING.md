# Team Git Manual

How the two of us work together on this repository. Read it once, come back to it when you are stuck.

## The golden rules

1. **Never work directly on `main`.** Every task gets its own branch.
2. **Every change goes through a pull request (PR).** The other person reviews it.
3. **Pull before you start.** Always begin with the latest code.
4. **Never use `git push --force`.**
5. **Never commit secrets or generated files** (passwords, tokens, `.env`, `__pycache__/`, virtual environments).
6. **Talk before you start.** Agree on who works on which file or feature.

## One-time setup (each of us)

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git config --global pull.rebase false
git config --global init.defaultBranch main
```

Use the email linked to your GitHub account so your commits show up under your name.

### Python environment

Create a virtual environment inside the repo folder (it is ignored by git):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install flake8 mypy
```

If the project has a `requirements.txt`, also run `pip install -r requirements.txt`.
Activate the environment (`source .venv/bin/activate`) every time you open a new terminal.

When one of us adds a dependency, update the file and mention it in the PR:

```bash
pip freeze > requirements.txt
```

## The daily workflow

### Step 1: Start from the latest `main`

```bash
cd ~/projects/42_A-Maze-ing
git checkout main
git pull
```

### Step 2: Create a branch for your task

```bash
git checkout -b feature/maze-generator
```

Name it after what you are doing, in lowercase with hyphens. Use prefixes such as `feature/`, `fix/` or `docs/`.

### Step 3: Make your changes

Edit your files in VS Code. Run and test your code as you go.

### Step 4: Check your code

Run the checks before every commit:

```bash
flake8 .
mypy .
```

Fix what they report. Check the project subject for the exact flags and rules that are required.

### Step 5: Check what changed

```bash
git status          # which files changed
git diff            # what exactly changed
```

### Step 6: Save your work (commit)

```bash
git add maze.py generator.py
git commit -m "Add maze generation with recursive backtracking"
```

- Add files by name. Avoid `git add .` until you are comfortable, because it can add files you did not intend.
- Write messages that say what you did, in the present tense. For example: "Fix wall collision in solver".
- Commit small and often. Every commit should leave the project in a working state.

### Step 7: Push your branch

```bash
git push -u origin feature/maze-generator
```

You only need `-u origin feature/maze-generator` the first time. After that, `git push` is enough.

### Step 8: Open a pull request

1. Go to the repo on GitHub. A yellow banner appears with **Compare & pull request**. Click it.
2. Fill in the template: what you changed and how to test it.
3. Click **Create pull request**.
4. Tell your partner that it is ready.

### Step 9: Review your partner's PR

1. Open the PR and go to **Files changed**.
2. Read the code. Click the `+` next to a line to leave a comment.
3. Click **Review changes** and choose:
   - **Comment** for questions
   - **Request changes** if something must be fixed
   - **Approve** if it looks good
4. Try to understand every line. In peer evaluations you must be able to explain all of it.

### Step 10: Merge

Once approved:

1. Click **Merge pull request**, then **Confirm merge**.
2. Click **Delete branch** (GitHub offers this after merging).

### Step 11: Clean up locally

Both of us:

```bash
git checkout main
git pull
git branch -d feature/maze-generator
```

Then start again from Step 2 for the next task.

## Keeping your branch up to date

If your partner merged something while you were working, bring those changes into your branch:

```bash
git checkout main
git pull
git checkout feature/maze-generator
git merge main
```

Do this regularly on long-running branches to keep conflicts small.

## Resolving a merge conflict

A conflict happens when we both changed the same lines. It is normal.

1. Run `git merge main`. Git lists the conflicting files.
2. Open the file in VS Code. You will see markers like this:

   ```
   <<<<<<< HEAD
   your version
   =======
   partner's version
   >>>>>>> main
   ```

3. VS Code shows buttons above the conflict: **Accept Current Change**, **Accept Incoming Change**, **Accept Both Changes**. Decide together which is correct. Often you need to combine both by hand.
4. Make sure no `<<<<<<<`, `=======` or `>>>>>>>` markers remain.
5. Finish:

   ```bash
   git add the-file.py
   git commit
   git push
   ```

To cancel the merge and start over, run `git merge --abort`.

## Useful commands

| Task | Command |
|---|---|
| See current branch and changes | `git status` |
| See history | `git log --oneline --graph` |
| See all branches | `git branch -a` |
| Switch branch | `git checkout branch-name` |
| Undo changes to a file (not yet committed) | `git restore file.py` |
| Unstage a file | `git restore --staged file.py` |
| Save work temporarily | `git stash` / `git stash pop` |
| Fix the last commit message (before pushing) | `git commit --amend` |
| Get partner's new branches | `git fetch` |

## Common problems

- **"Your branch is behind"**: run `git pull`.
- **Push rejected**: someone pushed first. Run `git pull`, fix any conflicts, and push again.
- **I committed to `main` by mistake**: do not push. Keep the commit on a new branch with `git branch my-work`, then move `main` back with `git reset --hard origin/main`. Ask your partner if unsure.
- **I committed a secret**: tell your partner. Revoke or change the secret immediately. Deleting the file does not remove it from history.
- **`git push` fails with "Connection refused" on port 22**: the network blocks SSH. Use SSH over port 443 by adding this to `~/.ssh/config`:

  ```
  Host github.com
      Hostname ssh.github.com
      Port 443
      User git
  ```

- **I am lost**: run `git status`. It almost always tells you what to do next.

## Before submitting to the school

1. Merge everything into `main` through PRs.
2. Clone a fresh copy of `main` into a temporary folder. Install the dependencies and run the project from scratch.
3. Run `flake8` and `mypy` one last time.
4. Check that no forbidden or unneeded files are in the repo.
5. Push to the school's git remote. Only that repo is evaluated.
6. Both of us check that we can explain every part of the code.
