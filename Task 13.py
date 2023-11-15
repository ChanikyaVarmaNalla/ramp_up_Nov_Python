def find_longest_square_streak(nums):
    square_streaks = []

    for current_num in nums:
        sub_streak = [current_num]
        current_square = current_num ** 2
        while current_square in nums:
            sub_streak.append(current_square)
            current_square = current_square ** 2
        if len(sub_streak) >= 2:
            square_streaks.append(sub_streak)
    return square_streaks

lt = [4, 3, 6, 16, 8, 2]
ss = find_longest_square_streak(lt)
streaks_by_length = {}
if len(ss) < 1:
    print(f"Length of the longest square streak: -1")
else:
    for streak in ss:
        streak_length = len(streak)
        if streak_length in streaks_by_length:
            streaks_by_length[streak_length].append(streak)
        else:
            streaks_by_length[streak_length] = [streak]
print(f"Original numbers: {lt}"
      f"\nSquare streaks: {ss}"
      f"\nLongest square streaks: {streaks_by_length[max(streaks_by_length)]}"
      f"\nLength of longest square streaks: {max(streaks_by_length)}")
