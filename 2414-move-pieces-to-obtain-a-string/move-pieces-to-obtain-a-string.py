class Solution:
    def canChange(self, start: str, target: str) -> bool:

        n = len(start)
        n = len(target)

       

        s = ""
        for i in range(n):
            if start[i] == "_":
                continue
            else:
                s += start[i]

        t = ""
        for j in range(n):
            if target[j] == "_":
                continue

            else:
                t += target[j]
       

        if s != t:
            print("1.")
            return False

        i , j = 0 , 0
        while i < n or j < n:

            while i < n and start[i] == '_':
                i += 1
            
            
            while j < n and target[j] == "_":
                j += 1

            if i == n or j == n:
                print("5.")
                return i == n and j == n

            if start[i] != target[j]:
                print("2.")
                return False

            else:
                if start[i] == 'L' and i < j:
                    print("3.")
                    return False

                elif start[i] == 'R' and i > j:
                    print("4.")
                    return False

            
            i += 1
            j += 1

        return True


            

            
                

        

