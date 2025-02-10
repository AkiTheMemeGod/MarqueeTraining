class Solution(object):
    def __init__(self):
        self.i = -1

    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        if n == 1:
            return True
        if self.i < 32:
            self.i += 1
            if 2 ** self.i == n:
                return True
            else:
                return self.isPowerOfTwo(n)
        else:
            return False


c = Solution()
print(c.isPowerOfTwo(8))