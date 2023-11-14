from itertools import combinations

def calculate_power_with_subsets(nums):
    subsets = []
    MOD = 10**9 + 7
    power = 0
    for subset_size in range(1, len(nums) + 1):
        for subset in combinations(nums, subset_size):
            max_val = max(subset)
            min_val = min(subset)
            power += (max_val**2 * min_val) % MOD
            subsets.append(list(subset))
    print(f"These are all possible combinations: {subsets}")
    return power

lt = [2, 1, 4]
result = calculate_power_with_subsets(lt)
print(f"Sum of Power of all possible combinations: {result % (10**9 + 7)}")
