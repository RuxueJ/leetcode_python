class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        m_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = m_map[s[-1]]

        for i in range(len(s) - 2, -1, -1):
            if m_map[s[i]] >= m_map[s[i + 1]]:
                result += m_map[s[i]]
            else:
                result -= m_map[s[i]]

        return result