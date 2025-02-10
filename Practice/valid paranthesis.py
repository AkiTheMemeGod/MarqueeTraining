class Solution():

    def isValid(self, string):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        left = ['{', '[', '(']
        maps = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        if string:
            for i in string:
                if i in left:
                    stk.insert(0, i)

                else:
                    if stk[0] == maps[i]:
                        stk.pop(0)

        print(stk)
        if stk == []:
            return True
        else:
            return False

s = Solution()
print(s.isValid("(){}{()[]}"))

