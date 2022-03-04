def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels


def list_of_squares(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d


print(list_of_squares(6))
print(fact(10))
print(vowels("python"))