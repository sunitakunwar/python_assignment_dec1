def lhs(a,b):
    return (a-b)**2
def rhs(a,b):
    return a**2-2*a*b+b**2
ls=lhs(3,2)
rs=rhs(3,2)
print('LHS={},RHS={}'.format('ls','rs'))