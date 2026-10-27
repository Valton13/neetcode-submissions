class Trie():
    def __init__(self):
        self.child ={}
        self.end = False
    def insert(self,word):
        curr = self
        for w in word:
            if w not in curr.child:
                curr.child[w] = Trie()
            curr = curr.child[w]
        curr.end = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            root.insert(w)
        rows , cols = len(board) , len(board[0])
        res , visit = set() , set()
        def dfs(r,c,node , word):
            if (r<0 or c<0 or r>= rows or c>= cols or (r,c) in visit or board[r][c] not in node.child):
                return 
            visit.add((r,c))
            node = node.child[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)