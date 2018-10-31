import itertools

data = input()

rows = [sorted([int(number) for number in lines.split()]) for lines in data.splitlines()]
print(sum([abs(max(row) - min(row)) for row in rows]))

sum_2 = sum(b//a for row in rows for a,b in itertools.combinations(row,2) if b%a==0)

print(sum_2)
