# Rapid Path Planning Algorithm for Mobile Robot in Dynamic Environment

## Paper

**Title:** Rapid Path Planning Algorithm for Mobile Robot in Dynamic Environment

**Authors:** Hong-mei Zhang and Ming-long Li

**Published:** Advances in Mechanical Engineering, Volume 9, Issue 12, 2017, pp. 1-12

**Paper:** https://journals.sagepub.com/doi/epub/10.1177/1687814017747400

**Type:** Experimental Algorithm / Dynamic Path Planning / Robotics

---

## Problem

The paper studies path planning for a mobile robot operating in a dynamic environment.

The general objective of path planning is to move a robot from an initial state to a goal state while minimizing the total cost of the path.

This becomes more difficult in a dynamic environment because the robot may encounter moving obstacles that were unknown when the original path was calculated.

A path that was optimal when the robot began moving may therefore become unsafe or unusable later.

The robot must be able to:

1. Calculate an initial path to the goal.
2. Detect moving obstacles.
3. Predict possible collisions.
4. Modify its path when necessary.
5. Perform re-planning quickly enough for real-time navigation.

The paper focuses particularly on reducing the computational cost of this re-planning process.

---

## Environment Representation

The environment is represented using a grid.

The map is divided into equally sized cells, with each cell representing a possible state of the robot.

Each state can be connected to as many as eight neighboring states.

The environment contains:

- free cells,
- known static obstacles,
- and unknown moving obstacles.

Static obstacles are known before the robot begins moving.

Moving obstacles are initially unknown and are detected by the robot's sensors during navigation.

In the first simulation environment, the authors use a:

`50 x 50`

grid.

The robot begins at:

`S = (3, 8)`

and attempts to reach:

`G = (45, 46)`.

The robot can move horizontally, vertically, or diagonally between neighboring cells.

---

## Main Idea

The authors propose a rapid path planning algorithm that combines:

- Dijkstra's algorithm,
- A* search,
- collision prediction,
- and the rolling window principle.

The basic strategy is:

Initial Environment
-> Dijkstra Pre-processing
-> Calculate Initial Global Path
-> Robot Begins Moving
-> Detect Moving Obstacles
-> Predict Possible Collision
-> Select Local Target
-> Use A* for Local Re-planning
-> Rejoin Known Path
-> Continue Toward Goal

The central idea is that the robot should not calculate an entirely new global path every time something changes.

Instead, it performs local re-planning when necessary.

---

## Role of Dijkstra's Algorithm

Dijkstra's algorithm is used during the initial planning stage.

Rather than calculating only one path from the starting position to the goal, the algorithm expands outward from the goal and calculates optimal path costs from the goal to the obstacle-free states in the environment.

These paths and costs are stored.

Conceptually:

Goal
-> Explore Free States
-> Calculate Minimum Costs
-> Store Paths Toward Goal

This creates previously calculated information that can later be reused when the robot encounters a moving obstacle.

The disadvantage is that this initial preprocessing requires more work than simply searching for one source-to-goal path.

The advantage is that the stored information can make later re-planning much faster.

---

## Role of A* Search

A* is used for local re-planning.

Unlike Dijkstra's algorithm, A* incorporates heuristic information to focus the search.

The paper represents its estimated path cost using:

`f(X) = g(X) + h(X)`

where:

- `g(X)` represents known path-cost information,
- `h(X)` represents heuristic estimated cost,
- `f(X)` represents the estimated total cost.

The paper uses diagonal distance as its heuristic.

When a possible collision is detected, A* searches for an optimal local path from the robot's current location to a selected local target.

The robot can then continue from that local target toward the original goal using previously calculated path information.

---

## Rolling Window Principle

The robot does not have complete knowledge of moving obstacles throughout the entire environment.

Instead, its sensors observe a limited area surrounding its current position.

This local detection area acts as an observation window.

As the robot moves, the window moves with it.

When a moving obstacle enters the detection range, the robot examines the local environment and determines whether the obstacle is likely to interfere with its current path.

