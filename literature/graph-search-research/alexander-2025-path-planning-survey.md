# A Comprehensive Survey of Path Planning Algorithms for Autonomous Systems and Mobile Robots

## Paper

**Title:** A Comprehensive Survey of Path Planning Algorithms for Autonomous Systems and Mobile Robots: Traditional and Modern Approaches

**Authors:** Anusha Alexander, Kalaichelvi Venkatesan, Jinane Mounsef, and Karthikeyan Ramanujam

**Published:** IEEE Access, Volume 13, 2025, pp. 176287-176326

**Paper:** https://ieeexplore.ieee.org/document/11195089

**Type:** Systematic Survey / Literature Review


## Problem

Path planning is one of the fundamental problems in robotics and autonomous systems.

A robot or autonomous vehicle needs to determine how to move from a starting position
to a destination while avoiding obstacles and satisfying constraints imposed by the
environment.

At first, this sounds like a simple shortest-path problem:

> "How do I get from the start to the goal?"

However, real-world environments make the problem much more complicated.

An environment may be:

- Static or constantly changing.
- Completely known or partially unknown.
- Small and simple or extremely large.
- Filled with stationary or moving obstacles.
- Represented as a grid, graph, continuous space, or dynamic map.

Different path planning algorithms behave differently under these conditions.

An algorithm that works well in a small static environment may perform poorly when the
environment becomes large or dynamic. Likewise, an algorithm that produces an optimal
path may require more computational resources than an algorithm that produces a good
path quickly.

The purpose of this survey is therefore not to identify one universally best path
planning algorithm.

Instead, the researchers examine a wide range of traditional and modern approaches,
their strengths and limitations, the environments in which they operate, and the
metrics used to evaluate their performance.


## Research Methodology

Rather than introducing a new path planning algorithm, this paper performs a systematic
review of existing research.

The researchers followed a PRISMA-based literature review process.

They searched several major research databases, including:

- IEEE Xplore
- Web of Science
- ScienceDirect
- SpringerLink
- Google Scholar
- ACM Digital Library

The search focused primarily on path planning research published between 2019 and 2024.

The initial search produced 769 articles.

After removing duplicates and papers that did not satisfy the inclusion criteria, the
researchers retained 188 papers for the final survey.

This is important because the conclusions of the paper are not based on one experiment.

Instead, the authors attempt to combine observations and results from a large collection
of previous studies to understand the broader state of path planning research.


## Path Planning Categories

One of the major ideas in the paper is that path planning algorithms can be classified
according to how they approach the navigation problem.

The survey broadly discusses traditional approaches such as:

- Graph and grid-based algorithms
- Sampling-based algorithms
- Optimization-based algorithms
- Potential field methods
- Bio-inspired algorithms

It also examines modern approaches involving:

- Reactive methods
- Predictive methods
- Optimization techniques
- Machine learning
- Deep learning
- Reinforcement learning
- Hybrid approaches

For my research, the most relevant category is the graph and grid-based family.

These methods represent an environment using structures that can be searched
algorithmically.

A graph representation can be thought of as:

    Location A ----- Location B
         |               |
         |               |
    Location C ----- Location D

The vertices represent possible locations or states.

The edges represent possible transitions or paths between them.

Once the environment has been represented as a graph, algorithms can search that
structure to determine how to reach a goal.


## Graph Search Algorithms

The survey discusses several algorithms that directly overlap with the algorithms I am
studying.


### Depth-First Search

Depth-First Search explores one branch of a graph as deeply as possible before
backtracking and exploring another branch.

The survey describes DFS as useful for tasks such as:

- Graph traversal
- Cycle detection
- Topological sorting
- Pathfinding

DFS can operate on both directed and undirected graphs.

However, DFS does not inherently attempt to find the shortest path.

This distinction is important for my experiments because DFS should not automatically
be treated as solving the same optimization problem as algorithms such as Dijkstra's
algorithm or A*.


### Breadth-First Search

Breadth-First Search explores the graph level by level.

Instead of following one branch deeply, BFS first explores the neighboring vertices,
then the vertices one step farther away, and so on.

Conceptually:

```text
Start
    |
---------
|       |
A       B
|       |
C       D
```

BFS explores:

    Start -> A/B -> C/D -> ...

This makes BFS useful for traversal and shortest-path problems in appropriate
unweighted or equal-cost graph settings.

The survey also notes that BFS may experience computational overhead as the search
space becomes large.

This is particularly relevant to my research because one of the questions I want to
investigate is how changes in graph structure and size affect the amount of work
performed by different search algorithms.


### Dijkstra's Algorithm

Dijkstra's algorithm is one of the foundational shortest-path algorithms discussed in
the survey.

Unlike BFS, Dijkstra's algorithm considers edge costs when determining which vertex
should be explored next.

The basic idea is:

