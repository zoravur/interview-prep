# https://leetcode.com/problems/longest-common-prefix/
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    m = min(len(s) for s in strs)
    for i in range(m):
        for j in range(1, len(strs)):
            if strs[j-1][i] != strs[j][i]:
                return strs[0][:i]
    return strs[0][:m]


# debug
print(longestCommonPrefix(["flower","flow","flight"]))

# tests
assert(longestCommonPrefix(["flower","flow","flight"]) == "fl")
assert(longestCommonPrefix(["dog","racecar","car"]) == "")
assert(longestCommonPrefix([]) == "")
assert(longestCommonPrefix(["hello"]) == "hello")
assert(longestCommonPrefix(["hello", "hell"]) == "hell")

# demo
            

