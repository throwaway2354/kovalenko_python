from collections import defaultdict

accounts = defaultdict(int)

while True:
    try:
        op, *params = input().split()
    except:
        break
    if op == 'DEPOSIT':
        name, sum_ = params
        sum_ = int(sum_)
        accounts[name] += sum_
    if op == 'WITHDRAW':
        name, sum_ = params
        sum_ = int(sum_)
        accounts[name] -= sum_
    if op == 'TRANSFER':
        name1, name2, sum_ = params
        sum_ = int(sum_)
        accounts[name1] -= sum_
        accounts[name2] += sum_
    if op == 'INCOME':
        percent = int(params[0])
        for name, balance in accounts.items():
            if balance > 0:
                accounts[name] += int(balance * percent / 100)
    if op == 'BALANCE':
        name = params[0]
        if name in accounts:
            print(accounts[name])
        else:
            print('ERROR')
