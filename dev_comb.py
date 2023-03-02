from more_itertools import combination_with_replacement_index
from itertools import combinations_with_replacement


print(combination_with_replacement_index((1, 2), range(6)))
print(combination_with_replacement_index("abc", "abcdef"))
print(combination_with_replacement_index("aaa", "abcdef"))
print(combination_with_replacement_index("bbc", "abcdef"))
print(combination_with_replacement_index("ggg", "abcdef"))
