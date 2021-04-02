from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        step = m
        list = [0]*len(arr)
        flag = []
        for index in range(len(arr)):
            list[arr[index]-1] = 1
            if index < m:
                continue
            for item in list:
                step += 1
                count = m
                if item == 1:
                    count -= 1
                if item == 0:
                    if count == 0:
                        flag.append(True)
                        continue
            if flag == False & index == len(arr):
                return step
        return -1
so = Solution()
print(so.findLatestStep([3,5,1,2,4], 1))