This allows the planner to respond to new information without repeatedly solving the entire global planning problem.

---

## Collision Prediction

When a moving obstacle is detected, the algorithm attempts to determine whether the robot and obstacle are likely to collide.

The prediction uses information including:

- robot position,
- robot speed,
- obstacle position,
- obstacle speed,
- obstacle movement direction,
- sensor detection range,
- and safety distance.

If no collision is predicted, the robot continues following its existing path.

If a collision is predicted, local re-planning begins.

The detailed geometric equations used to predict collisions are specific to the robotics application and are not central to the graph-search comparison studied in this repository.

---

## Local Target Selection

If a collision is predicted, the algorithm selects a local target within the robot's observation region.

Choosing the local target is important.

Selecting an arbitrary nearby state could allow the robot to avoid an obstacle but produce an unnecessarily expensive path.

The proposed method uses previously calculated path-cost information from Dijkstra's algorithm when selecting the local target.

For candidate state `X`, the paper evaluates a cost of the form:

`f(R, X) = g(X) + h(R, X)`

where:

- `R` is the robot's current position,
- `X` is a candidate local target,
- `g(X)` is the previously calculated minimum cost from `X` to the goal,
- `h(R, X)` estimates the cost from the robot to `X`.

The candidate with the minimum estimated total path cost is selected.

A* is then used to construct the local path from the robot to that target.

---

## Complete Proposed Algorithm

The overall procedure can be summarized as:

1. Convert the environment into a grid.
2. Use Dijkstra's algorithm to preprocess the known static environment.
3. Store optimal path information toward the goal.
4. Begin moving the robot along the initial path.
5. Detect moving obstacles using sensors.
6. Predict whether a collision will occur.
7. If no collision is predicted, continue on the current path.
8. If a collision is predicted, select a local target.
9. Use A* to calculate a local path to that target.
10. Reconnect with the previously calculated path toward the goal.
11. Continue until the goal is reached.

The proposed algorithm therefore combines global preprocessing with local search.

---

# Experimental Evaluation

## Purpose of the Experiments

The authors first demonstrate that the proposed algorithm can successfully guide the robot around moving obstacles.

They then conduct comparative simulation experiments to evaluate its performance against other path-planning approaches.

The comparison includes:

- Ant Colony Optimization (ACO)
- A* Search
- D* Search
- Proposed Rapid Path Planning Algorithm

This is particularly relevant to experimental algorithm research because multiple algorithms are evaluated using defined performance metrics.

---

## Experimental Metrics

The authors compare the algorithms using four primary measurements.

### Path Length

The total distance traveled by the robot.

A shorter path generally represents a better route if other conditions are equivalent.

### Pre-processing Time

The amount of computation required before the robot begins moving.

This measures the initial planning cost of the algorithm.

### Re-planning Times

The number of times the robot must calculate a new path while navigating.

Different algorithms may encounter moving obstacles at different locations because their initial paths are different.

Therefore, the number of re-planning events may differ.

### Average Re-planning Time

The average amount of computation required to produce a new path after a possible collision is detected.

This metric is especially important in a dynamic environment because the robot must respond to changing conditions quickly.

---

## First Experimental Comparison

The four algorithms are initially evaluated in the same simulation environment.

The reported results are:

| Algorithm | Path Length (m) | Pre-processing Time (ms) | Re-planning Times | Average Re-planning Time (ms) |
| --- | ---: | ---: | ---: | ---: |
| ACO | 64.4 | 1304 | 2 | 232 |
| A* | 62.4 | 48 | 2 | 42 |
| D* | 63.3 | 163 | 2 | 32 |
| Rapid Path Planning | 63.3 | 135 | 3 | 3 |

The proposed method does not dominate every metric.

A* has the lowest initial preprocessing time.

However, the proposed method has substantially lower average re-planning time.

Compared with A*, the authors report that the proposed method reduces average re-planning time by approximately:

`92.9%`

The trade-off is that its preprocessing time is approximately:

`2.8x`

that of A*.

This demonstrates an important experimental point:

