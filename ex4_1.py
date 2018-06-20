#Transform given loop into comprehension list
#numbers = range(10)
#odds = []
#for x in numbers:
#if x % 2 == 1:
#odds.append(x)

odds = [x for x in range(10) if x%2==1]
print odds
