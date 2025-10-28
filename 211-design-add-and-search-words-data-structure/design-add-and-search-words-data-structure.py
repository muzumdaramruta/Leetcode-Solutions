class WordDictionary:

    def __init__(self):
        self.root = {}
    
    def addWord(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node['$'] = None

    def search(self, word):
        nodes = [self.root]
        for char in word + '$':
            nodes = [kid for node in nodes for kid in
                     ([node[char]] if char in node else
                      filter(None, node.values()) if char == '.' else [])]
        return bool(nodes)