**An algorithm can perform better according to one metric while performing worse according to another.**

---

# Experiments in a More Complex Environment

The authors then create a larger:

`200 x 200`

environment.

The environment contains known static obstacles and eight unknown moving obstacles.

The robot travels at:

`1 m/s`

and has a sensor detection radius of:

`7 m`.

The moving obstacles have different starting positions, speeds, and directions.

---

## Multiple Experimental Scenarios

Three simulation experiments are performed for each algorithm.

The start and goal locations are changed between experiments.

### Experiment 1

Start:

`(8, 12)`

Goal:

`(190, 180)`

### Experiment 2

Start:

`(18, 188)`

Goal:

`(185, 35)`

### Experiment 3

Start:

`(180, 183)`

Goal:

`(6, 30)`

The algorithms are therefore evaluated across multiple source-target configurations rather than only one path-planning scenario.

---

## Complex Environment Results

### Experiment 1

| Algorithm | Path Length (m) | Pre-processing (ms) | Re-planning Times | Avg. Re-planning (ms) |
| --- | ---: | ---: | ---: | ---: |
| ACO | 268.7 | 6740 | 1 | 1206 |
| A* | 255.7 | 417 | 1 | 65 |
| D* | 255.7 | 2947 | 1 | 13 |
| Rapid Path Planning | 255.7 | 2568 | 1 | 4 |

### Experiment 2

| Algorithm | Path Length (m) | Pre-processing (ms) | Re-planning Times | Avg. Re-planning (ms) |
| --- | ---: | ---: | ---: | ---: |
| ACO | 231.9 | 6029 | 2 | 955 |
| A* | 231.5 | 154 | 2 | 53 |
| D* | 231.5 | 2614 | 2 | 15 |
| Rapid Path Planning | 231.5 | 2387 | 2 | 7 |

### Experiment 3

| Algorithm | Path Length (m) | Pre-processing (ms) | Re-planning Times | Avg. Re-planning (ms) |
| --- | ---: | ---: | ---: | ---: |
| ACO | 242.1 | 6130 | 2 | 945 |
| A* | 239.1 | 164 | 3 | 75 |
| D* | 238.0 | 2835 | 2 | 14 |
| Rapid Path Planning | 239.1 | 2542 | 3 | 4 |

---

## Experimental Findings

Across the complex-environment experiments, the authors report several patterns.

### ACO

ACO has the worst computational performance among the four tested approaches.

It requires substantially greater preprocessing and re-planning time.

### A*

A* generally has the lowest preprocessing time.

However, when an obstacle requires re-planning, it performs a new global search from the robot's current position to the goal.

Its average re-planning time is therefore greater than that of the proposed method in these experiments.

### D*

D* performs substantially better than A* and ACO in re-planning time in the reported experiments.

Its initial preprocessing time is relatively high.

### Rapid Path Planning

The proposed algorithm requires considerable initial preprocessing because Dijkstra's algorithm computes path information throughout the free environment.

However, it can reuse this information and perform smaller local A* searches when moving obstacles appear.

The authors report that its average re-planning time is lower than the other three algorithms across the tested complex-environment scenarios.

They report reductions in average re-planning time of approximately:

`53.3% - 99.7%`

relative to the compared algorithms, depending on the algorithm and experiment.

---

## Important Trade-Off

One of the most useful findings from this paper is the distinction between:

**Initial computation cost**

and

**Dynamic re-planning cost**

The proposed algorithm performs more work before the robot begins moving so that less work may be required later.

Conceptually:

More Pre-processing
-> Store Useful Path Information
-> Environment Changes
-> Reuse Previous Information
-> Smaller Local Search
-> Faster Re-planning

A* follows a different trade-off in these experiments:

Less Initial Processing
-> Environment Changes
-> Perform New Global Search
-> Greater Re-planning Cost

This shows why evaluating an algorithm using only one performance metric can hide important behavior.

---

## Experimental Methodology

The experimental structure of this paper is useful for designing algorithm comparisons.

The authors:

