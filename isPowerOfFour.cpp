class Solution {
public:
    bool isPowerOfFour(int n) {
        bool t=false;
    long long int r=4;
    if(n==1)
        t=true;
    else if (n<=0)
        t= false;
    else if (n%4!=0)
        t= false;
    else{
        cout<<"in ";
        while (r!=n&&r<n)
            r*=4;
        if (r==n)
         t= true;
        else
            t=false;
        
    }

    return t;
    }
};
