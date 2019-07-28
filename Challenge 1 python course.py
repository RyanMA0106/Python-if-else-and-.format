
print('Hello and welcome to Holiday central, lets check if you are eligible ')
name = input('please start off by telling us your name ')
print('welcome {}'.format(name))
age = input('now please tell us your age {} '.format(name))
if 18 < age < 31:
    print('Great news you are able to get the deal on our holiday!')
else:
    print('sorry, unfortunately you are not able to get the deal on our holiday')
    print('please check some of our other offers')
