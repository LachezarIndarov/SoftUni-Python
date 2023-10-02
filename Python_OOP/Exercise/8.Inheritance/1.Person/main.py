from project.child  import Child

child = Child("Peter", 25)
print(child.name)
print(child.age)
print(child.__class__.__bases__[0].__name__)

print
"""
output:

Peter
25
Person


"""
