class Solution:
    def beautySum(self, s: str) -> int:

        ans = 0
        n = len(s)

        for i in range(n):
            m = {}
            
            for j in range(i,n):
               
                
                m[s[j]] = m.get(s[j],0) + 1

                m_f , l_f = 0 , float("inf")
             

            
      

                for value in m.values():
                    m_f = max(m_f,value)
                    l_f = min(l_f,value)
            

                ans += (m_f - l_f)

        return ans





                