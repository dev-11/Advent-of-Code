data = input()

rows = [[word for word in lines.split()] for lines in data.splitlines()]
lines_without_duplicates = []
for row in rows:
    if len(row) == len(set(row)):
        lines_without_duplicates.append(row)

print(len(lines_without_duplicates))

lines_without_anagrams = 0
for line in lines_without_duplicates:
    sorted_words = []
    for word in line:
        sorted_words.append(''.join(sorted(word)))
    if len(sorted_words) == len(set(sorted_words)):
        lines_without_anagrams += 1
        
print(lines_without_anagrams)
  
