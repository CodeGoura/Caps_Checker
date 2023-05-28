a = eval(input('please chose method 1 or 2'))
if a == 1:
    cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    smale = 'abcdefghijklmnopqrstuvwxyz'
    dig = '0123456789'
    v = input('Please Input a data to check the data :')
    if v in cap:
     print(f'{v} is a capital case')
    elif v in smale:
        print(f'{v} is a small case')
    elif v in dig:
        print(f'{v} is a digit case')
    else:
        print(f'{v} is a spacial case')
else : # second method
   x = input('Please Enter character to check')
   y = ord(x)
   if y >= 65 and y <= 90:
         print(f'{x} is capital case')
   elif y >= 97 and y <= 122:
         print(f'{x} is small case')
   elif y >= 48 and y <= 57:
        print(f'{x} is digit case')
   else:
        print(f'{x} is spacial charactor case')
   

