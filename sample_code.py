
def get_formatted_name(first_name, last_name):
    """Formats full name using two args.

    Args:
        first_name (str): first name
        last_name (str): last name

    Returns:
        str: full name
    """
    full_name = f"{first_name} {last_name}"
    return full_name.title()


def build_dict_person(first_name, last_name, age):
    """Using 3 arguments creates dictionary with information about name, last name and age

    Args:
        first_name (str): User first name.
        last_name (str): User last name.
        age (int): Age of user.

    Returns:
        dict: dictionary with first name, last name and age.
    """
    person = {'user_name': first_name.title(
    ), 'user_lastName': last_name.title(), 'user_age': age}
    return person


user_names = ['max', 'thomas', 'harry']
user_last_names = ['payne', 'wayne', 'potter']
user_age = [38, 45, 30]

dict_basic = dict(zip(user_names, user_last_names))
print(f"Original key, value: {dict_basic}\n")

lst_user_names = [build_dict_person(
    user_names[i], user_last_names[i], user_age[i]) for i in range(len(user_names))]
print(lst_user_names)


def greet_users(names):
    for name in names:
        msg = f'Hello, {name}.'
        print(msg)


print('\n')
username = ['Harry', 'James', 'Lily']
greet_users(username)

usernames = []
while username:
    users = username.pop()
    print(f'Printing {users} and adding to the new list.')
    usernames.append(users)


print(f'\nNew List:')


def print_names(*args):
    for x in args:
        print(x)


print_names(usernames)


def print_user_info(*args):
    """Prints dictionary informations by user.
    """
    for x in args:
        for z, y in enumerate(x, 1):
            print(f'User_{z}: {y}')


print_user_info(lst_user_names)
print('\n')


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


new_user = build_profile('Janek', 'Nowak', age=29, city='Warsaw')
print(new_user)
print('\n')
# cars
brand = 'Audi'


def make_car(*args, **info):
    info['Car_brand'] = args[0]
    info['Car model'] = args[1]
    return info


car_1 = make_car(brand, 'A8', color='Red', is_4x4=False)
car_2 = make_car('Toyota', 'Cupra', color='white', is_4x4=True)
print(car_1)
print(car_2)


def make_car_default(*args, **info):
    info['Car_brand'] = args[0]
    info['Car_model'] = 'Corsa'
    return info


car_3 = make_car_default('Opel', color='White', is_4x4=True)
print(car_3)

# adding setdefault to for_family key with value True
car_3.setdefault('for_family', True)
print(car_3)
print('-----------------')

car_info = ['color', 'is_4x4', 'car_brand', 'car_model']
car_values = ['Red', True, 'Toyota', 'Cupra']


def make_car(*args, **info):
    info['Car_brand'] = args  # as tuple
    info['Car model'] = args  # as tuple
    return info

# creates dict from two lists


def create_dict(list_1, list_2):
    dict_car = dict(zip(list_1, list_2))
    return dict_car


new_dict = create_dict(car_info, car_values)

new_lst = []
# adding new dict to the list


def func(dict):
    def add_lst():
        new_lst.append(dict)
    add_lst()


# Driver's code
car_first = func(new_dict)
car_first
print(new_lst)
