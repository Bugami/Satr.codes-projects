def dict_search(value):
    if type(value) == str:
        return phone_dict_list[value]
    else:
        return list(phone_dict_list.keys())[list(phone_dict_list.values()).index(value)]
    
if __name__=='__main__':
    phone_dict_list = {'Amal'    : 1111111111, 'Mohammed': 2222222222,
                       'Khadijah': 3333333333, 'Abdullah': 4444444444,
                       'Rawan'   : 5555555555, 'Faisal'  : 6666666666,
                       'Layla'   : 7777777777}
    type1 = input('please choose weather to [1] add a name and phone number in dictionary or [2] search for a number\n')
    if int(type1) == 1:
        name = input('please enter the name: ')
        phone = input('please enter phone number: ')
        if not phone.isnumeric() and len(phone) != 10:
            print('This is invalid number')
        else:
            phone_dict_list[name] = int(phone)
            print("phone number added in phone dictionary")
    else:
        type2 = input('what would you like to search by [1] name or [2] phone number: ')
        if int(type2) == 2:
            value  = int(input('please enter the phone number: '))
            try:
                result = dict_search(value)
                print('The name of the phone number you are looking for is: '+result)
            except ValueError:
                print('\nThe phone number you are entered is not in the phone dictionary...please try again')
        else:
            value = input('please enter the name: ')
            try:
                result = dict_search(value)
                print('the phone number you are looking for '+value+' is: '+str(result))
            except KeyError:
                print('\nthe name you are entered is not in the phone dictionary...please try again')
