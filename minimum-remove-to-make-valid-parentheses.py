https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        opened = 0
        res = []
        for i in s:
            if i.isalpha():    # appending all alphabets to list
                res.append(i)
            elif i == '(':     # 
                opened += 1
                res.append(i)
            elif i == ')' and opened > 0: #if opened > 0 it means there are opening braces which cancel out with a closing brace, so we can add it to result
                opened -= 1
                res.append(i)
        length = len(res) - 1
        while opened > 0 and length >= 0: #Remove extra opening braces
            if res[length] == '(':
                res[length] = ''  # if a open brace is found, replacing it with "" empty
                opened -= 1       # then reducing opened braces count
            length -= 1           # But for every element, reducing lenght which to reduce the result string        
        return ''.join(res)
