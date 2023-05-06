"""03-27-2022 LeetCode 881. Boats to Save People"""


class Solution:
    def numRescueBoats(self, people, limit) -> int:
        people = sorted(people)
        boats = 0
        heaviest = len(people) - 1
        lightest = 0
        count = 0

        # I've always been supsicious that this solution, choosing the lightest person
        # paired with the heaviest, is lazy and not guarenteed to be correct if there
        # are more than 2 spots on the boat. Really, you should try to maximize # of
        # people first, THEN weight, so for three spots you want:
        # The absolute heaviest person, then The heaviest 2nd person SUCH THAT
        # a 3rd person would also definitely fit (if possible), followed by the heaviest
        # 3rd person possible. This ALWAYS leaves lighter people, who will fit better

        # two pointer method, meeting in middle

        while count < len(people):
            if people[heaviest] + people[lightest] <= limit and heaviest != lightest:
                lightest += 1
                count += 1
            boats += 1
            count += 1
            heaviest -= 1

        return boats


print(Solution().numRescueBoats([3, 2, 2, 1], 3))
