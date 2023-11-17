def mirrorReflection(square_size, distance_hit):
    while square_size % 2 == 0 and distance_hit % 2 == 0:
        square_size //= 2
        distance_hit //= 2

    if square_size % 2 == 0:
        return 2
    elif distance_hit % 2 == 0:
        return 0
    else:
        return 1

p = 2
q = 1
result = mirrorReflection(p, q)
print(result)
