# TASK7
a = float(input("Сумма вклада: "))
years = float(input("Срок вклада, лет: "))
def deposit(a, years):
    amount = a
    year = 0
    interest = 0.1
    while  year < years:
        calculation = (a + (a * 0.1))
        amount += calculation
        year += 1
    return amount
res = deposit(a, years)
print(res)