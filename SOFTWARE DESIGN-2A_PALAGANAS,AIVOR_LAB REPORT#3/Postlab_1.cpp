#include<stdio.h>
#include<dos.h>
#include "iostream"
#include "ctype.h"
#include "fstream"
#include <assert.h>

using namespace std;
typedef struct Node
{
char character[80];
Node *next, *pre;
}Line;
Line *currentline;
Line *firstline;
Node *head, *tail;
int col;
void createfirstline()
{
Node *p;
p = new Node;
currentline = p;
head = currentline;
tail = currentline;
col = -1;
}
void newline()
{
Node *p;
p = new Node;
p -> next = NULL;
p->pre = currentline;
currentline->next = p;
tail = p;
currentline=p;
col = 0;
}
void createnewline()
{
Node *p;
p = new Node;
p -> next = NULL;
if (head == NULL)
{
head = p;
tail = p;
}
else
{
Node *q = tail;
q->next = p;
p->pre = q;
}
tail = p;
currentline = p;
}

int main()
{
cout << "Text editor : ";
char string[30];
cin.getline (string,30);
ifstream instream;
instream.open(string);

char reading;
currentline = firstline;
createfirstline();
while(instream.read(&reading,sizeof(reading)))
{
if (reading == '\n')
newline();
else
{
col++;
currentline->character[col] = reading;

}
}
instream.close();
}
