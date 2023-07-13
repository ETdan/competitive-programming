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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* temp=head;
        ListNode* temp1=head;
        if(head==NULL or head->next==NULL)
            return head;
        temp1=temp1->next;

        while(temp)
        {
            if(temp1 == NULL)
            {
                temp->next=NULL;
                temp=temp->next;
            }
            else
            {
                if(temp->val==temp1->val)
                    temp1=temp1->next;
                else{
                    temp->next=temp1;
                    temp=temp1;
                    temp1=temp1->next;
                }
            }
        }
        
        return head;
    }
};
