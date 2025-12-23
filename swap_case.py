# Problem: Swap Case
# Platform: HackerRank
# Domain: Python
# Description: Convert lowercase letters to uppercase and uppercase letters to lowercase in a string.
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
