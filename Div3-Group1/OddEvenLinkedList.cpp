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
    ListNode* oddEvenList(ListNode* head) {
        if(head==NULL or head->next==NULL or head->next->next==NULL)
            return head;
        
        ListNode* even=new ListNode(head->val);
        ListNode* temp=head;
        ListNode* evenHead=even;
        
        while(head)
        {
            if(head->next!=NULL)
            {
                even->next=head->next;
                even=even->next;
                if(head->next->next==NULL)
                    break;
                head->next=head->next->next;
                head=head->next;
            }
            else 
            {
                even->next=NULL;
                break;
            }
        }
        // head->next=NULL;
        // head=NULL;
        if(head!=NULL)
            head->next=evenHead->next;
     

        // return evenHead->next;
        return temp;
    }
};
