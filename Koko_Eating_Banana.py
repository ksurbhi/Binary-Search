class Solution:
    # Brute Force Solution
    # Space: O(1)
    #Time: O(max(pile)*n) In the worst case, k ranges from 1 to max(piles)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize the eating speed `k` to 1 (minimum possible speed).
        k = 1
        # Iterate until a valid speed `k` is found.
        while True:
            total_time = 0  # Initialize total time taken to eat all bananas.

            # Calculate the total time required to eat bananas at speed `k`.
            for p in piles:
                # Use math.ceil to compute the time for each pile at speed `k`.
                total_time += math.ceil(p / k)

            # If the total time is within the allowed hours, return `k`.
            if total_time <= h:
                return k
            else:
                # Increment `k` to check the next possible eating speed.
                k += 1

        # Return `k` (though this line is redundant due to the return inside the loop).
        return k


class Solution:
  # time Complexity: O(log(max(piles))*n)
    def 
        # Initialize the search range for the eating speed.
        start = 1  # Minimum possible speed.
        end = max(piles)  # Maximum possible speed (eat the largest pile in one hour).

        # Initialize the result with the upper bound of the search range.
        res = end

        # Perform binary search to find the minimum eating speed.
        while start <= end:
            # Calculate the middle speed of the current range.
            mid = start + (end - start) // 2

            # Calculate the total time required to eat all bananas at speed `mid`.
            total_time = 0
            for p in piles:
                # Use math.ceil to compute time for each pile at speed `mid`.
                total_time += math.ceil(p / mid)

            # Check if the total time is within the allowed hours.
            if total_time <= h:
                # If valid, update the result and search for a lower speed.
                res = mid
                end = mid - 1
            else:
                # Otherwise, search for a higher speed.
                start = mid + 1

        # Return the minimum valid eating speed.
        return res


        
            


        
