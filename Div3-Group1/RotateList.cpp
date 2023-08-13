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
    ListNode* rotateRight(ListNode* head, int k) {

        if(k==0 || head==NULL || head->next==NULL)
            return head;
        int length=0;
        ListNode* t=head;
        
        while(t!=NULL)
        {
            t=t->next;
            length++;
        }

        // cout<<length<<endl;

        if(k > length)
        {
            while(k > length)
                k-=length;
        }
        
        if(length == k)
            return head;

        ListNode* temp=head;
        ListNode* follower=head;
        ListNode* leader=head;
        
        while(leader->next != NULL)
        {
            if(k<=0)
                follower=follower->next;
            
            leader=leader->next;
            k--;
        }
        
        temp=follower->next;
        follower->next=NULL;
        leader->next=head;

        return temp;
        
    }
};
