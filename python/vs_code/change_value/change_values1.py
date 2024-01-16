with open('test.cs', 'r') as f:
    lines = f.read()

for line in lines:
    if 'assembleversion' in line:
        print(line)