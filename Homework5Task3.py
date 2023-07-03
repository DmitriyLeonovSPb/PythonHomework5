names = ['Валерий', 'Артур', 'Андрей', 'Василий']
salary = [15000, 20000, 18000, 50000]
bonus = ['10.25%', '15.00%', '18.50%', '12.05%']
i = 0
j = 0
bonus_convertation = [0]*len(bonus)
while i < len(bonus):
    bonus_convertation[i] = float(bonus[i].split("%")[0])
    i = i + 1
while j < len(bonus):
    bonus_convertation[j] = bonus_convertation[j] * (salary[j])/100
    j = j + 1

def list_generator(names: list[str], bonus: list[float]) -> dict[str: float]:
    dictionary = dict(zip(names, bonus_convertation))
    return dictionary
dicto = list_generator(names, bonus_convertation)
print(dicto)