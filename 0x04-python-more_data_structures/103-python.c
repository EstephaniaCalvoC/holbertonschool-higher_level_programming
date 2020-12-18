#include <Python.h>

/**
 * print_python_bytes - Print some basic info about Python bytes objects.
 * @p: Pointer to a PyObject
 */
void print_python_bytes(PyObject *p)
{
	long unsigned int i, len, size;
	const char *type = p->ob_type->tp_name;
	PyVarObject *obj = (PyVarObject *)p;
	PyBytesObject *obj_bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	/*Validate input*/
	if (strcmp(type, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/*If is an valid input*/
	size = obj->ob_size;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", obj_bytes->ob_sval);

	if (size > 10)
		len = 10;
	else
		len = size + 1;

	printf("  first %lu bytes: ", size);

	for (i = 0; i < len; i++)
	{
		/*Convert to char and print*/
		printf("%02hhx", obj_bytes->ob_sval[i]);
		if (i < len -1)
			printf(" ");
		else
			printf("\n");
	}
}

/**
 * print_python_list - Print some basic info about Python lists
 * @p: Pointer to a PyObject
 */
void print_python_list(PyObject *p)
{
	int size, bytes, i;
	const char *type;

	PyListObject *list = (PyListObject *)p;
	PyVarObject *obj = (PyVarObject *)p;
	PyObject *element = NULL;

	size = obj->ob_size;
	bytes = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", bytes);

	for (i = 0; i < size; i++)
	{
		element = list->ob_item[i];
		type = element->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);

		if (strcmp(type, "bytes") == 0)
			print_python_bytes(element);
	}
}
