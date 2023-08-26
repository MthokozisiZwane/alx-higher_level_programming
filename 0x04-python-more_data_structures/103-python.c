#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject representing Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects
 * @p: PyObject representing the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	printf("  size: %ld\n", size);

	printf("  trying string: ");
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		char byte = PyBytes_AS_STRING(p)[i];

		if (byte >= 32 && byte <= 126)
		printf("%c", byte);
	else
		printf("\\x%.2x", (unsigned char)byte);
	}
	printf("\n");

	printf("  first %ld bytes: ", size < 10 ? size : 10);
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
	printf("%.2x", (unsigned char)PyBytes_AS_STRING(p)[i]);
	if (i != size - 1)
	printf(" ");
	}
	printf("\n");
}
