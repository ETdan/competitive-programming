class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> New;
        for (int i = 0; i < nums.size(); i++)
            for (int j = i+1; j < nums.size(); j++)
                if (nums[i]+nums[j]==target)
                {
                    New.push_back(i);
                    New.push_back(j);
                    return New;
                }
        return New;
    }
};
