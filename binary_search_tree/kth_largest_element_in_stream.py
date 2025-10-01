from typing import Optional
from binary_tree.common_utils.tree_node import TreeNode

class TreeNodeExpanded:
    def __init__(
            self,
            node_val: int,
            left: Optional["TreeNodeExpanded"],
            right: Optional["TreeNodeExpanded"],
    ) -> None:
        self.val = node_val
        self.left = left
        self.right = right
        self.val_count = 1
        # self.node_count_of_subtree: int = 0

    def get_node_count_of_subtree_right(self) -> int:
        if self.right is None:
            return 0
        else:
            return 1 + sum(self.right.get_subtree_node_counts())

    def get_subtree_node_counts(self) -> tuple[int, int]:
        lhs_counts, rhs_counts = 0, 0
        if self.left is not None:
            lhs_counts = (1+ sum(self.left.get_subtree_node_counts()))
        if self.right is not None:
            rhs_counts = (1 + sum(self.right.get_subtree_node_counts()))

        return lhs_counts, rhs_counts

    @property
    def ge_count(self) -> int:
        # _, rhs_counts = self.get_subtree_node_counts()
        if self.right is None:
            return 0
        else:
            return self.right.ge_count + self.val_count

    @property
    def gt_count(self) -> int:
        _, rhs_counts = self.get_subtree_node_counts()
        return rhs_counts + self.val_count
        # if self.right is None:
        #     return 0
        # else:
        #     return self.right.ge_count + 1


def insert_bst_helper(root: TreeNodeExpanded, val: int) -> None:

    if root.val < val:
        # go right
        if root.right is None:
            root.right = TreeNodeExpanded(val, None, None)
        else:
            insert_bst_helper(root.right, val)

    else: # root.val >= p.val
        # go left
        if root.left is None:
            root.left = TreeNodeExpanded(val, None, None)
        else:
            insert_bst_helper(root.left, val)


def init_tree_from_array(nums: list[int]) -> TreeNodeExpanded:
    root = TreeNodeExpanded(node_val=nums[0], left=None, right=None)
    for new_node_val in nums[1:]:
        insert_bst_helper(root, new_node_val)
    return root

def init_tree_from_array_helper(
    tree_array: list[int],
    tree_array_index: int,
    parent_node: TreeNodeExpanded,
) -> TreeNodeExpanded:
    node_value = tree_array[tree_array_index]

    # add child nodes
    if node_value <= parent_node.val:
        # -> go left
        assert parent_node.left is None
        parent_node.left = TreeNodeExpanded(node_val=node_value, left=None, right=None)
        next_parent_node = parent_node.left

    else: # node_value >= parent_node.val
        # -> go right
        assert parent_node.right is None
        parent_node.right = TreeNodeExpanded(node_val=node_value, left=None, right=None)
        next_parent_node = parent_node.right

    # check if at end
    next_tree_array_index = tree_array_index + 1
    if next_tree_array_index < len(tree_array):
        init_tree_from_array_helper(
            tree_array=tree_array,
            tree_array_index=next_tree_array_index,
            parent_node=next_parent_node,
        )
    return parent_node


def find_kth_largest_element(root: TreeNodeExpanded, k: int) -> TreeNodeExpanded:
    """
    for each node in a BST,
    if m nodes in the right subtree,
    -> the node itself is the m + 1 largest element in the array
    """
    num_elements_gt_root = root.gt_count
    num_elements_ge_root = root.ge_count
    root_largest_element_index_min = num_elements_gt_root + 1
    root_largest_element_index_max = num_elements_ge_root + 1
    # lhs_node_count, rhs_node_count = root.get_subtree_node_counts()
    # root_largest_element_index = rhs_node_count + 1
    if k in [root_largest_element_index_min, root_largest_element_index_max]:
        return root

    elif root_largest_element_index_min < k:
        # if (m + 1) < k -> find smaller elements
        # -> LEFT
        smaller_elements_to_go = k - root_largest_element_index_min
        if root.val_count > 1 and (root.val_count - 1) >= smaller_elements_to_go:
            return root

        return find_kth_largest_element(root=root.left, k=k)
    else:  # root_largest_element_index > self.k:

        # if (m + 1) > k -> find larger elements
        # -> RIGHT
        return find_kth_largest_element(root=root.right, k=k)


