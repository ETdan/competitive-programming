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
    bool isPalindrome(ListNode* head) {
        bool answer= true;
        vector<int> container;

        ListNode* holder = head;

        if(holder->next==NULL)
        {
            return true;
        }
        else
        {
            while(holder)
            {
                container.push_back(holder->val);
                holder=holder->next;
            }
        }
        
        long long int start=0;
        long long int end=container.size()-1;

        while(start<end)
        {
            if(container[start]!=container[end])
            {
                answer=false;
                break;
            }   
            else{
                start++;
                end--;
            }
        }
        return answer;
    }
};
