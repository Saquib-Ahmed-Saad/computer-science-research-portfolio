# Independent Computer Science Research Portfolio

## Research Focus

**Experimental Analysis of Graph Search Algorithms Across Different Graph Structures**

---

## About

This repository documents my independent study and research project focused on graph algorithms, graph search, and experimental algorithm analysis.

The project began with a structured study of the theoretical foundations behind graph algorithms and has progressed toward the design of controlled experiments investigating how graph characteristics influence the behavior and performance of different search algorithms.

The repository contains:

- theoretical notes and algorithm studies,
- Python implementations,
- graph theory foundations,
- literature review notes,
- experimental planning and methodology,
- research questions,
- and, as the project progresses, experimental results and analysis.

The objective is not simply to compare which algorithm is "fastest," but to investigate how algorithm behavior changes under different graph structures, assumptions, and problem conditions.

---

## Research Question

The central question motivating this project is:

> **How do different graph structures and problem characteristics affect the performance and behavior of graph search algorithms?**

Potential experimental variables include:

- graph size,
- graph density,
- directed vs. undirected graphs,
- weighted vs. unweighted graphs,
- weight distributions,
- connectivity,
- graph topology,
- and source-target configuration.

Potential measurements include:

- execution time,
- memory usage,
- vertices processed,
- edges examined,
- relaxation operations,
- path cost and optimality,
- and algorithm-specific operations.

The final experimental methodology will be refined through literature review and pilot experiments.

---

## Project Status

### Phase 1 - Foundations and Algorithm Study

This is the core graph theory concepts and relevant algorithms that I have studied and documented.

Topics include:

- Graph Theory Fundamentals
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Heaps and Priority Queues
- Topological Sorting
- Dijkstra's Algorithm
- A* Search
- Minimum Spanning Trees
- Union-Find
- 0-1 BFS
- Bidirectional Search
- Multi-Source Search
- Bellman-Ford
- Branch-and-Bound
- Dynamic Shortest Paths

These topics do not necessarily belong to a single experimental comparison. Some provide theoretical or algorithmic foundations, while others may participate directly in specific experiments where their assumptions and objectives are compatible.

### Phase 2 - Literature Review

**Current phase**

The literature review examines prior research involving:

- experimental evaluation of graph search algorithms,
- graph structure and algorithm performance,
- path-planning and graph-search applications,
- experimental methodology and benchmarking,
- and real-world applications of graph algorithms.

The purpose of this phase is to identify established experimental practices, relevant metrics, limitations of previous studies, and opportunities for controlled experimentation.

### Phase 3 - Implementation and Validation

Planned work includes:

- reviewing each relevant algorithm,
- implementing research versions in Python,
- validating correctness,
- standardizing instrumentation,
- and freezing implementations before benchmarking.

### Phase 4 - Experimental Framework

A configurable graph-generation framework will be developed to create reproducible graph instances under controlled conditions.

The framework is expected to support variations in graph properties such as size, density, direction, weighting, connectivity, and topology.

Random seeds and stored graph instances will be used to improve reproducibility and ensure that compatible algorithms are evaluated on equivalent inputs.

### Phase 5 - Experiments and Analysis

After pilot testing and methodology refinement, controlled experiments will be conducted.

Raw measurements will be preserved separately from analysis.

Results will then be examined to determine how changes in graph characteristics influence algorithm behavior and performance.

---

## Repository Structure

```text
algorithms/
    A_Star/
    Bellman_Ford/
    Bidirectional_Search/
    Branch_and_Bound/
    bfs/
    dfs/
    Dijkstra/
    Dynamic_Shortest_Paths/
    Heaps_PriorityQueue/
    Minimum_Spanning_Trees/
    Multi_Source_Search/
    README.md
    Topological_Sort/
    Union_Find/

foundations/
    Graph_Theory/
    README.md

literature/
    graph-applications/
    graph-search-research/
    README.md

references/
    algorithms-and-data-structures/
    graph-search-and-path-planning-research/
    graph-theory-and-network-applications/
    README.md

research-projects/
    graph-search-comparison/
    README.md

future-ideas/
    README.md

roadmap/
    README.md

publications/
    README.md
```

---

## Learning and Research Methodology

Algorithm study follows a consistent process:

1. Study the underlying theory.
2. Develop an intuitive understanding of the algorithm.
3. Implement the algorithm in Python.
4. Examine correctness, complexity, assumptions, and limitations.
5. Investigate questions that may influence experimental behavior.

Research development follows a separate process:

1. Review relevant academic literature.
2. Define experimental questions and hypotheses.
3. Identify appropriate algorithms and compatible problem settings.
4. Design controlled and reproducible graph experiments.
5. Validate and freeze implementations.
6. Collect raw experimental measurements.
7. Analyze results.
8. Interpret findings in relation to theory and previous research.
9. Document limitations and potential future work.

---

## Literature Review

The literature section contains structured notes on academic papers relevant to the project.

Current literature includes work involving:

- graph representations in real-world applications,
- graph-based robotic path planning,
- graph search and path-planning surveys,
- experimental evaluation methodology,
- and benchmarking criteria.

Literature notes distinguish between findings reported by the original authors and interpretations or connections made specifically in relation to this project.

---

## References

The theoretical foundations of this project draw primarily from established algorithm and graph theory resources including:

- *Introduction to Algorithms* (CLRS)
- *Algorithms* by Robert Sedgewick and Kevin Wayne
- MIT OpenCourseWare 6.006 - Introduction to Algorithms

Peer-reviewed research papers used throughout the literature review and experimental design are documented separately in the reference index:

- [references/README.md](references/README.md)

---

## Use of AI Tools

AI-assisted tools, including ChatGPT (OpenAI), were used during this project as supplementary learning and documentation aids. Academic literature, textbooks, and primary sources remain the basis for the technical and research content of this repository.

---

## Future Direction

The immediate focus of the project is completing the initial literature review and transitioning into implementation review and experimental design.

The longer-term goal is to produce a reproducible experimental study examining relationships between graph characteristics and graph-search algorithm behavior, while documenting both successful results and limitations encountered during the research process.
