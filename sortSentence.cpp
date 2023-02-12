class Solution {
public:
    string sortSentence(string s) {
        string a[10];
        string g;
        char x;
    for(int i=0;i<s.length();i++)
        {
            x=s[i];
            if(!(x>=48&&x<=57)){
                if (x!=' ')
                    g+=x;
            }
            if(s[i]>=48&&s[i]<=57){
                int y=int(s[i])-48;
                a[y]=g;
                g="";
            }
        }
        for (int i = 1; i <= 9; i++)
        {
            if (a[i]!="")
            {
                g+=a[i]+" ";
            }
            
        }
       g.erase(g.length()-1);
        return g;
        
    }
};
