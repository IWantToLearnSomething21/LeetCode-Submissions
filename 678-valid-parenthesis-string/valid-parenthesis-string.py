class Solution:
    def checkValidString(self, s: str) -> bool:
        pos1 = []
        pos2 = []
        c = s.count("*")
        for i in range(len(s)):
            if s[i] == "(":
                pos1 += [i]
            elif s[i] == ")":
                if pos1:
                    last = pos1[-1]
                    pos1.pop(-1)
                    s = s[:last] + " " + s[last + 1 : i] + " " + s[i + 1 :]
                elif pos2:
                    last = pos2[-1]
                    pos2.pop(-1)
                    s = s[:last] + " " + s[last + 1 : i] + " " + s[i + 1 :]
            else:
                pos2 += [i]

        for i in range(len(pos1)):
            for j in range(len(pos2)):
                if pos1[i] < pos2[j]:
                    s = s[:pos1[i]] + " " + s[pos1[i] + 1 : pos2[j]] + " " + s[pos2[j] + 1 :]
                    pos2 = pos2[j + 1:]
                    break

        if ")" in s or "(" in s:
            return False
        return True
