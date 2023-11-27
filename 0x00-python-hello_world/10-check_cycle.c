#include "lists.h"

/**
 * check_cycle - Checks for a cycle in a singly-linked list.
 * @list: A pointer to the head of the list.
 *
 * Return: 1 if a cycle exists, 0 if there is no cycle.
 */
 
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list)
		return (0);

	fast = list->next;
	slow = list;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
