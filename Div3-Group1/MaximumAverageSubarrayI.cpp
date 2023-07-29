class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double max=0;
        double average=0;
        int kDouble=k;

        while(kDouble--)
        {
            max+=nums[kDouble];
        }
        
        average=max;
        max/=k;

        for(int i=k; i<nums.size();i++)
        {
            average+=nums[i];
            average-=nums[i-k];

            if(max<(average/k))
                max=average/k;
        }

        return max;
    }
};
