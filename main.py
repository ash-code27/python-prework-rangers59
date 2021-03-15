def greeting(name):
    print('Hello ' + name.title() + '!')

def greeting_2(name):
    print('Hello {} !'.format(name.title()))
    print(f'Hello again {name.title()} !')

greeting_2('Ash')

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([2,3,5,8,9])
print(max_num_in_list([2,3,5,8,9]))




def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')


# Question 4 1.b solution

def is_leap(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

is_leap_year(2019)


def welcome(marvel_character):
    print(f'Welcome to {marvel_character} Vision')

welcome('Wanda')