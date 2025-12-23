# Problem: Text Wrap
# Platform: HackerRank
# Domain: Python
# Description: Wrap a given string into a paragraph of fixed width using text formatting.
import textwrap

def wrap(string, max_width):
    return '\n'. join (textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