1. Define a controlled simulation environment.
2. Select multiple algorithms.
3. Define measurable performance criteria.
4. Run the algorithms in the same environment.
5. Record numerical results.
6. Introduce a more complex environment.
7. Change the start and goal positions.
8. Repeat the comparison.
9. Analyze performance trade-offs rather than relying only on theoretical complexity.

This provides a practical example of empirical algorithm evaluation.

---

## Limitations

The experiments are designed specifically for mobile robot path planning in dynamic grid environments.

The paper does not systematically vary general graph properties such as:

- graph density,
- arbitrary graph topology,
- degree distribution,
- weighted vs. unweighted structure,
- directed vs. undirected structure,
- or large ranges of graph sizes.

The comparison also includes algorithms designed for different path-planning strategies, including the authors' specialized hybrid approach.

Therefore, the results should not be interpreted as general evidence that one algorithm is superior across arbitrary graphs.

The experiments demonstrate performance within the particular dynamic path-planning environments studied by the authors.

The paper also uses a relatively small number of complex-environment scenarios, with three start-goal configurations reported in the larger environment.

---

# Connection to My Research

This paper is directly useful to the experimental methodology of my graph-search research.

My project investigates how graph characteristics affect the behavior and performance of search algorithms.

Although Zhang and Li focus on dynamic robot navigation rather than general graph structures, their experimental process demonstrates several principles that can be adapted to my work.

## Controlled Inputs

Algorithms should be evaluated under comparable conditions.

For my experiments, compatible algorithms should operate on the same generated graph instances whenever a direct comparison is being made.

## Multiple Metrics

The paper demonstrates why runtime alone may not completely describe algorithm performance.

Possible measurements for my experiments include:

- execution time,
- peak memory usage,
- vertices processed,
- edges examined,
- relaxation attempts,
- queue or priority-queue operations,
- path cost,
- and path optimality.

The exact metrics should depend on the algorithms being compared.

## Repeated Experimental Conditions

Zhang and Li evaluate their algorithms using multiple start-goal configurations.

Similarly, my experiments should avoid drawing conclusions from a single graph or source-target pair.

Multiple graph instances and source-target configurations can help determine whether an observed result is consistent or specific to one case.

## Problem Complexity

The authors test both an initial environment and a larger, more complex environment.

My project can extend this idea more systematically by controlling graph properties such as:

Graph Size
-> Graph Density
-> Connectivity
-> Weight Structure
-> Graph Topology

and observing how algorithm behavior changes.

## Performance Trade-Offs

The paper shows that an algorithm may perform well according to one metric and poorly according to another.

A* performs well in preprocessing time in their experiments, while the proposed algorithm performs much better in re-planning time.

Therefore, my experiments should avoid reducing performance to a single statement such as:

"Algorithm A is faster than Algorithm B."

A more meaningful question is:

**Under which graph conditions, and according to which metric, does an algorithm perform better or worse?**

---

## Difference From My Research

The paper asks approximately:

> How can dynamic mobile-robot path re-planning be made faster while maintaining effective paths?

My research asks a different question:

> How do different graph structures and problem characteristics affect the behavior and performance of graph search algorithms?

The paper changes the algorithm and path-planning scenario.

My research intends to systematically change characteristics of the graph itself.

This makes the paper highly useful for experimental methodology while leaving a different research question for my project to investigate.

---

## What I Learned

This paper helped connect theoretical graph-search algorithms with experimental computer science research.

Knowing the theoretical complexity of an algorithm is not enough to completely describe how it behaves in a particular application.

Algorithms can have different computational trade-offs depending on:

- when computation occurs,
- what information is stored,
- what information can be reused,
- the environment being searched,
- and the performance metric being measured.

The experiments also demonstrate the importance of comparing algorithms under controlled conditions and recording multiple quantitative measurements.

Most importantly, the paper reinforces the idea that the experimental question should not simply be:

**Which algorithm is best?**

A more useful question is:

**Under what conditions does each algorithm perform well or poorly, and why?**

This principle is central to the experimental direction of my graph-search research.
