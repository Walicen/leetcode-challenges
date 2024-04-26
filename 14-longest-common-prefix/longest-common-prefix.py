class Solution(object):
    def longest_common_prefix(self, strs):
        if len(strs) == 0: return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix


if __name__ == "__main__":
    s = Solution()
    print(s.longest_common_prefix(["flower","flow","flight"])) 
    print(s.longest_common_prefix(["dog","racecar","car"])) 