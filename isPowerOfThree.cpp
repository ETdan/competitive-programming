class Solution {
public:
    bool isPowerOfThree(int n) {
        bool t=false;
    long long int r=3;
    if(n==1)
        t=true;
    else if (n<=0)
        t= false;
    else if (n%3!=0)
        t= false;
    else{
        cout<<"in ";
        while (r!=n&&r<n)
            r*=3;
        if (r==n)
         t= true;
        else
            t=false;
        
    }

    return t;
    }
};
