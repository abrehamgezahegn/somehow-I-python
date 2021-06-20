from sys import argv
# text = open(argv[0])
# print(text.read())

text_file =open("text.txt", 'w')
text_file.truncate()
text_file.write("Thst's\n")
text_file.write("What\n")
text_file.write("She said\n")
text_file.close()

print("text file" , text_file.name)
text_file = open(text_file.name)
content = text_file.readline()
text_file.seek(2)
print("1" , content)
content = text_file.readline()
text_file.seek(2)
print("2" , content)

# content = text_file.readline()
# text_file.seek(1)
# print("1" , content)


content = text_file.readlines()
print("All lines" , content)