"""
Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

"""
# Возможно я несовсем понял задачу :(
    # Уравнение само неверное т.к.: 
    # 10 в -1 = 0.1, 
    # а 10 в -10 = 1е-10, 
    # значит первое НЕ может быть "меньше либо равно" второго.

a = 10/100
b = 1/10000000000
print(a)
print(b)

c = a - b

def rounds(num, max_=2):                                        # Округление числа до заданных требований
    left, right = str(num).split('.')
    zero, nums = zero_nums = [], []
    for n in right:
        zero_nums[0 if not nums and n == '0' else 1].append(n)
        if len(nums) == max_:
            break
    return '.'.join([left, ''.join(zero) + ''.join(nums)])

print(rounds(c, 2))