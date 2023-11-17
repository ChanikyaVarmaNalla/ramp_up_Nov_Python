class FreqStack:
    def __init__(self):
        self.stack = []
        self.freq_map = {}
        self.index_map = {}

    def push(self, num):
        self.stack.append(num)

        if num not in self.freq_map:
            self.freq_map[num] = 1
        else:
            self.freq_map[num] += 1
        freq = self.freq_map[num]

        if freq not in self.index_map:
            self.index_map[freq] = [len(self.stack) - 1]
        else:
            self.index_map[freq].append(len(self.stack) - 1)

    def pop(self):
        if not self.stack:
            raise ValueError("Stack is empty")

        max_freq = max(self.index_map.keys())
        idx_to_pop = self.index_map[max_freq].pop()

        if not self.index_map[max_freq]:
            del self.index_map[max_freq]

        popped_num = self.stack[idx_to_pop]
        self.stack[idx_to_pop] = None  # Mark the element as removed
        self.freq_map[popped_num] -= 1

        if self.freq_map[popped_num] == 0:
            del self.freq_map[popped_num]
        return popped_num

nums = [5, 7, 5, 7, 4, 5]
freq_stack = FreqStack()
for i in range(len(nums)):
    freq_stack.push(nums[i])
print(f"Stack: {freq_stack.stack}\n")

for _ in range(4):
    print(f"Popped Numbers: {freq_stack.pop()}")
    print(f"Updated Stack: {freq_stack.stack}")
