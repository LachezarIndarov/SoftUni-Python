prints_count = 0 # Global scope


def print_list(ll):
    # global makes `prints_count`
    # like an object of a reference type
    global prints_count # Take value from Global scope

    prints_count += 1
    print(ll)


ll = list(range(5))

print(prints_count)
print_list(ll)
print(prints_count)
print_list(ll)
print(prints_count)
print_list(ll)
print(prints_count)
print_list(ll)
print(prints_count)
print_list(ll)
print(prints_count)
