# *args = tuple         **kwargs = dictionaries
def f(*args, **kwargs):
    print('-----------')
    print(args)
    print(kwargs)
    print('-----------')

f(1, 2, 3)          # (1, 2, 3)
                    # {}

f(x=1, y=2, z=3)    # ()
                    # {'x': 1, 'y': 2, 'z': 3}

f(1, 2, 3, d=4)     # (1, 2, 3)
                    # {'d': 4}

#-----------------------------------------

def f2(x, *args, **kwargs):
    print(f'x={x}, args={args}, kwargs={kwargs}')

f2(1)        # x=1, args=(), kwargs={}
f2(1,2)      # x=1, args=(2,), kwargs={}
f2(1, 2, 3)  # x=1, args=(2, 3), kwargs={}

#------------------------------------------

def f3(x, *args, **kwargs):
    print(f'x={x}, args={args}, kwargs={kwargs}')

f3(1)                # x=1, args=(), kwargs={}
f3(1, 2)             # x=1, args=(2,), kwargs={}
f3(1, 2, 3)          # x=1, args=(2, 3), kwargs={}

f3(x=11)             # x=11, args=(), kwargs={}
f3(x=11, y=12)       # x=11, args=(), kwargs={'y': 12}
f3(1,2,3,4,5, y=12)  # x=1, args=(2, 3, 4, 5), kwargs={'y': 12}

