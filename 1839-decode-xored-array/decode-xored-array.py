class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:

        n = len(encoded)
        arr = [0] * (n + 1)
        arr[0] = first
        i = 1
        for x in encoded:
            res = first ^ x
            arr[i] = res
            i += 1
            first = res

        return arr
        
        