# Graph Theory-Based Complete Coverage Path Planning for Reconfigurable Robots

## Paper

**Title:** Graph Theory-Based Approach to Accomplish Complete Coverage Path Planning Tasks for Reconfigurable Robots

**Authors:** Ku Ping Cheng, Rajesh Elara Mohan, Nguyen Huu Khanh Nhan, Anh Vu Le

**Published:** IEEE Access, Volume 7, 2019, pp. 94642-94657

**Paper:** https://ieeexplore.ieee.org/document/8761971

**Type:** Applied Graph Theory / Robotics / Path Planning Research

---

## Problem

The paper studies the **Complete Coverage Path Planning (CCPP)** problem for a self-reconfigurable robot called **hTetro**.

Unlike ordinary shortest-path problems, where the goal is generally to move from a starting point to a destination with minimum cost, complete coverage path planning requires the robot to cover the accessible workspace.

This introduces a different optimization problem:

- The workspace should be covered as completely as possible.
- Obstacles must be avoided.
- The robot may need to change its shape while navigating.
- The total number of robot actions should be minimized.

The ability of hTetro to change shape provides additional navigation possibilities, but it also increases the complexity of the path-planning problem.

---

## The hTetro Robot

hTetro is a modular self-reconfigurable floor-cleaning robot composed of four square blocks connected through active hinges.

The robot can transform between several tetromino-like shapes.

Because the robot can change morphology, its state cannot be represented only by its position.

The paper represents a robot configuration using:

- x-coordinate
- y-coordinate
- orientation of block 1
- orientation of block 2
- orientation of block 3
- orientation of block 4

This allows the path planner to represent both the robot's location and its current morphology.

---

## Workspace Representation

The environment is represented using a **grid-based decomposition**.

The workspace is divided into uniform square cells.

Each grid cell records whether it is:

- an obstacle,
- uncovered,
- or already covered by the robot.

The paper refers to this information as **grid activity**.

A grid containing an obstacle receives an activity value of -1.

An uncovered accessible grid begins with an activity value of 0.

Once the robot covers the grid, its activity becomes 1.

The workspace is considered completely covered when every accessible grid has been covered.

---

## Graph Representation

The authors transform the robot navigation problem into a graph problem.

The hTetro workspace is represented as a **weighted graph**.

A vertex represents a possible robot configuration at a particular grid location.

Because the robot can have multiple morphologies, the graph contains multiple **morphology layers**.

Within a morphology layer, edges represent possible movements of the robot while keeping the same morphology.

Edges between morphology layers represent changes in robot shape while remaining at the same grid position.

Therefore, the graph represents both:

1. movement through the environment, and
2. transformation of the robot.

If there are:

- `nrow` rows,
- `ncol` columns,
- `nshape` allowed robot morphologies,

the workspace graph contains approximately:

`nrow * ncol * nshape`

vertices.

As the workspace and number of available morphologies increase, exhaustive search over the entire graph becomes increasingly impractical.

---

## Graph Partitioning

To reduce the size of the search problem, the authors divide the workspace graph into smaller regions called **stripe layer subgraphs**.

Instead of solving the complete coverage problem over the entire workspace graph at once, the algorithm solves smaller coverage problems inside individual stripes.

Conceptually:

Workspace Graph
-> Stripe Layer Subgraphs
-> Solve Coverage Within Each Stripe
-> Connect Stripe Solutions
-> Construct Final Robot Path

The stripe partitioning strategy reduces the size of the individual search spaces that must be explored.

---

## Recursive Backtracking

Inside each stripe layer, the paper uses a **recursive backtracking algorithm**.

The authors describe backtracking as a modified form of depth-first search.

The algorithm explores possible robot actions and builds candidate paths.

If an action produces an invalid or non-promising path, the algorithm restores the previous state and explores another possibility.

During the search, the algorithm checks:

- whether the robot action is valid,
- whether collisions occur,
- whether the required area has been covered,
- and the action cost of the candidate path.

The objective is to achieve maximum coverage while minimizing total action cost.

---

## Dynamic Programming and Memoization

The authors use **dynamic programming and memoization** to avoid repeatedly solving the same expensive subproblems.

Coverage calculations within stripe layers are treated as subproblems.

Once the cost of traversing a stripe configuration has been calculated, the result can be stored and reused later.

Several tables are used to cache information such as:

- valid robot actions,
- action costs,
- paths through stripe subgraphs,
- and edge weights.

This reduces unnecessary recomputation during the search process.

---

## Auxiliary Graph

After the individual stripe-layer costs have been determined, the authors construct a higher-level **auxiliary graph**.

Vertices in this graph represent possible transitions between stripe layers.

Edge weights incorporate:

- the cost of covering stripe layers,
- and the cost of moving between stripes.

The auxiliary graph therefore represents the higher-level decision:

**Which sequence of stripe transitions produces the lowest total action cost?**

---

