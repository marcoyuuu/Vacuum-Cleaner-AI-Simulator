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

## Jupyter Notebook

A comprehensive Jupyter Notebook (`Vacuum_Cleaner_AI_Simulator.ipynb`) is provided to:
- **Integrate all aspects** of the project in one document.
- **Demonstrate Exercise 2.11** by animating a two-location vacuum world.
- **Showcase simulations and visualizations** for Exercise 2.14, including performance comparisons and analysis.
- **Provide interactive code and detailed explanations** that answer all assignment questions.

### How to Open and Run the Notebook:
1. **Open the Project Folder:**  
   Clone the repository and open the project folder (`vacuum_agents_groupM`) in VS Code or your preferred Jupyter interface.
2. **Locate the Notebook:**  
   Find `Vacuum_Cleaner_AI_Simulator.ipynb` in the project root.
3. **Open in Notebook Editor:**  
   Double-click the file or right-click and choose "Open With" → "Jupyter Notebook Editor."
4. **Select Kernel and Run Cells:**  
   Choose the appropriate Python kernel (or your virtual environment) and run all cells sequentially to view the animations and visualizations.

---

## Project Structure

```
vacuum_agents_groupM/
│── 📁 src/                        # Source code directory (organized logically)
│   │── 📁 berkeley_ai/            # UC Berkeley AI repository (unchanged files)
│   │   │── agents.py              # Berkeley AI agent implementations
│   │   │── utils.py               # Berkeley AI utilities
│   │
│   │── 📁 agents/                 # Modified and custom agent implementations
│   │   │── reflex_grid_agent.py   # Updated Reflex Agent for 4-direction movement
│   │   │── random_grid_agent.py   # Updated Random Agent for 4-direction movement
│   │   │── model_based_grid_agent.py  # Updated Model-Based Agent for 4-direction movement
│   │   │── my_rational_agent.py   # BFS-based Rational Agent
│   │
│   │── 📁 environment/             # Environment simulation logic
│   │   │── environment.py          # Environment and world logic
│   │
│   │── 📁 simulation/              # Performance measurement and experiment logic
│   │   │── simulation.py           # Main simulation script
│   │   │── visualize_two_location.py  # Visualization for Exercise 2.11
│   │
│── 📁 tests/                       # Testing directory
│   │── tests.py                    # Unit tests for agents and environment
│
│── 📁 visualizations/               # Generated images and results
│   │── 📁 initial_states/          # Initial state images
│   │   │── initial_default.png
│   │   │── initial_worst.png
│   │
│   │── 📁 bar_charts/              # Bar charts (Performance comparison)
│   │   │── bar_chart_default.png
│   │   │── bar_chart_worst.png
│   │
│   │── 📁 box_plots/               # Box plots (Performance distribution)
│   │   │── boxplot_default.png
│   │   │── boxplot_worst.png
│   │
│   │── 📁 line_charts/             # Time-series performance trends
│   │   │── linechart_Model-Based_default.png
│   │   │── linechart_Model-Based_worst.png
│   │   │── linechart_Random_default.png
│   │   │── linechart_Random_worst.png
│   │   │── linechart_Rational_default.png
│   │   │── linechart_Rational_worst.png
│   │   │── linechart_Reflex_default.png
│   │   │── linechart_Reflex_worst.png
│   │
│   │── 📁 heatmaps/                # Spatial exploration heatmaps
│   │   │── heatmap_Model-Based_default.png
│   │   │── heatmap_Model-Based_worst.png
│   │   │── heatmap_Random_default.png
│   │   │── heatmap_Random_worst.png
│   │   │── heatmap_Rational_default.png
│   │   │── heatmap_Rational_worst.png
│   │   │── heatmap_Reflex_default.png
│   │   │── heatmap_Reflex_worst.png
│
│── 📁 docs/                         # Documentation files
│   │── EXERCISE_2_14_ANSWERS.md      # Written responses for Exercise 2.14
│
│── 📁 config/                        # Configuration and dependencies
│   │── requirements.txt              # Required dependencies
│
│── .gitignore                         # Specifies files and directories that should be ignored by Git (e.g., __pycache__, virtual environments, logs).
│── README.md                          # Main project documentation; includes an overview, installation guide, usage instructions, and project structure.
│── LICENSE                            # Project license; defines the legal terms under which the code can be used, modified, and shared.
│── Vacuum_Cleaner_AI_Simulator.ipynb  # Jupyter Notebook integrating all exercises; contains explanations, simulations, visualizations, and analysis.

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
pip install -r config/requirements.txt
```

3. **Visualize Two-Location Vacuum Environment (Exercise 2.11)**  
```bash
python -m src.simulation.visualize_two_location
```

4. **Run Simulations (Exercise 2.14)**  
```bash
python -m src.simulation.simulation
```
---

## Running Simulations & Interpreting Results

### Execute Simulations:
Run performance comparisons and visualizations by executing:
```bash
python -m src.simulation.simulation
```
---

## **Example Visualizations**

Our simulation produces various visualizations to analyze agent performance across different environments. These include **initial state representations, bar charts, box plots, line charts, and heatmaps**. Below are some sample outputs from our experiments.

### **Initial Environment States**
The following images illustrate the **starting configurations** of both the **Default** and **Worst-Case** environments before agents begin their tasks.

#### **Default Environment**
![Default Environment](https://github.com/user-attachments/assets/957541fd-983b-4b90-bfcc-d3ba63dce3fd)

#### **Worst-Case Environment**
![Worst-Case Environment](https://github.com/user-attachments/assets/f0f4b239-d7c1-437e-bac3-6c86b9c03eff)

---

### **Performance Comparisons**
The following bar charts show **average agent performance** with standard deviation error bars, comparing results across different environments.

#### **Default Environment - Performance Comparison**
![Bar Chart Default](https://github.com/user-attachments/assets/7e6fa63f-ef1e-4c09-aac2-7bddaa9ea9be)

#### **Worst-Case Environment - Performance Comparison**
![Bar Chart Worst](https://github.com/user-attachments/assets/a8ca040f-7060-4b14-99cf-1ab992dbd8a6)

---

### **Performance Distribution**
Box plots below display the **spread of agent performance scores** in each environment, highlighting variability.

#### **Default Environment - Performance Distribution**
![Box Plot Default](https://github.com/user-attachments/assets/a8597a77-58b8-4bc9-a361-e7b52a3b2437)

#### **Worst-Case Environment - Performance Distribution**
![Box Plot Worst](https://github.com/user-attachments/assets/c8e5c9bf-b334-4353-8bb2-2543fc2c3fb2)

---

### **Performance Over Time**
Line charts illustrate **how cumulative agent performance evolves** throughout the simulation.

#### **Reflex Agent - Default Environment**
![Line Chart Reflex Default](https://github.com/user-attachments/assets/6c50c66e-d698-4560-bc58-c17f9e2b6bfb)

#### **Rational Agent - Worst Environment**
![Line Chart Rational Worst](https://github.com/user-attachments/assets/938f6ce4-c6b2-4caf-9e63-8244a355bb61)

---

### **Agent Movement and Spatial Coverage**
Heatmaps represent **how frequently each agent visits different locations** within the environment.

#### **Reflex Agent - Default Environment**
![Heatmap Reflex Default](https://github.com/user-attachments/assets/d15018d1-6385-441d-afdb-87435efeafde)

#### **Rational Agent - Worst Environment**
![Heatmap Rational Worst](https://github.com/user-attachments/assets/c13fd859-4dc9-44e2-86fc-c6d869b26a7d)

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
