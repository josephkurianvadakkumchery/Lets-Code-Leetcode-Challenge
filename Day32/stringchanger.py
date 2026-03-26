class Solution:
    def interpret(self, command: str) -> str:
        x=""
        i=0
        while(i<len(command)):
            if(command[i]=="G"):
                    x+="G"
            elif(command[i]=="("):
                if(command[i+1]==")"):
                     x+="o"
                     i+=1
                else:
                    x+="al"
                    i+=3    
            else:
                None
            i+=1
        return x
