def FUN_000670c4(param_1, param_2):
    if param_2 == 0:
        raise ArithmeticError("Division by zero")
    return FUN_0006701c(param_1, param_2)

def lzcount(x):
    return 0 if x == 0 else (32 - len(bin(x)[2:]))

def FUN_0006701c(param_1, param_2):
    if param_2 == 0:
        raise ArithmeticError("Division by zero")
    
    # Случай деления на 1
    if param_2 == 1:
        return (param_1, 0)
    
    # Случай когда делимое меньше делителя
    if param_1 < param_2:
        return (0, param_1)
    
    # Оптимизация для степеней двойки
    if (param_2 & (param_2 - 1)) == 0:
        shift = 32 - lzcount(param_2) - 1
        quotient = param_1 >> shift
        return (quotient, param_1 - (quotient * param_2))
    
    # Общий алгоритм деления с использованием битовых операций
    a = param_1
    b = param_2
    lz_b = lzcount(b)
    lz_a = lzcount(a)
    
    shift = lz_b - lz_a
    b_shifted = b << shift
    quotient = 0
    current_bit = 1 << shift
    
    while b_shifted >= b and a >= b:
        if a >= b_shifted:
            a -= b_shifted
            quotient |= current_bit
        
        b_shifted >>= 1
        current_bit >>= 1
        
        if b_shifted == 0:
            break
    
    return (quotient, a)

# Модифицированная функция генерации кода
def generate_unlock_code(imei):
    lookup_table = [6, 4, 1, 5, 3, 8, 2, 9, 7, 0]
    
    if len(imei) != 15 or not imei.isdigit():
        return None
    
    local_50 = [lookup_table[int(c)] for c in imei]
    
    unlock_code = []
    for xnum in range(8):
        total = sum(local_50[xnum:xnum+8])
        try:
            _, remainder = FUN_0006701c(total, 10)
        except:
            remainder = total % 10
        unlock_code.append(str(remainder))
    
    return ''.join(unlock_code)

print(f"Код разблокировки: {generate_unlock_code(input("Введите IMEI: "))}")
