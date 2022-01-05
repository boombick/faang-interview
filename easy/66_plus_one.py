# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = 0
        len_d = len(digits)
        for i in range(len_d):
            multiplier = pow(10, len_d - 1)
            position = digits[i] * multiplier
            result = result + position
            len_d = len_d - 1
        result = result + 1
        return list(map(int, str(result)))

