#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef struct LLNode {
    int val;
    struct LLNode* next;
} node;

class LinkedList {
    node* first;

public:
    LinkedList(){
      first = NULL;
    }

    int size(){
        node* temp = first;

        if(temp == NULL)
            return 0;

        int c = 0;

        while(temp -> next != NULL){
            c++;
            temp = temp -> next;
        }

        return c;
    }

    void append(int i){
        node* lol=first;
                node* lol2=new node;
                lol2->val=i;lol2 -> next = lol; first = lol2;

    }

    int get(int n){
      node* lol=first;
      while((n--)&&(lol->next!=NULL))
             {
                  lol=lol->next;
              }
           int num= lol->val;
       return num;


    }

    void insert(int n, int i){
            node* lol=first;
            if(n)
            while(--n)
             {
                  lol=lol->next;
              }
       node* lol2= new node;
           lol2->val=i;
           lol2->next=lol->next;
           lol->next=lol2;



    }

    int del(int n){
          node* lol=first;
          if(n==0)
            {first=first->next;
              delete lol;
              return 0;
            }
              while(--n)
             {
                  lol=lol->next;
              }
          node* lol2=lol->next;
                  lol->next=lol2->next;
          delete lol2;
          return 0;

    }

    int search(int i){
     node* lol=first;
     int num=-1;
     while((lol->next!=NULL))
       {
         ++num;
            if(lol->val==i)
           return num;
             lol=lol->next;

       }
     return -1;

    }

    void add(LinkedList x) {
        node* l2 = x.first;
        node* l1 = first;
        node* temp = first;

        int c = 0;

        while(l1 != NULL || l2 != NULL){
            int s = c;

            bool flag = true;

            if(l1 != NULL){
                s += l1 -> val;
                l1 = l1 -> next;

                flag = false;
            }

            if(l2 != NULL){
                s += l2 -> val;
                l2 = l2 -> next;

                flag = false;
            }

            if(flag)
                break;

            c = s / 10;

            temp -> val = s % 10;

            if(l1 != NULL || l2 != NULL){
                temp -> next = new node;
                temp = temp -> next;
            }
        }

        if(c != 0){
            temp -> next = new node;
            temp -> next -> val = c;
        }
    }
};

int main() {
    LinkedList l;
    int i,j,n,t,m,lol;
    cin>>t;
    cin>>n;
    for(i=0;i<n;i++)
        {
            cin>>lol;
            l.append(lol);
        }
    --t;
    while(t--)
    {
        cin>>m;
        LinkedList k,r;
        for(i=0;i<m;i++)
        {
            cin>>lol;
            r.append(lol);
        }
        l.add(r);
    }

    for(i=0;i<=l.size();++i)
     cout<<l.get(l.size()-i)<<" ";
    return 0;
}
