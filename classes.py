class myFirstClass:
    def __init__(self,myName,myAge) :
        self.myName=myName
        self.myAge=myAge
        self.current =0
    def print_info(abc):
        print('my age :{0} my name {1}'.format(abc.myAge,abc.myName))

name,age=input('enter your name and age :').split()
x= myFirstClass(name,age)
x.print_info()
        