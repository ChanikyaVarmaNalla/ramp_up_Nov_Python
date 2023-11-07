import matplotlib.pyplot as plt

def plot_letter_counts(input_string):
    string_dict = dict(sorted({j: input_string.count(j) for j in input_string.lower() if j.isalpha()}.items()))

    plt.figure(figsize=(12, 6))
    plt.bar(list(string_dict.keys()), list(string_dict.values()), color='yellow')
    plt.title(f'Letter Counts in the Given String: {input_string}')
    plt.xlabel('Letters')
    plt.ylabel('Counts')
    plt.show()

st = "The quick brown fox jumps over the lazy dog and " \
     "the dog barks at the moon while others watch silently without a sound"
print(f"Initial Strings: {st}")
plot_letter_counts(st)
