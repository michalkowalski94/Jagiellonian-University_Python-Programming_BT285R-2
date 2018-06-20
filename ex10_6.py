#create a script that will coumpute how much time left between current date and battle of grunwalnd
#let's assume that they have started to fight at 12:00 AM

import datetime
grunwald = datetime.datetime.strptime('15.08.1410 12:00', '%d.%m.%Y %H:%M')
print 'Battle of Grunwald took place %s ago' %(datetime.datetime.now() - grunwald)
