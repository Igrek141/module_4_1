import fake_math as v1
import true_math as v2
def fake_divide(first, second):
    y = v1.divide1(first, second)
    return y
def true_divide(first, second):
    x = v2.divide2(first, second)
    return x
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)