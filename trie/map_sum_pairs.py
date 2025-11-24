
class MapSumSimple:

    def __init__(self):
        self.str_to_val: dict[str, int] = dict()

    def insert(self, key: str, val: int) -> None:
        self.str_to_val[key] = val

    def sum(self, prefix: str) -> int:
        return sum(
            v
            for k,v in self.str_to_val.items()
            if k.startswith(prefix)
        )


# region: using 'trie'
class TrieNode(object):
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSumWithTrie:

    def __init__(self):
        self.root = TrieNode()
        self.map: dict[str, int] = dict()

    def insert(self, key: str, val: int) -> None:

        # use delta to update the node score of:
        # -> each child node on 'prefix path' of key[0] -> key[-1]
        delta = val - self.map.get(key, 0)

        # update mapping
        self.map[key] = val

        # for every node of the trie corresponding to some prefix...
        # -> update the score based on the incoming entry
        curr_node = self.root
        curr_node.score += delta
        for key_char in key:
            curr_node = curr_node.children.setdefault(key_char, TrieNode())
            curr_node.score += delta

    def sum(self, prefix: str) -> int:
        # for every node along the prefix
        curr_node = self.root
        for prefix_char in prefix:
            if prefix_char not in curr_node.children:
                return 0
            # jump to child node of this prefix
            curr_node = curr_node.children[prefix_char]
        return curr_node.score

# endregion

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


if __name__ == "__main__":
    # map_sum = MapSum()
    pass