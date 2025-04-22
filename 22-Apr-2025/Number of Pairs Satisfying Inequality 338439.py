# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [a - b for a, b in zip(nums1, nums2)]
        
        def merge_sort(arr):
            def sort(lo, hi):
                if hi - lo <= 1:
                    return 0
                mid = (lo + hi) // 2
                count = sort(lo, mid) + sort(mid, hi)
                
                j = mid
                for i in range(lo, mid):
                    while j < hi and arr[i] > arr[j] + diff:
                        j += 1
                    count += hi - j
                arr[lo:hi] = sorted(arr[lo:hi])
                return count
            
            return sort(0, len(arr))
        
        return merge_sort(arr)
