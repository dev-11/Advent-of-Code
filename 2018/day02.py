lines = [line.strip() for line in open("day02.input").readlines()]

threes = 0
twos = 0

for line in lines:
    found_three = False
    found_two = False
    for letter in line:
        if line.count(letter) == 3 and not found_three:
            threes += 1
            found_three = True
        if line.count(letter) == 2 and not found_two:
            twos += 1
            found_two = True

# answer 1
print(twos*threes)

result = None

for line1 in lines:
    for line2 in lines:
        if sum([char1 != char2 for char1, char2 in zip(line1, line2)]) == 1:
            result = ''.join([char1 for char1, char2 in zip(line1, line2) if char1 == char2])
            break
    if result:
        break

# answer 2
print(result)
