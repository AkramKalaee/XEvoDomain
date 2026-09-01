# XEvoDomain

### Learning-Guided White-Box Test Generation for Autonomous Driving Systems

XEvoDomain is a **learning-guided, multi-objective test generation framework** for autonomous driving systems with rule-based decision-making components.

The framework uses **critical execution paths**, **behavioral-region learning**, and **white-box information from the system under test** to generate test scenarios that target critical behavioral regions and expose undesirable system behavior.

XEvoDomain was developed for simulation-based testing of autonomous driving systems using the **CARLA simulator**.

<p align="center">
  <img src="docs/images/xevodomain-overview.png" width="750" alt="XEvoDomain overview">
  <br>
  <em>Overview of the XEvoDomain framework.</em>
</p>

---

## Overview

Autonomous driving systems operate in complex environments where undesirable behavior may only emerge under specific combinations of environmental and system conditions.

XEvoDomain addresses this challenge by directing test generation toward **critical execution paths** and progressively learning the **behavioral regions** associated with the system's behavior.

The framework combines:

* **White-box testing** to exploit internal execution information
* **Critical-path analysis** to identify interaction-intensive execution paths
* **Multi-objective evolutionary search** using NSGA-II
* **Behavioral-region learning** to guide the search iteratively
* **Surrogate models** to improve search efficiency
* **Rule learning** to characterize undesirable behavioral regions

The central idea is to move from simply generating diverse scenarios toward systematically exploring **where and under which conditions the autonomous system exhibits undesirable behavior**.

---

## 🎯 Key Contributions

### 1. Behavior-Oriented Test Requirements

XEvoDomain introduces a behavior-oriented criterion for identifying test requirements based on **critical execution paths**.

A path with more interactions with the surrounding environment is considered more critical because it exposes a larger portion of the system's behavior.

### 2. Critical-Path Boundary Coverage

The framework introduces a boundary-oriented criterion for measuring how effectively generated tests explore the domain of a target critical path.

### 3. Learning-Guided Multi-Objective Search

XEvoDomain combines behavioral-region learning with **NSGA-II** to progressively guide the evolutionary search toward critical and failure-prone regions.

### 4. White-Box Behavioral Guidance

Instead of relying only on observable input/output behavior, XEvoDomain exploits internal execution information, including critical paths, to provide more precise search guidance.

### 5. Ensemble Rule Learning

Multiple rule-learning models are used to characterize behavioral regions and guide subsequent exploration, providing broader coverage than relying on a single rule-learning model.

---

## 🔬 Testing Approach

The XEvoDomain testing process can be summarized as:

```text
Initial Test Population
          ↓
   CARLA Simulation
          ↓
   Behavior Collection
          ↓
 Behavioral-Region Learning
          ↓
 Multi-Objective Evolutionary Search
          ↓
  New Test Scenarios
          ↓
     More Simulation
          ↓
Failure Characterization
          ↓
    Rule Extraction
```

The process is **incremental**. Knowledge obtained from previously generated tests is incorporated into subsequent search iterations.

This allows the framework to progressively refine its understanding of the system's behavioral space.

---

## 🧩 Critical Execution Paths

XEvoDomain uses white-box information from the autonomous driving system to identify execution paths that contain substantial interaction with the environment.

For example, a function such as `cruise_control` can be represented through its **control-flow graph (CFG)**. The framework analyzes such execution information to identify paths that are important for system-level behavioral testing.

<p align="center">
  <img src="docs/images/cruise-control-cfg.png" width="700" alt="Cruise control function and control-flow graph">
  <br>
  <em>Example of the <code>cruise_control</code> function and its control-flow graph used for critical-path analysis.</em>
</p>

The selected critical paths become behavioral test requirements for the evolutionary search.

---

## 🗺️ Behavioral Search Space

For each target critical path, XEvoDomain searches for input conditions that exercise the path and expose undesirable behavior.

The domain of the input variables associated with a target path effectively partitions the search space and provides a behavior-oriented target for test generation.

