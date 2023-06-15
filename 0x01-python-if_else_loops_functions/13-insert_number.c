#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: pointer to the head of the linked list
 * @number: number to be inserted
 * Return: pointer to the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (ptr == NULL || ptr->n >= number)
	{
		new->next = ptr;
		*head = new;
		return (new);
	}
	while (ptr && ptr->next && ptr->next->n < number)
		ptr = ptr->next;

	new->next = ptr->next;
	ptr->next = new;

	return (new);
}
