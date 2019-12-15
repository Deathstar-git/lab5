import argparse
import json


def create_parser():
    p = argparse.ArgumentParser()
    p.add_argument('act', type=int)  # Ввод номера нужного действия для дальнейшей работы

    return p


def show_db(transactions):  # вывод базы данных
    print('   Счет списания ', 'Счет зачисления', 'Дата', 'Время ', 'Сумма ')
    for i in range(len(transactions)):
        print(i + 1, ':', transactions[i])


def add_transaction(transactions):  # Добавление транзакции
    new_trans = []
    while True:
        read = input("Введите счет списания:")
        if len(read) != 6:
            print("Введите 6-ти значный счёт!")
            continue
        else:
            new_trans.append(read)
            break
    while True:
        read = input("Введите счёт зачисления:")
        if len(read) != 6:
            print("Введите 6-ти значный счёт!")
            continue
        else:
            new_trans.append(read)
            break
    read = input("Введите дату:")
    new_trans.append(read)
    read = input("Введите время:")
    new_trans.append(read)
    while True:
        try:
            read = int(input("Введите сумму:"))
            new_trans.append(read)
        except ValueError:
            print("Введите корректную сумму.")
        else:
            break
    transactions.append(new_trans)
    return transactions


def del_transaction(transactions):  # удаление транзакции
    nom = int(input('Введите номер транзакции, которую хотите удалить:'))
    transactions.pop(nom - 1)
    return transactions


def sort_by_amount(transactions):  # фильтрование по сумме (по убыванию)
    for i in range(len(transactions)):
        for j in range(len(transactions)):
            if transactions[j][4] < transactions[i][4]:
                transactions[j], transactions[i] = transactions[i], transactions[j]
    return transactions


def sort_by_time(transactions):
    times = []
    for i in range(len(transactions)):  # создание нового списка с часами и минутами
        time = transactions[i][3].split(':')
        times.append(time)
    for i in range(len(times) - 1):  # Сортировка пузырьком (часы)
        for j in range(len(times) - i - 1):
            if times[j][0] < times[j + 1][0]:
                times[j], times[j + 1] = times[j + 1], times[j]
    for n in range(len(times) - 1):  # Сортировка пузырьком (минуты)
        for m in range(len(times) - n - 1):
            if times[m][0] == times[m + 1][0]:  # Если часы равны,то срабатывает сортировка
                if times[m][1] < times[m + 1][1]:  # По минутам
                    times[m][1], times[m + 1][1] = times[m + 1][1], times[m][1]
                    break
    print(times)


def main(act):
    with open('C:/Users/lenovo/PycharmProjects/prog5/transactions.json', "r") as f:
        transactions = json.load(f)
    # Вызов конкретной функции в зависимости от выбранного действия
    if act == 1:
        add_transaction(transactions)
    if act == 2:
        del_transaction(transactions)
    if act == 3:
        sort_by_amount(transactions)
    if act == 4:
        sort_by_time(transactions)
    if act == 5:
        show_db(transactions)
    if act == 6:
        print("Выход из программы...")
    with open('C:/Users/lenovo/PycharmProjects/prog5/transactions.json', "w") as f:
        json.dump(transactions, f, indent=1)


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args()
    main(namespace.act)
