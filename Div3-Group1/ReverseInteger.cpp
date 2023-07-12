class Solution {
public:
    int reverse(int x) {
        if(x >= pow(2,31)-1 || x <= -2147483648)
            return 0;
        int var=0;
        if(x<0)
            var=abs(x);
        else
            var=x;
        int answer=0;
        string holder="";
        vector<int> list(16);
        while(var!=0)
        {
            holder+=to_string(var%10);
            var/=10;
        }
        // cout<<holder;
        stringstream ss;
        ss << holder;
        ss >> answer;

        if(answer >= pow(2,31)-1 || answer <= -2147483648)
            return 0;

        if(x<0)
            return 0-answer;
        return answer;
    }
};
