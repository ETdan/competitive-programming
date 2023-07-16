#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int t=0;
    int n=0;
    int a=1;
    bool status=false;
    int counter=0;

    cin>>t;
    while(t--)
    {
        cin>>n;
        vector<int> b(n);

        for (int i = 0; i < n; i++)
            cin>>b[i];


        sort(b.begin(),b.end());

        while (a<b.size())
        {
            if(abs(b[a]-b[a-1])>1)
            {
                status=true;
                break;
            }

            a++;
        }
            
        if (status)
            cout<<"NO"<<endl;
        else
            cout<<"YES"<<endl;
        status=false;
        a=1;
    }

    return 0;
}
