def max_students(seats):
    m, n = len(seats), len(seats[0])
    dp = [[0] * (1 << n) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1 << n):
            if all((j >> k) & 1 == 0 or seats[i - 1][k] == '.' for k in range(n)):
                for k in range(1 << n):
                    if not (k & j) and not (j & (k << 1)) and not (j & (k >> 1)):
                        dp[i][j] = max(dp[i][j], dp[i - 1][k] + bin(j).count('1'))
    return max(dp[-1])

seats = [["#", ".", "#", "#", ".", "#"],
         [".", "#", "#", "#", "#", "."],
         ["#", ".", "#", "#", ".", "#"]]


result = max_students(seats)
print(f"Maximum number of students that can take the exam together without any cheating being possible: {result}")
