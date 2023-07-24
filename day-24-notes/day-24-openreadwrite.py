file = open('sometext.txt')
contents = file.read()
print (contents)

with open('sometext.txt', mode='w') as write_file: # this will close the file after code has finished executing
    write_file.write("no more text")
    # if writing to a file that does not exist a new file will be created

contents = file.read()
print (contents) 

with open('sometext.txt', mode='a') as append_file: # this will append text
    append_file.write('\n bottom text')

contents = file.read()
print (contents)

with open('sometext.txt', mode='w') as reset_file:
    reset_file.write("""top text
        
mannnnnnn this be some text

absolutely wild

some text dot text

bottom text""")

contents = file.read()
print (contents)

file.close()