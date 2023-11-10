def full_justify(words, maxWidth):
    result, cur, num_of_letters = [], [], 0
    for word in words:
        if num_of_letters + len(word) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += ' '
            result.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [word]
        num_of_letters += len(word)
    result.append(' '.join(cur).ljust(maxWidth))
    return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 21
output = full_justify(words, maxWidth)

for line in output:
    print(line)
