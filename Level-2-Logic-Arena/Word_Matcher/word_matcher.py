sentence = input("Enter a sentence: ").lower()

search_word = input("Enter word to search: ").lower()

words = sentence.split()

count = 0

positions = []

index = 1

for word in words:
    if word == search_word:
        count += 1
        positions.append(index)

    index += 1

print("\n----- Result -----")

if count > 0:
    print("Word found!")
    print("Appeared", count, "times")
    print("Positions:", positions)
else:
    print("Word not found")