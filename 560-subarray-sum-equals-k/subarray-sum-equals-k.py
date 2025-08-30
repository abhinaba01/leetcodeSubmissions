class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # HashMap to store frequency of prefix sums
        prefix_count = {0: 1}  

        current_sum = 0   # running prefix sum
        subarray_count = 0  

        for num in nums:
            current_sum += num

            # Check if there exists a prefix with sum = current_sum - k
            if (current_sum - k) in prefix_count:
                subarray_count += prefix_count[current_sum - k]

            # Record the current prefix sum
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return subarray_count
