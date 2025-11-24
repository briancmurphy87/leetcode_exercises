class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if current.children[ord(c) - ord("a")] is None:
                current.children[ord(c) - ord("a")] = TrieNode()
            current = current.children[ord(c) - ord("a")]
        current.is_end = True

    # Find the shortest root of the word in the trie
    def shortest_root(self, word):
        current = self.root
        for i in range(len(word)):
            c = word[i]
            if current.children[ord(c) - ord("a")] is None:
                # There is not a corresponding root in the trie
                return word
            current = current.children[ord(c) - ord("a")]
            if current.isEnd:
                return word[: i + 1]
        # There is not a corresponding root in the trie
        return word


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        word_array = sentence.split()

        dict_trie = Trie()
        for word in dictionary:
            dict_trie.insert(word)

        # Replace each word in the sentence with the corresponding shortest root
        for word in range(len(word_array)):
            word_array[word] = dict_trie.shortest_root(word_array[word])

        return " ".join(word_array)

if __name__ == "__main__":
    """
    ["cat","bat","rat"]
    "the cattle was rattled by the battery"
    ["a","b","c"]
    "aadsfasf absbs bbab cadsfafs"
    """
    pass