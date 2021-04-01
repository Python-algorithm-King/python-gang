from traitlets import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pair = 0
        count = 0
        max = 0
        for item in nums:
            if item == 1:
                if pair == 1:
                    count+=1
                    if count>max:
                        max = count
                    continue
                count = 1;
                pair = item
                if count > max:
                    max = count
                continue
            count = 0
            pair = item
        return max

a = Solution()
a.findMaxConsecutiveOnes(List())