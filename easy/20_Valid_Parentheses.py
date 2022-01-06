# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' and stack and stack[-1] != "(":
                return False
            elif i == ']' and stack and stack[-1] != "[":
                return False
            elif i == '}' and stack and stack[-1] != "{":
                return False
            elif stack: 
                stack.pop(-1)
            else: 
                return False

        return (0 == len(stack))
