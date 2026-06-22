class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            for i in range(len(numbers)):
                rest = target - numbers[i]
                if (rest == numbers[i]):
                    continue
                for j in range(i+1, len(numbers)):
                    if (numbers[j] == rest):
                        return [i + 1, j + 1]