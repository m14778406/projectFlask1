import sqlite3

def getAllProducts():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM products')
    result = cursor.fetchall()

    connection.close()

    return result

def getRangeProducts(minPrice, maxPrice):
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT *
        FROM products
        WHERE price > ? AND price < ?
    ''', (minPrice, maxPrice))
    result = cursor.fetchall()

    connection.close()

    return result


def getUser(login, password):
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT *
        FROM users
        WHERE login = ? AND password = ?
    ''',(login, password))
    result = cursor.fetchone()

    connection.close()
    
    return result