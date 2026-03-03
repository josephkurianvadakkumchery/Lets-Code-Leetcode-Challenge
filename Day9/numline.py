class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count=0
        dist=0
        for i in moves:
            if i == 'L':
                dist -= 1
            elif i == 'R':
                dist += 1
            else:
                count += 1
        return abs(dist) + count
