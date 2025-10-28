Trie = dict[str, "Trie"]

class WordDictionary:
  def __init__(self):
    self._storage: Trie = {}
    self._end = "#"
    self._any = "."

  def addWord(self, word: str) -> None:
    curr = self._storage
    for char in word:
      if char not in curr:
        curr[char] = {}
      curr = curr[char]
    curr[self._end] = {}

  def search(self, word: str) -> bool:
    return self._recursive_search(self._storage, 0, word)

  def _recursive_search(self, node: Trie, idx: int, word: str) -> bool:
    if idx == len(word):
      return self._end in node

    char = word[idx]
    if char is self._any:
      res = False
      for entry in node:
        res |= self._recursive_search(node[entry], idx + 1, word)
      return res

    if char not in node:
      return False

    return self._recursive_search(node[char], idx + 1, word)