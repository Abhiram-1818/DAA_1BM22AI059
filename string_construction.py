def stringConstruction(s):
    return len(set(s))

# Reading input
n = int(input())
strings = [input().strip() for _ in range(n)]

# Processing each string
for s in strings:
    print(stringConstruction(s))
