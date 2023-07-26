#include<iostream>
#include<math.h> 
using namespace std;
int main(){
    
    long double n,m,a;
    cin>>n;
    cin>>m;
    cin>>a;
    
    long long int result=ceil(n/a)*ceil(m/a);
    
    cout<<result;
    
    return 0;
}
