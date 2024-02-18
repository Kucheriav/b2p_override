class Student:
    def __init__(self, filled_params, empty_params, delimeters):
        for key in filled_params:
            setattr(self, key, filled_params[key])
        for key in empty_params:
            setattr(self, key, '')
        self.delimeters = delimeters


    def __str__(self):
        s = list()
        for key, value in vars(self).items():
            if not key.startswith('_'):  # Проверяем, что ключ не начинается с "_"
                s.append(f"{key}: {value}")
        return '\n'.join(s)

    def __repr__(self):
        return self.__str__()

    def get_all_params_dict(self):
        s = dict()
        for key, value in vars(self).items():
            if not key.startswith('_') and not key == 'delimeters':  # Проверяем, что ключ не начинается с "_"
                s[key] = value
        return s


    def get_all_params_keys(self):
        s = list()
        for key, value in vars(self).items():
            if not key.startswith('_') and not key == 'delimeters':  # Проверяем, что ключ не начинается с "_"
                s.append(key)
        return s

    def get_all_params_values(self):
        s = list()
        for key, value in vars(self).items():
            if not key.startswith('_') and not key == 'delimeters':  # Проверяем, что ключ не начинается с "_"
                s.append(value)
        return s

    def get_delimeters_list(self):
        return self.delimeters