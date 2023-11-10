def int_to_roman(num):
    symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    values = [1000, 500, 100, 50, 10, 5, 1]

    result = ""
    for i, value in enumerate(values):
        while num >= value:
            result += symbols[i]
            num -= value
    result = result.replace('DCCCC', 'CM').replace('CCCC', 'CD')
    result = result.replace('LXXXX', 'XC').replace('XXXX', 'XL')
    result = result.replace('VIIII', 'IX').replace('IIII', 'IV')
    return result

num = 149
result = int_to_roman(num)
print(result)
