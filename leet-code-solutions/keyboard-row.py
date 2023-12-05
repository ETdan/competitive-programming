class Solution(object):
    def findWords(self,words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        row_number = {'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1, 'a':2,'s':2, 'd':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3}

        answer=[]

        for word in words:
            val=row_number[word[0].lower()]
            Append=True
            for letter in word:
                if  val != row_number[letter.lower()]:
                    Append=False
                    break
            if Append:
                answer.append(word)
        return answer