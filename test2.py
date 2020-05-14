import datetime
y = input("年")
m = input("月")
d = input("日")
date1 = datetime.date(year=2000,month=1,day=1)
date2 = datetime.date(year=int(y),month=int(m),day=int(d))
z = int(((date2-date1).days)/4)
r = ((date2-date1).days)%4+1
print("{} {}\n".format(z+1,r))
