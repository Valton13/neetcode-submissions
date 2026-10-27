class Trie():
    def __init__(self):
        self.child = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = Trie()
            curr = curr.child[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            curr = root
            for i in range(j , len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.child.values():
                        if dfs(i+1 , child):
                            return True
                    return False
                else:
                    if c not in curr.child:
                        return False
                    curr = curr.child[c]
            return curr.end
        return dfs(0 , self.root)   
                        