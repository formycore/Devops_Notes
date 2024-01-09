def replace_text(file_path, search_word, replace_word):
    with open(file_path, 'r') as file:
        file_contents = file.read()

    new_contents = file_contents.replace(search_word, replace_word)

    with open(file_path, 'w') as file:
        file.write(new_contents)
