# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# Input
n = int(input())  # number of shoes
shoe_sizes = list(map(int, input().split()))  # list of shoe sizes
m = int(input())  # number of customers

# Count shoe sizes
shoe_inventory = Counter(shoe_sizes)
total_earned = 0

for _ in range(m):
    size, price = map(int, input().split())
    if shoe_inventory[size] > 0:
        total_earned += price
        shoe_inventory[size] -= 1

print(total_earned)
