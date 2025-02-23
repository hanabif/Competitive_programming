# Problem: Number of Submatrices That Sum to Target - https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        def subarraySumEqualsK(arr, k):

            prefix_sums = defaultdict(int)
            prefix_sums[0] = 1  
            curr_sum = 0
            count = 0

            for num in arr:
                curr_sum += num
                count += prefix_sums[curr_sum - k]
                prefix_sums[curr_sum] += 1

            return count

        for r1 in range(rows):
            col_sums = [0] * cols

            for r2 in range(r1, rows):
                
                for c in range(cols):
                    col_sums[c] += matrix[r2][c]

                count += subarraySumEqualsK(col_sums, target)

        return count

       
