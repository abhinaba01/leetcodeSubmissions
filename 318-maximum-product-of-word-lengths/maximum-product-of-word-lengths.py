class Solution:
    def maxProduct(self, words: List[str]) -> int:

        n = len(words)

        

        

        def convert(word):

            mask = 0
            cnt = 0

            for ch in word:
                cnt += 1

                index = ord(ch) - 97
                mask = mask | (1 << index)

            
            return mask,cnt

        ans = 0

        masks = [convert(w) for w in words]
        print(masks)
        
        for i in range(n):

        
            for j in range(i+1,n):

                mask1,n1 = masks[i]
                mask2,n2 = masks[j]

                if (mask1 & mask2) == 0:
                    ans = max(ans,n1 * n2)

    
        return ans
                

        