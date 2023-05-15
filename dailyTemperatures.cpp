class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
    vector<int> answer;
    int counter=0,end=0;
        for (int i = 0; i < temperatures.size(); i++)   
        {
            for (int j = i+1; j < temperatures.size(); j++)
            {
                if (temperatures[i]<temperatures[j])
                {
                    counter++;
                    break;
                }else{
                    counter++;
                }
                end=j;
            }
            if(end==temperatures.size()-1)
            {
                answer.push_back(0);
            }else
                answer.push_back(counter);
            
            counter=0;
            end=0;
        }
        return answer;
}
};
