import os
import psycopg2
import sqlite3 as lite
import message
import crawl

def check_result_send_mess():
    chat_id = 714481749
    container_class_name = 'contenedor-imagen'

    try:
       DATABASE_URL = os.environ['DATABASE_URL']
       conn = psycopg2.connect(DATABASE_URL, sslmode='require')
       cars_db = conn.cursor()
       cars_db.execute('CREATE TABLE IF NOT EXISTS cars (id SERIAL, car TEXT NOT NULL)')
    except:
       message.send_message(chat_id, 'The database could not be accessed')
        
    results = crawl.crawling('https://www.maspocovendo.com/buscar/suran', container_class_name)

    resultsPage2 = crawl.crawling('https://www.maspocovendo.com/buscar/suran?page=2', container_class_name)
    results.append(resultsPage2)

    resultsPage3 = crawl.crawling('https://www.maspocovendo.com/buscar/suran?page=3', container_class_name)
    results.append(resultsPage3)
    
    for item in results:
        car_exists = cars_db.execute('SELECT car FROM cars WHERE car = %s', [item.text])
        
        if len(cars_db.fetchall()) != 1:
            mess_content = item.text + item['href']
            message.send_message(chat_id, mess_content)
            cars_db.execute('INSERT INTO cars (car) VALUES (%s);', [item.text])
            conn.commit()
        else:
            continue
            
    cars_db.close()