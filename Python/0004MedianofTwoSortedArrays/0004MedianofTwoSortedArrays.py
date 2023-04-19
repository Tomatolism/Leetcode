class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums2 is the shorter array
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        # Initialize the binary search boundaries for the shorter array
        left, right = 0, len(nums2)

        while left <= right:
            # Calculate partition points for both arrays
            partition2 = (left + right) // 2
            partition1 = (len(nums1) + len(nums2)) // 2 - partition2

            # Determine the elements immediately to the right of the partition points
            partition_right = min(nums2[partition2] if partition2 < len(nums2) else float('inf'),
                                  nums1[partition1] if partition1 < len(nums1) else float('inf'))

            # Determine the elements immediately to the left of the partition points
            partition_left2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            partition_left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')

            # Check if the correct partition has been found
            if partition_left2 > partition_right:
                # Move the binary search boundary in the shorter array to the left
                right = partition2 - 1
            elif partition_left1 > partition_right:
                # Move the binary search boundary in the shorter array to the right
                left = partition2 + 1
            else:
                # The correct partition has been found, break the loop
                break

        # Calculate the median based on the combined length of the arrays
        if (len(nums1) + len(nums2)) % 2 == 1:
            # If the combined length is odd, return the partition_right value as the median
            return partition_right
        else:
            # If the combined length is even, return the average of partition_right and the maximum value on the left side of the partition
            partition_left_max = max(partition_left1, partition_left2)
            return (partition_right + partition_left_max) / 2
