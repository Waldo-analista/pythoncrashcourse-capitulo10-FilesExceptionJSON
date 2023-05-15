'''
with open(r'text_files\pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents.rstrip())
'''
'''
filename=r'text_files\pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip('\n'))
'''
'''
filename=r'text_files\pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.rstrip('\n'))
'''
filename=r'text_files\pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()

#print(lines)




pi_string=''
for line in lines:
    pi_string+=line.strip()
    
print(pi_string)
