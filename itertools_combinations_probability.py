# Problem: Itertools Combinations
# Platform: HackerRank
# Domain: Python
# Description: Calculate the probability that at least one selected index contains the letter 'a' using itertools.combinations.
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

indices = list(range(n))
comb = list(combinations(indices, k))

count = 0
for c in comb:
    for i in c:
        if letters[i] == 'a':
            count += 1
            break

probability = count / len(comb)
print(f"{probability:.4f}")
