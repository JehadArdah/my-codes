

grade =int(input('Enter your grade ...'))
result =''
if grade>=90 :
    result='A'
elif grade >=80 and grade<90:
    result='B'
elif grade >=70 and grade<80:
    result='C'
elif grade >=60 and grade<70:
    result='D'
else:
    result='Faile'

print('you have got a :{0}'.format(result))
   
