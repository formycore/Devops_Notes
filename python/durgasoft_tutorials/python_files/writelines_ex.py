f = open('ab', 'w')
sentence = "This is a line of text"
list_of_words = sentence.split()
for sen in list_of_words:
    f.writelines(sen+ " ")
f.close()
