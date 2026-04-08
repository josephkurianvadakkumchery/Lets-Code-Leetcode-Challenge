class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance_count = 0
        for x in arr1:
            valid_element = True
            for y in arr2:
                if abs(x - y) <= d:
                    valid_element = False
                    break
            if valid_element:
                distance_count += 1
        return distance_count
