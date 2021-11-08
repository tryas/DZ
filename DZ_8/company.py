class Company:
    def __init__(self, name):
        self.name = name


class Department1(Company):
    def __init__(self, name, depart_name):
        super(Department1, self).__init__(name)
        self.items = dict()
        self.name = name
        self.depart_name = depart_name

    def add_items(self, item):
        try:
            self.items[item.to_str()] = self.items[item.to_str()] + 1
        except KeyError:
            self.items[item.to_str()] = 1

    def get_items(self, item):
        try:
            self.items[item.to_str()] = self.items[item.to_str()] - 1
            if self.items[item.to_str()] == 0:
                self.items.pop(item.to_str())
        except KeyError:
            print('Этой техники нет')

    def from_depart_to_store(self, store, item):
        self.get_items(item)
        try:
            store.items[item.to_str()] = store.items[item.to_str()] + 1
        except KeyError:
            store.items[item.to_str()] = 1
