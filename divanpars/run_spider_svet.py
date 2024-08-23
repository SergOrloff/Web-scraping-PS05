import os
import datetime
import csv
from openpyxl import Workbook

# Имя паука
spider_name = "svetnewpars"

# Генерация уникального имени файла на основе текущей даты и времени
current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
csv_filename = f"svet_output_{current_time}.csv"
xlsx_filename = f"svet_output_{current_time}.xlsx"

# Формирование команды для запуска Scrapy
# Указываем формат экспорта (csv) и кодировку (UTF-8)
command = (f"scrapy crawl {spider_name} -o {csv_filename}:csv -s FEED_EXPORT_ENCODING=utf-8")

# Выполнение команды Scrapy для запуска паука
result = os.system(command)
if result != 0:
    print("Ошибка: Команда Scrapy не была выполнена.")
print(f"Данные сохранены в {csv_filename}")

# Чтение данных из CSV и запись в XLSX
# Создание нового Excel-файла
workbook = Workbook()
sheet = workbook.active

# Открытие CSV-файла для чтения
with open(csv_filename, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    # Добавление каждой строки из CSV в Excel
    for row in reader:
        sheet.append(row)

# Сохранение данных в XLSX-файл
workbook.save(xlsx_filename)
print(f"Данные перекодированы и сохранены в  {xlsx_filename}")