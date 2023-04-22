# Simple projects for my AI course

I am coding various little projects throughout my AI course and publish them on this repository. All Jupyter Notebooks are executable with vanilla Python 3.11

## Usage

Install the environment for simple-projects with:

```bash
conda env create -f environment.yml
```

The environment.yml was created with that command:

```bash
conda env export --from-history --no-builds --name simple-projects | findstr -v "prefix:" > environment.yml
```

## Projects

### [Tic Tac Toe](tic_tac_toe.ipynb)

A simple Tic Tac Toe game with a simple AI. The AI uses the minimax algorithm with alpha-beta pruning to find the best move.

### [Gauss algorithm for matrix inversion](gauss.ipynb)

A simple implementation of the Gauss algorithm for matrix inversion.

### [8-Puzzle](8_puzzle.ipynb)

A simple implementation of the 8-Puzzle game with a simple AI. The AI uses the A* algorithm to find the best move.

### [ASCII File Tree Generator](ascii_tree.ipynb)

A simple implementation of a file tree generator. The generator uses the ASCII characters like └─ and ├─ to draw the tree.

This change is a test
