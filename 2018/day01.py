numbers = [int(string_number) for string_number in open("day01.input").readlines()]

# answer 1
print(sum(numbers))

index = 0
numbers_length = len(numbers)

frequencies = set()
frequency = 0

while True:
    frequency += numbers[index % numbers_length]
    if frequency in frequencies:
        break
    frequencies.add(frequency)
    index += 1

# answer 2
print(frequency)
