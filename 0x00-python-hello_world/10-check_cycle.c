#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to be checked
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list;
	listint_t *next_of_next = list;

	if (!list)
		return (0);

	while (ptr && next_of_next && ptr->next)
	{
		ptr = ptr->next;
		next_of_next = next_of_next->next->next;
		if (ptr == next_of_next)
			return (1);
	}
	return (0);
}
