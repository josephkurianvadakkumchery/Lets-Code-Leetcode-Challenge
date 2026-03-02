class Solution:
    def judgeCircle(self, moves: str) -> bool:
        valid=["R","L","U","D"]
        v=0
        h=0
        move=list(moves)
        for i in move:
            if i in valid:
                if(i=="R"):
                    h+=1
                elif(i=="L"):
                    h-=1
                elif(i=="U"):
                    v+=1
                else:
                    v-=1
        if(h==0 and v==0):
            return True
        else:
            return False
