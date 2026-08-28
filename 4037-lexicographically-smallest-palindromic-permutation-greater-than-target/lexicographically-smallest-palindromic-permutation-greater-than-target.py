class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:

        n = len(s)
        freq = Counter(s)


        odd = [x for x in freq if freq[x] % 2 != 0]

        if len(odd) > 1:
            return ""
        
        
        mid = odd[0] if n % 2 else ""
        half = n // 2

        half_freq = Counter()

      
        for x in freq:
            count = freq[x] // 2
            if count > 0:
                half_freq[x] = count
        
        left = []
        ans = ''

        def build(pos ,greater):

            if pos == half:
                left_part = ''.join(left)

                if greater:
                    return True

                candidate = left_part + mid + left_part[::-1]
                return candidate > target


            if greater:

                for c in sorted(half_freq):
                    left.extend(c * half_freq[c])

                return True

            else:

                for c in sorted(half_freq):

                    if c < target[pos]:
                        continue

                    left.append(c)
                    half_freq[c] -= 1

                    if half_freq[c] == 0:
                        del half_freq[c]

                    new_greater = c > target[pos]

                    if build(pos + 1 , new_greater):
                        return True

                    half_freq[c] += 1
                    left.pop()


                return False

        if build(0,False):
            left_part = ''.join(left)
            return left_part + mid + left_part[::-1]

        return ""
                    

