class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string answer="";
        int j=0;
        
        for(int i=0;i<s.length();i++)
        {
            if(j<spaces.size()&&i==spaces[j])
            {
                answer+=" ";
                answer+=s[i];
                j++;
            }
            else
                answer+=s[i];
        }
        return answer;
    }
};
