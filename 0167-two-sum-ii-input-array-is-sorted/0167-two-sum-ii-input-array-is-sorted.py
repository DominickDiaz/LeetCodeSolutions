class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers) - 1
        temp = 0 
        
        while left < right:
            temp = numbers[right] + numbers[left]
            if temp == target:
                return [left+1, right+1]
            if temp < target:
                left += 1
            else:
                right -= 1
            