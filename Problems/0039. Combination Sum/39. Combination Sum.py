""" 02-17-2022 LeetCode 39. Combination Sum """

candidates = [3, 2, 6, 7]
TARGET = 7

results = []
candidates.sort()
# new_target = target


def backtrack(new_target, curr_combination, start_candidates):
    """Recursive function to build a tree where of every combo compared to sum"""
    if new_target == 0:
        # if weve hit our target, this branch sums to the main target
        results.append(list(curr_combination))  # append this branch as a solution
        return

    for i in range(start_candidates, len(candidates)):
        if new_target - candidates[i] >= 0:
            curr_combination.append(candidates[i])
            new_target -= candidates[i]
            backtrack(new_target, curr_combination.copy(), i)
            new_target += candidates[i]
            curr_combination.pop()

        # Note !!! Originally I was passing a list (curr_combination) without the .copy. Passing a list
        # is passing BY REFERENCE, so the modifications in the next iteration of the recursive step
        # where permanant/global. NOT instanced to that steps iteration. YOU MUST PASS A COPY
        # I didnt test it, but presumably was about to run into this problem for passing the
        # curr_candidates too. new_target is an int, which seems to get passed by value

        # Yes, "immutable" objects (strings, ints etc) are passed by value (pass by object actually)


backtrack(TARGET, [], 0)
print(results)
