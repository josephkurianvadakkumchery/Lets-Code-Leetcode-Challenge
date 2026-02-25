class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        if(0<=celsius and celsius<=1000):
            kel=celsius+273.15
            far=celsius*1.80+32.00
            tem=[kel,far]
            return tem
