with open('newfile.txt', 'a') as f:
    f.write('\nHere’s some additional content.')

with open('newfile.txt', 'r') as f:
    data = f.read()
print(data)
