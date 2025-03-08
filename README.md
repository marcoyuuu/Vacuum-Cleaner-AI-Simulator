# University of Puerto Rico at Mayagüez  
### Department of Electrical and Computer Engineering  
#### ICOM5015 - Artificial Intelligence  

**Project Title:** Vacuum Cleaner AI Simulator  
**Assignment:** Programming homework assignment Chapter 2 - Agents (Exercises 2.11 & 2.14)  

**Team:** Group M  
- **Marco Yu** (Undergraduate, Computer Science)  
- **Samir Rivera** (Undergraduate, Software Engineering)  
- **Lex Feliciano** (Undergraduate, Electrical and Computer Engineering)  
- **Shadiel López** (Undergraduate, Computer Engineering)  

**Professor:** J. Fernando Vega Riveros  
**Date:** March 7, 2025  

<p align="center">
  <img src="https://www.uprm.edu/wdt/resources/seal-rum-uprm-1280x1280px.png" alt="UPRM Logo" width="250" height="250">
</p>

---

# Vacuum Cleaner AI Simulator  
**AI Performance Evaluation and Agent Analysis (Exercises 2.11 & 2.14): Programming homework assignment Chapter 2 - Agents**  
*(Based on Russell & Norvig, Artificial Intelligence: A Modern Approach, 3rd Edition, UC Berkeley AI Repository)*  

---

## 📖 **Overview & Purpose**

This project implements a modular, **performance-measuring environment simulator** for Russell & Norvig's classic Vacuum-Cleaner World, addressing **Exercises 2.11** and **2.14** from their textbook (*Artificial Intelligence: A Modern Approach*, 3rd Edition). It analyzes and compares multiple AI agent types in environments of varying complexity.

