class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        
            left, right = 0, len(numbers) - 1
            tempSum = 0
 
            
            
            while left < right:
                temp = numbers[left] + numbers[right]
                if temp > target:
                    right -= 1
                    continue 
                if temp < target:
                    left += 1
                    continue
                if temp == target:
                    return [left +1, right + 1]
                
            return []