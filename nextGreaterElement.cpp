class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    vector<int> New;
    bool found=false;

    for (size_t i = 0; i < nums1.size(); i++)
    {
        found=false;
        for (size_t j = 0; j < nums2.size(); j++)
        {
            if (nums1[i]==nums2[j])
                found=true;
            if (found && nums2[j]>nums1[i])
            {
                New.push_back(nums2[j]);
                found=false;
            }
        }
        if (found)
            New.push_back(-1);   
    }

    return New;

}
};
