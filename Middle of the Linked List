/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
    int counter=0;
    ListNode *temp=head;
    while (head->next!=NULL)
    {
        head=head->next;
        counter++;
    }
    if (counter%2==0)
    {
        counter/=2;
    }
    else
    {
        counter/=2;
        counter++;
    }
    for (int i = 0; i < counter; i++)
    {
        temp=temp->next;
    }
    return temp;
    }
};