<p align="center">
  <img src="docs/images/search-space-partitioning.png" width="700" alt="Search-space partitioning by the input domain of a target path">
  <br>
  <em>Illustration of search-space partitioning according to the input domain of a target critical path.</em>
</p>

The evolutionary search simultaneously considers:

* proximity to undesirable behavior,
* proximity to critical-path boundaries, and
* behavioral exploration.

---

## 🧠 Learning Behavioral Regions

The failure pattern of a decision-making component can be complex and difficult to describe explicitly.

XEvoDomain therefore uses machine-learning models to identify behavioral regions during the testing process.

A **behavioral region** represents a set of input conditions associated with a particular system behavior.

The search proceeds iteratively:

1. Generate an initial set of test scenarios.
2. Execute the scenarios in CARLA.
3. Collect their input, execution, and behavioral information.
4. Learn behavioral regions from the accumulated test data.
5. Use the learned regions to construct the next search population.
6. Generate and execute new tests.
7. Update the behavioral knowledge with the new observations.

This feedback loop allows the search to focus progressively on regions that are more relevant to undesirable behavior.

---

## 📐 Rule Extraction

After the learning-guided search, the accumulated test data is used to extract interpretable rules describing the identified behavioral regions.

<p align="center">
  <img src="docs/images/rule-extraction.png" width="700" alt="Behavioral rule extraction">
  <br>
  <em>Illustration of behavioral-rule extraction from the accumulated test data.</em>
</p>

These rules provide an interpretable description of the conditions under which particular behaviors occur and can be used to characterize critical or failure-prone regions.

---

## 📊 Experimental Evaluation

XEvoDomain was evaluated on an autonomous driving system with a rule-based decision-making component using the CARLA simulator.

The experimental evaluation investigates:

| Aspect                               | Evaluation                                               |
| ------------------------------------ | -------------------------------------------------------- |
| **Behavioral-region identification** | Ability to discover relevant behavioral regions          |
| **Failure detection**                | Ability to expose undesirable system behavior            |
| **Boundary detection**               | Ability to identify behavioral boundaries                |
| **Search effectiveness**             | Quality of the multi-objective evolutionary search       |
| **Behavioral diversity**             | Diversity of the discovered behavioral conditions        |
| **Rule consistency**                 | Agreement between extracted rules and reference behavior |

### Behavioral-Region Identification

The effectiveness of selected test-generation approaches is compared in identifying behavioral regions.

<p align="center">
  <img src="docs/images/behavioral-region-comparison.png" width="700" alt="Behavioral-region identification comparison">
  <br>
  <em>Comparison of selected approaches in identifying behavioral regions.</em>
</p>

### Behavioral Boundaries

The experiments also evaluate the ability of different approaches to identify the boundaries between behavioral regions.

The distribution of boundary test pairs provides an additional view of how effectively the generated tests explore behavioral transitions.

Additional experimental figures and tables are available in the [`docs/`](docs/) directory.

---

## 🔎 Research Findings

The experimental results indicate that incorporating **white-box information** into test generation can substantially improve the search for behavioral regions compared with black-box approaches.

In particular:

* Critical execution paths provide more targeted guidance than black-box behavioral information alone.
* Learning behavioral regions during the search improves the exploration of failure-prone areas.
* Ensemble rule learning provides broader behavioral exploration than relying on a single rule-learning model.
* XEvoDomain achieves stronger performance than the evaluated baseline approaches in behavioral-region identification and boundary detection.
* The behavioral rules identified by XEvoDomain are consistent with those obtained by the evaluated black-box approach, while providing additional guidance from internal system behavior.

---

## 🚗 CARLA-Based Testing

XEvoDomain uses **CARLA 0.9.9** for simulation-based testing.

The experiments use predefined routes and simulated driving scenarios to evaluate the behavior of the autonomous driving system under different environmental conditions.

The framework generates test scenarios, executes them in the simulator, collects execution and behavioral information, and feeds the results back into the learning-guided search.

---

## ⚙️ Installation

### System Requirements

The original implementation was developed and evaluated using:

* **Operating System:** Windows
* **Python:** 3.7
* **CARLA:** 0.9.9
* **Scenario Runner:** 0.9.8

