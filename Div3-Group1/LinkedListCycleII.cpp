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
    ListNode *detectCycle(ListNode *head) {
        unordered_map<ListNode *, int> m;
        int index=0;
        if(head ==NULL || head->next ==NULL )
            return NULL;
        
        while(head != NULL)
        {
            if (m.count(head)== 0)
                m[head]=index;
            else
            {
                index=m[head];
                for (const auto& pair : m)
                    if (pair.second == index)
                        return pair.first;
            }
            head=head->next;
            index++;
        }
        
    return NULL;
    }
};
