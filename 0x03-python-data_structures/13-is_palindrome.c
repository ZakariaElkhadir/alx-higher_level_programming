#include "lists.h"
/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: The list
 *
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrom(listint_t **head)
{
    listint_t *tmp;
    int i, s, count;

    count = 0;
    tmp = *head;
    
    while (tmp !=0)
    {
        count++;
        tmp = tmp->next;
    }
    int arr[count];

    tmp = *head;

    for (i = 0; i < count; i++)
    {
        arr[i] = tmp->n;
        tmp = tmp->next;
    }
    for (i = 0,s = count - 1; i < s; i++, s-- )
    {
        if (arr[i] != arr[s])
        return (0);
    }
    return (1);
}