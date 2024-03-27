class Solution(object):
    def moveZeroes(self, nums):
        # prev_idx, sıfır olmayan son elemanın indeksini takip eder
        prev_idx = 0
        
        # nums üzerinde gezin
        for i in range(len(nums)):
            # eğer eleman sıfır değilse
            if nums[i] != 0:
                hold = nums[prev_idx]
                nums[prev_idx] = nums[i]
                nums[i] = hold
                prev_idx += 1
        
        return nums

# Örnek giriş
nums = [0, 3, 0, 5, 44, 0, 7, 0, 8, 12, 11]
solution = Solution()
print(solution.moveZeroes(nums))  # Çıktı: [1, 3, 12, 0, 0]
