with open('test.cs', 'r') as f:
    lines = f.readlines()

    for i in lines:
        if 'assembleversion' in i:
            replace_value = i.split(':')[1][len('assembleversion')+2:-4]
print(replace_value)            

new_value = input("Enter new value: ")
with open('test.cs','r') as file:
    lines = file.read()
new_contents = lines.replace(replace_value, new_value)

with open('test.cs', 'w') as file:
    file.write(new_contents)