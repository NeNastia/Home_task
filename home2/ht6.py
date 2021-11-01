# TASK6
def get_nod(num1, num2):
    while num1 != num2: 
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1 or num2
    
result = get_nod(18, 24)
print(result)