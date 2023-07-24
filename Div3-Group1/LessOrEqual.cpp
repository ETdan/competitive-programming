#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int n=0;
    int k=0;

    cin>>n;
    cin>>k;

    vector<long int> b(n);

    for (int i = 0; i < n; i++)
        cin>>b[i];

    sort(b.begin(),b.end());

    if (k==n)
        cout<< b[k-1]<<endl;
    else
    {
        if(k==0)
        {
            if(b[0]-1>0)
                cout<<b[0]-1<<endl;
            else
                cout<<-1<<endl;
        }
        else if (b[k]==b[k-1])
            cout<< -1<<endl;
        else
            cout<< b[k-1]<<endl;
    }
  
    return 0;
}

