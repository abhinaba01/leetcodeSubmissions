class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        set_row = defaultdict(list)
        res = 0
        reservedSeats.sort(key = lambda x : (x[0] , x[1]))
        


        for row , seat in reservedSeats:

            set_row[row].append(seat)

   


    

        for row in set_row:

            flag1 , flag2 , flag3 = 1 , 1 , 1

            for seat in set_row[row]:
                

                if seat in [1,10]:
                    continue
                if seat  in [2 ,3 , 4 ,5]:
                    flag1 = False
                    
                if seat in [4,5,6,7]:
                    flag2 = False
                    
                if seat in [6,7, 8, 9]:
                    flag3 = False



            if flag1  and flag3:
                res += 2
            elif flag1 or flag2 or flag3:
                res += 1 
            else:
                res += 0
                    
                    

               

    


        return (n - len(set_row)) * 2 + res



    