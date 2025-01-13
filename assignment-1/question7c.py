with open('newfile.txt', 'r') as f:
    lines = f.readlines()
line_count = len(lines)
print("Total lines:", line_count)
