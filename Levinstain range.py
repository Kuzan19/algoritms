def levinstein(A: str, B: str):
    """Поиск редакционного расстояния в словах"""
    rang = [[(i + j) if i * j == 0 else 0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                rang[i][j] = rang[i - 1][j - 1]
            else:
                rang[i][j] = 1 + min(rang[i - 1][j], rang[i][j - 1], rang[i - 1][j - 1])
    return rang[len(A)][len(B)]


def equal(A, B):
    """Сравниваем два слова на идентичность"""
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True


def search_substring(s, sub):
    """Поиск первого индекса подстроки в строке"""
    for i in range(0, len(s)-len(sub)):
        if equal(s[i:i+len(sub)], sub):
            print(i)


word = 'milk'
word2 = 'milf'
string_1 = "abhcdadbcb"
string_2 = "cdad"


if __name__ == "__main__":
    search_substring(string_1, string_2)
