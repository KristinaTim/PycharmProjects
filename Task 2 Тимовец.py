# 2. Напишите функцию, которая возвращает True, если введенный текст читается одинаково
# слева-направо и справа-налево. Иначе – False.

def Slovo(s):
    return s[::-1]
def k(s):
    rev = Slovo(s)
    if (s == rev):
        return True
    return False
s = input("Введите слово: ")
ans = k(s)
print(ans)
