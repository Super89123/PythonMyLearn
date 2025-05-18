




def is_valid_triangle(side1, side2, side3):
    if side1< side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        return True
    else: return False
def is_prime(num):
    isPr = False
    for i in range(2, num):
        if num % i == 0:
            isPr = True
            break
    if num == 2:
        return True
    if num == 1:
        return False
    return isPr
def get_next_prime(num):
        x = num
        while not is_prime(x):
            x +=1
        return x
def is_one_away(word1, word2):
    if len(word2) == len(word1):
        errors = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                errors+=1
        if errors > 1:
            return False
        else:
            return True
def is_palindrome(text):
    x = text.lower()

    chars = ",.!?-"

    for char in chars:
        x = x.replace(char, "")
    if x == x[::-1]:
        return True
    else: return False

def can_fit(x1, y1, x2, y2):
    if x1 < x2 and y1 < y2:
        return True
    else:
        return False

print(is_valid_triangle(10, 10 ,5))
print(is_prime(1))
print(get_next_prime(123))
print(is_one_away("hi", "fu"))
print(is_palindrome("jofJ"))
