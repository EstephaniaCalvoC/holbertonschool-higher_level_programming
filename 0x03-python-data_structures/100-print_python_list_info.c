#include <Python.h>

/**
 * print_python_list_info - Print basic info about Python lists.
 * @p: Pointer to PyObject.
 */
void print_python_list_info(PyObject *p)
{
	int size, bytes, i;
	PyObject *element;

	size = Py_SIZE(p);
	bytes = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", bytes);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		element = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(element)->tp_name);
	}
}
