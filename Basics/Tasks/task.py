clients = [
    {
        "Name": 'Ian',
        "Amount": 30000,
        "House_No": 4,
        "Rent_payment": 'Paid'
    },
    {
        "Name": 'Alex',
        "Amount": 30000,
        "House_No": 2,
        "Rent_payment": 'Not paid'
    },
    {
        "Name": 'John',
        "Amount": 30000,
        "House_No": 3,
        "Rent_payment": 'Paid'
    }, {
        "Name": 'Pauline',
        "Amount": 30000,
        "House_No": 9,
        "Rent_payment": 'Paid'
    },
    {
        "Name": 'Jacky',
        "Amount": 30000,
        "House_No": 10,
        "Rent_payment": 'Paid'
    },
    {
        "Name": 'Kelly',
        "Amount": 30000,
        "House_No": 7,
        "Rent_payment": 'Not Paid'
    },
    {
        "Name": 'Susan',
        "Amount": 30000,
        "House_No": 6,
        "Rent_payment": 'Paid'
    }
]

# Looping through to identify paid and unpaid rent
for Payment in range(len(clients)):
    if clients[Payment]['Rent_payment'] == 'Paid':
        print(f'Thanks,Payment received')
    else:
        print(f'{clients[Payment]["Name"]},Remember to pay your rent')
