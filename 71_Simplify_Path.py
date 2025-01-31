class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        my_list = path.split('/')
        stack = []

        for element in my_list:
            if element == '.' or element == '':
                continue
            elif element == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(element)

        return '/' + '/'.join(stack)

