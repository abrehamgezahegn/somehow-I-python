from os.path import exists

print("copying from onw file to another")

FROM_PATH = 'text.txt'
TO_PATH = 'another.txt'

if exists(FROM_PATH) and exists(TO_PATH) : 
    pass
else: 
    print("1 or both files don't exist")
    quit()



from_file_content = open(FROM_PATH).read()
to_file = open(TO_PATH, 'w')
to_file.truncate()
to_file.write(from_file_content)

anything = input("anything you want to add before we close? >")
to_file.write(anything)

to_file.close()

to_file_content = open(to_file.name).read()
to_file_content = open(TO_PATH).read()



print(f"to {to_file_content}")

