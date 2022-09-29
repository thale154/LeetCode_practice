class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #use low and high to find first elemet
        low, high = 0, len(arr) - k
        while low < high:
            mid = (low + high) // 2
            if x - arr[mid] > arr[mid + k] - x: #x closer to arr[mid+k] than arr[mid]
                low = mid + 1
            else:
                high = mid
        return arr[low:low+k]