class Solution:
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        # Check if the input array is None or empty. If so, return -1.
        if nums == None or len(nums) == 0:
            return -1

        # Initialize the search space with start and end pointers.
        start = 0
        end = len(nums) - 1

        # Perform binary search while the search space is valid.
        while start <= end:
            # Calculate the middle index of the current search space.
            mid = start + (end - start) // 2

            # If the middle element matches the target, return its index.
            if nums[mid] == target:
                return mid

            # Check if the left portion of the array is sorted.
            if nums[start] <= nums[mid]:
                # If the target lies within the sorted left portion, narrow the search to this range.
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                # Otherwise, narrow the search to the right portion.
                else:
                    start = mid + 1
            # Check if the right portion of the array is sorted.
            elif nums[mid] <= nums[end]:
                # If the target lies within the sorted right portion, narrow the search to this range.
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                # Otherwise, narrow the search to the left portion.
                else:
                    end = mid - 1

        # If the target is not found after exiting the loop, return -1.
        return -1

# Explanation of the algorithm:
# - The input array is assumed to be rotated and sorted. This means the array consists of atleast 1 sorted subarrays.
# - The binary search leverages the property of sorted subarrays to decide which half to search next.
# - The mid-point of the current search space is used to determine whether the left or right part is sorted.
# - The target is compared with the boundaries of the sorted portion to decide whether to search within it.

# Time Complexity:
# - O(log n): Binary search reduces the search space by half in each iteration.

# Space Complexity:
# - O(1): No additional memory is used apart from a few variables for indexing.
