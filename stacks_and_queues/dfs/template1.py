"""
from:
https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1384/

/*
 * Return true if there is a path from cur to target.
 */
boolean DFS(Node cur, Node target, Set<Node> visited) {
    return true if cur is target;
    for (next : each neighbor of cur) {
        if (next is not in visited) {
            add next to visited;
            return true if DFS(next, target, visited) == true;
        }
    }
    return false;
}
"""
class GraphNode:
    def __init__(self, val: int, adjacent_nodes: list["GraphNode"]):
        self.val = val
        self.adjacent_nodes = adjacent_nodes

def depth_first_search(
        node_curr: GraphNode,
        node_target: GraphNode,
        nodes_visited: set[GraphNode],
) -> bool:
    if node_curr == node_target:
        return True

    for node_next in node_curr.adjacent_nodes:
        if node_next not in nodes_visited:
            nodes_visited.add(node_next)
            node_next_dfs_result = depth_first_search(
                node_curr=node_next,
                node_target=node_target,
                nodes_visited=nodes_visited,
            )
            if node_next_dfs_result:
                return True
    return False    