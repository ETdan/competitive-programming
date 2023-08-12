class Solution {
public:
    vector<int> arrayChange(vector<int>& nums, vector<vector<int>>& operations) {
         
        unordered_map<int,int> m;
        
        for(int i=0; i<nums.size();i++) {
            m[nums[i]]=i;
        }
        for(auto a: operations)
        {
            int index=m[a[0]];
            nums[index]=a[1];
             m.erase(a[0]);
             m[a[1]]=index;
        }

    //     for (const auto& pair : m) {
    //     int key = pair.first;
    //     int value = pair.second;
    //     cout << "Key: " << key << ", Value: " << value << endl;
    // }

        return nums;
    }
};
