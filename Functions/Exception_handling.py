def func(x):
    try:
        return 100 / x
    except:
        return "there is a zero division error"


answer = func(0)
print(answer)
answer2 = func(10)
print(answer2)
answer3 = func(6)
print(answer3)
