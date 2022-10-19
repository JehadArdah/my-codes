my_file = open('reading_text','r')
contents=my_file.readlines()
for content in contents:
    print(content)
my_file.close()