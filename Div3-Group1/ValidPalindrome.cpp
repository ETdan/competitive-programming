#include<cctype>
#include<vector>
class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> ar;
        int nume=0;
        
        for(int i=0;i<s.length();i++)
        {
            if(isdigit(s[i]))
                ar.push_back(tolower((char)s[i]));
            if(isalpha(s[i]))
                ar.push_back(tolower((char)s[i]));
                
        }
        int r=ar.size()-1;
        // cout<<r;
        int i=0;
        while(i<r)
        {
            if(ar[i]!=ar[r])
                return false;
                // cout<<endl<<r<<(char)ar[i];
            r--;
            i++;
        }
        return true;
    }
};
