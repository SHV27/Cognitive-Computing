scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

highest = max(scores)
highest_index = scores.index(highest)
lowest = min(scores)
lowest_count = scores.count(lowest)
reversed_list = list(scores[::-1])

value = 76
if value in scores:
    print(f"{value} is present at index {scores.index(value)}.")
else:
    print(f"{value} is not present.")

print(f"Highest: {highest} (Index: {highest_index})")
print(f"Lowest: {lowest} (Count: {lowest_count})")
print("Reversed List:", reversed_list)
