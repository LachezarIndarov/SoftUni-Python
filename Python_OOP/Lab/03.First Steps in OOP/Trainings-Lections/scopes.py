"""
scopes:
- Global scope (module)
- Function scope
- Class scope (from function scope)

"""
text = "Hello from global"

def print_greeting():
    print(text) # Hello from global


print_greeting()

#--------------------------------------

text = "Hello from global"

def print_greeting():
    text = "Hello from func scope"
    print(text) # Hello from func scope


print_greeting()
print(text) # Hello from global

#----------------------------------------
text = "Lachezar"

def f1():
    text = 'Hello from f1'

    def fi_inner():
        text = "Hello from f_inner"

        def f1_innermost():
            text = 'Hello from f1_innermost'
            print(text) # Hello from f1_innermost

        print(text) # Hello from  f_inner
        f1_innermost()

    print(text) # Hello from f1
    fi_inner()


f1()
print(text) # Lachezar

#---------------------------------------------------
text = "Lachezar"
text2 = "Radoslav"

def f1():
    text = 'Hello from f1'

    def fi_inner():
        text = "Hello from f_inner"

        def f1_innermost():
            text = 'Hello from f1_innermost'
            print(text) # Hello from f1_innermost
            print(text2) # Radoslav

        print(text) # Hello from  f_inner
        f1_innermost()

    print(text) # Hello from f1
    fi_inner()


f1()
print(text) # Lachezar