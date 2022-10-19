class EvenNumbers(object):
    def __init__(self):
        self.number=0
    def get_next_number(self):
        result=self.number 
        self.number  +=2
        return result
class OddNumbers(object):
    def __init__(self):
        self.number=1
    def get_next_number(self):
        result=self.number 
        self.number  +=2
        return result
def get_Stream(n,action=None):
     if action == None :
        action = EvenNumbers()
     for _ in range(n) :
        print(action.get_next_number())
nn ,mode=input('enter numbers then mode').split()
nn=int(nn)
if mode =='odd' :
    my_object = OddNumbers()
    get_Stream(nn,my_object)
else:
    get_Stream(nn)


    
     
    
