class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
         int c=0;
    vector<int> n;
    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = 0; j < nums.size(); j++)
            if (nums[i]>nums[j])
                c++;
        n.push_back(c);
        c=0;
    }
    return n;
    }
};
