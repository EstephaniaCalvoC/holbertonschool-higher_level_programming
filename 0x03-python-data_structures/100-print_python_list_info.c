#include <Python.h>
/**
 * print_python_list_info - Print some basic info about Python lists.
 * @p: Pointer to Python object
 */
void print_python_list_info(PyObject *p)
{
	int size, bytes, i;
	PyObjct *element;
	PyListObject *list = (PyListObject *)p;
	char *type_element = NULL;

	size = Py_SIZE(p);
	bytes = list->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", bytes);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		element = PyList_GET_ITEM(p, i);
		type_element = Py_TYPE(element)->tp_name;

		printf("%s\n", type_element);
	}
}
