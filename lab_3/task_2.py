# TODO Напишите функцию find_common_participants
def find_common_participants(participants_list_1, participants_list_2, sep=","):
    common_participants = set(participants_list_1.split(sep)).intersection(participants_list_2.split(sep))
    common_participants = list(common_participants)
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))