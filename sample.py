lt = [1, 2, 3, 4, 5, 6]
k = 3
out_put = []
for i in range(len(lt)):
    if lt is None:
        break
    else:
        sub_lt = lt[:k]
        if len(sub_lt) == k:
            for j in sub_lt:
                lt.remove(j)
            out_put.extend(sub_lt[::-1])
            sub_lt = []
        else:
            out_put.extend(sub_lt)
            break
print(out_put)
