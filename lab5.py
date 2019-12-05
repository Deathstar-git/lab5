# import argparse
import json
from datetime import datetime

# def create_parser():
#     p = argparse.ArgumentParser()
#     p.add_argument('act', type=int)
#
#     return p


def init_db(transactions):
    act = int(input("Выберите действие:"))
    j = 0

    if act == 1:
        j += 1
        reading = int(input("Укажите счёт списания:"))
        transactions['write-off account'].append(reading)
        reading = int(input("Укажите счёт зачисления:"))
        transactions['credit account'].append(reading)
        date = input('Укажите дату: ')
        date_str = str(datetime.strptime(date, '%d.%m.%Y'))
        transactions['date'] += [date_str]
        time = input("Укажите время:")
        time_str = str(datetime.strptime(time, '%H:%M:%S').time())
        transactions['time'] += [time_str]
        reading = int(input("Укажите сумму:"))
        transactions['amount'] += [reading]
        print(transactions)
        input()
        with open('transactions.json', 'w') as f:
            json.dump(transactions, f, indent=1)
        with open('transactions.json', 'r') as f:
            json_db = json.load(f)
        print(json_db)
        init_db(transactions)
    if act == 2:
        j = int(input("Укажите номер транзакции для удаления:"))
        for i in transactions.keys():
            del(transactions[i][j])
        with open('transactions.json', 'w') as f:
            json.dump(transactions, f, indent=1)
        with open('transactions.json', 'r') as f:
            json_db = json.load(f)
        print(json_db)
        init_db(transactions)

    if act == 3:
        transactions['amount'] = sorted(transactions['amount'])
        print(transactions)

    if act == 5:
        print("Завершение работы...")


def main():
    transactions = {'write-off account': [], 'credit account': [], 'date': [],
                    'time': [], 'amount': []}
    init_db(transactions)


main()
# if __name__ == "__main__":
#     parser = create_parser()
#     namespace = parser.parse_args()
#     init_db(namespace.act)
