class Solution:
    # Time Complexity: O(log(n))
    # Space Complexity: O(1)

    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start +(end -start)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid +1
            else:
                end = mid-1
        return -1

        
