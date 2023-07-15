class Solution {
public:
    void sortColors(vector<int>& nums) {
        int c=0;
        for (int i = 0; i < nums.size(); i++)
    {
        for (int j = 0; j < nums.size(); j++)
        {
            if (nums[i]<nums[j])
            {
                c=nums[i];
                nums[i]=nums[j];
                nums[j]=c;
            }
        }
    }
    }
};
