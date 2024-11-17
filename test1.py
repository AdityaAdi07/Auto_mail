import pandas
import datetime

data = pandas.read_csv('birthdays.csv')
now= datetime.datetime.now()
yr= now.year
month= now.month
date= now.day
day= now.weekday()
today_tup= (date, month)


birthday_dict={(data_row['day'], data_row['month']): data_row for (index, data_row) in data.iterrows()}
# in abv (index, data_row) where index is ech row and data_row is value in tht rwo, and data.itterows loops thrgh every
#rows. i.e what for ..... in...: does, and the key is a tuple. finally this abv method is dictionary comprehension
#For each (index, data_row) pair yielded by data.iterrows(), it creates a key-value pair in the dictionary birthday_dict.
#The key is a tuple (month, day) representing a birthday.
#The value is the entire data_row corresponding to that birthday.
boring= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
booring_day= boring[day]

name=''
age=''
for key in birthday_dict:
    if key == today_tup:
        person= list(birthday_dict[key])
        name= person[0]
        to_email= person[1]
        year =person[2]
        age= yr-year

list=[]
with open ('qut.txt', 'r') as file:
    wish=file.readlines()
    for ech in wish:
        wish1= ech.strip()
        body = wish1.replace('[NAME]', f'{name}') \
            .replace('[yearth]', f'{age}') \
            .replace('[day]', f'{booring_day}')  # remember this how to multiple replace
print(body)






