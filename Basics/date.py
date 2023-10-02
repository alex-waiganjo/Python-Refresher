import datetime,date


current_time = datetime.datetime.now()

print(current_time.year)
print(current_time.day)
print(current_time.month)
print(current_time.strftime("%A")) #Saturday
print(current_time.strftime("%a")) #Sat
print(current_time.time())


# Creating my Date Objects
my_date =  datetime.datetime(2015,3,2)
print(my_date)
