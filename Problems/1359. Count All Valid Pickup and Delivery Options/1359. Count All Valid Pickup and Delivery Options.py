class Solution:
    def countOrders(self, n: int) -> int:
        # pretty sure this is pretty basic combinatronics. If you have n = 3, there are
        # 6 distinct elements to be arranged, 3 pickups and 3 deliveries. We MUST begin
        # doing at least one pickup, so the two classes ARE distinct. Choose 1 of 3.
        # We can then choose any of the remaining pickups, or only this one delivery.
        # Choose 1 of 2, or 1 of 1: 3 choices....

        # well... This "came to me in a dream". It seemed clear there were 2n! choices
        # less the incorrect ones. The question gave 3 examples and it was pretty easy
        # to work out on paper the following. I have the vague intuition for it, but
        # wouldnt have been able to prove WHY it works.

        return (factorial(2 * n) // (2 ** n)) % 1_000_000_007
