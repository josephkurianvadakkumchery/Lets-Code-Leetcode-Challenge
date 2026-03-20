class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        return max((l**2 + w**2, l * w) for l, w in dimensions)[1]
