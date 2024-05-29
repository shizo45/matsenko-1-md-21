capital = {'Russia':'Moskow', 'Spain':'Madrid', 'Poland':'Warsaw', 'Japan':'Tokyo', 'Germany':'Berlin', 'Finland':'Helsinki'}
for key in capital:
    print(key, '-', capital[key])
country = input('enter the country name: ')
if country in capital:
    print ('capital city: ', capital[country])
list_country = list(capital.keys())
list_country.sort()
for i in list_country:
    print(i,'-', capital[i])