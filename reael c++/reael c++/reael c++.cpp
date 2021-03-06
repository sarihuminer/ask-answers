// reael c++.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h> 
#include <stdlib.h> 
using namespace std;

struct Node {
	int data;
	struct Node *next;
};


/* Function to push a node */
void push(struct Node** head_ref, int new_data)
{
	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
	newNode->data = new_data;
	newNode->next = *head_ref;
	(*head_ref) = newNode;
}

void reverse(struct Node** head) {
	struct Node* prev = NULL;
	struct Node* next = NULL;
	struct Node* current=*head;

	while (current!=NULL) {
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
void printList(struct Node** head) {
	struct Node* tmp = (struct Node*)malloc(sizeof(struct  Node));
	tmp = *head;
	while (tmp) {
		printf("%d ", tmp->data);
		tmp = tmp->next;
	}
}
void main()
{
	struct Node* head = NULL;
	push(&head, 20);
	push(&head, 4);
	push(&head, 15);
	push(&head, 85);
	printf("given linked list");
	printList(&head);
	reverse(&head);
	printf("reverse linked list");
	printList(&head);

}

