class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        w = len(words[0])

        k = len(words)

        n = len(s)

        need = Counter(words)

        result = []

        for offset in range(w):

            freq = defaultdict(int)
            formed = 0
            l  = offset

            for r in range(offset, n - w + 1 , w):

                word = s[r:r+w]

                if word in words:

                    freq[word] += 1

                    if freq[word] == need[word]:
                        formed += 1

                
                else:
                    freq.clear()
                    l = r + w
                    formed = 0
                    continue

                

                while freq[word] > need[word]:
                    left_word = s[l:l+w]
                 
                    
                    if freq[left_word] == need[left_word]:
                        formed -= 1
                    freq[left_word] -= 1
                    l = l + w

                
                if len(need) == formed:
                    result.append(l)
                

        return result











        
       