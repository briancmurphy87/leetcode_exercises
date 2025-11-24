from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    entries_by_group_label: defaultdict[str, list[str]] = defaultdict(list)
    for item in strs:
        entries_by_group_label["".join(sorted(item))].append(item)

    return list(entries_by_group_label.values())


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

if __name__ == '__main__':
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))