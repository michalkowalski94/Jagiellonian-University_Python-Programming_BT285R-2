# create datetime object from '21.11.2011' and diplay current time
import datetime
string = '21.11.2011'
first = datetime.datetime.strptime(string,'%d.%m.%Y')
print first
second = datetime.datetime.now().strftime('%H:%M:%S')
print second
