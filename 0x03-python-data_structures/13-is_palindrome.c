#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks is linked list is a palindrome
 * @head: Double pointer to head
 * Return: 1 if true else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *c1;
	unsigned int len = 0, i = 0;
	unsigned int *arr;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	c1 = *head;
	while (c1 != NULL)
	{
		c1 = c1->next;
		len++;
	}
	if (len == 1)
		return (1);
	arr = malloc(sizeof(int) * len);
	if (arr == NULL)
	{
		free(arr);
		return (0);
	}
	c1 = *head;
	for (i = 0; c1 != NULL; i++)
	{
		arr[i] = c1->n;
		c1 = c1->next;
	}
	len = len - 1;
	for (i = 0; i <= len / 2; i++)
	{
		if (arr[i] != arr[len - i])
		{ 
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
