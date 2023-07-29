class Solution {
public:
    void rotate(vector<int>& nums, int k) {

        if(nums.size()<nums.size()-k)
            while(nums.size()<nums.size()-k)
                k-=nums.size();

        int tempK=k;
        vector<int> firstPart;
        
        while(k)
            firstPart.push_back(nums[nums.size()-(k--)]);
        
        nums.erase(nums.end() - tempK, nums.end());
        

        nums.insert(nums.begin(), firstPart.begin(), firstPart.end());
    }
};
