initial_valor = []
transaction = []
normalized_transaction = []
total_sum = 0
numbers_list = []





while True:
    accounting = input("Enter today's accounting values: ")

    if accounting == "finish":
        break
    else:
        accounting = int(accounting)
        initial_valor.append(accounting)

for i in range(len(initial_valor)):

    if initial_valor[i] == 0:
        continue
    elif initial_valor[i] > 0:
        x = initial_valor [i]
        y = "Income"
    else:
        x = initial_valor [i]
        y = "Expenses"
    
    transaction.append([x,y])

for i in transaction:
    valor_transaction = i[0]
    type_transaction = i[1]

    if valor_transaction > 0:
        valor = valor_transaction * 2
    else:
        valor = valor_transaction * (-2)
    
    normalized_transaction.append([valor_transaction,type_transaction,valor])
    numbers_list.append (valor_transaction)

for i in numbers_list:
    total_sum += i

average = total_sum / len(numbers_list)
max_numbers = numbers_list[0]
min_numbers = numbers_list[0]


for i in numbers_list:

    if i > max_numbers:
        max_numbers = i

print(max_numbers)














    
        

    
        