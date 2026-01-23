class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        ops = []

        def precedence(op):
            if op in ('+', '-'):
                return 1
            return 2  # * or /

        def apply_op():
            b = nums.pop()
            a = nums.pop()
            op = ops.pop()

            if op == '+':
                nums.append(a + b)
            elif op == '-':
                nums.append(a - b)
            elif op == '*':
                nums.append(a * b)
            else:
                nums.append(int(a / b))  # truncate toward zero

        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue

            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                nums.append(num)
                continue

            # operator
            while ops and precedence(ops[-1]) >= precedence(s[i]):
                apply_op()

            ops.append(s[i])
            i += 1

        while ops:
            apply_op()

        return nums[0]
