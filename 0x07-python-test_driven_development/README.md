This is a README.md file for this repository

**Files - `0-add_integer.py`, and `tests/0-add_integer.txt`:** Write a function that adds 2 integers.

-   Prototype:  `def add_integer(a, b=98):`
-   `a`  and  `b`  must be integers or floats, otherwise raise a  `TypeError`  exception with the message  `a must be an integer`  or  `b must be an integer`
-   `a`  and  `b`  must be first casted to integers if they are float
-   Returns an integer: the addition of  `a`  and  `b`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x07$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
guillaume@ubuntu:~/0x07$ 
```

**Files - `2-matrix_divided.py`, and `tests/2-matrix_divided.txt`:** Write a function that prints  `My name is <first name> <last name>`

-   Prototype:  `def say_my_name(first_name, last_name=""):`
-   `first_name`  and  `last_name`  must be strings otherwise, raise a  `TypeError`  exception with the message  `first_name must be a string`  or  `last_name must be a string`
-   You are not allowed to import any module

**Files - `3-say_my_name.py`, and `tests/3-say_my_name.txt`:** Write a function that prints a square with the character  `#`.

-   Prototype:  `def print_square(size):`
-   `size`  is the size length of the square
-   `size`  must be an integer, otherwise raise a  `TypeError`  exception with the message  `size must be an integer`
-   if  `size`  is less than  `0`, raise a  `ValueError`  exception with the message  `size must be >= 0`
-   if  `size`  is a float and is less than 0, raise a  `TypeError`  exception with the message  `size must be an integer`
-   You are not allowed to import any module

**Files - `4-print_square.py`, and `tests/4-print_square.txt`:** Write a function that prints a square with the character  `#`.

-   Prototype:  `def print_square(size):`
-   `size`  is the size length of the square
-   `size`  must be an integer, otherwise raise a  `TypeError`  exception with the message  `size must be an integer`
-   if  `size`  is less than  `0`, raise a  `ValueError`  exception with the message  `size must be >= 0`
-   if  `size`  is a float and is less than 0, raise a  `TypeError`  exception with the message  `size must be an integer`
-   You are not allowed to import any module

**Files - `5-text_indentation.py`,  and `tests/5-text_indentation.txt`:** Write a function that prints a text with 2 new lines after each of these characters:  `.`,  `?`  and  `:`

-   Prototype:  `def text_indentation(text):`
-   `text`  must be a string, otherwise raise a  `TypeError`  exception with the message  `text must be a string`
-   There should be no space at the beginning or at the end of each printed line
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x07$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

guillaume@ubuntu:~/0x07$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/5-text_indentation.txt
guillaume@ubuntu:~/0x07$ 
```

**File - `tests/6-max_integer_test.py`:** Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function  `def max_integer(list=[]):`.

-   Your test file should be inside a folder  `tests`
-   You have to use the  [unittest module](https://intranet.alxswe.com/rltoken/hX5a13o-1mXGTQASWBitFQ "unittest module")
-   Your test file should be python files (extension:  `.py`)
-   Your test file should be executed by using this command:  `python3 -m unittest tests.6-max_integer_test`
-   All tests you make must be passable by the function below
-   We strongly encourage you to work together on test cases, so that you don’t miss any edge case

```
guillaume@ubuntu:~/0x07$ cat 6-max_integer.py
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

