#include "lists.h"
/**
 * reverse_listint - reverses a singly linked listint_t list
 * @head: a pointer to the starting node of the list to reverse
 *
 * Return: a pointer to the head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head, *prev = NULL, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to the head of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *copy = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			copy = slow->next;
			break;
		}
		if (!fast->next)
		{
			copy = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&copy);

	while (copy && temp)
	{
		if (temp->n == copy->n)
		{
			copy = copy->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!copy)
		return (1);

	return (0);
}
