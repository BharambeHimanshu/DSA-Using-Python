# Print x , n times

def func(x,n):
    if n==0:
        return
    print(x)
    func(x,n-1)
func(15,3)

# Print 1 to N Using Recursion Using Head

def func(i,n):
    if i > n:
        return
    print(i)
    func(i+1,n)
func(1,5)


# Print N to 1 Using Recursion Using Tail
def func(i,n):
    if i > n:
        return
    func(i+1,n)
    print(i)

func(1,5)

