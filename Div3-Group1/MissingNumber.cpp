#include <algorithm>
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int answer;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i++)
            if(nums[i]!=i)
            {
                answer= i;
                break;
            }
        return answer;
    }
};
