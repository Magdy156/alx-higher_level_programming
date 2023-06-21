#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);
/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: head of sllist to be reversed
 * Return: head of the reversed linked list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *ptr = *head, *next, *prev = NULL;

	while (ptr)
	{
		next = ptr->next;
		ptr->next = prev;
		prev = ptr;
		ptr = next;
	}

	*head = prev;
	return (*head);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the head of singly-llist
 * Return: 0 or 1
*/
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *rev;
	int size = 0, i;

	if (!(*head) || (*head)->next == NULL)
		return (1);

	ptr = *head;
	/*claculate the size linked list*/
	while (ptr)
	{
		size++;
		ptr = ptr->next;
	}

	ptr = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		ptr = ptr->next;

	/*[1,2,3,3,2,1]*/
	if ((size % 2) == 0 && ptr->n != ptr->next->n)
		return (0);

	ptr = ptr->next->next;
	rev = reverse_listint(&ptr);

	ptr = *head;
	while (rev)
	{
		if (ptr->n != rev->n)
			return (0);
		ptr = ptr->next;
		rev = rev->next;
	}
	return (1);
}
