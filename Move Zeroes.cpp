class Solution {
public:
    void moveZeroes(vector<int>& nums) {
    int count=0;
        int i=0;
        while(i<nums.size()){
            if(nums[i]!=0)
                nums[count++]=nums[i];
            i++;
        }
        while(count<nums.size())
            nums[count++]=0;

  
    }
};
