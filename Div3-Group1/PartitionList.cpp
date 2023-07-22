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
    ListNode* partition(ListNode* head, int x) {

        if(head==NULL or head->next==NULL)
            return head;
        
        ListNode* lessThan=new ListNode();
        ListNode* greaterThan=new ListNode();
        ListNode* greaterThanHead=new ListNode();
        ListNode* answer= new ListNode();
        greaterThanHead->next=greaterThan;
        answer->next=lessThan;

        while(head->next!=NULL)
        {
            if(head->val<x)
            {
                lessThan->next=head;
                lessThan=lessThan->next;

            }
            else
            {
                greaterThan->next=head;
                greaterThan=greaterThan->next;

            }
            head=head->next;
        }
        if(head->val<x)
        {
            lessThan->next=head;
            lessThan=lessThan->next;
            lessThan->next=greaterThanHead->next->next;
            greaterThan->next=NULL;

        }
        else
        {
            greaterThan->next=head;
            greaterThan=greaterThan->next;
            lessThan->next=greaterThanHead->next->next;

        }

        
        return answer->next->next;
    }
};
