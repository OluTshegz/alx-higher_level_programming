#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: Python list as an object, an object of type list in Python
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size_p = PyList_Size(p), index;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	PyListObject *element = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size_p);
	printf("[*] Allocated = %ld\n", allocated);
	for (index = 0; index < size_p; index++)
		printf("Element %ld: %s\n", index, Py_TYPE(element->ob_item[index])->tp_name);
}
