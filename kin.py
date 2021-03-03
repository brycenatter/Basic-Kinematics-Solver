import math as m


def function1(a, b, c, d):
    #First Kinematic Equation
    #a = velcoity
    #b = inital velcoity
    #c = acceleration
    #d = time
    if a == "s":
        b = float(b)
        c = float(c)
        d = float(d)
        ans = (c*d)+b
        return print('Velocity = ' + str(ans))
    if b == "s":
        a = float(a)
        c = float(c)
        d = float(d)
        ans = a-(c*d)
        return print('Velocity (Inital) = ' + str(ans))
    if c == "s":
        a = float(a)
        b = float(b)
        d = float(d)
        ans = (a-b)/d
        return print('Accelration = ' + str(ans))
    if d == "s":
        a = float(a)
        b = float(b)
        c = float(c)
        ans = (a-b)/c
        return print('Time = ' + str(ans))
    else:
        return "Failed"

def function2(a, b, d, e, f):
    #Second Kinematic Equation
    #a = velcoity
    #b = inital velcoity
    #d = time
    #e = position
    #f = inital position

    if a == "s":
        b = float(b)
        d = float(d)
        e = float(e)
        f = float(f)
        ans = (2*(e-f)/d)-b
        return print('Velocity = ' + str(ans))
    if b == "s":
        a = float(a)
        d = float(d)
        e = float(e)
        f = float(f)
        ans = (2*(e-f)/d)-a
        return print('Velocity (Inital) = ' + str(ans))
    if d == "s":
        a = float(a)
        b = float(b)
        e = float(e)
        f = float(f)
        ans = (2*(e-f))/(a+b)
        return print('Time = ' + str(ans))
    if e == "s":
        a = float(a)
        b = float(b)
        d = float(d)
        f = float(f)
        ans = (0.5*(a+b)*d)+f
        return print('Position = ' + str(ans))
    if f == "s":
        a = float(a)
        b = float(b)
        d = float(d)
        e = float(e)
        ans = (-1)*((0.5*(a+b)*d)-e)
        return print('Position (Inital)= ' + str(ans))
    else:
        return "Failed"


def function3(b, c, d, e, f):
    #Third Kinematic Equation
    #b = inital velcoity
    #c = acceleration
    #d = time
    #e = position
    #f = inital position
    if b == "s":
        c = float(c)
        d = float(d)
        e = float(e)
        f = float(f)
        ans = ((e-f)-(0.5*c*(d**2)))/d
        return print('Velocity (Inital) = ' + str(ans))
    if c == "s":
        b = float(b)
        d = float(d)
        e = float(e)
        f = float(f)
        ans = (2*((e-f)-(b*d)))/(d**2)
        return print('Accelration = ' + str(ans))
    if d == "s":
        b = float(b)
        c = float(c)
        e = float(e)
        f = float(f)
        ans = (((-1)*(b))+m.sqrt((b**2)+(2*c*(e-f))))/c
        ans2 = (((-1)*(b))-m.sqrt((b**2)+(2*c*(e-f))))/c
        return print('Time = ' + str(ans) + '\nTime 2 = ' + str(ans2))
    if e == "s":
        b = float(b)
        c = float(c)
        d = float(d)
        f = float(f)
        ans = ((b*d)+(0.5*c*(d**2)))+f
        return print('Position = ' + str(ans))
    if f == "s":
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
        ans = (-1)*(((b*d)+(0.5*c*(d**2)))-e)
        return print('Position (Inital)= ' + str(ans))

    else:
        return "Failed"
    


def function4(a, b, c, e, f):
    #Fourth Kinematic Equation
    #a = velcoity
    #b = inital velcoity
    #c = acceleration
    #e = position
    #f = inital position
    if a == "s":
        b = float(b)
        c = float(c)
        e = float(e)
        f = float(f)
        ans = m.sqrt(abs((b**2)+(2*c*(e-f))))
        ans2 = (-1)*m.sqrt(abs((b**2)+(2*c*(e-f))))
        return print('Velocity = ' + str(ans) + '\nVelocity 2 = ' + str(ans2))
    if b == "s":
        a = float(a)
        c = float(c)
        e = float(e)
        f = float(f)
        ans = m.sqrt(abs((-1)*(2*c*(e-f)-(a**2))))
        ans2 = (-1)*m.sqrt(abs((-1)*(2*c*(e-f)-(a**2))))
        return print('Velocity (Inital) = ' + str(ans) + '\nVelocity (Inital) 2 = ' + str(ans2))
    if c == "s":
        a = float(a)
        b = float(b)
        e = float(e)
        f = float(f)
        ans = ((a**2)-(b**2))/(2*((e-f)))
        return print('Accelration = ' + str(ans))
    if e == "s":
        a = float(a)
        b = float(b)
        c = float(c)
        f = float(f)
        ans = (((a**2)-(b**2))/(2*c))+f
        return print('Position = ' + str(ans))
    if f == "s":
        a = float(a)
        b = float(b)
        c = float(c)
        e = float(e)
        ans = (-1)*((((a**2)-(b**2))/(2*c))-e)
        return print('Position (Inital)= ' + str(ans))
       
    else:
        return "Failed"



def run(a, b, c, d, e, f):
    #a = velcoity
    #b = inital velcoity
    #c = acceleration
    #d = time
    #e = position
    #f = inital position
    if e == 'n' and f == 'n':
        function1(a, b, c, d)
    if c == 'n':
        function2(a, b, d, e, f)
    if a == 'n':
        function3(b, c, d, e, f)
    if d == 'n':
        function4(a, b, c, e, f)

def usrInput():
    #a = velcoity
    #b = inital velcoityn
    #c = acceleration
    #d = time
    #e = position
    #f = inital position
    print('\nEnter Data:')
    a = input('Velocity (Final) : ')
    b = input('Velocity (Inital) : ')
    c = input('Acceleration : ')
    d = input('Time : ')
    e = input('Position (Final) : ')
    f = input('Position (Inital) : ')

    print('\nAnswer: ')
    run(a, b, c, d, e, f)
    
    usrInput()

usrInput()
