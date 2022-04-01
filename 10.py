# open
"""
The open() function is used for to open files.
"""

f = open("file.txt")
print(f.read()) # for read the file
"""
The argument of the open() function is the path to the file.

You can specify the mode used to open a file by appling a second argument to the open function.

'r' corresponds to read mode and is the default:
"""

f = open("filename.txt", "r")
print(f.read()) # for read the file
"""
Hear are the other modes avaliable:
w - write mode
a - append mode
b - binary mode
x - create mode
"""
#-------------------------------------------------------------------
#read
"""
The read() method is used to read the content of an opened file
"""
f = open("filename.txt", "r")
d = f.read()
print(d) # for read the file
"""
This will output the entire content of the file.
"""

#-------------------------------------------------------------------

#readlines
"""
The readline() method returns a list, where each element is a line in the file.
"""

f = open("filename.txt", "r")
print(f.readlines()[1]) # {{start from 0, 1, 2, 3, ... }}

"""
This will output the 2nd line of the file.
"""

#-------------------------------------------------------------------

#write

"""
Use the write() method to write content to a file.
"""

# If the file is opend in write mode, the content of the file will be overwritten:
f = open('newfile.txt', 'w')
f.write("Some new text")

# You can use the append mode to add content to an existing file:
f = open('newfile.txt', 'a')
f.write("Some append text")

# {{{ Both 'w' and 'a' modes will create the file, if it doesn't exist.}}}


#-------------------------------------------------------------------

# close
"""
The close() method is used to close the file after reading/writing.
"""

f = open("filename.txt", "r")
print(f.read())
f.close()

# It's good idea to always close the file to avoid wasting resources.

#-------------------------------------------------------------------

#with

"""
The with statement is used in exception handeling and makes your code shorter.
"""
#ex.

#without with
f = open('file1.txt', 'w')
try:
    f.write('some text')
finally:
    f.close()

#using with
with open('file1.txt', 'w') as f:
    f.write('some text')

'''
The file is automatically closed at the end of the with statement, even if exceptions happen.
'''