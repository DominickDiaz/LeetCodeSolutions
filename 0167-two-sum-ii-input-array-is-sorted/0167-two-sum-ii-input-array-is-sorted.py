class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointerF = 0
        pointerR = len(numbers) - 1
        
        while pointerF != pointerR:
            tempSum = numbers[pointerF] + numbers[pointerR]

            if tempSum == target: 
                return [pointerF + 1, pointerR + 1]
            elif tempSum < target: 
                pointerF += 1
            elif tempSum > target: 
                pointerR -= 1
            
        return []
        