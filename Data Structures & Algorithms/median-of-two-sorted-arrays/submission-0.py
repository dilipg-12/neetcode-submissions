class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2) 
        total_elements = l1 + l2
        half = total_elements // 2

        if l2 > l1:
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums2)
        while l<=r:
            num2_i = (l+r)//2
            num1_i = half - num2_i
            
            left_1 = nums1[num1_i - 1] if num1_i > 0 else float("-inf")
            right_1 = nums1[num1_i] if num1_i < len(nums1) else float("inf")
            left_2 = nums2[num2_i - 1] if num2_i > 0 else float("-inf")
            right_2 = nums2[num2_i] if num2_i < len(nums2) else float("inf")
            

            if left_1 <= right_2 and left_2 <= right_1:
                if total_elements % 2:
                    return min(right_1,right_2)
                else:
                    return (max(left_1, left_2) + min(right_1,right_2)) / 2
            elif left_1 > right_2:
                l = num2_i + 1
            else:
                r = num2_i - 1


