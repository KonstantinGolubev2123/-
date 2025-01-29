# Исходные данные
disk_capacity_mb = 1.44  # Информационный объем дискеты в Мб
pages_per_book = 100     # Количество страниц в книге
lines_per_page = 50      # Число строк на странице
chars_per_line = 25      # Количество символов в строке
bytes_per_char = 4       # Байтов для хранения одного символа

# Шаг 1: Преобразуем информационный объем дискеты из Мб в байты
disk_capacity_bytes = int(disk_capacity_mb * 1024 * 1024)  # 1 Мб = 1024 Кб = 1024 * 1024 байт

# Шаг 2: Рассчитываем информационный объем одной книги в байтах
book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

# Шаг 3: Рассчитываем количество книг, которые можно поместить на дискете
number_of_books = disk_capacity_bytes // book_size_bytes

# Выводим результат
print(f"Количество книг, помещающихся на дискету: {number_of_books}")
