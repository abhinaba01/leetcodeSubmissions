class TrieNode():

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie():

    def __init__(self):
        self.root = TrieNode()

    def insert(self,word:str):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.is_end = True

    def findRoot(self,word:str):
        node = self.root
        ans = ""
        
        for ch in word:

            if node.is_end == True:
                return ans
            else:
                if ch not in node.children:
                    if node.is_end == True:
                        return ans
                    else:
                        return ""
                        
                else:
                    ans += ch
                    node = node.children[ch]
            
        if node.is_end == True:
            return ans
        else:
            return ""



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        res = ""
        for word in sentence.split():
        
            ans = trie.findRoot(word)
            if ans == "":
                res += (word + " ")
            else:
                res += (ans + " ")
            


        return res.rstrip()

        




        