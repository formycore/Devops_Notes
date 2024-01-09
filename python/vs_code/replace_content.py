with open('test.cs', 'r') as file:
        file_contents = file.read()

new_contents = file_contents.replace("4.5.6", "1.2.3")

with open('test.cs', 'w') as file:
        file.write(new_contents)


