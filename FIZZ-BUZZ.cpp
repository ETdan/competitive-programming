class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> x;
        for(int i=1;i<=n;i++)
        {
            if(i%3==0&&i%5==0)
                x.push_back("FizzBuzz");
            else if(i%3==0)
                x.push_back("Fizz");
            else if(i%5==0)
                x.push_back("Buzz");
            else
                x.push_back(to_string(i));
        }
        return x;
    }
};
