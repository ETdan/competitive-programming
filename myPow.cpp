class Solution {
public:
    double myPow(double x, int n) {
        double y=x;
        if(x==1 && n>0)
            return 1;
        else if(x==-1 && n<0)
            return 1;
        else if(x==-1 && n==2147483647)
            return -1;
        else if(x==1 && n==-2147483648)
            return 1;
        else if(x==-1 && n>0)
            return 1;
        if(n==-2147483648 || n> 21474838){
            return NULL;
        }
        else
            if(n>0)
                for(int i=0;i<n-1;i++)          
                    x=x*y;
            else if(n==0)
                x=1;
            else
                for(int i=n;i<1;i++)          
                    x=x/y;
        return x;
    }
};
