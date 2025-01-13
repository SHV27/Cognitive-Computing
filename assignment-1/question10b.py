import sys

if len(sys.argv) < 2:
    print("Please provide a string as an argument.")
else:
    print(f"Length of the string: {len(sys.argv[1])}")
