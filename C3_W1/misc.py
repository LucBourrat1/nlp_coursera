
class MyClass():
    def __init__(self, y):
        self.y = y
    def my_method(self, x):
        return x + self.y
    def __call__(self, x):
        return self.my_method(x)
    
class SubClass(MyClass):
    def my_method_bis(self, x):
        return x * self.y

def main():
    
    f = SubClass(10)
    print(f(2))
    print(f.my_method_bis(2))
    
    return

if __name__ == '__main__':
    main()
    