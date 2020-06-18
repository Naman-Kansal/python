from functools import cmp_to_key


def compare(a, b):
    a = str(a)
    b = str(b)
    return 1 if int(a+b) >= int(b+a) else -1


class Solution:
    def largestNumber(self, A):
        key = cmp_to_key(lambda a, b: compare(a, b))
        A = sorted(A, key=key, reverse=True)
        return(''.join(str(i) for i in A))


obj = Solution()
print(obj.largestNumber([54, 546, 548, 60]))
