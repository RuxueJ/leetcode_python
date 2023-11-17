# Hashability: Dictionary keys must be hashable, which means they need to
# have a fixed hash value. Since dictionaries are mutable (can be changed
# after creation), they are not hashable. Therefore, you cannot use a dictionary
# as a key directly in another dictionary.
#
# Workaround: If you need to use a dictionary-like object as a key, you can
# convert the dictionary to a hashable type. One common approach is to convert
# the dictionary to a tuple of its items using tuple(dictionary.items()), and
# then use this tuple as the key.

# convert the values of a dictionary to a list
from collections import defaultdict
# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#
#         my_dict = defaultdict(list)
#         result = []
#
#         for strr in strs:
#
#             # create a dictionary for each string
#             dic = {}
#             for char in strr:
#                 dic[char] = dic.get(char, 0) + 1
#
#             # add the dictionary and string pair to the dictionary
#             my_dict[tuple(dic.items())].append(strr)
#
#         # for value in my_dict.values():
#         #     result.append(value)
#         # return result
#         return list(my_dict.values())

# elements in tuples matter

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        my_dict = defaultdict(list)

        for strr in strs:

            sorted_string = ''.join(sorted(strr))

            if sorted_string not in my_dict:
                my_dict[sorted_string] = []

            my_dict[sorted_string].append(strr)
        return list(my_dict.values())

        # for value in my_dict.values():
        #     result.append(value)
        # return result
        return list(my_dict.values())







