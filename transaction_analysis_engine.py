# main lists
initial_valor = []  # stores original input values
transaction = []  # stores [value, type]
normalized_transaction = []  # stores [value, type, processed_value]

# analysis variables
total_sum = 0
average = 0

sum_pairs = []
inc_expen_pairs = []
diference_ten = []
repeat_income = []
repeat_expenses = []


# input until "finish"
while True:
    accounting = input("Enter today's accounting values: ")

    if accounting == "finish":
        break
    else:
        accounting = int(accounting)  # convert to number
        initial_valor.append(accounting)  # store original value


# classify transactions
for i in range(len(initial_valor)):

    if initial_valor[i] == 0:
        continue  # ignore invalid values
    elif initial_valor[i] > 0:
        x = initial_valor[i]
        y = "Income"
    else:
        x = initial_valor[i]
        y = "Expenses"
    
    transaction.append([x, y])  # store structure


# normalization
for i in transaction:
    valor_transaction = i[0]  # original value
    type_transaction = i[1]  # type

    if valor_transaction > 0:
        valor = valor_transaction * 2
    else:
        valor = valor_transaction * (-2)  # make positive
    
    normalized_transaction.append([valor_transaction, type_transaction, valor])


# initialize max and min
max_num = normalized_transaction[0][2]
min_num = normalized_transaction[0][2]

total_income = 0
total_expenses = 0
count_income = 0
count_expenses = 0
length = 0


# data analysis
for i in normalized_transaction:

    normalized_valor = i[2]  # processed value
    behavior = i[1]  # type

    total_sum += normalized_valor
    length += 1

    # max
    if max_num < normalized_valor:
        max_num = normalized_valor
    
    # min
    if min_num > normalized_valor:
        min_num = normalized_valor

    # behavior analysis
    if behavior == "Income":
        total_income += normalized_valor
        count_income += 1
    elif behavior == "Expenses":
        total_expenses += normalized_valor
        count_expenses += 1


# average
average = total_sum / length

# iterate through all unique pairs (avoid duplicates with i + 1)
for i in range(len(normalized_transaction)):
    for j in range(i + 1, len(normalized_transaction)):

        # get processed values
        normalized_valor_one = normalized_transaction[i][2]
        normalized_valor_two = normalized_transaction[j][2]

        # get transaction types (Income / Expenses)
        normalized_type_one = normalized_transaction[i][1]
        normalized_type_two = normalized_transaction[j][1]

        # pairs that sum to 50
        if normalized_valor_one + normalized_valor_two == 50:
            sum_pairs.append([normalized_valor_one, normalized_valor_two])

        # pairs with different types (Income vs Expenses)
        if normalized_type_one != normalized_type_two:
            inc_expen_pairs.append([normalized_valor_one, normalized_valor_two])

        # pairs with difference less than 10 and different types
        if abs(normalized_valor_one - normalized_valor_two) < 10:
            if normalized_type_one != normalized_type_two:
                diference_ten.append([normalized_valor_one, normalized_valor_two])

        # detect repeated values in income
        if normalized_type_one == "Income" and normalized_type_two == "Income":
            if normalized_valor_one == normalized_valor_two:
                repeat_income.append([normalized_valor_one, normalized_valor_two])

        # detect repeated values in expenses
        elif normalized_type_one == "Expenses" and normalized_type_two == "Expenses":
            if normalized_valor_one == normalized_valor_two:
                repeat_expenses.append([normalized_valor_one, normalized_valor_two])


if repeat_income > repeat_expenses:
    print("Hay mas ingresos repetidos que egresos")
else:
    print("Hay mas egresos repetidos que ingresos")


# print system results

# original input values
print(f'Initial values: {initial_valor}')

# classified transactions [value, type]
print(f'Transactions: {transaction}')

# normalized transactions [original_value, type, processed_value]
print(f'Normalized transactions: {normalized_transaction}')

# average of processed values
print(f'Average: {average}')

# maximum value
print(f'Max value: {max_num}')

# minimum value
print(f'Min value: {min_num}')

# total income
print(f'Total income: {total_income}')

# total expenses
print(f'Total expenses: {total_expenses}')

# count of income transactions
print(f'Income count: {count_income}')

# count of expense transactions
print(f'Expense count: {count_expenses}')

# pairs that sum to 50
print(f'Pairs that sum to 50: {sum_pairs}')

# pairs with different types
print(f'Income-Expense pairs: {inc_expen_pairs}')

# pairs with difference < 10
print(f'Pairs with difference < 10: {diference_ten}')

# repeated income values
print(f'Repeated income values: {repeat_income}')

# repeated expense values
print(f'Repeated expense values: {repeat_expenses}')

        



            



    



    
        







    

    

    














    
        

    
        