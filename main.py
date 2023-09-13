import pymysql.cursors
import pandas as pd
import warnings
import os

import env
import universal

warnings.filterwarnings("ignore")

def check_db() -> None:
    conn = pymysql.connect(host='localhost',
                             user=env.USER,
                             password=env.PASSWORD,
                             database=env.DATABASE,
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    print("База данных подключена")

    try:
        cursor.execute("SELECT * FROM operations")
    except BaseException as e:
        print(e)
        with open('create_structure.sql', 'r') as sql_file:
            sql_script = sql_file.read()
            cursor.execute(sql_script)
            conn.commit()
            print("Скрипт SQL успешно выполнен")

def save_result(operation, result):
    conn = pymysql.connect(host='localhost',
                             user=env.USER,
                             password=env.PASSWORD,
                             database=env.DATABASE,
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO operations(operat, result) VALUES (%s, %s)", (operation, str(result)))
    conn.commit()

def save_db_to_xlxs():
    conn = pymysql.connect(host='localhost',
                            user=env.USER,
                            password=env.PASSWORD,
                            database=env.DATABASE,
                            cursorclass=pymysql.cursors.DictCursor)
    new_df = pd.read_sql("SELECT * FROM operations", conn)
    new_df.to_excel("out.xlsx")

def print_db():
    conn = pymysql.connect(host='localhost',
                            user=env.USER,
                            password=env.PASSWORD,
                            database=env.DATABASE,
                            cursorclass=pymysql.cursors.DictCursor)
    new_df = pd.read_sql("SELECT * FROM operations", conn)
    print(new_df)

def print_exel():
    name = input('Путь до файла и название: ')
    new_df = pd.read_excel(name)
    print(new_df)


def op_plus():
    number_a = float(input('a: '))
    number_b = float(input('b: '))
    print('a + b =', number_a + number_b)
    save_result('a + b', number_a + number_b)

def op_minus():
    number_a = float(input('a: '))
    number_b = float(input('b: '))
    print('a - b =', number_a - number_b)
    save_result('a - b', number_a - number_b)

def op_ymn():
    number_a = float(input('a: '))
    number_b = float(input('b: '))
    print('a * b =', number_a * number_b)
    save_result('a * b', number_a * number_b)

def op_del():
    number_a = float(input('a: '))
    number_b = float(input('b: '))
    if number_b != 0:
        print('a / b =', number_a / number_b)
        save_result('a / b', number_a / number_b)

def op_step():
    number_a = float(input('a: '))
    number_b = float(input('b: '))
    print('a ** b =', number_a ** number_b)
    save_result('a ** b', number_a ** number_b)

def op_abs():
    number_a = float(input('a: '))
    print('abs(a) =', abs(number_a))
    save_result('abs(a)', abs(number_a))

def main():
    run = True
    commands = """==========================================================================
1. Создать таблицу в MySQL.
2. Ввести числа с клавиатуры и суммировать их, результат сохранить в MySQL.
3. Ввести числа с клавиатуры и вычесть одно число из другого, результат сохранить в MySQL.
4. Ввести числа с клавиатуры и умножить их, результат сохранить в MySQL.
5. Ввести числа с клавиатуры и найти частное, результат сохранить в MySQL.
6. Ввести число с клавиатуры и возвести его в степень, результат сохранить в MySQL.
7. Ввести число с клавиатуры и найти его абсолютное значение (модуль), результат сохранить в MySQL.
8. Все результаты вывести на экран из MySQL.
9. Все результаты сохранить в Excel.
10. Все результаты вывести на экран (в консоль) через Excel.
11. Завершить"""
    while run:
        run = universal.uni(commands, 
                      check_db, op_plus, op_minus,
                      op_ymn, op_del, op_step, op_abs,
                      print_db, save_db_to_xlxs, print_exel)

if __name__ == '__main__':
    main()



