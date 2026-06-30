class TrieNode:

    def __init__(self):
        self.children = [None , None]
   
class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,num:int):

        node = self.root
        
        for i in range(31,-1,-1):
            bit = (num >> i) & 1
            if node.children[bit] is None:
                node.children[bit] = TrieNode()

            
            node = node.children[bit]

    
    def find_max_xor(self, num:int):

        node = self.root
        max_xor = 0

        for i in range(31 , -1 , -1):
            bit = (num >> i) & 1

            oppo = 1 - bit

            if node.children[oppo] is not None:
                node = node.children[oppo]
                max_xor = max_xor | (1 << i)
            else:
                node = node.children[bit]


        return max_xor



class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        trie = Trie()
        max_xor = 0

        for num in nums:
            trie.insert(num)

        for num in nums:
            max_xor = max(max_xor ,trie.find_max_xor(num))

        
        return max_xor





        