The simulator and agent implementations are based on the unmodified [UC Berkeley AI repository](https://github.com/aimacode/aima-python) (`agents.py` and `utils.py`).

**Core AI Concepts Applied:**  
- **Simple Reflex Agents**
- **Randomized Reflex Agents**
- **Model-Based Reflex Agents**
- **Goal-Based (Rational) Agents** using BFS for planning
- **Performance Measurement and Visualization Techniques**

---

## Assignment Overview

This assignment consists of two major exercises:

### **Exercise 2.11: Vacuum-Cleaner World Simulator**
- Implement a modular and configurable environment simulator.
- Clearly visualize environments showing dirt placement, obstacles, and agents.
- Measure agent performance based on cleanliness achieved and actions taken.

### **Exercise 2.14: Agent Analysis in a Modified Vacuum Environment**
- Environment characteristics (extent, boundaries, obstacles, dirt placement) are unknown to the agent.
- Agents have extended movement capabilities (`Up`, `Down`, `Left`, `Right`).
- Analyze performance of agent types:
  - Simple Reflex Agent
  - Randomized Reflex Agent
  - Model-Based Reflex Agent
  - Rational (BFS-based) Agent
- Design and demonstrate a worst-case scenario for the randomized reflex agent.

These tasks help illustrate fundamental AI agent types, their limitations, and potential optimizations.

---

## Implemented Agents

This project implements and extends four types of agents:

| Agent Type             | Description                                      | Source File                     |
|------------------------|--------------------------------------------------|----------------------------------|
| **Simple Reflex**      | Makes decisions based solely on the current percept. | `reflex_grid_agent.py`          |
| **Randomized Reflex**  | Introduces exploration by making random decisions.  | `random_grid_agent.py`          |
| **Model-Based Reflex** | Maintains an internal memory (simple model).     | `model_based_grid_agent.py`     |
| **Rational (BFS-based)** | Systematically explores unknown areas using BFS. | `my_rational_agent.py`          |

---

## Performance-Measuring Environment Simulator

The simulator (`environment.py`) is highly modular and customizable, allowing easy modification of:

- Grid size (e.g., 2x1 or larger grids)
- Dirt placement probability
- Obstacle frequency and distribution
- Agents' starting positions and movement constraints (4-directional)

### **Visualization Features:**
- **Initial State Visualization:** Clearly shows dirt (red), clean cells (green), and obstacles (gray).
- **Performance Metrics:** Average scores, standard deviations, cumulative performance over time.
- **Comparative Visualizations:** Bar charts, box plots, line charts, heatmaps.

---

## Project Structure

```
vacuum_agents_groupM/
│
├── agents.py                      # Base agents (unchanged, from UC Berkeley)
├── utils.py                       # Utility functions (from Berkeley repository, unchanged)
├── environment.py                  # Custom environment simulator
├── my_rational_agent.py            # Rational BFS-based agent
├── reflex_grid_agent.py            # 4-direction reflex agent wrapper
├── random_grid_agent.py            # 4-direction random agent wrapper
├── model_based_grid_agent.py       # 4-direction model-based agent wrapper
├── simulation.py                   # Simulation & visualization scripts
├── tests.py                        # Unit tests
├── EXERCISE_2_14_ANSWERS.txt       # Answers to Exercise 2.14
└── *.png                           # Generated visualization plots
```

**Note:**  
- `agents.py` and `utils.py` are from the UC Berkeley repository and remain unchanged.

---

## Installation & Setup

### Requirements:
- Python 3.8 or higher
- numpy
- matplotlib
- ipythonblocks
- IPython

### Setup Instructions:
1. **Clone or Download the Project**  
```bash
git clone <repository-url>
cd vacuum_agents_groupM
```

2. **Install Dependencies**  
```bash
pip install -r requirements.txt
```

3. **Visualize Two-Location Vacuum Environment (Exercise 2.11)**  
```bash
python visualize_two_location.py
```

4. **Run Simulations (Exercise 2.14)**  
```bash
python simulation.py
```
---

## Running Simulations & Interpreting Results

### Execute Simulations:
Run performance comparisons and visualizations by executing:
```bash
python simulation.py
```

### Output Interpretation:
- **Textual Logs:**  
  ```
  Reflex: Avg Performance = -24.25, Std Dev = 44.87
  Random: Avg Performance = 149.60, Std Dev = 95.51
  Model-Based: Avg Performance = 1.00, Std Dev = 0.00
  Rational: Avg Performance = 556.45, Std Dev = 114.17
  ```
- **Visualizations:**  
  - **Initial Environment States**: `initial_default.png`, `initial_worst.png`
  - **Bar Charts:** `bar_chart_default.png`, `bar_chart_worst.png`
  - **Box Plots:** `boxplot_default.png`, `boxplot_worst.png`
  - **Line Charts:** `linechart_<Agent>_<Env>.png`
  - **Heatmaps:** `heatmap_<Agent>_<Env>.png`

---

## Grading Criteria Alignment

This project aligns clearly with the rubric:

| Rubric Criterion | How Addressed |
| ---------------- | -------------- |
| **Purpose** | Clearly demonstrates understanding through visualizations, comparative analyses. |
| **Key Problem** | Clearly defines and explores the rationality limitations of reflex agents and the benefits of stateful and rational agents. |
| **Information** | Uses systematic experiments (multiple trials) to gather credible data on agent performance. |
| **Interpretations** | Deeply analyzes differences between agent types, with clear visual and textual inferences. |
| **Implications** | Connects agent performance to real-world AI systems (navigation, exploration, decision-making). |
| **Citations** | Properly references Russell & Norvig’s textbook and acknowledges UC Berkeley's AI code repository. |

---

## Challenges, Lessons Learned & Future Work

### Challenges Encountered:
- Adapting two-location agents to handle grid environments required careful wrappers without modifying the original Berkeley code.
- Balancing the randomness of dirt and obstacles to fairly evaluate all agents.

### Lessons Learned:
- Memory and planning (state-based agents) significantly improve rationality in complex environments.
- Visualization methods like heatmaps and box plots significantly enhance insight into agent behavior.

### Future Work:
- Implement more sophisticated planning algorithms (e.g., A* search).
- Introduce dynamic dirt generation or moving obstacles to better simulate real-world conditions.

---

## References and Citations
- **Textbook:**  
  Russell, S., & Norvig, P. *(2010). Artificial Intelligence: A Modern Approach* (3rd Edition).
- **Code Base:**  
  [UC Berkeley AI Repository](https://github.com/aimacode/aima-python) (files `agents.py` and `utils.py` remain unmodified).
- **Exercises:**
    - [Exercise 2.11](https://aimacode.github.io/aima-exercises/agents-exercises/ex_11/): Implement a modular environment simulator and evaluate agent performance.
    - [Exercise 2.14](https://aimacode.github.io/aima-exercises/agents-exercises/ex_14/): Analyze agent rationality in unknown environments and design worst-case scenarios.
- **Additional Resources:**  
  - Matplotlib documentation: [https://matplotlib.org](https://matplotlib.org)  
  - NumPy documentation: [https://numpy.org](https://numpy.org)

---

## Conclusion

This project meets all the specified assignment objectives, rigorously evaluates AI agent rationality in complex, unknown environments, and provides professional-level visualization and analysis tools to illustrate agent performance and behaviors clearly.

---