## A-MAZE-ING

O objetivo do projeto é construir um gerador e solucionador de labirintos interativo em Python 3.10+ (`python3 a_maze_ing.py config.txt`), com exportação em formato hexadecimal, tratamento rigoroso de erros (zero crashes) e empacotamento reutilizável:

1. **Configuração (`config.txt`)**: Lê dimensões (`WIDTH`, `HEIGHT`), coordenadas (`ENTRY`, `EXIT`), arquivo de saída (`OUTPUT_FILE`), modo (`PERFECT=True/False`) e parâmetros opcionais como semente (`SEED`), ignorando linhas de comentário iniciadas por `#`.
2. **Representação em Hexadecimal**: Cada célula codifica suas paredes fechadas (`1`) ou abertas (`0`) em 4 bits: Norte (bit 0 = `1`), Leste (bit 1 = `2`), Sul (bit 2 = `4`) e Oeste (bit 3 = `8`), exigindo coerência simétrica entre células vizinhas e bordas externas fechadas.
3. **Padrão "42"**: O labirinto deve conter a forma visível do número **42** desenhada com células totalmente fechadas (`0xF`), ou exibir uma mensagem de erro no console caso as dimensões da grade sejam pequenas demais para comportá-lo.
4. **Modos de Geração (Reproduzíveis via `seed` e sem áreas abertas `3x3`)**:
   - `PERFECT=True`: Labirinto perfeito (exatamente um único caminho entre entrada e saída, sem loops).
   - `PERFECT=False` (Padrão): Tabuleiro jogável estilo Pac-Man (conectividade total, 4 cantos e centro abertos, no mínimo duas rotas independentes/loops e poucos ou nenhum beco sem saída), respeitando em ambos os modos o limite máximo de 2 células de largura por corredor (proibido áreas abertas `3x3`).
5. **Arquivo de Saída e Visualizador**: Exporta o arquivo hexadecimal seguido de linha em branco, entrada, saída e menor caminho (`N`, `E`, `S`, `W`), e exibe interface interativa em terminal (ASCII) ou gráfica (MLX) permitindo re-gerar labirintos, mostrar/ocultar o menor caminho e alterar cores das paredes (e opcionalmente do `"42"`).
6. **Empacotamento e Documentação**: A classe `MazeGenerator` (com acesso à estrutura, solução e documentação de uso) deve ser empacotada em arquivo único (`mazegen-*.whl` ou `.tar.gz`) na raiz do repositório, acompanhada de `LICENSE.md`, `Makefile` e `README.md`.

---

## Divisão de Papéis (Arl vs. Mau)

| Responsável | Foco Principal | Responsabilidades Chave |
| :--- | :--- | :--- |
| **Arl** | Motor do Labirinto & Algoritmos (`mazegen.py`) | Estrutura da classe `MazeGenerator` (PEP 257 e type hints), matriz de paredes em 4 bits, carimbo do padrão `"42"`, geração `PERFECT=True` com `seed`, modo Pac-Man `PERFECT=False` (com trava contra áreas `3x3`) e busca do menor caminho (`BFS`). |
| **Mau** | Automação, CLI, I/O, UI & Pacote | `Makefile` (`install`, `run`, `debug`, `clean`, `lint`), script principal `a_maze_ing.py`, parser do `config.txt`, escrita do `OUTPUT_FILE`, interface visual interativa (ASCII/MLX), empacotamento `pip` (`mazegen-*`), `LICENSE.md` e testes com `maze_analyzer.py`. |

---

## Roteiro de Desenvolvimento (10 Etapas Sequenciais)

### Parte 1: Estrutura Base, Configuração e Algoritmos de Geração

#### Etapa 1: Estrutura Inicial, Automação e Contrato da Interface
* **Mau**: Criar o `Makefile` com as regras obrigatórias `install`, `run`, `debug`, `clean` e `lint` (`flake8` e `mypy` com flags estritas), o `.gitignore` e o ponto de entrada `a_maze_ing.py`.
* **Arl**: Criar a estrutura inicial da classe `MazeGenerator` em `mazegen.py` com docstrings (PEP 257), type hints e retorno mockado `5x5`, além do arquivo `config.txt` padrão na raiz.

#### Etapa 2: Parsing de Configuração e Matriz Hexadecimal em Bits
* **Mau**: Escrever o parser do `config.txt` (usando `with open` e `try-except`), ignorando comentários `#` e validando `WIDTH`, `HEIGHT`, `ENTRY`, `EXIT`, `OUTPUT_FILE`, `PERFECT` e `SEED` sem permitir exceções não tratadas.
* **Arl**: Implementar na classe `MazeGenerator` a matriz de células em 4 bits (`N=1, E=2, S=4, W=8`), garantindo bordas externas fechadas e funções auxiliares que abrem/fecham paredes de forma simétrica entre células vizinhas.

