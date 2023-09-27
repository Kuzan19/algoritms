string_1 = "лилилось лилилась"
string_2 = "лилила"


def prefix(s: str):
    """Поиск максимального префикса строки"""
    i = 1
    j = 0
    p = [0]*len(s)
    while i < len(s):
        if s[i] == s[j]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j-1]
    return p


def kmt(s1: str, s2: str):
    i = 0
    j = 0
    while i < len(s1):
        if s1[i] == s2[j]:
            i += 1
            j += 1
            if j == len(s2):
                return "YES"
        else:
            if j > 0:
                j = prefix(s2)[j-1]
            else:
                i += 1
    if i == len(s1):
        return "NO"


if __name__ == "__main__":
    print(kmt('flower', "flow"))
