rules, updates = open('/Users/tanumoykolay/Documents/AdventOfCode/day5.txt').read().split('\n\n')
updates = [x.split(',') for x in updates.split('\n')]

def true_pos(x, nums): return len(nums) - 1 - sum(f"{x}|{y}" in rules for y in nums)
def mid(nums): return next(x for x in nums if true_pos(x, nums) == len(nums)//2)
def is_ordered(nums): return all(i == true_pos(x, nums) for i,x in enumerate(nums))

print(sum(int(mid(nums)) for nums in updates if is_ordered(nums)))
print(sum(int(mid(nums)) for nums in updates if not is_ordered(nums)))