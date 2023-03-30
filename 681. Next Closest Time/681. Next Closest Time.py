digits = {time[0], time[1], time[3], time[4]}
tim = time[:2] + time[3:]
if tim == "0000":
    tim = "2400"

max_dif = 100000  # arbitrary big int
curr_best = ""

for dig1 in digits:
    if dig1 not in {"0", "1", "2"}:
        continue
    for dig2 in digits:
        if dig1 == "2":
            if dig2 not in {"0", "1", "2", "3"}:
                continue
        for dig3 in digits:
            if dig3 not in {"0", "1", "2", "3", "4", "5"}:
                continue
            for dig4 in digits:
                new_tim = dig1 + dig2 + dig3 + dig4
                # Account for wrap and ONLY one time possible: 11:11 can only be 11:11 TWENTRY FOUR HOURS LATER
                if int(new_tim) <= int(tim):
                    if abs(int(new_tim) + 2400 - int(tim)) < max_dif:
                        max_dif = abs(int(new_tim) + 2400 - int(tim))
                        curr_best = new_tim
                else:
                    if abs(int(new_tim) - int(tim)) < max_dif:
                        max_dif = abs(int(new_tim) - int(tim))
                        curr_best = new_tim

return curr_best[:2] + ":" + curr_best[2:]
