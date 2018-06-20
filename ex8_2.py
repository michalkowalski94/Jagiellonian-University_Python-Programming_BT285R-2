#Using strftime, create an object with day, month and year of your birthday

import datetime
birthday = datetime.datetime.strptime('1994/09/02',  "%Y/%m/%d")
pars = birthday.strftime('%A %d/ %B %m/ %Y')
print pars
