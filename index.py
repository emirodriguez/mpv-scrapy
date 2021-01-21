import requests
import db_check
import crawl

chat_id = 714481749
container_class_name = 'contenedor-imagen'

results = crawl.crawling('https://www.maspocovendo.com/buscar/suran', container_class_name)

resultsPage2 = crawl.crawling('https://www.maspocovendo.com/buscar/suran?page=2', container_class_name)
results.append(resultsPage2)

resultsPage3 = crawl.crawling('https://www.maspocovendo.com/buscar/suran?page=3', container_class_name)
results.append(resultsPage3)


print(results)