> Always continue from the currently known cheapest reachable vertex.

This allows Dijkstra's algorithm to find shortest paths in graphs with appropriate
non-negative edge weights.

The survey identifies Dijkstra's algorithm as a widely used traditional path planning
method because it is reliable and capable of producing optimal paths.

However, its computational requirements can become a disadvantage as the search space
becomes larger and more complicated.


### A* Search

A* extends shortest-path search by using heuristic information about the goal.

Instead of considering only the cost already accumulated, A* combines:

    f(n) = g(n) + h(n)

where:

- `g(n)` represents the known cost from the start to the current node.
- `h(n)` estimates the remaining cost from the current node to the goal.

The heuristic gives A* information about which direction appears more promising.

This can allow A* to explore substantially less of the search space than an uninformed
search.

The survey identifies A* as one of the most important traditional path planning
algorithms and discusses its widespread use in robotics.

However, its effectiveness depends heavily on the quality of the heuristic and the
representation of the environment.

This is especially important for my experiments.

If I compare A* with other algorithms, I cannot simply generate arbitrary graphs and
give A* an arbitrary heuristic. The graph must contain enough meaningful information
for a valid heuristic to be defined.


### Bellman-Ford Algorithm

The survey also discusses the Bellman-Ford algorithm.

Bellman-Ford is another shortest-path algorithm, but unlike Dijkstra's algorithm, it
can operate on graphs containing negative edge weights.

This gives Bellman-Ford greater flexibility in the kinds of weighted graphs it can
handle.

However, this flexibility comes with greater computational cost.

This makes Bellman-Ford particularly interesting experimentally because it demonstrates
an important tradeoff:

> Supporting a broader class of graph conditions may require more computation.

It also reinforces the importance of testing algorithms only on graph types that
satisfy their assumptions.


### Bidirectional Search

The survey discusses bidirectional search as another way of reducing the amount of
search required to reach a goal.

Instead of searching only:

    Start -> Goal

the search can proceed from both directions:

    Start -> -> Meeting Point <- <- Goal

If the two searches meet, a complete path can be constructed.

The main motivation is that two smaller search spaces may require less exploration than
one large search space.

This gives me another experimentally measurable question:

> How much search effort can be avoided by searching from both directions?

Rather than measuring only runtime, this could also be studied through the number of
vertices explored or other measures of algorithmic work.


## Static and Dynamic Environments

Another major distinction made throughout the survey is between static and dynamic
environments.

In a static environment, the relevant parts of the environment remain unchanged while
the path is being planned.

For example:

    Start ---- A ---- B ---- Goal

If this graph remains unchanged, the algorithm can calculate a route without worrying
that an edge or obstacle will suddenly change.

Dynamic environments are different.

An obstacle may move.

A previously available path may become blocked.

A new route may become available.

The cost of traveling through part of the environment may change.

This means that a path calculated earlier may no longer be useful.

The survey emphasizes that modern path planning systems increasingly need to operate
under these changing conditions.

This connects directly to the dynamic shortest-path problem I have studied.

Instead of asking only:

> "What is the shortest path?"

a dynamic setting may require asking:

> "The graph changed. How should the path be updated?"

This distinction becomes especially important in robotics because real environments do
not necessarily remain fixed while a robot is moving.


## Performance Evaluation

One of the most useful parts of this survey for my research is its discussion of how
path planning algorithms are evaluated.

The paper identifies several important performance measures, including:

- Success rate
- Computation time
- Path optimality
- Safety
- Adaptability
- Robustness
- Computational resource requirements
- Scalability

These metrics measure different aspects of algorithm performance.

For example, computation time asks:

> "How quickly does the algorithm produce a solution?"

Path optimality asks:

> "How good is the resulting path?"

Resource efficiency asks:

> "How much memory, processing power, or energy does the algorithm require?"

Scalability asks:

> "Does the algorithm continue to perform effectively when the problem becomes larger
> or more complicated?"

The survey identifies success rate, computation time, path optimality, and safety as
particularly important benchmarks for robotics and autonomous vehicles.

However, it also emphasizes that the appropriate metrics depend on the application.

This is an important lesson for my own experiments.

There is no single measurement called "algorithm performance."

Different measurements reveal different behaviors.


## Benchmarking

The survey also discusses the importance of standardized benchmarking.

Path planning algorithms are often tested using simulation platforms and datasets so
that researchers can evaluate algorithms under controlled or repeatable conditions.

Examples discussed in the paper include:

- ROS
- Gazebo
- CARLA
- AirSim
- OpenAI Gym
- KITTI
- BARN

These tools and datasets are mainly designed for robotics and autonomous systems, so
they are not necessarily the benchmarks I will use in my graph algorithm experiments.

However, the underlying idea is directly relevant.

If algorithms are tested under completely different conditions, their results are
difficult to compare.

