size = 1.44 * 1024 * 1024 # TODO Найдите количество книг, которое можно разместить на дискете
number_of_pages = 100
lines_per_page = 50
chars_per_line = 25
char_size = 4

answer = int(size // (char_size * chars_per_line * lines_per_page * number_of_pages))

print("Количество книг, помещающихся на дискету:", answer)
