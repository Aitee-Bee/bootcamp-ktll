"""
What do you think is a file?
A contiguous set of bytes used to store data.
The smallest unit of storing data in a computer is bits.
8bits -> 1byte
1024bytes -> 1KB
1024KB -> 1MB

Data in a file is organized in a specific format. Could be because of the
file type or could be because of the character encoding.

For the modern file systems, files have 3 main parts
Header: contains meta data of the file like file name, size, type
Data: this is the content of the file.
End of File (EOF): special character that indicate the end of a file. (CR and LF)
CR: Carriage Return ()
LF: Line Feed ()
Windows (CR+LF)()
Linux (LF)()

FILE PATH
A string representation of the location of a file.
We have relative file path and absolute file path.

Relative file path is when you can specify the location of a file
relative to the current location that you are in the OS.

Absolute file path is when you can specify the location  of file
using the full path from the origin (e.g from the C:/ drive in windows OS)

A file path is made up of 3 parts:
Folder path: is simply the listing of all the directories
leading up to the file. Linus uses (/) in seperating directory names
while windows uses the (\). 
Linux /home/shield/training

File name: is the actual name of the file
File extension: is the last part prepended with a dot (.) and it
indicates the type of the file.

Example:
On Linux or Mac: /home/ussd/bianace/bitcoin/wallet.txt


Folder Path is /home/ussd/bianace/bitcoin/
File Name is wallet
Extension is .txt, .xlsx, .docx

CHARCTER ENCODING
An encoding is simply a translation from byte data into
human readable format. (utf-8)

OPENING A FILE IN PYTHON
In Python, you use the function open() to open a file. 
Open takes a single required positional argument with is the filepath
as the least argument and it has to be string.

After you have openned a file, the next most important thing is
to ensure the file is closed.
"""
pointer = open('hello.txt')
try:
    pointer.write("Please create the file and add this line for me.")
except FileNotFoundError as e:
    pass
finally:
    pointer.close()

p = open('hello.txt')
p.close()

print("Can you please print me?")
