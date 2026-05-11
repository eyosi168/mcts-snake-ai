# MCTS Snake Visualizer

A Monte Carlo Tree Search (MCTS) based Snake AI visualizer built with Python and Pygame.

This project demonstrates how Monte Carlo Tree Search can be applied to sequential decision-making problems through an interactive Snake game simulation.

The system includes two operational modes:

- **Fast Intelligent Mode** — optimized for strong gameplay performance
- **Visualization Mode** — educational mode that demonstrates the four phases of MCTS in real time

---

## Project Overview

The Snake game is modeled as a decision-making problem where the AI must repeatedly choose the optimal move to maximize reward while avoiding terminal states.

Monte Carlo Tree Search is used to:

- Explore future possible moves
- Simulate outcomes
- Evaluate decision quality
- Select the best action based on accumulated statistics

---

## Features

### Intelligent Snake Agent
- Autonomous gameplay
- Monte Carlo based planning
- Dynamic food collection
- Collision avoidance

### MCTS Visualization
Real-time visualization of the four MCTS phases:

1. **Selection**
2. **Expansion**
3. **Simulation**
4. **Backpropagation**

---

### Tree Visualization
Displays:

- Search tree growth
- Node visit counts
- Reward propagation
- Decision paths

---

### Rollout Visualization
Shows random simulation traces used during evaluation.

---

### Multiple Modes

#### Fast Mode
Optimized for AI performance

- High-speed decision making
- Full search per move
- Better food acquisition

Run:

```bash
python main_fast.py
```

---

#### Visualization Mode
Optimized for learning and explanation

- Step-by-step MCTS execution
- Tree evolution rendering
- Educational presentation mode

Run:

```bash
python main.py
```

---

## Project Structure

```text
mcts-snake-ai/
│
├── core/
│   ├── constants.py
│   ├── game_state.py
│   └── snake.py
│
├── mcts/
│   ├── node.py
│   ├── rollout.py
│   ├── search.py
│   └── search_fast.py
│
├── visualization/
│   ├── renderer.py
│   ├── stats_panel.py
│   └── tree_view.py
│
├── main.py
├── main_fast.py
└── README.md
```

---

## Installation

Clone project:

```bash
git clone <repository-url>
cd mcts-snake-ai
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install pygame numpy
```

---

## Controls

### General Controls

| Key | Action |
|-----|--------|
| SPACE | Pause / Resume |
| R | Reset Game |

---

### Visualization Mode Controls

| Key | Mode |
|-----|------|
| 1 | Demo Mode |
| 2 | Balanced Mode |
| 3 | Fast Visualization |

---

## Monte Carlo Tree Search Workflow

### 1. Selection
Traverse the tree using UCB1 to select promising nodes.

---

### 2. Expansion
Generate child states from unexplored actions.

---

### 3. Simulation
Run random rollouts from expanded states.

---

### 4. Backpropagation
Propagate rollout reward upward through the tree.

---

## Why MCTS?

Monte Carlo Tree Search is ideal for Snake because:

- It handles large decision spaces
- It balances exploration vs exploitation
- It requires no prior training
- It adapts online during gameplay

---

## Technical Tradeoff

The project includes two implementations:

### Fast Mode
Prioritizes:
- Decision quality
- Search efficiency
- Responsiveness

---

### Visualization Mode
Prioritizes:
- Explainability
- Transparency
- Educational insight

Visualization introduces rendering overhead and phased execution, reducing real-time search efficiency.

---

## Future Improvements

Potential extensions:

- Parallelized search
- Neural-guided rollouts
- Heatmap-based decision analysis
- Asynchronous tree rendering
- Policy learning integration

---

## Author

Eyosyas Solomon

Artificial Intelligence / Search Algorithms Project