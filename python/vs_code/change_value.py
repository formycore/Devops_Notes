import re
with open('test.cs', 'r') as file:
    content = file.readlines()

for i ,line in enumerate(content):
    match = re.search(r"\[assemble:fileversion\((.*?)\)]",line)
    print(line)
    if match:
        content[i] = line.replace(match.group(1),"3.4.5")
        break
with open('test.cs', 'w') as file:
    file.writelines(content)