import deal


@deal.has("__len__")
def my_function(my_list):
    return len(my_list)




@deal.hasattr("name")
class Person:
    def __init__(self, name):
        self.name = name





@deal.module("os")
def delete_file(file_path):
    os.remove(file_path)
