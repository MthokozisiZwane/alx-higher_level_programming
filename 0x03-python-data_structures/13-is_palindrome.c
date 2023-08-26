#include <stddef.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the list.
 * Return: Pointer to the new head.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *next, *current = head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the pointer of the head of the list.
 * Return: 1 if palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	if (!*head || !(*head)->next)
	return (1);

	listint_t *slow = *head, *fast = *head, *prev_slow = NULL, *second_half;
	int palindrome = 1;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	second_half = fast ? slow->next : slow;
	prev_slow->next = NULL;
	second_half = reverse_list(second_half);

	for (listint_t *first = *head, *second = second_half; first && second;
	first = first->next, second = second->next)
	{
		if (first->n != second->n)
		{
			palindrome = 0;
			break;
		}
	}

	prev_slow->next = reverse_list(second_half);
	return (palindrome);
}

