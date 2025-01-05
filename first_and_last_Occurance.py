class Solution:
    #Time Complexity: O(N)
    # Space Complexity: O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums ==None:
            return [-1,-1]
        first_occ = self.firstOccurance(nums, target)
        last_occ = self.lastOccurance(nums, target)
        return [first_occ, last_occ]
    
    def firstOccurance(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start +(end-start)//2
            if target == nums[mid]:
                if (mid == start) or (target != nums[mid-1]):
                    return mid
                else:
                    end = mid -1
            elif target > nums[mid]:
                start = mid+1
            else:
                end = mid -1
        return -1
    
    def lastOccurance(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start +(end-start)//2
            if target == nums[mid]:
                if (mid == end) or (target != nums[mid+1]):
                    return mid
                else:
                    start = mid+1
            elif target > nums[mid]:
                start = mid +1
            else:
                end = mid -1
        return -1
