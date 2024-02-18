from student_class import *


SYMBOLS_ORD_LIST_ALL = [7, 5, 6, 10, 10, 15, 10, 7, 3, 11, 0, 16, 4, 16, 6, 16, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 15, 0, 7, 0, 14, 0, 10, 0, 12, 14, 11, 10, 12, 0, 15, 12, 9, 0, 9]
SYMBOLS_ORD_SET = {0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18}


def parse_student_params(info_list: list):
    filled_params = dict()
    empty_params = dict()
    for i in range(0, 10, 2):
        filled_params[info_list[i]] = info_list[i + 1]
    empty_params[info_list[10]] = ''
    filled_params[info_list[11]] = info_list[12]
    filled_params[info_list[13]] = info_list[14]
    for i in range(15, 39):
        empty_params[info_list[i]] = ''
    for i in range(39, 41):
        a, b = info_list[i].split('$')
        filled_params[a] = b
    filled_params[info_list[41]] = info_list[42]
    empty_params[info_list[43]] = ''
    filled_params[info_list[44]] = info_list[45]
    empty_params[info_list[46]] = ''
    return filled_params, empty_params


def split_student(student: str):
    student_splitted = list()
    freaky_symbols = list()
    cur_st = ''
    for el in student:
        if el.isprintable():
            cur_st += el
        else:
            if cur_st:
                student_splitted.append(cur_st)
                cur_st = ''
            freaky_symbols.append(el)
    return student_splitted, freaky_symbols


def get_raw_info_list_from_file(filename, limit=10**5):
    file = open(filename).read()
    data = []
    i = file.find('Фамилия')
    x = 0
    info = file[:i]
    while file.find('Фамилия', i + 1, len(file)) != -1 and x < limit:
        new_i = file.find('Фамилия', i + 1, len(file))
        data.append(file[i:new_i])
        i = new_i
        x += 1
    data.append(file[i:])
    return info, data


def browse_file(filename):
    metainfo_raw, students_info = get_raw_info_list_from_file(filename)
    metainfo = {'header': metainfo_raw}
    students_list = list()
    i = 0
    empty_souls = 0
    for student in students_info:
        i += 1
        s_, delimeters = split_student(student)
        if s_[1].startswith('Имя'):
            empty_souls += 1
            continue
        filled_params, empty_params = parse_student_params(s_)
        s = Student(filled_params, empty_params, delimeters)
        students_list.append(s)
    metainfo['empty_souls'] = empty_souls
    return metainfo, students_list

def write_to_file(filename, metainfo, students_list):
    file = open(filename, 'w')
    file.write(metainfo['header'])
    for student in students_list:
        keys = student.get_all_params_keys()
        values = student.get_all_params_values()
        delimeters = student.get_delimeters_list()
        for i in range(11):
            file.write(keys[i])
            file.write(delimeters[i * 2])
            file.write(values[i])
            file.write(delimeters[i * 2 + 1])


if __name__ == '__main__':
    metainfo, students_list = browse_file('empty.b2p')
    student = students_list[0]
    keys = student.get_all_params_keys()
    values = student.get_all_params_values()
    delimeters = student.get_delimeters_list()
    print(len(keys), len(values), len(delimeters))
