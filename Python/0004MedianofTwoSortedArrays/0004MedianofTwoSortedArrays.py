class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # make sure nums2 is shorter:
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums2)

        while left<=right:
            partition2 = (left + right) //2
            partition1 = (len(nums1)+ len(nums2)) //2 - partition2

            partition_right = min(nums2[partition2] if partition2<len(nums2) else float('inf'),nums1[partition1] if partition1<len(nums1) else float('inf'))

            partition_left2 = nums2[partition2-1] if partition2>0 else float('-inf')
            partition_left1 = nums1[partition1-1] if partition1>0 else float('-inf')

            if partition_left2 > partition_right:
                right = partition2 - 1
            elif partition_left1 > partition_right:
                left = partition2 + 1
            else:
                break

        if (len(nums1)+len(nums2))%2 ==1:
            return partition_right
        else:
            partition_left_max = max(partition_left1, partition_left2)
            
            return (partition_right + max(partition_left1, partition_left2))/2

