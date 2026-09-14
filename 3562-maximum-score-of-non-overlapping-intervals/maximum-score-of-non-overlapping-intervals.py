from typing import List
import bisect

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # Append original index to each interval: (start, end, weight, original_index)
        intervals_with_id = []
        for i in range(n):
            intervals_with_id.append((intervals[i][0], intervals[i][1], intervals[i][2], i))
            
        # Sort intervals by end time (ascending). 
        # Tie-break with start time, then original index.
        intervals_with_id.sort(key=lambda x: (x[1], x[0], x[3]))
        
        # Extract purely the end times for fast binary search
        R = [x[1] for x in intervals_with_id]
        
        # DP table: dp[i][k] stores (max_weight, tuple_of_indices)
        # i goes from 0 to n, k goes from 0 to 4
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            curr_l, curr_r, curr_w, curr_id = intervals_with_id[i-1]
            
            # Find the number of intervals that end STRICTLY BEFORE the current interval starts.
            # bisect_left gives the first index where R[idx] >= curr_l, 
            # meaning all elements before it strictly satisfy R[idx] < curr_l.
            prev_idx = bisect.bisect_left(R, curr_l)
            
            for k in range(1, 5):
                # Option 1: Skip current interval
                skip = dp[i-1][k]
                
                # Option 2: Take current interval
                prev_weight, prev_indices = dp[prev_idx][k-1]
                take_weight = prev_weight + curr_w
                # Merge the indices and keep them sorted to maintain lexicographical order representation
                take_indices = tuple(sorted(list(prev_indices) + [curr_id]))
                take = (take_weight, take_indices)
                
                # Determine the best option between Skipping and Taking
                best = skip
                if take[0] > best[0]:
                    best = take
                elif take[0] == best[0]:
                    # Tie-breaker: lexicographically smaller indices win
                    if take[1] < best[1]:
                        best = take
                        
                # Ensure the property "up to k" intervals is maintained by comparing
                # the best result with the result of picking fewer intervals (k-1)
                cand = dp[i][k-1]
                if cand[0] > best[0]:
                    best = cand
                elif cand[0] == best[0]:
                    if cand[1] < best[1]:
                        best = cand
                        
                dp[i][k] = best
                
        # The result resides in evaluating the whole array (n) choosing up to 4 intervals
        return list(dp[n][4][1])