class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1] )
        print(boxTypes)
        res = 0
        numBox = 0
        for i in range(len(boxTypes)):
            if numBox + boxTypes[i][0] > truckSize:
                res += (truckSize - numBox) * boxTypes[i][1]
                return res
            numBox += boxTypes[i][0]
            res += boxTypes[i][0] * boxTypes[i][1]
        return res
