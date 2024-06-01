import os
from docx import Document
from functions import change_font_size, change_font, change_line_spacing

# Путь к вашему файлу .docx
file_path = # ссылка на файл типа .docx

# Открытие файла .docx
document = Document(file_path)

# Вызов функций для изменения документа
change_font_size(document)
change_font(document)
change_line_spacing(document)

# Сохранение изменений
document.save(file_path)


