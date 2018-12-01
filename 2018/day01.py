numbers = [int(x) for x in open("day01.input").readlines()]

# answer 1
print(sum(numbers))

frequencies = set()
frequency = 0
index = 0

while True:
    frequency += numbers[index % len(numbers)]
    if frequency in frequencies:
        break
    frequencies.add(frequency)
    index += 1

# answer 2
print(frequency)
