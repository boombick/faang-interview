# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = ""
        length = len(strs)
        if length == 1:
            return strs[0] # just one element in list
        sample = strs.pop()
        len_sample = len(sample)
        for l_index in range(len(sample)): # each letter in sample: sample[l_index]
            for w_index in range(len(strs)): # we will compare with sample each letter
                if l_index + 1 > len(strs[w_index]) or len(strs[w_index]) == 0:
                    return common_prefix # word is too short, return what we have for now
                if sample[l_index] != strs[w_index][l_index]:
                    return common_prefix # letters are not the same
            common_prefix = common_prefix + sample[l_index]

        return common_prefix
