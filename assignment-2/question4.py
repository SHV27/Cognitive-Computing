A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

union_set = A | B
intersection_set = A & B
sym_diff_set = A ^ B
is_subset = A.issubset(B)
is_superset = B.issuperset(A)

X = int(input("Enter a score to remmove from A: "))
if X in A:
    A.remove(X)
    print(f"{X} removed from A.")
else:
    print(f"{X} not found inn A.")

print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Symmetric Difference: {sym_diff_set}")
print(f"A is subset of B: {is_subset}")
print(f"B is superset of A: {is_superset}")
print("Updated Set A:", A)
