"""
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    int step = 0;       // number of steps needed from root to current node
    // initialize
    add root to queue;
    // BFS
    while (queue is not empty) {
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                add next to queue;
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
    step = 0

    # init
    nodes_to_process: deque[GraphNode] = deque()
    nodes_to_process.append(root)

    # do bfs
    while nodes_to_process:
        node_curr = nodes_to_process.popleft()
        if node_curr == target:
            return step

        for node_next in node_curr.adjacent_nodes:
            nodes_to_process.append(node_next)

        step += 1
    return -1