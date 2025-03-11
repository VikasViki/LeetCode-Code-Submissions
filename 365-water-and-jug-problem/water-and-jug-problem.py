class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y: return False
        gcd = math.gcd(x, y)
        return target % gcd == 0