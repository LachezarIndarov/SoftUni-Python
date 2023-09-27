class X:
    def fx(self):
        print('I am X') # I am X

    def f(self):
        print('I am f() from X') # I am f() from X

class Y:
    def fy(self):
        print('I am Y') # I am Y

    def f(self):
        print('I am f() from Y')

class XY(X, Y):
    pass


xy = XY()
xy.fx()
xy.fy()
xy.f()


#---------------------------------------------------------------------------------
class X:
    def fx(self):
        print('I am X') # I am X

    def f(self):
        print('I am f() from X')

class Y:
    def fy(self):
        print('I am Y') # I am Y

    def f(self):
        print('I am f() from Y') #  I am f() from Y

class XY(Y, X): # Тук разменяме X и Y и затова изпълнява  в принта  #  I am f() from Y.Защото просто гледа реда а той започва в примера с Y в скобите
    pass


xy = XY()
xy.fx()
xy.fy()
xy.f()

#---------------------------------------------------------------------------
