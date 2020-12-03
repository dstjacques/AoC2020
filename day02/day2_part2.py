def is_valid(line):
    policy, password = line.split(": ")

    limit, letter = policy.split(" ")
    low, high = limit.split("-")
    low = int(low)
    high = int(high)

    if (password[low-1] == letter) ^ (password[high-1] == letter):
        return True
    return False

input = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

valid_count = 0
for line in input.strip().split("\n"):
    if is_valid(line):
        valid_count += 1
print(valid_count)
