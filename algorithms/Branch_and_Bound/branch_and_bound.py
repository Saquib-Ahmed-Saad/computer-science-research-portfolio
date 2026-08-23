from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple


@dataclass
class Item:
    """A single item for 0/1 knapsack."""

    weight: int
    value: int


@dataclass
class Node:
    """A state in the Branch and Bound search tree."""

    level: int
    profit: int
    weight: int
    bound: float
    chosen: Tuple[int, ...]


def _upper_bound(node: Node, capacity: int, items: List[Item]) -> float:
    """Fractional knapsack upper bound for remaining items.

    This bound is safe for maximization: it never underestimates what could still
    be achieved from this branch.
    """
    if node.weight >= capacity:
        return 0.0

    profit_bound = float(node.profit)
    total_weight = node.weight
    i = node.level + 1

    # Fill remaining capacity greedily by value/weight order.
    while i < len(items) and total_weight + items[i].weight <= capacity:
        total_weight += items[i].weight
        profit_bound += items[i].value
        i += 1

    # Add fractional part of the next item if any capacity remains.
    if i < len(items):
        remaining = capacity - total_weight
        profit_bound += remaining * (items[i].value / items[i].weight)

    return profit_bound


def branch_and_bound_knapsack(items: Iterable[Item], capacity: int) -> Tuple[int, List[int]]:
    """Solve 0/1 knapsack using Best-First Branch and Bound.

    Returns:
        (best_value, chosen_item_indices)
    """
    indexed_items = list(enumerate(items))

    # Sort by value density to build a strong upper bound.
    indexed_items.sort(key=lambda x: x[1].value / x[1].weight, reverse=True)

    sorted_indices = [idx for idx, _ in indexed_items]
    sorted_items = [item for _, item in indexed_items]

    # Use a list as a simple priority queue by bound (max-bound first).
    live_nodes: List[Node] = []

    root = Node(level=-1, profit=0, weight=0, bound=0.0, chosen=tuple())
    root.bound = _upper_bound(root, capacity, sorted_items)
    live_nodes.append(root)

    best_profit = 0
    best_choice_sorted: Tuple[int, ...] = tuple()

    while live_nodes:
        # Best-first: pick node with highest bound.
        live_nodes.sort(key=lambda n: n.bound, reverse=True)
        node = live_nodes.pop(0)

        # Prune if node cannot improve incumbent.
        if node.bound <= best_profit:
            continue

        next_level = node.level + 1
        if next_level >= len(sorted_items):
            continue

        item = sorted_items[next_level]

        # Branch 1: include next item.
        include_weight = node.weight + item.weight
        include_profit = node.profit + item.value
        include_choice = node.chosen + (next_level,)

        if include_weight <= capacity:
            if include_profit > best_profit:
                best_profit = include_profit
                best_choice_sorted = include_choice

            include_node = Node(
                level=next_level,
                profit=include_profit,
                weight=include_weight,
                bound=0.0,
                chosen=include_choice,
            )
            include_node.bound = _upper_bound(include_node, capacity, sorted_items)

            if include_node.bound > best_profit:
                live_nodes.append(include_node)

        # Branch 2: exclude next item.
        exclude_node = Node(
            level=next_level,
            profit=node.profit,
            weight=node.weight,
            bound=0.0,
            chosen=node.chosen,
        )
        exclude_node.bound = _upper_bound(exclude_node, capacity, sorted_items)

        if exclude_node.bound > best_profit:
            live_nodes.append(exclude_node)

    # Convert chosen indices back to original item indices.
    chosen_original_indices = [sorted_indices[i] for i in best_choice_sorted]
    chosen_original_indices.sort()

    return best_profit, chosen_original_indices


if __name__ == "__main__":
    sample_items = [
        Item(weight=2, value=40),
        Item(weight=3, value=50),
        Item(weight=5, value=100),
        Item(weight=4, value=60),
    ]
    sample_capacity = 8

    best_value, chosen = branch_and_bound_knapsack(sample_items, sample_capacity)

    print("Best value:", best_value)
    print("Chosen item indices:", chosen)
