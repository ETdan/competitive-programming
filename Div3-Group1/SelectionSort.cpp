class Solution
{
    public:
    int select(int arr[], int i)
    {
        // code here such that selectionSort() sorts arr[]
    }
     
    void selectionSort(int arr[], int n)
    {
       //code here
       for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n-1; j++)
            {
                if (arr[j]>arr[j+1])
                    swap(arr[j],arr[j+1]);
            }    
        }
    }
};
