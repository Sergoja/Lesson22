# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def read_users_list(csv):
    return [file.split(';') for file in csv.split('\n')]


def sort_user_list():
    data = read_users_list(csv)
    return sorted(data, key=lambda x: int(x[1]))


def filter_user_list():
    data = sort_user_list()
    return [element for element in data if int(element[1]) > 10]


def get_users_list():
    return filter_user_list()


if __name__ == '__main__':
    print(get_users_list())
