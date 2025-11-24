from collections import defaultdict

_TRIE_NODE_INSTANCE_ID_COUNTER = 0

class TrieNode:
    def __init__(self) -> None:
        self.is_word = False

        global _TRIE_NODE_INSTANCE_ID_COUNTER
        _TRIE_NODE_INSTANCE_ID_COUNTER += 1
        self.instance_id = _TRIE_NODE_INSTANCE_ID_COUNTER


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        # key = node instance id
        # val = dict[character -> tree node]
        self.instance_to_children_map: defaultdict[int, dict[str, TrieNode]] = defaultdict(dict)


    def insert(self, word: str) -> None:
        curr: TrieNode = self.root
        for c_index, c in enumerate(word):
            if c not in self.instance_to_children_map[curr.instance_id]:
                # insert a new node if the path does not exist
                self.instance_to_children_map[curr.instance_id][c] = TrieNode()

            # next child node
            curr = self.instance_to_children_map[curr.instance_id][c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr: TrieNode = self.root
        for c_index, c in enumerate(word):
            if c not in self.instance_to_children_map[curr.instance_id]:
                return False
            # next child node
            curr = self.instance_to_children_map[curr.instance_id][c]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr: TrieNode = self.root
        for c_index, c in enumerate(prefix):
            if c not in self.instance_to_children_map[curr.instance_id]:
                return False
            # next child node
            curr = self.instance_to_children_map[curr.instance_id][c]
        # if we get here, then we walked over 'prefix' with no reason to reject
        return True