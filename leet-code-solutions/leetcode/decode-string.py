class Solution:
    def decodeString(self, s: str) -> str:

        def recurse(index):
            num=0
            mult=1
            word = []

            while s[index].isdigit():
                num= num * mult + int(s[index])
                index+=1
                mult=10
                # print(num)
            index+=1

            while s[index] != ']':
                if s[index].isdigit():
                    w,index=recurse(index)
                    word.append(w)
                else:
                    word.append(s[index])
                    index+=1

            return num*"".join(word),index+1
            
        i=0
        answer=[]
        
        while i < len(s):
            
            if not s[i].isdigit():
                answer.append(s[i])
                i+=1

            else:
                inner = recurse(i)
                answer.append(inner[0])
                i=inner[1]

        return "".join(answer)


            #     if s[i].isdigit():
            #         num = 0
            #         mult = 1
            #         while s[i].isdigit():
            #             num = mult*num + int(s[i])
            #             mult *= 10
            #             i += 1
            #         print(num)
            #         j=i+1
            #         temp=[]
            #         opens=0
            #         start=i+1
            #         while s[j] != ']' or  opens > 0:
            #             if s[j] == '[':
            #                 opens+=1
            #             if s[j] == ']':
            #                 opens-=1
            #             temp.append(s[j])
            #             j+=1
            