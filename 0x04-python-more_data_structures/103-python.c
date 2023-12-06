#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: a Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		if (strcmp(Py_TYPE(PyList_GetItem(p, i))->tp_name, "bytes") == 0)
			print_python_bytes(PyList_GetItem(p, i));
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: a Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

	if (size > 10)
		size = 10;
	else
		size++;
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)*(((PyBytesObject *)p)->ob_sval + i));
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}
