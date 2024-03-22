# Pattern 1
def print_pattern(rows):
    for i in range(1, rows + 1):
        print('*' * i)

print_pattern(5)  # Prints a triangle pattern

# Pattern 2
def print_pattern2(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '*' * i)

print_pattern2(5)  # Prints an inverted triangle pattern
