def beauty_of_sub_arrays(nums, k, x):
    beauty_list = []
    if x <= k:
        for i in range(len(nums) - k + 1):
            sub_array = nums[i:i+k]
            sub_array.sort()
            if sub_array[x - 1] < 0:
                beauty_list.append(sub_array[x - 1])
            else:
                beauty_list.append(0)
        return beauty_list
    else:
        print(f"xth value {x} is greater than the subarray length kth value {k}")
        return None

lt = [1, -1, -3, 2, 3]
kth = 3
xth = 2
output = beauty_of_sub_arrays(lt, kth, xth)
if output is not None:
    print(f"List of Numbers: {lt}")
    print(f"Beauties of List: {output}")
