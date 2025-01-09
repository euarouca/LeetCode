class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_to_index:
                return [num_to_index[complement], i]

            num_to_index[num] = i

        return []
    
    
    # Solução Alternativa #
    
    # def twoSum(self, nums, target):
	#     for i in range(len(nums)):
	# 	    for j in range(i + 1, len(nums)):
	# 		    if nums[j] == target - nums[i]:
	# 			    return [i, j]
	# 	# Return an empty list if no solution is found
	#     return []
    
    

if __name__ == "__main__":
    solution = Solution()
    nums = [15, 7, 11, 2]
    target = 9
    solution.twoSum(nums, target)