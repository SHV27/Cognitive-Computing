with open('example.txt', 'w') as f:
    f.write('This is a new file.\n')
    f.write('It has some different text.')

with open('example.txt', 'r') as f:
    data = f.read()
print(data)
