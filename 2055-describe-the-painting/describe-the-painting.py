class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:

        diff = defaultdict(int)
        painting = [0] * 100
       
        ans = []

        for start , end , paint in segments:
            diff[start] += paint
            diff[end] -= paint

        keys = sorted(diff.keys())

        curr_color = 0
        prev_pos = None

        for pos in keys:
            if prev_pos is not None and curr_color > 0:
                ans.append([prev_pos, pos, curr_color])

            curr_color += diff[pos]
            prev_pos = pos

        
        return ans