#### Etapa 3: Escrita do Arquivo de Saída e Padrão "42"
* **Mau**: Implementar o gerador do `OUTPUT_FILE` (linhas em hexadecimal, linha em branco, coordenadas de entrada, saída e string do caminho terminadas com `\n`) usando a grade da `MazeGenerator`.
* **Arl**: Implementar o carimbo fixo do número **42** com células fechadas (`0xF`) no centro da matriz, validando se a grade comporta o padrão sem bloquear `ENTRY`/`EXIT` e emitindo mensagem de erro no console caso o tamanho seja insuficiente.

#### Etapa 4: Labirinto Perfeito (`PERFECT=True`) e Testes de Coerência
* **Arl**: Implementar o algoritmo de geração de labirinto perfeito reproduzível por `seed` (ex: Backtracker Iterativo com pilha ou Kruskal) desviando das células do `"42"` e garantindo caminho único e conectividade total.
* **Mau**: Criar testes unitários (`pytest`) para validar a coerência das paredes entre células vizinhas, integridade das bordas externas e tratamento de arquivos de configuração inválidos.

#### Etapa 5: Modo Pac-Man (`PERFECT=False`) e Busca do Menor Caminho (`BFS`)
* **Arl**: Implementar o algoritmo `BFS` (retornando a sequência `N`, `E`, `S`, `W` e coordenadas da rota) e adaptar a geração para `PERFECT=False` (cantos e centro abertos, remoção de becos sem saída, mínimo de 2 loops independentes e verificação que impede áreas abertas `3x3`).
* **Mau**: Preparar a camada de integração entre o `config.txt`, a chamada da `MazeGenerator` em `a_maze_ing.py` e a preparação dos dados para renderização visual.

---

### Parte 2: Validação, Visualização Interativa, Pacote e README

#### Etapa 6: Integração do Motor e Validação com `maze_analyzer.py`
* **Arl**: Ajustar casos de borda da geração (grades pequenas sem o `"42"`, sementes variadas e garantia de 0 becos sem saída no modo `PERFECT=False`).
* **Mau**: Conectar o motor completo ao gerador de arquivo e validar os arquivos `OUTPUT_FILE` gerados em ambos os modos executando o script oficial `maze_analyzer.py`.

#### Etapa 7: Visualizador Interativo (Renderização e Eventos)
* **Mau**: Criar a exibição visual do labirinto (ASCII/Unicode no terminal ou janela MLX) destacando paredes, entrada, saída, padrão `"42"` e menor caminho, incluindo os comandos interativos em tempo real (re-gerar labirinto, mostrar/ocultar caminho e alterar cores).
* **Arl**: Dar suporte na integração do método de re-geração dinâmica da `MazeGenerator` (atualizando a semente, a solução `BFS` e o `OUTPUT_FILE` a cada nova geração solicitada na interface).

#### Etapa 8: Empacotamento Reutilizável (`mazegen`) e Licença
* **Mau**: Configurar o `pyproject.toml` e gerar o pacote instalável em arquivo único (`mazegen-1.0.0-py3-none-any.whl` ou `.tar.gz`) na raiz do repositório Git.
* **Arl**: Criar o arquivo `LICENSE.md` na raiz permitindo o reuso e distribuição da biblioteca e revisar as docstrings internas da `MazeGenerator` com exemplos claros de instanciação e acesso à solução.

#### Etapa 9: Documentação Técnica (`README.md`)
* **Arl**: Escrever as seções do `README.md` detalhando a estrutura completa do `config.txt`, o algoritmo de geração escolhido, o motivo da escolha e a documentação de uso do módulo reutilizável `mazegen`.
* **Mau**: Escrever as seções do `README.md` com a primeira linha obrigatória em itálico, descrição, instruções de compilação/execução, recursos e uso de IA, além da gestão da equipe (papéis, evolução do planejamento, pontos de melhoria e ferramentas).

#### Etapa 10: Validação Final, Linting Estrito e Simulação de Defesa
* **Ambos**: Executar `make lint` (e `make lint-strict`) até obter 0 erros no `flake8` e no `mypy` em todos os arquivos do repositório.
* **Ambos**: Testar o rebuild e a instalação via `pip` do pacote `mazegen-*` a partir do zero em um ambiente virtual (`venv`) limpo e revisar o código um do outro para a avaliação.