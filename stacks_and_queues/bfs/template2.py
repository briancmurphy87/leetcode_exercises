"""
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    Set<Node> visited;  // store all the nodes that we've visited
    int step = 0;       // number of steps needed from root to current node
    // initialize
    add root to queue;
    add root to visited;
    // BFS
    while (queue is not empty) {
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                if (next is not in visited) {
                    add next to queue;
                    add next to visited;
                }
            }
            remove the first node from queue;
        }
        step = step + 1;
    }
    return -1;          // there is no path from root to target
}
"""
from collections import deque


class GraphNode:
    def __init__(self, val: int, adjacent_nodes: list["GraphNode"]):
        self.val = val
        self.adjacent_nodes = adjacent_nodes

def breadth_first_search(root: GraphNode, target: GraphNode) -> int:

    # init
    distance = 0
    nodes_visited: deque[GraphNode] = deque([root])
    nodes_to_process: deque[GraphNode] = deque([root])

    while nodes_to_process:
        node_curr = nodes_to_process.popleft()
        if node_curr == target:
            return distance

        for node_next in node_curr.adjacent_nodes:
            if node_next not in nodes_visited:
                nodes_visited.append(node_next)
                nodes_to_process.append(node_next)
        distance += 1

    return -1
