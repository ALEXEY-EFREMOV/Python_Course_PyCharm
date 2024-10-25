# TODO Найдите количество книг, которое можно разместить на дискете
Mb_in_Kb = 1024
max_memory_in_bites = 1.44 * Mb_in_Kb ** 2
count_pages = 100
count_str = 50
count_symbols = 25
symbol_bytes = 4
result = round(max_memory_in_bites / (count_pages * count_str * count_symbols * symbol_bytes))
print("Количество книг, помещающихся на дискету:", result)