class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_int=000
        i=0
        got_something=False
        while i+3<=len(num):
            Int=num[i:i+3]
            if Int[0] == Int[1] == Int[2]:
                max_int=max(max_int,int(Int))
                got_something=True
            i+=1

        if got_something:
            if max_int == 0:
                max_int="000"
        else:
            max_int=""

        return str(max_int)