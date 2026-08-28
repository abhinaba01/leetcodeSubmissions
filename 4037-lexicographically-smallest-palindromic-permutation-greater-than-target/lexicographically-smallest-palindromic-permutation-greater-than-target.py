from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        # Check if a palindromic permutation is even possible
        odd_chars = [ch for ch, f in cnt.items() if f % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Frequencies available for the left half of the palindrome
        half = {}
        for ch, f in cnt.items():
            if f // 2 > 0:
                half[ch] = f // 2
                
        m = n // 2
        
        # Helper to construct the full palindrome string
        def build_palindrome(left_str: str) -> str:
            return left_str + mid_char + left_str[::-1]
            
        # 1. Try to exactly match the left half of the target
        target_left = target[:m]
        req = Counter(target_left)
        possible_exact = True
        
        for ch, f in req.items():
            if half.get(ch, 0) < f:
                possible_exact = False
                break
                
        if possible_exact:
            cand = build_palindrome(target_left)
            if cand > target:
                return cand
                
        # 2. Try to diverge at index i (iterating from right to left to ensure smallest valid string)
        for i in range(m - 1, -1, -1):
            req = Counter(target[:i])
            possible_prefix = True
            
            # Check if we have enough characters to form the prefix target[0:i]
            for ch, f in req.items():
                if half.get(ch, 0) < f:
                    possible_prefix = False
                    break
            
            if not possible_prefix:
                continue
                
            # Remaining characters available to use
            avail = {ch: f - req.get(ch, 0) for ch, f in half.items()}
            
            target_char = target[i]
            
            # Find the smallest available character strictly greater than target[i]
            cand_chars = [ch for ch, count in avail.items() if count > 0 and ch > target_char]
            
            if not cand_chars:
                continue
                
            best_c = min(cand_chars)
            
            # Build the new left half
            left_res = list(target[:i])
            left_res.append(best_c)
            avail[best_c] -= 1
            
            # Sort the rest of the available characters in ascending order
            rem_chars = []
            for ch, count in avail.items():
                rem_chars.extend([ch] * count)
            rem_chars.sort()
            
            left_res.extend(rem_chars)
            left_str = "".join(left_res)
            
            return build_palindrome(left_str)
            
        # If no valid palindromic permutation strictly greater than target exists
        return ""