A meaningful experiment therefore requires controlled inputs and clearly defined
evaluation conditions.

For my research, this reinforces the importance of generating or selecting graph
instances that can be reused across algorithms rather than allowing every algorithm to
operate on a different random graph.


## Findings

The survey concludes that there is no single path planning technique that dominates
every environment and application.

Traditional algorithms such as Dijkstra's algorithm and A* remain important because
they are well understood, reliable, and relatively straightforward to implement.

However, the paper notes that these methods can experience computational difficulties
as the search environment becomes larger and more complex.

Graph-based approaches provide flexibility for representing complex environments, but
their effectiveness also depends on how the graph itself is constructed.

Modern methods attempt to improve characteristics such as adaptability, scalability,
and real-time performance.

The survey also highlights growing interest in hybrid systems that combine multiple
approaches rather than depending on a single algorithm.

The major lesson is therefore not:

> "Algorithm X is the best."

Instead, the paper repeatedly shows that algorithm performance depends on the problem,
environment, representation, and evaluation criteria.


## Limitations

This paper is highly relevant to the background of my research, but it is not a direct
experimental study of the research question I am investigating.

The survey focuses primarily on path planning for mobile robots and autonomous
vehicles.

My research focuses more specifically on experimentally studying graph search
algorithms across different graph structures.

The survey also combines findings from many different studies.

Those studies may use different:

- Hardware
- Programming languages
- Implementations
- Environments
- Datasets
- Graph representations
- Performance measurements

Because of this, the comparisons presented by the survey should not automatically be
interpreted as controlled head-to-head experimental comparisons.

For example, if one study reports that one algorithm performs quickly and another study
reports that another algorithm performs slowly, those results cannot necessarily be
compared directly unless the experimental conditions are similar.

Therefore, this paper is most useful to me as:

- Background literature
- A map of existing path planning research
- A source of experimental evaluation ideas
- A source for discovering more specific empirical studies

The original experimental papers cited by this survey will be more useful when I begin
examining previous experiments that closely resemble my own.


## Connection to My Research

My independent research focuses on experimentally comparing graph search algorithms
across different graph structures.

This survey is much closer to my research than the HELEN paper because several of the
algorithms discussed here directly overlap with the algorithms I am studying.

These include:

- BFS
- DFS
- Dijkstra's algorithm
- A*
- Bellman-Ford
- Bidirectional search

The most important connection, however, is the paper's repeated emphasis that algorithm
performance depends on the environment and the characteristics of the problem.

That connects directly to the question motivating my experiments:

> How does the structure of a graph affect the behavior and performance of different
> graph search algorithms?

The paper also gives me a clearer idea of what "performance" can mean.

Runtime alone is not enough.

Depending on the experiment, useful measurements may include computational time,
resource consumption, path optimality, scalability, and the amount of search performed.

The survey also reinforces the importance of controlled benchmarking.

If I want to determine whether graph structure affects algorithm behavior, I need to
control other variables carefully enough that differences in the results can reasonably
be connected to the graph or algorithm rather than unrelated experimental conditions.


## What I Learned

Before reading this survey, I mostly thought about comparing graph algorithms in terms
of their theoretical properties:

    BFS -> O(V + E)

    DFS -> O(V + E)

    Dijkstra -> depends on the implementation and priority queue

    Bellman-Ford -> O(VE)

Those theoretical complexities are important, but this paper helped me see that
experimental algorithm analysis asks a broader question.

Two algorithms can have known theoretical complexities while still behaving very
differently depending on:

- The structure of the environment
- The size of the search space
- The available information
- The representation of the graph
- The performance metric being measured
- Whether the environment is static or dynamic

I also learned that asking:

> "Which algorithm is fastest?"

is usually too broad.

A better question is:

> "Under what conditions does an algorithm perform well or poorly, and why?"

That distinction is important for my research.

My goal should not simply be to run several algorithms, record their execution times,
and declare a winner.

Instead, I should construct controlled experiments that allow me to observe how changes
in graph structure influence algorithm behavior.

The survey also helped me understand why multiple metrics are necessary.

An algorithm may have:

    Lower runtime

but:

    Explore more vertices

or produce:

    A different quality of path

or require:

    More memory

These measurements describe different properties of the algorithm.

Finally, the paper showed me the importance of looking beyond individual algorithms.

Path planning research does not treat algorithms as isolated pieces of code. Researchers
consider the environment, representation, computational constraints, evaluation
criteria, and application together.

For my research, that leads to a useful mental model:

    Graph Structure
          |
          v
    Algorithm Behavior
          |
          v
    Measured Performance
          |
          v
    Appropriate Algorithm Choice

Rather than asking which graph search algorithm is universally best, I want to better
understand how the characteristics of the graph influence which algorithms are more
appropriate under different conditions.