> The repository reflects the environment used for the original experiments. Newer versions of CARLA, Python, or Scenario Runner may require compatibility adjustments.

### 1. Install CARLA

Install **CARLA 0.9.9** and extract it to a location of your choice.

### 2. Configure the CARLA Python API

The repository contains the Python API used by the experiments.

Replace the default `PythonAPI` directory in the CARLA installation with the compatible version provided in this repository:

```text
<repository>/CARLA_0.9.9/PythonAPI
        ↓
<your CARLA installation>/PythonAPI
```

> This step ensures compatibility between XEvoDomain and the CARLA version used in the experiments.

### 3. Create the Python Environment

Using Anaconda:

```bash
conda create -n xevodomain_env python=3.7
conda activate xevodomain_env
```

### 4. Install Dependencies

From the repository root:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running XEvoDomain

Make sure the CARLA simulator is running before starting the framework.

From the repository root:

```bash
python scenario-runner/explorer.py
```

> If the main script has a different location in your local version of the repository, use the corresponding script path shown in the repository structure.

---

## 📂 Repository Structure

The repository is organized directly from the project root:

```text
XEvoDomain/
│
├── configs/
├── CARLA_0.9.9/
├── scenario-runner/
├── leaderboard/
├── dataset/
├── roads/
├── tools/
├── docs/
│   └── images/
│       ├── xevodomain-overview.png
│       ├── cruise-control-cfg.png
│       ├── search-space-partitioning.png
│       ├── rule-extraction.png
│       ├── behavioral-region-comparison.png
│       ├── boundary-pair-distribution.png
│       └── boundary-detection-comparison.png
│
├── requirements.txt
├── README.md
└── LICENSE
```

> The exact directory contents may vary depending on the included CARLA and experiment files. The important point is that the project files are located at the **repository root**, rather than under a `src/` directory.

---

## 📤 Outputs

The framework produces test scenarios, simulation results, behavioral information, and rule-learning outputs during execution.

Typical outputs include:

* Generated test scenarios
* Simulation logs
* Execution traces
* Behavioral-region information
* Failure-model data
* Extracted behavioral rules
* Search and evaluation metrics

The exact output location depends on the configuration used for the experiment.

---

## 🛠️ Troubleshooting

### CARLA Does Not Start or Connect

Make sure:

* CARLA 0.9.9 is running.
* The correct CARLA server instance is being used.
* No previous CARLA process is interfering with the connection.

Restart CARLA if necessary.

### PythonAPI Errors

Verify that the Python API from this repository is compatible with **CARLA 0.9.9** and that the required `PythonAPI` files have been installed correctly.

### Missing Dependencies

Reinstall the required packages:

```bash
pip install -r requirements.txt
```

### Scenario Runner Issues

Make sure that the repository uses **Scenario Runner 0.9.8** with **CARLA 0.9.9**.

Mixing incompatible versions can result in import errors or simulator-connection problems.

---

## 📚 Additional Experimental Material

Additional figures and tables from the experimental study are provided in the [`docs/`](docs/) directory.

These materials include:

* Comparison of selected approaches for behavioral-region identification
* Extracted rules for critical behavioral regions
* Selected critical execution paths
* I/O calls appearing more than once in the execution paths
* Distribution of boundary scenario pairs
* Comparison of boundary-detection effectiveness

---

## 🔬 Research Context

XEvoDomain was developed as part of the Ph.D. research on:

**Domain Analysis and Its Effect on Improving Testability and Explainability of Learning-based Cyber Physical Systems**

The framework represents the system-level testing approach developed for systems with **rule-based decision-making components**.

The research investigates how internal execution information and learned behavioral knowledge can be combined with evolutionary search to improve the effectiveness of testing complex autonomous systems.

The dissertation contains additional technical details, mathematical formulations, experimental settings, figures, tables, and analyses.

---

## License

This project is released under the license specified in [`LICENSE`](LICENSE).

---

## Author

**Akram Kalaee**
Ph.D. in Software Engineering
Iran University of Science and Technology
