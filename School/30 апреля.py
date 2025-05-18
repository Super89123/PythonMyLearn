def get_circle_info(r):
    return 2 * 3.1415 * r, 3.14 * r ** 2
def swap(a,b):
    return b,a
def first_last(sequence):
    return sequence[0], sequence[len(sequence)-1]
def min_max(numbers):
    return min(numbers), max(numbers)
def analyze_text(text):
    chisla = 0
    bykvi = 0
    for elem in text:
        if elem.isdigit():
            chisla+=1
        if elem.isalpha():
            bykvi+=1

    anot = len(text)-chisla-bykvi
    return bykvi,chisla,anot
def split_list(nums):
    chet = []
    nechet = []
    for elem in nums:
        if elem % 2 == 0:
            chet.append(elem)
        else:
            nechet.append(elem)
    return chet, nechet
def time_to_seconds(h, m, s):
    itog  = s + (m*60) + (h * 3600)
    return itog
def seconds_to_time(seconds):
    h = 0
    m = 0
    s = 0
    while seconds > 3600:
        seconds -= 3600
        h+=1
    while seconds > 60:
        seconds -= 60
        m+=1
    s = seconds
    itog = f"{h}:{m}:{s}"
    return itog
print(seconds_to_time(3661))
