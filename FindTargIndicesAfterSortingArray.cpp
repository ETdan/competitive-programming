class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        int temp=0;
    vector<int> list;
    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = 0; j < nums.size(); j++)
        {
            if (nums[i]<nums[j])
            {
                temp=nums[i];
                nums[i]=nums[j];
                nums[j]=temp;
            }
        }
    }
    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i]==target)
        {
            list.push_back(i);
        }
        
    }
    return list;
    }
};
