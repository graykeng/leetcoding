class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for char in s:
            if ord(char) >= 65 and ord(char) <= 90:
                char = chr(ord(char) + 32)
            res += char
        return res