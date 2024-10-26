# #"Zad1"
# import re
# from itertools import count
# from typing import Counter
#
#
# def zadanie1(text):
#
#     paragraph = text.strip().split('\n')
#     numParagraph  = len(paragraph)
#
#     #Zdania
#     zdania = text.strip().split('.') # ? ! .
#     zdanie = re.split( r'[.!?]+', text)
#     numZdania = len([s for s in zdania if s.strip()])
#
#     slowa = len(text.split())
#     slowanum = len(slowa)
#
#     #def stop words
#     stop_word = {'i', 'o','a','z','w','u'}
#
#     filter_words = filter(lambda slowo: slowa not in stop_word, slowa)
#     filter_wordsNumber = Counter[filter_words]
#
#
#     print(f"liczba akapitów  {paragraph}")
#     print(f"liczba zdań  {numZdania}")
#     print(f"liczba słow  {slowanum}")
#
#
#
#
#
#text = "Reprezentacja Polski w meczu z Chorwacją zaserwowała kibicom emocjonalny rollercoaster. Po kiepskim meczu z Portugalią (1:3) oczekiwania wobec ekipy Michała Probierza były bardzo duże. I początek zwiastował, że tym razem może nastąpić przełom. Polacy prowadzili 1:0, potem przegrywali 1:3, ostatecznie wyrównali na 3:3. Bój był szalony i ciężki. To, co wydarzyło się na Narodowym, oglądał także Zbigniew Boniek. Oto co miał do przekazania po meczu."

# #zad2
#
# def waliduj_macierze(A, B, operacja):
#     if operacja in ['dodaj', 'odejmij']:
#         if len(A) != len(B) or len(A[0]) != len(B[0]):
#             raise ValueError("Macierze muszą mieć te same wymiary do dodawania lub odejmowania.")
#     elif operacja == 'mnoz':
#         if len(A[0]) != len(B):
#             raise ValueError(
#                 "Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy do mnożenia.")
#     return True
#
#
# def dodaj_macierze(A, B):
#     return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
#
#
# def odejmij_macierze(A, B):
#     return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
#
#
# def mnoz_macierze(A, B):
#     wynik = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
#     for i in range(len(A)):
#         for j in range(len(B[0])):
#             for k in range(len(B)):
#                 wynik[i][j] += A[i][k] * B[k][j]
#     return wynik
#
#
# def transponuj_macierz(A):
#     return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
#
#
# def operacje_na_macierzach(operacja_str):
#     try:
#
#         operacja = eval(operacja_str)
#
#
#         A = operacja['A']
#         B = operacja.get('B')
#         typ_operacji = operacja['operacja']
#
#
#         if B is not None:
#             waliduj_macierze(A, B, typ_operacji)
#
#
#         if typ_operacji == 'dodaj':
#             wynik = dodaj_macierze(A, B)
#         elif typ_operacji == 'odejmij':
#             wynik = odejmij_macierze(A, B)
#         elif typ_operacji == 'mnoz':
#             wynik = mnoz_macierze(A, B)
#         elif typ_operacji == 'transponuj':
#             wynik = transponuj_macierz(A)
#         else:
#             raise ValueError("Nieznana operacja.")
#
#         return wynik
#     except Exception as e:
#         return str(e)
#
#
#
# operacja_str = "{'A': [[1, 2], [3, 4]], 'B': [[5, 6], [7, 8]], 'operacja': 'dodaj'}"
# print(operacje_na_macierzach(operacja_str))

# #Zad3.
# def dynamic_analysis(data):
#     # Znalezienie największej liczby (liczbowe wartości)
#     max_number = max(filter(lambda x: isinstance(x, (int, float)), data), default=None)
#
#     # Znalezienie najdłuższego napisu
#     longest_string = max(filter(lambda x: isinstance(x, str), data), key=len, default=None)
#
#     # Znalezienie krotki o największej liczbie elementów
#     largest_tuple = max(filter(lambda x: isinstance(x, tuple), data), key=len, default=None)
#
#     return max_number, longest_string, largest_tuple
#
#
#
# data = [123, "krótszy napis", "najdłuższy napis w zbiorze", (1, 2), (1, 2, 3, 4), [5, 6], {"a": 1}]
# print(dynamic_analysis(data))

# #Zad4.
# from functools import reduce
#
#
# def matrix_operation(matrices, operation):
#
#     def apply_operation(a, b):
#
#         result = []
#         for row_a, row_b in zip(a, b):
#             result_row = []
#             for elem_a, elem_b in zip(row_a, row_b):
#
#                 result_row.append(eval(operation))
#             result.append(result_row)
#         return result
#
#
#     return reduce(apply_operation, matrices)
#
#
#
# matrix_list = [
#     [[1, 2], [3, 4]],
#     [[5, 6], [7, 8]],
#     [[9, 10], [11, 12]]
# ]
#
#
# result_sum = matrix_operation(matrix_list, 'elem_a + elem_b')
# print("Suma macierzy:")
# for row in result_sum:
#     print(row)
#
#
# result_product = matrix_operation(matrix_list, 'elem_a * elem_b')
# print("\nIloczyn macierzy elementów:")
# for row in result_product:
#     print(row)

# #Zad5.
# def generate_and_run_code(template, context):
#
#
#     try:
#
#         code = template.format(**context)
#
#
#         compiled_code = compile(code, '<string>', 'exec')
#
#
#         local_scope = {}
#         exec(compiled_code, {}, local_scope)
#
#
#         if 'run' in local_scope:
#             result = eval("run()", {}, local_scope)
#             return result
#         else:
#             return "Brak funkcji 'run' do uruchomienia."
#
#     except Exception as e:
#         return f"Błąd generowania lub wykonania kodu: {e}"
#
#
#
# template = """
# def run():
#     def funkcja(x):
#         return x + {y}
#     return funkcja({x})
# """
#
# context = {
#     "y": 5,
#     "x": 10
# }
#
#
# result = generate_and_run_code(template, context)
# print("Wynik:", result)
