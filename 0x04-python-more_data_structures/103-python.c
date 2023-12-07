#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var_obj = (PyVarObject *)p;
	Py_ssize_t size = var_obj->ob_size;
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", var_obj->ob_alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
		if (PyBytes_Check(list->ob_item[i]))
			printf("[.] bytes object info\n");
	}
}

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyObject *bytes;
	PyBytesObject *bytes_obj;
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = PyBytes_FromStringAndSize(NULL, 0);
	bytes_obj = (PyBytesObject *)p;
	size = PyBytes_GET_SIZE(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyUnicode_AsUTF8(PyObject_Str(p)));

	printf("  first %ld bytes: ", size > 10 ? 10 : size);
	for (i = 0; i < (size > 10 ? 10 : size); i++)
		printf("%02x%s", (unsigned char)bytes_obj->ob_sval[i], i + 1 <
				(size > 10 ? 10 : size) ? " " : "\n");
	Py_DECREF(bytes);
}
