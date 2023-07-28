class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> merged;
        int nm=0;
        int nn=0;

        while (nm!=m && nn!=n) 
        {
            if(nums1[nm]>nums2[nn])
            {
                merged.push_back(nums2[nn]);
                nn++;
            }else
            {
                merged.push_back(nums1[nm]);
                nm++;
            }
        }

        if(nm!=m)
        {
            while (nm!=m)
            {
                merged.push_back(nums1[nm]);
                nm++;
            }
        }

        if(nn!=n)
        {
            while (nn!=n)
            {
                merged.push_back(nums2[nn]);
                nn++;
            }
        }

        nums1=merged;
    }
};
