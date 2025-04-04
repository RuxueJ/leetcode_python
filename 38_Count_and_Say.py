class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        pre = "1"

        for i in range(n - 1):
            result = []
            j = 0
            while j < len(pre):
                count = 1
                num = pre[j]
                while j + 1 < len(pre) and pre[j] == pre[j + 1]:
                    count += 1
                    j += 1
                result.append(str(count))
                result.append(str(num))
                j += 1

            pre = ''.join(result)
            print(pre)

        return pre