# class KthLargest:
#
#     def __init__(self, k: int, nums: list[int]) -> None:
#         self.k = k
#         self.nums = nums
#         self.root_node = init_tree_from_array(nums=nums)
#
#     def add(self, val: int) -> int:
#         insert_bst_helper(self.root_node, val)
#         kth_largest_node = find_kth_largest_element(self.root_node, self.k)
#         return kth_largest_node.val


# region: leetcode solution
"""
from here: 
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1026/

c++ code
struct Node {
    Node* left;
    Node* right;
    int val;
    int cnt;
    Node(int v, int c) : left(NULL), right(NULL), val(v), cnt(c) {}
};

class KthLargest {
private:
    Node* insertNode(Node* root, int num) {
        if (!root) {
            return new Node(num, 1);	    // return a new node if root is null
        }
        if (root->val < num) {			// insert to the right subtree if val > root->val
            root->right = insertNode(root->right, num);
        } else {						// insert to the left subtree if val <= root->val
            root->left = insertNode(root->left, num);
        }
        root->cnt++;
        return root;
    }
    int searchKth(Node* root, int k) {
        // m = the size of right subtree
        int m = root->right ? (root->right)->cnt : 0;
        // root is the m+1 largest node in the BST
        if (k == m + 1) {
            return root->val;
        }
        if (k <= m) {
            // find kth largest in the right subtree
            return searchKth(root->right, k);
        } else {
            // find (k-m-1)th largest in the left subtree
            return searchKth(root->left, k - m - 1);
        }
    }
    Node* root;
    int m_k;
public:
    KthLargest(int k, vector<int> nums) {
        root = NULL;
        for (int i = 0; i < nums.size(); ++i) {
            root = insertNode(root, nums[i]);
        }
        m_k = k;
    }
    
    int add(int val) {
        root = insertNode(root, val);
        return searchKth(root, m_k);
    }
};

"""
def search_kth(root: TreeNodeExpanded, k: int) -> int:
    m = root.get_node_count_of_subtree_right()

    # root is the m+1 largest node in the BST
    if k == m + 1:
        return root.val

    elif k <= m:
        # find kth largest in the right subtree
        return search_kth(root.right, k)

    else: # k > m
        # find (k-m-1)th largest in the left subtree
        return search_kth(root.left, k - m - 1)

class KthLargest:

    def __init__(self, k: int, nums: list[int]) -> None:
        self.k = k
        self.root_node = init_tree_from_array(nums=nums) if nums else None

    def add(self, val: int) -> int:
        if self.root_node is None:
            self.root_node = TreeNodeExpanded(val, None, None)
        else:
            insert_bst_helper(self.root_node, val)

        return search_kth(root=self.root_node, k=self.k)

# endregion

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    """
    ["KthLargest","add","add","add","add","add"]
    [[1,[]],[-3],[-2],[-4],[0],[4]]
    """
    kthLargest = KthLargest(1, [])
    print(kthLargest.add(-3))
    print(kthLargest.add(-2))
    print(kthLargest.add(-4))
    print(kthLargest.add(0))
    print(kthLargest.add(4))

    """
    Example 1:

    Input:
    ["KthLargest", "add", "add", "add", "add", "add"]
    
    [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    
    Output: [null, 4, 5, 5, 8, 8]
    
    Explanation:
    
    KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    kthLargest.add(3); // return 4
    kthLargest.add(5); // return 5
    kthLargest.add(10); // return 5
    kthLargest.add(9); // return 8
    kthLargest.add(4); // return 8
    """
    # kthLargest = KthLargest(3, [4, 5, 8, 2])
    # print(kthLargest.add(3))
    # print(kthLargest.add(5))
    # print(kthLargest.add(10))
    # print(kthLargest.add(9))
    # print(kthLargest.add(4))

