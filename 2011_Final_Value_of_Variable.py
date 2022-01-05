# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result = 0
        print range(len(operations))
        for exp in range(len(operations)):
            if operations[exp][1] == "+":
                result = result + 1
            else:
                result = result - 1

        return result