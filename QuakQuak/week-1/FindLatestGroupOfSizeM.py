from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        list = [0]*len(arr)
        step = 0
        for item in arr:
            step += 1
            list[item-1]= 1
            count = 0
            safe = False
            for i in list:
                if i == 1:
                    count += 1
                    continue
                if i == 0:
                    if count == m:
                        safe=True
                    count = 0
                    continue
                if count == m:
                    safe = True
            if safe == False:
                return step
        return -1




so = Solution()
print(so.findLatestStep([3,1,5,4,2], 2))