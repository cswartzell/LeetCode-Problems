# 04-03-2023 Leetcode 2102. Sequentially Ordinal Rank Tracker
# https://leetcode.com/problems/sequentially-ordinal-rank-tracker/desc

# Python heaps are priority queues and nicely handle tuples sorting by first element
# then second, so we could merely maintain a heap when pushing, then just pop X times
# (probably off a throw away copy) when querying. This would be good if there are lots of
# adds, and few queries.

# Instead, if an interviewer did not want me to abuse the existing heap class you could keep
# two dicts place:score, and vice versa, and an ordered list of scores. This is perhaps a better
# choice as retrieval is faster, and there are probably more queries than adds.


class SORTracker:
    def __init__(self):
        self.num_queries = 0
        self.nth_best = []
        self.place_score = collections.defaultdict(int)

    def add(self, name: str, score: int) -> None:
        see_nth_best = self.nth_best
        see_place_score = self.place_score

        # negating score so the "most negative" is best, so order remains left to right or my head will pop.
        # otherwise we just slice backwards, or do a weird offset when doing get etc. It also affects the
        # lexigraphical ordering check
        self.place_score[name] = -score
        # Ugh, do I need to do a binary search here?
        insert_idx = bisect.bisect_left(
            self.nth_best, -score, key=lambda place: self.place_score[place]
        )
        # Look, Im not going to write my own lexigraphical order checker too
        while (
            insert_idx < len(self.nth_best)
            and self.place_score[self.nth_best[insert_idx]] == -score
            and self.nth_best[insert_idx] < name
        ):
            insert_idx += 1
        # self.nth_best = self.nth_best[:insert_idx] + [name] + self.nth_best[insert_idx:]
        self.nth_best.insert(insert_idx, name)

    def get(self) -> str:
        see_nth_best = self.nth_best
        see_num_queries = self.num_queries

        self.num_queries += 1
        return self.nth_best[self.num_queries - 1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
