class Solution {
public:
struct parentesis
{
    int top=-1;
    vector<int> x;

    void push(char c){
        cout<<"pushing:"<<c<<endl;
        x.push_back(c);
        top++;
    }
    char pop(){
        cout<<"popping:";
        if (top==-1)
           return '1';
        else{
            char r=x[top--];
            cout<<r<<endl;
            x.pop_back();
            return r;
        }
    }
};
    bool isValid(string s) {
        int pushPop=0;
        parentesis x;
        if (s.length()%2!=0)
            return false;
        else
        {
            for (int i = 0; i < s.length(); i++)
            {
                if (s[i]=='{'||s[i]=='('||s[i]=='[')
                {
                    x.push(s[i]);
                    pushPop++;
                }else{
                    char m=x.pop();
                    pushPop--;
                    if (m=='1')
                        return false;
                    else
                    {
                        if (m=='{')
                        {
                            if(s[i]!='}')
                                return false;
                        }
                        else if (m=='[')
                        {
                            if(s[i]!=']')
                                return false;
                        }
                        else if (m=='(')
                        {
                            if(s[i]!=')')
                                return false;
                        }
                    }
                }
            }
           if (pushPop>=2)
                return false;
            else
                return true;     
        }
}
};
