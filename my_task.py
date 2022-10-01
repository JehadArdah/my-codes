from operator import mod


mode =int(input('input number of task you want to exceute (1 for year leap calculator,2 for length class) ..:'))
if mode==1:
    print('this is task 1')
    my_year =int(input('input year to calculate leap year ..:'))
    f_flag = False ##common year is false , leap year is true
    if my_year%4!=0:
        f_flag=False
    elif my_year%100!=0:
        f_flag=True
    elif my_year%400!=0:
        f_flag=False
    else:
        f_flag=True

    if f_flag:
        print('{0} is Leap year and it has 366 days'.format(my_year))
    else:
        print('{0} is Common year and it has 365 days'.format(my_year))
elif mode==2:
    print('this is task 2')
    my_length =int(input('input your length ..:'))
    result = 0 ## 1 is tall , 2 is normal , 3 is short,0 is not assigned yet
    if my_length>= 170:
       result=1
    elif my_length<170 and my_length >160:
         result=2
    elif my_length<150:
        result=3

    if result ==0 :
        print('not calculated properly ..!')
    elif result==1:
        print('you are tall !')
    elif result==2:
        print('you are not tall and not short !')
    elif result==3:
        print('you are short !')   
else:
    print('wrong number !')