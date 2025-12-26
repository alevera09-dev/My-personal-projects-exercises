#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *next;
} node;

typedef struct
{
    node *head;
    size_t len;
} list;

//methods linked list
void insert(list *list, int n);
bool search(node *list, int n);
void delete(list *list, int n);
size_t len_list(list *list);
void free_list(node *list);

int main(void)
{
    list *list_numbers = malloc(sizeof(list));
    if (list_numbers != NULL)
    {
        list_numbers->len = 0;
        list_numbers->head = malloc(sizeof(node));
        list_numbers->head->next = NULL;
    }

    insert(list_numbers, 4);
    
    if (search(list_numbers->head, 4))
    {
        printf("No funciona\n");
    }
    else
    {
        printf("Funciona\n");
    }

    free_list(list_numbers->head);
    free(list_numbers);

    return 0;
}

void insert(list *list, int n)
{
    if (list->len == 0)
    {
        list->head->data = n;
        list->len++;
    }
    else
    {
        node *new_element = malloc(sizeof(node));
        new_element->data = n;
        new_element->next = list->head;
        list->head = new_element;
        list->len++;
    }
}

size_t len_list(list *list)
{
    return list->len;
}

bool search(node *head, int n)
{
    if (head->data == n)
    {
        return true;
    }
    else
    {
        if (head->next == NULL)
        {
            return false;
        }

        return search(head->next, n);
    }
}

void delete(list *list, int n)
{
   if (list->head == NULL)
   {
        return;
   }

   node *current = list->head;
   node *prev = NULL;

   //buscar nodo
   while (current != NULL && current->data != n)
   {
        prev = current;
        current = current->next;
   }

   if (current == NULL)
   {
        return;
   }

   if (prev == NULL)
   {
        list->head = current->next;
   }
   else
   {
        prev->next = current->next;
   }

   free(current);
}

void free_list(node *head)
{
    if (head->next == NULL)
    {
        free(head);
    }
    else
    {
        free_list(head->next);
        free(head);
    }
}

