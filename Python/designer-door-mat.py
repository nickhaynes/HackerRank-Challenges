dimensions = input().split()
n = int(dimensions[0])
m = int(dimensions[1])
pattern = '.|.'
wel = 'WELCOME'

# Set Top Pattern
for i in range(n // 2):
    j = ((2 * i) + 1) * pattern
    print(j.center(m, '-'))

# Set Middle Line
print(wel.center(m, '-'))

# Set Bottom Pattern
for i in range(n // 2):
    j = ((n - 2) - 2 * i) * pattern
    print(j.center(m, '-'))