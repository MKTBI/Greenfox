accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account in a list
# The output should be: "Igor", "203004099.2"

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

def get_name_and_balance(accounts, account_number):
    account = next((account for account in accounts if account['account_number'] == account_number), None)
    if account:
        return account['client_name'], account['balance']
    else:
        return "404 - account not found"

def transfer_amount(from_account_number, to_account_number, amount):
    from_account = next((account for account in accounts if account['account_number'] == from_account_number), None)
    to_account = next((account for account in accounts if account['account_number'] == to_account_number), None)
    if from_account and to_account:
        from_account['balance'] -= amount
        to_account['balance'] += amount
    else:
        print("404 - account not found")


print(get_name_and_balance(accounts, 11234543))  # ("Igor", 203004099.2)
transfer_amount(43546731, 23456311, 500.0)
print(accounts)  # [{'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2}, {'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204099571.23}, {'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1354100.0}]
