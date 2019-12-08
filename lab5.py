import argparse
import json


# from datetime import datetime


def create_parser():
    p = argparse.ArgumentParser()
    p.add_argument('act', type=int)

    return p


def add_transaction(transactions, trans_numbers):
    new_trans = ('transaction#' + str(len(trans_numbers) + 1))
    print("Введите счёт списания,счет зачисления,дату," +
          "время и сумму через запятую.")
    while True:
        try:
            trans_val = list(map(str, input().split(",")))
            transactions[new_trans] = {"write-off account": str(trans_val[0]), "credit account": str(trans_val[1]),
                                       "date": str(trans_val[2]),
                                       "time": str(trans_val[3]),
                                       "amount": str(trans_val[4])}
            print(transactions)
            with open('c:/Users/lenovo/PycharmProjects/prog5/transactions.json', 'w') as write_file:
                json.dump(transactions, write_file, indent=1)
        except IndexError:
            print("Введите корректные данные.")
        else:
            break


def del_transaction(transactions, trans_numbers):
    print("Транзакции,доступные для удаления:" + str(trans_numbers) + "\nВведите номер транзакции, который желаете удалить.")
    while True:
        try:
            pop_trans = int(input())
            transactions.pop("transaction#" + str(pop_trans))
            print("Данные о транзакции успешно удалены.\nОбновлённая база данных:\n " + str(transactions))
            with open('c:/Users/lenovo/PycharmProjects/prog5/transactions.json', 'w') as write_file:
                json.dump(transactions, write_file, indent=1)
        except KeyError:
            print("Введите корректный номер транзакции.")
            continue
        except ValueError:
            print("Введите корректный номер транзакции.")
            continue
        else:
            break


def main(act):
    with open('c:/Users/lenovo/PycharmProjects/prog5/transactions.json', 'r') as read_file:
        transactions = json.load(read_file)
        read_file.close()
    trans_numbers = [i for i in transactions.keys()]
    if act == 1:
        add_transaction(transactions, trans_numbers)
    if act == 2:
        del_transaction(transactions, trans_numbers)
    # if act = 3:
    #     sort_by_amount()
    # if act == 4:
    #     sort_by_time()
    if act == 5:
        print("Выход из программы...")


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args()
    main(namespace.act)
