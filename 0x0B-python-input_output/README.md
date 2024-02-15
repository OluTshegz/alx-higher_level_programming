This is a README.md file for this repository

**File - `0-read_file.py`:** Write a function that reads a text file (`UTF8`) and prints it to stdout:

-   Prototype:  `def read_file(filename=""):`
-   You must use the  `with`  statement
-   You don’t need to manage  `file permission`  or  `file doesn't exist`  exceptions.
-   You are not allowed to import any module

**File - `1-write_file.py`:** Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

-   Prototype:  `def write_file(filename="", text=""):`
-   You must use the  `with`  statement
-   You don’t need to manage file permission exceptions.
-   Your function should create the file if doesn’t exist.
-   Your function should overwrite the content of the file if it already exists.
-   You are not allowed to import any module

**File - `2-append_write.py`:**Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

-   Prototype:  `def append_write(filename="", text=""):`
-   If the file doesn’t exist, it should be created
-   You must use the  `with`  statement
-   You don’t need to manage  `file permission`  or  `file doesn't exist`  exceptions.
-   You are not allowed to import any module

**File - `3-to_json_string.py`:** Write a function that returns the JSON representation of an object (string):

-   Prototype:  `def to_json_string(my_obj):`
-   You don’t need to manage exceptions if the object can’t be serialized

**File - `4-from_json_string.py`:** Write a function that returns an object (Python data structure) represented by a JSON string:

-   Prototype:  `def from_json_string(my_str):`
-   You don’t need to manage exceptions if the JSON string doesn’t represent an object.

**File - `5-save_to_json_file.py`:** Write a function that writes an Object to a text file, using a JSON representation:

-   Prototype:  `def save_to_json_file(my_obj, filename):`
-   You must use the  `with`  statement
-   You don’t need to manage exceptions if the object can’t be serialized.
-   You don’t need to manage file permission exceptions.

**File - `6-load_from_json_file.py`:** Write a function that creates an Object from a “JSON file”:

-   Prototype:  `def load_from_json_file(filename):`
-   You must use the  `with`  statement
-   You don’t need to manage exceptions if the JSON string doesn’t represent an object.
-   You don’t need to manage file permissions / exceptions.

**File - `7-add_item.py`:** Write a script that adds all arguments to a Python list, and then save them to a file:

-   You must use your function  `save_to_json_file`  from  `5-save_to_json_file.py`
-   You must use your function  `load_from_json_file`  from  `6-load_from_json_file.py`
-   The list must be saved as a JSON representation in a file named  `add_item.json`
-   If the file doesn’t exist, it should be created
-   You don’t need to manage file permissions / exceptions.

**File - `8-class_to_json.py`:** Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

-   Prototype:  `def class_to_json(obj):`
-   `obj`  is an instance of a Class
-   All attributes of the  `obj`  Class are serializable: list, dictionary, string, integer and boolean
-   You are not allowed to import any module

**File - `9-student.py`:** Write a class  `Student`  that defines a student by:

-   Public instance attributes:
    -   `first_name`
    -   `last_name`
    -   `age`
-   Instantiation with  `first_name`,  `last_name`  and  `age`:  `def __init__(self, first_name, last_name, age):`
-   Public method  `def to_json(self):`  that retrieves a dictionary representation of a  `Student`  instance (same as  `8-class_to_json.py`)
-   You are not allowed to import any module

**File - `10-student.py`:** Write a class  `Student`  that defines a student by: (based on  `9-student.py`)

-   Public instance attributes:
    -   `first_name`
    -   `last_name`
    -   `age`
-   Instantiation with  `first_name`,  `last_name`  and  `age`:  `def __init__(self, first_name, last_name, age):`
-   Public method  `def to_json(self, attrs=None):`  that retrieves a dictionary representation of a  `Student`  instance (same as  `8-class_to_json.py`):
    -   If  `attrs`  is a list of strings, only attribute names contained in this list must be retrieved.
    -   Otherwise, all attributes must be retrieved
-   You are not allowed to import any module

**File - `11-student.py`:** Write a class  `Student`  that defines a student by: (based on  `10-student.py`)

-   Public instance attributes:
    -   `first_name`
    -   `last_name`
    -   `age`
-   Instantiation with  `first_name`,  `last_name`  and  `age`:  `def __init__(self, first_name, last_name, age):`
-   Public method  `def to_json(self, attrs=None):`  that retrieves a dictionary representation of a  `Student`  instance (same as  `8-class_to_json.py`):
    -   If  `attrs`  is a list of strings, only attributes name contain in this list must be retrieved.
    -   Otherwise, all attributes must be retrieved
-   Public method  `def reload_from_json(self, json):`  that replaces all attributes of the  `Student`  instance:
    -   You can assume  `json`  will always be a dictionary
    -   A dictionary key will be the public attribute name
    -   A dictionary value will be the value of the public attribute
-   You are not allowed to import any module

Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

```
guillaume@ubuntu:~/0x0B$ cat 11-main.py 
#!/usr/bin/python3
import os
import sys

Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))


save_to_json_file(j_student_1, path)
read_file(path)
print("\nSaved to disk")


print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

guillaume@ubuntu:~/0x0B$ ./11-main.py student.json
Initial student:
<11-student.Student object at 0x7f832826eda0>
<class '11-student.Student'>
<class 'dict'>
John Doe 23
{"last_name": "Doe", "first_name": "John", "age": 23}
Saved to disk
Fake student:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
Fake Fake 89
Load dictionary from file:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
John Doe 23
guillaume@ubuntu:~/0x0B$ cat student.json ; echo ""
{"last_name": "Doe", "first_name": "John", "age": 23}
guillaume@ubuntu:~/0x0B$ 
```

**File - `12-pascal_triangle.py`:** **Technical interview preparation**:

-   You are not allowed to google anything
-   Whiteboard first

Create a function  `def pascal_triangle(n):`  that returns a list of lists of integers representing the Pascal’s triangle of  `n`:

-   Returns an empty list if  `n <= 0`
-   You can assume  `n`  will be always an integer
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x0B$ cat 12-main.py
#!/usr/bin/python3
"""
12-main
"""
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x0B$ 
guillaume@ubuntu:~/0x0B$ ./12-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x0B$ 
```

**File - `100-append_after.py`:** Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

-   Prototype:  `def append_after(filename="", search_string="", new_string=""):`
-   You must use the  `with`  statement
-   You don’t need to manage  `file permission`  or  `file doesn't exist`  exceptions.
-   You are not allowed to import any module

**File - `101-stats.py`:** Write a script that reads  `stdin`  line by line and computes metrics:

-   Input format:  `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
-   Each 10 lines and after a keyboard interruption (`CTRL + C`), prints those statistics since the beginning:
    -   Total file size:  `File size: <total size>`
    -   where  is the sum of all previous  (see input format above)
    -   Number of lines by status code:
        -   possible status code:  `200`,  `301`,  `400`,  `401`,  `403`,  `404`,  `405`  and  `500`
        -   if a status code doesn’t appear, don’t print anything for this status code
        -   format:  `<status code>: <number>`
        -   status codes should be printed in ascending order

```
guillaume@ubuntu:~/0x0B$ cat 101-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

guillaume@ubuntu:~/0x0B$ ./101-generator.py | ./101-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./101-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./101-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
guillaume@ubuntu:~/0x0B$ 
```
