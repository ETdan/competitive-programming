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
    ListNode* reverseList(ListNode* head) {
        if(head==NULL || head->next==NULL)
            return head;
            
        ListNode* present=head;
        ListNode* Next=head->next;
        ListNode* preve=NULL;

        while(present->next!=NULL)
        {
            present->next=preve;
            preve=present;

            if(Next!=NULL)
                present=Next;
            if(Next->next!=NULL)
                Next=Next->next;
            else
                Next==NULL;
        }

            present->next=preve;
            preve=present;

        
        return preve;
    }
};
