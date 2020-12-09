#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL;
	listint_t *new_node = NULL;

	if (!head)
		return (NULL);

	/*Created new node*/
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	/*Identify split node*/
	tmp = *head;

	/*List empty*/
	if (!tmp || tmp->n >= number)
	{
		new_node->next = tmp;
		*head = new_node;
		return (new_node);
	}

	for (; tmp->next && tmp->next->n < number;)
		tmp = tmp->next;

	new_node->next = tmp->next;
	tmp->next = new_node;

	return (tmp->next);
}
