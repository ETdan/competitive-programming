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
    ListNode* reverseList(ListNode* head,ListNode* AR,int l, int r) {
        if(head==NULL || head->next==NULL)
            return head;
            
        ListNode* present=head;
        ListNode* Next=head->next;
        ListNode* preve=AR;

        while(present->next!=NULL && l++ < r)
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

    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if(head==NULL || head->next==NULL || right-left==0)
            return head;

        ListNode* temp=head;
        ListNode* present=head;
        ListNode* Next=head->next;

        ListNode* Interval=NULL;

        ListNode* AR=NULL;

        int l=1;

        while(l++ < left-1)
            temp=temp->next;
        
        AR=temp->next;
        
        while(l++ < right)
            AR=AR->next;
        
        if(AR -> next)
            AR=AR->next;
        else
            AR=NULL;


        if(left==1)
        {
            Interval = reverseList(temp,AR,left,right);
            return Interval;
        }
        else
        {
            Interval = reverseList(temp->next,AR,left,right);
        }

        
        temp->next = Interval;

        // cout<<AR->val;

        // Interval->next=AR;
    
       
       return head;
    }
};
