class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        index_of_first_space = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                index_of_first_space = i
                break
        if index_of_first_space == -1:
            return len(s)
        return len(s) - index_of_first_space - 1

