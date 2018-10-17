class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        #给定一个字符串 S，返回 “反转后的” 字符串，
        #其中不是字母的字符都保留在原地，而所有字母的位置发生反转
        res = ''
        for i in range(len(S)):
            if S[i].isalpha:
                res += S[-i-1]
            else:
                res += S[i]
        return res
            
            
