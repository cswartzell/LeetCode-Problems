class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # def two_ops ( sx: int, sy: int, tx: int, ty: int )
        if sx > tx or sy > ty:
            return False
        if sx == tx and sy == ty:
            return True
        return self.reachingPoints( sx, sx + sy, tx, ty ) or self.reachingPoints( sx + sy, sy, tx, ty )

print(Solution().reachingPoints( 1, 1, 3, 5))
