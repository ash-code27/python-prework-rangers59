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