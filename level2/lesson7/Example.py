class Customer:
    name = "quynh";

    def __set_name__(self, name):
        self.name = name
    def __get_name__(self):
        return self.name


st = Customer()
st.__set_name__("liem")

print(st)