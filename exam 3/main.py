# create a python application which has a func calculate total that accepts  the prices of multiply items and
# return total cost then define a function apply discount .that apply 10%discount
# if the total exceeds greater than 1500
# finally create a function final bill that accepts keyword agruments such as amount ,tax , and packing charges etc and returns the final bill
# display the final amount using the single  nested function call
# q1
_username='baby'
_password='1234'
successful_attempts=0
unsuccessful_attempts_u=0
unsuccessful_attempts_p=0
def decorator(func):
    def wrapper(*args, **kwargs):
        print('welcome to this application')
        func(*args, **kwargs)
    return wrapper
@decorator
def login(username,password):
    global successful_attempts,unsuccessful_attempts_u,unsuccessful_attempts_p
    if _username==username and _password==_password:
        print('login success')
        successful_attempts+= 1

    elif _password!=_password:
        unsuccessful_attempts_p+= 1
        if unsuccessful_attempts_p<=3:
            print('it is a wrong password')
        else:
            print('login failed')
    else:
        unsuccessful_attempts_u+= 1
        if unsuccessful_attempts_u<=3:
            print('it is a wrong username')
        else:
            print('login failed')


login('baby','1234')
login('baby','1264')
print('success attempts:',successful_attempts)
print('unsucess user:',unsuccessful_attempts_u)
print('unsuccess password:',unsuccessful_attempts_p)

#q2


def calculate_total(*prices):
    total=0
    for price in prices:
        total+=price
    print(total)
calculate_total(23,99,100)
def apply_discount(price):
    if price>1500:
        price=price*1.1
        print(price)

def final_bill(**kwargs):
    for key, value in kwargs.items():
        apply_discount(value)
    return
print(final_bill(amount=900,tax=60,packing_charges=100))







