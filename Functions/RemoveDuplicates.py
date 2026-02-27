def remove_duplicates(seq):
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

raw = input("Enter numbers separated by spaces: ")
items = []
for i in raw.split():
    items.append(int(i))
print(remove_duplicates(items)) 