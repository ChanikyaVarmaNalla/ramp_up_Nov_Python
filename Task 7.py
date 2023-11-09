import re

def find_matching_substrings(pattern, input_string):
    return re.findall(pattern, input_string)

st = "OpenAI is developing cutting-edge artificial intelligence technology."
pt = r".e+.l?"
res = find_matching_substrings(pt, st)
print(res)
