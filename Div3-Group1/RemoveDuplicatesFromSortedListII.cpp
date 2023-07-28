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
        ListNode* temp=new ListNode();
        ListNode* temp1=temp;
        int revious=-101;
        if(head==NULL or head->next==NULL)
            return head;

        while(head->next!=NULL)
        {
            if(head->next != NULL)
            {
                if(head->val!=head->next->val && head->val!=revious)
                {
                    temp->next=head;
                    temp=temp->next;
                }
                else
                {
                    revious=head->val;
                }
                    head=head->next;
            }

        }
        if(head->val!=revious)
        {
            temp->next=head;
            temp=temp->next;
        }
        else
            temp->next=NULL;
        cout<<head->val<<endl;
        
        return temp1->next;
    }
};
