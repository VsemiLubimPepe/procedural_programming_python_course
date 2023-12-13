users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
user_visit_dict = {"Общее количество": 0, "Уникальные посещения": 0}

user_visit_dict["Общее количество"] = len(users)
user_visit_dict["Уникальные посещения"] = len(set(users))

print(user_visit_dict)