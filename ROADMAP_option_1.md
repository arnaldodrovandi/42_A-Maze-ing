
---

## AMAZING

O objetivo do projeto é construir um gerador de labirintos interativo em Python 3.10+ com exportação em formato hexadecimal e empacotamento reutilizável [2, 3]:

1. **Configuração (`config.txt`)**: Lê dimensões (`WIDTH`, `HEIGHT`), coordenadas (`ENTRY`, `EXIT`), arquivo de saída (`OUTPUT_FILE`) e o modo (`PERFECT=True/False`) [4].
2. **Representação em Hexadecimal**: Cada célula codifica suas paredes em 4 bits: Norte (bit 0), Leste (bit 1), Sul (bit 2), Oeste (bit 3) [5].
3. **Padrão "42"**: O centro do labirinto deve conter a forma do número **42** com células fechadas [6].
4. **Modos de Geração**:
   - `PERFECT=True`: Labirinto perfeito (apenas um caminho entre entrada e saída) [6].
   - `PERFECT=False`: Tabuleiro jogável estilo Pac-Man (múltiplas rotas, cantos/centro abertos, poucos becos sem saída) [6].
5. **Visualizador**: Interface interativa em terminal (ASCII) ou gráfica (MLX) permitindo re-gerar labirintos, alterar cores e alternar exibição do caminho [7].
6. **Empacotamento**: A classe `MazeGenerator` deve ser empacotada em uma biblioteca reutilizável (`mazegen-*.whl` ou `.tar.gz`) na raiz do repositório [8, 9].

---

## 👥 Divisão de Papéis (Arl vs. Mau)

| Responsável | Foco Principal | Responsabilidades Chave |
| :--- | :--- | :--- |
| **Arl** | Dados & Algoritmos | Parser do `config.txt`, representação da grade em bits, algoritmos de geração de labirinto, busca do menor caminho (`BFS`) e geração do arquivo de saída [3-6]. |
| **Mau** | Automação, UI & Pacote | `Makefile` (`install`, `run`, `debug`, `clean`, `lint`), interface visual (ASCII/MLX), empacotamento `pip` (`mazegen`), `LICENSE.md` e `README.md` [1, 7, 9-12]. |

---

## 🗓️ Cronograma de 2 Semanas (Tasks Diárias)

### 📅 Semana 1: Estrutura Base e Algoritmos de Geração

#### Dia 1: Estrutura Inicial e Automação
* **Mau**: Criar o `Makefile` com as regras obrigatórias `install`, `run`, `debug`, `clean` e `lint` (`flake8` e `mypy`) [10, 11].
* **Arl**: Criar a estrutura inicial de arquivos em Python 3.10+, o `.gitignore` e um arquivo `config.txt` básico de testes [2, 4, 11].

#### Dia 2: Parsing de Configuração e Módulo Base
* **Arl**: Escrever o parser do arquivo `config.txt` tratando exceções e validando chaves obrigatórias (`WIDTH`, `HEIGHT`, `ENTRY`, `EXIT`, `OUTPUT_FILE`, `PERFECT`) [2, 4, 13].
* **Mau**: Estruturar a classe `MazeGenerator` no módulo reutilizável com docstrings (PEP 257) e type hints [2, 8].

#### Dia 3: Grade Hexadecimal e Padrão "42"
* **Arl**: Criar a estrutura de matriz onde cada célula armazena suas paredes em bits (Norte=1, Leste=2, Sul=4, Oeste=8) [5].
* **Mau**: Implementar o padrão fixo do número **42** bloqueando células no centro e emitir mensagem de erro caso o tamanho seja insuficiente [6, 14].

#### Dia 4: Labirinto Perfeito (`PERFECT=True`)
* **Arl**: Implementar o algoritmo de geração de labirinto perfeito (ex: Backtracker Recursivo ou Kruskal) garantindo caminho único [6].
* **Mau**: Criar testes unitários para verificar se a abertura e fechamento de paredes entre células vizinhas é coerente [6, 11].

#### Dia 5: Modo Pac-Man (`PERFECT=False`) e Busca de Caminho
* **Arl**: Adaptar a geração para o modo `PERFECT=False` (múltiplas rotas, sem becos sem saída isolados, cantos e centro abertos) [6].
* **Mau**: Criar o algoritmo de busca do menor caminho (ex: BFS) retornando a sequência de passos (`N`, `E`, `S`, `W`) [5].

---

### 📅 Semana 2: Exportação, Visualização, Pacote e README

#### Dia 6: Exportação do Arquivo de Saída
* **Arl**: Implementar a escrita do `OUTPUT_FILE` (linhas em hexadecimal, linha em branco, entrada, saída e sequência do caminho) [5].
* **Mau**: Validar a coerência do arquivo gerado executando o script `maze_analyzer.py` [15].

#### Dia 7: Visualizador Interativo
* **Arl**: Criar a exibição visual do labirinto (ASCII no terminal ou janela MLX) destacando paredes, entrada, saída e o "42" [7].
* **Mau**: Adicionar o menu interativo com os comandos: re-gerar labirinto, mostrar/ocultar caminho e alterar cores das paredes [7].

#### Dia 8: Empacotamento Reutilizável (`mazegen`)
* **Mau**: Configurar a estrutura de build em Python para gerar o pacote `mazegen-*.whl` ou `.tar.gz` na raiz do Git [9].
* **Arl**: Criar o arquivo `LICENSE.md` na raiz estabelecendo os termos de licença de código aberto para o reuso da biblioteca [12].

#### Dia 9: Documentação Técnica (`README.md`)
* **Arl**: Escrever as seções do `README.md` detalhando a estrutura do config, escolha do algoritmo de geração e partes reutilizáveis do código [16].
* **Mau**: Escrever as seções do `README.md` com a primeira linha obrigatória em itálico, instruções de instalação/uso, referências, uso de IA e papéis da equipe [1, 16].

#### Dia 10: Validação Final e Coerência do Código
* **Ambos**: Executar `make lint` até obter 0 erros no `flake8` e `mypy` [10, 11].
* **Ambos**: Testar a criação e instalação do pacote `mazegen` a partir do zero em um ambiente virtual (`venv`) limpo [11, 12].

---
