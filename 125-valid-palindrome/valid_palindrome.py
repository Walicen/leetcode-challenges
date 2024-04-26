class Solution(object):
    def is_palindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.is_palindrome("arara"))