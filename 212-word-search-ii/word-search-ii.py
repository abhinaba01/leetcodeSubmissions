class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            
            node = node.children[ch]

        node.is_end = True
        node.word = word

    
    def search(self,word):

        node = self.root

        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]
        
        return node.is_end



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:


        rows = len(board)
        cols = len(board[0])

        trie = Trie()

        for word in words:
            trie.insert(word)

        visited = [[0] * cols for _ in range(rows)]

        ans = []

        def dfs(r,c,node):

            

            if not (0 <= r < rows and 0 <= c < cols):
                return
            
            if visited[r][c] == 1:
                return

            ch = board[r][c]

            if ch not in node.children:
                return

            node = node.children[ch]

            if node.word:
                ans.append(node.word)
                node.word = None

            visited[r][c] = 1

            dfs(r + 1,c,node)
            dfs(r - 1,c,node)
            dfs(r,c + 1,node)
            dfs(r,c - 1,node)

            visited[r][c] = 0

            


        for r in range(rows):
            for c in range(cols):

                dfs(r,c,trie.root)


        return ans




        