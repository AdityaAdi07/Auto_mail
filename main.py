import smtplib
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
to_mail=''
body='' #always intiaalize smtng that u want outside for, if and fxn.
for key in birthday_dict:
    if key == today_tup:
        person= list(birthday_dict[key])
        name= person[0]
        to_mail= person[1]
        year =person[2]
        age= yr-year


with open ('qut.txt', 'r') as file:
    wish=file.readlines()
    for ech in wish:
        wish1= ech.strip()
        modified_line = wish1.replace('[NAME]', f'{name}') \
            .replace('[yearth]', f'{age}') \
            .replace('[day]', f'{booring_day}')  # remember this how to multiple replace
        body+=modified_line+'\n' #here modified line is modifying each line from wish1 strip now to get a string of each line with proper


my_email = "sushmaaditya717@gmail.com"
passw = "adkyjtsjguuzqlmn"
Msg= body
recive= to_mail
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls() #for security and encryption
    connection.login(user=my_email, password=passw)
    connection.sendmail(from_addr='sushmaaditya717@gmail.com',
                        to_addrs=to_mail,
                        msg=f'subject: Happy Bday \n\n {body}'
                        )
