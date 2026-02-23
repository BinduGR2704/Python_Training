class Sum:
    def use(a, b):
        return a + b
    
class Concatinate:
    def use(str1, str2):
        return str1 + str2
    
class Merging():
    def use(l1, l2):
        return l1 + l2
    
def perform_task(tool, x, y):
    print(tool.use(x, y))

perform_task(Sum, 15, 25)
perform_task(Concatinate, "Hello", " Everyone")
perform_task(Merging, [1,2], [3,4])