guillaume@ubuntu:~/0x07$ 
guillaume@ubuntu:~/0x07$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ ./6-main.py
4
4
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
OK
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
guillaume@ubuntu:~/0x07$ 
```

**Files - `100-matrix_mul.py`, and `tests/100-matrix_mul.txt`:** Write a function that multiplies 2 matrices:

-   Read:  [Matrix multiplication - only Matrix product (two matrices)](https://intranet.alxswe.com/rltoken/Qw_rYR3lYYL5DHDH-iCWCA "Matrix multiplication - only Matrix product (two matrices)")
    
-   Prototype:  `def matrix_mul(m_a, m_b):`
    
-   `m_a`  and  `m_b`  must be validated with these requirements in this order
    
-   `m_a`  and  `m_b`  must be an list of lists of integers or floats:
    
    -   if  `m_a`  or  `m_b`  is not a list: raise a  `TypeError`  exception with the message  `m_a must be a list`  or  `m_b must be a list`
    -   if  `m_a`  or  `m_b`  is not a list of lists: raise a  `TypeError`  exception with the message  `m_a must be a list of lists`  or  `m_b must be a list of lists`
    -   if  `m_a`  or  `m_b`  is empty (it means:  `= []`  or  `= [[]]`): raise a  `ValueError`  exception with the message  `m_a can't be empty`  or  `m_b can't be empty`
    -   if one element of those list of lists is not an integer or a float: raise a  `TypeError`  exception with the message  `m_a should contain only integers or floats`  or  `m_b should contain only integers or floats`
    -   if  `m_a`  or  `m_b`  is not a rectangle (all ‘rows’ should be of the same size): raise a  `TypeError`  exception with the message  `each row of m_a must be of the same size`  or  `each row of m_b must be of the same size`
-   If  `m_a`  and  `m_b`  can’t be multiplied: raise a  `ValueError`  exception with the message  `m_a and m_b can't be multiplied`
    
-   You are not allowed to import any module
    

```
guillaume@ubuntu:~/0x07$ cat 100-main.py
#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

guillaume@ubuntu:~/0x07$ ./100-main.py 
[[7, 10], [15, 22]]
[[13, 16]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2
6 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
```

**Files - `101-lazy_matrix_mul.py`, and `tests/101-lazy_matrix_mul.txt`:** Write a function that multiplies 2 matrices by using the module  [NumPy](https://intranet.alxswe.com/rltoken/sXnBuOVSyhKEGt-biOyOWg "NumPy")

To install it:  `pip3 install numpy==1.15.0`

-   Prototype:  `def lazy_matrix_mul(m_a, m_b):`
-   Test cases should be the same as  `100-matrix_mul`  but with new exception type/message

```
guillaume@ubuntu:~/0x07$ cat 101-main.py
#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

guillaume@ubuntu:~/0x07$ ./101-main.py 
[[ 7 10]
 [15 22]]
[[13 16]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt 
guillaume@ubuntu:~/0x07$ 
```

**File - `102-python.c`:** Create a function that prints Python strings.

-   Prototype:  `void print_python_string(PyObject *p);`
-   Format: see example
-   If  `p`  is not a valid string, print an error message (see example)
-   Read:  [Unicode HOWTO](https://intranet.alxswe.com/rltoken/UkkHHaILiYf9d_a3nc4Bxw "Unicode HOWTO")

About:

-   Python version: 3.4
-   You are allowed to use the C standard library
-   Your shared library will be compiled with this command line:  `gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`

```
julien@ubuntu:~/0x07. Pyhton Strings$ cat 102-tests.py
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "The spoon does not exist"
lib.print_python_string(s)
s = "ложка не существует"
lib.print_python_string(s)
s = "La cuillère n'existe pas"
lib.print_python_string(s)
s = "勺子不存在"
lib.print_python_string(s)
s = "숟가락은 존재하지 않는다."
lib.print_python_string(s)
s = "スプーンは存在しない"
lib.print_python_string(s)
s = b"The spoon does not exist"
lib.print_python_string(s)
julien@ubuntu:~/0x07. Pyhton Strings$ gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
julien@ubuntu:~/0x07. Pyhton Strings$ python3 ./102-tests.py
[.] string object info
  type: compact ascii
  length: 24
  value: The spoon does not exist
[.] string object info
  type: compact unicode object
  length: 19
  value: ложка не существует
[.] string object info
  type: compact unicode object
  length: 24
  value: La cuillère n'existe pas
[.] string object info
  type: compact unicode object
  length: 5
  value: 勺子不存在
[.] string object info
  type: compact unicode object
  length: 14
  value: 숟가락은 존재하지 않는다.
[.] string object info
  type: compact unicode object
  length: 10
  value: スプーンは存在しない
[.] string object info
  [ERROR] Invalid String Object
julien@ubuntu:~/0x07. Pyhton Strings$ 
```
