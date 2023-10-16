# ///////////_1_Задача_////////////

# def is_alive(health):
#     if health <= 0:
#         return False
#     else:
#         return True
# print(is_alive(int(input('Введите число:  '))))

# ///////////_2_Задача_////////////

# def season_events(number_of_month):
#     months = ['Январь - ', 'Февраль - ', 'Март - ', 'Апрель - ', 'Май - ', 'Июнь - ', 'Июль - ', 'Август - ', 'Сентябрь - ', 'Октябрь - ', 'Ноябрь - ', 'Декабрь - ']
#     winter = 'За окном падал белый снег'
#     winter_number = [12, 1, 2]
#     spring = 'Птицы пели прекрасные песни'
#     spring_number = [3, 4, 5]
#     summer = 'Солнце светило ярче чем когда-либо'
#     summer_number = [6, 7, 8]
#     autumn = 'Урожай был невероятным'
#     autumn_number = [9, 10, 11]
#     if 1 <= number_of_month <= 12:
#         if number_of_month in spring_number:
#             return months[number_of_month - 1] + spring
#         elif number_of_month in winter_number:
#             return months[number_of_month - 1] + winter
#         elif number_of_month in summer_number:
#             return months[number_of_month - 1] + summer
#         elif number_of_month in autumn_number:
#             return months[number_of_month - 1] + autumn
# print(season_events(int(input('Введите номер месяца от 1 до 12:  '))))

# ///////////_3_Задача_////////////
# def check_pass(pswd):
#     numbers = '1234567890'
#     specialchar = '*-#'
#     lowercase = 'abcdefghijklmnopqrstuvwxyz'
#     uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     flagx = 0
#     flagy = 0
#     flagz = 0
#     flagn = 0
#     errors = []
#     errors1 = ''
#
#     if len(pswd) == 8:
#         for i in pswd:
#             for j in numbers:
#                 if i == j:
#                     flagx += 1
#                 else:
#                     flagx += 0
#             for k in lowercase:
#                 if i == k:
#                     flagz += 1
#                 else:
#                     flagz += 0
#             for y in uppercase:
#                 if i == y:
#                     flagn += 1
#                 else:
#                     flagn += 0
#             for p in specialchar:
#                 if i == p:
#                     flagy += 1
#                 else:
#                     flagy += 0
#
#     elif len(pswd) < 8:
#         return 'Вы ввели меньше 8 символов'
#     elif len(pswd) > 8:
#         return 'Вы ввели больше 8 символов'
#
#     if flagx == 0:
#         errors.append('Вы забыли числа')
#     if flagz == 0:
#         errors.append('Вы забыли прописные буквы')
#     if flagn == 0:
#         errors.append('Вы забыли заглавные буквы')
#     if flagy == 0:
#         errors.append('Вы забыли специальные знаки *-#')
#     if len(errors) != 0:
#         errors1 = "\n".join(errors)
#         return errors1
#     elif flagx + flagz + flagn + flagy == len(pswd):
#         return 'Пароль идеален'
#
#
# print(check_pass(input('Введите придуманный пароль:  ')))

# ///////////_4_Задача_////////////

# def is_divisible_by_6(number):
#
#     x_str = str(number)
#     len_str = len(x_str)
#     summ = 0
#
#     for i in range(0, len_str):
#         summ += int(x_str[i])
#
#     if number != 0 and number % 2 == 0 and summ % 3 == 0:
#         return f'Число {str(number)} делится на 6'
#     else:
#         return f'Число {str(number)} неделимо на 6'
#
# print(is_divisible_by_6(int(input('Введите число:  '))))

# ///////////_5_Задача_////////////

# def search_substr(subst, st):
#
#     st_x = st.upper()
#     subst_n = subst.upper()
#     text_repeat = subst_n.count(st_x)
#
#     if text_repeat != 0:
#         return 'Есть контакт!'
#     else:
#         return 'Мимо!'
#
# print(search_substr(input('Введите строку:  '), input('Введите элемент который надо найти:  ')))

# ///////////_16_Задача_////////////


# ///////////_7_Задача_////////////
# ///////////_8_Задача_////////////
# ///////////_9_Задача_////////////
# ///////////_10_Задача_////////////
# ///////////_11_Задача_////////////
# ///////////_12_Задача_////////////
# ///////////_13_Задача_////////////
