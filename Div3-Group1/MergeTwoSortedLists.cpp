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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *temp=new ListNode();
        ListNode *tm=temp;

        while (list1 != NULL && list2 != NULL)
        {
            if (list1->val < list2->val)
            {
                ListNode * x=new ListNode(list1->val);
                tm->next=x;
                tm=tm->next;
                list1=list1->next;
            }
            else
            {
                ListNode * x=new ListNode(list2->val);
                tm->next=x;
                tm=tm->next;
                list2=list2->next;

            }
        }
        while (list1!=NULL)
        {
            ListNode * x=new ListNode(list1->val);
            tm->next=x;
            tm=tm->next;
            list1=list1->next;
        }
        while (list2!=NULL)
        {
            ListNode * x=new ListNode(list2->val);
            tm->next=x;
            tm=tm->next;
            list2=list2->next;
        }
        
        return temp->next;

    }
};
