class Solution:
    # time Complexity: O(log n)
    # Space Complexity: O(1)
    def findMin(self, nums: List[int]) -> int:
        # Check if the input list is empty or None.
        if len(nums) == 0 or nums == None:
            return -1  # Return -1 as the minimum cannot be determined.

        # Initialize pointers for binary search.
        start = 0
        end = len(nums) - 1

        # Perform binary search to find the minimum element.
        while start <= end:
            # If the subarray is already sorted, the first element is the minimum.
            if nums[start] <= nums[end]:
                return nums[start]

            # Calculate the middle index of the current range.
            mid = start + (end - start) // 2

            # Check if the middle element is the minimum:
            # - It must be smaller than the element before it or be at the start.
            # - It must be smaller than the element after it or be at the end.
            if (mid == start or nums[mid - 1] >= nums[mid]) and \
               (mid == end or nums[mid] <= nums[mid + 1]):
                return nums[mid]  # Return the middle element if it's the minimum.

            # Determine if the left part of the array is sorted:
            # - If sorted, the minimum must be in the right part.
            elif nums[start] <= nums[mid]:
                start = mid + 1  # Narrow the search range to the right part.

            # Otherwise, the right part is unsorted, so the minimum must be there.
            else:
                end = mid - 1  # Narrow the search range to the left part.

        # If the loop ends without finding the minimum (unlikely in valid input).
        return -1
