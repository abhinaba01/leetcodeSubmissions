class TrieNode():
    
    def __init__(self):
        self.children = [None , None]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self,num):

        node = self.root

        for i in range(31 , -1 , -1):
            bit = (num >> i) & 1

            if node.children[bit] is None:
                node.children[bit]  = TrieNode()

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
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        trie = Trie()

        nums.sort()

        queries = sorted(
            [(m, x, i) for i, (x, m) in enumerate(queries)]
        )

        trie = Trie()
        j = 0
        ans = [-1] * len(queries)

        for m, x, idx in queries:

            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1

            if j == 0:
                ans[idx] = -1
            else:
                ans[idx] = trie.find_max_xor(x)



        return ans
            





                


        