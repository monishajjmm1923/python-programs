import datetime
x = datetime.datetime.now()    #display the current date
print(x)

print(x.year)                  #display year
print(x.strftime("%A"))        #display day
print(x.strftime("%B"))        #display month
print(x.strftime("%a"))        #Weekday, short version
print(x.strftime("%b"))        #Month name, short version
print(x.strftime("%p"))        #AM/PM
print(x.strftime("%f"))        #Microsecond 000000-999999
print(x.strftime("%x"))        #Local version of date
print(x.strftime("%X"))        #Local version of time
print(x.strftime("%y"))	       #Year, short version, without century