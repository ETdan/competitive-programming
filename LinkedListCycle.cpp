/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_map<ListNode *, int> m;
        if(head ==NULL || head->next ==NULL )
            return false;
        while(head != NULL)
        {
            if (m[head]!=1)
                m[head]=1;
            else
                return true;; 
            head=head->next;
        }
        
    return false;
        
    }
};