## Dijkstra's Algorithm

Once the auxiliary graph and its edge weights are known, the paper applies **Dijkstra's algorithm with a priority queue**.

Dijkstra's algorithm determines the minimum-cost path through the auxiliary graph.

The selected path determines which robot morphologies and transition positions should be used when moving between stripe layers.

The final roadmap is then constructed by combining the stored paths from the selected stripe solutions.

Therefore, Dijkstra is not being used directly to solve the entire complete-coverage problem.

Instead, it solves the higher-level shortest-path problem created after the original workspace has been partitioned into smaller subproblems.

---

## Experimental Evaluation

The proposed approach is evaluated through simulations using **MATLAB Simulink**.

The paper demonstrates the algorithm on grid-based workspaces containing obstacles.

One example uses a `16 x 7` grid and allows two hTetro morphologies.

The generated path successfully connects the stripe-layer solutions, with the auxiliary-graph Dijkstra search producing a total action cost of 73 for the demonstrated configuration.

The authors also conduct experiments examining how the algorithm's starting variables affect performance.

---

## Experimental Variables

Two important starting variables are examined:

### Stripe Column Width

The workspace is divided into stripe layers.

Different stripe widths affect the amount of space available for robot movement and transformation.

Stripes that are too narrow can restrict possible robot morphologies and make navigation around obstacles more difficult.

### Allowed Robot Morphologies

The authors also vary which hTetro morphologies the planner is allowed to use.

Allowing additional morphologies provides the robot with more possible ways to navigate and cover difficult regions.

---

## Evaluation Metrics

The starting-variable configurations are evaluated using several criteria.

### Complete Coverage

The algorithm must successfully generate a path capable of covering the accessible workspace.

### Total Action Cost

Robot movements and transformations have associated costs.

The planner attempts to minimize the total cost of the actions required to complete the coverage task.

### Coverage Overlap

The authors also examine how frequently areas are covered multiple times.

Repeated coverage can indicate inefficient movement.

The simulation estimates this by examining how long different portions of the workspace remain covered by the robot during navigation.

---

## Results

The experiments show that the choice of starting variables affects the resulting navigation strategy.

In the `16 x 16` workspace experiment, the authors compare different stripe-width configurations and combinations of robot morphologies.

The tested configuration using all three selected morphologies with the `Nstr,2` stripe setup produced the best performance among the tested configurations, including lower action cost and lower average coverage time.

The authors also observe that allowing more robot morphologies can improve navigation efficiency because the robot can select shapes better suited to different parts of the environment.

---

## Limitations

The approach is designed specifically around the geometry and movement capabilities of the hTetro reconfigurable robot.

The optimization problem is also **complete coverage**, rather than the conventional single-source shortest-path problem.

Therefore, the experimental results should not be interpreted as a general comparison showing that one graph-search algorithm is superior to another.

The paper instead demonstrates how several graph and optimization techniques can be combined to solve a specialized robotics problem.

The authors identify possible future improvements including:

- improved graph partitioning strategies,
- alternative optimization objectives such as energy consumption,
- reducing repeated coverage,
- and adapting the approach to other reconfigurable robot platforms.

---

## Connection to My Research

This paper provides an example of how the structure and representation of a graph can directly influence the search strategy used to solve a problem.

The authors do not simply construct one large graph and apply a single search algorithm.

Instead, they:

Workspace
-> Construct Graph Representation
-> Partition Graph
-> Search Smaller Subgraphs
-> Store Subproblem Results
-> Construct Auxiliary Graph
-> Apply Dijkstra
-> Generate Final Solution

This is relevant to my research because I am investigating how graph characteristics influence the behavior and performance of graph search algorithms.

The paper also provides an example of an experimental methodology in which algorithm parameters are systematically varied and the resulting performance is evaluated using predefined metrics.

However, this paper does not directly compare BFS, DFS, Dijkstra, A*, and other graph search algorithms across different graph structures.

Its role in my literature review is therefore primarily as an **applied graph-search and experimental-design example**, rather than direct evidence for my main experimental comparison.

---

## What I Learned

A real-world robotics problem can become significantly easier to reason about once it is represented as a graph.

However, the graph representation itself can become extremely large when additional state information, such as robot morphology, is included in each vertex.

Instead of searching the entire graph directly, the problem can be divided into smaller subproblems using graph partitioning.

Different algorithms can then solve different parts of the overall problem.

In this paper:

- recursive backtracking explores possible coverage paths,
- dynamic programming and memoization reuse previously calculated results,
- graph partitioning reduces the size of individual search problems,
- and Dijkstra's algorithm determines the minimum-cost route through the resulting auxiliary graph.

The paper also demonstrates that algorithm performance can depend on the structure and parameters of the problem being tested.

This reinforces an important idea for my own research:

**Graph representation, graph structure, algorithm design, and evaluation metrics should be considered together when studying graph-search performance.**
