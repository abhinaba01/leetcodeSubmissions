class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        stack = []
        freq = {}

        for num in s:
            freq[num] = freq.get(num,0) + 1
        
        for ch in s:

            freq[ch] -= 1
            if ch in stack:
                continue

            while stack and stack[-1] > ch and freq[stack[-1]] > 0:
         
                stack.pop()
                

            stack.append(ch)

        
        return "".join(stack)


        