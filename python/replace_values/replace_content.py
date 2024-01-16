with open('test.cs', 'r') as file:
        file_contents = file.read()
        #file_contents = file.readlines() 

new_contents = file_contents.replace("1.2.3", "1.2.4")

with open('test.cs', 'w') as file:
        file.write(new_contents)


