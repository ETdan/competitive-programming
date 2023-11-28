class Solution {
public:
    int maxArea(vector<int>& height) {
        int max=0;
        int value=0;
        int start=0;
        int end=height.size()-1;
        while (start<end)
        {
            value=(height[start]>=height[end] ? height[end] : height[start]) * (end-start);
            
            if(value>max)
                max=value;

            if(height[start]<height[end])
                start++;
            else
                end--;
        }
        
        return max;
    }
};