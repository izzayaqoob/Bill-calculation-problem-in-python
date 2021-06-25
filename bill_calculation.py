rate_1=21.8
rate_2=25.8
rate_3=27.8

units=input('Enter number of units: ')
if int(units)>0 and int(units)<=200:
    print('Bill: ',rate_1*int(units))

if int(units)>200 and int(units)<=800:
    extra=int(units)-200
    print('Bill: ',rate_1*200+rate_2*extra)
if int(units)>800:
    extra=int(units)-800
    print('Bill: ',rate_1*200+rate_2*600+rate_3*extra)