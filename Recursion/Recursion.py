# Recursion

# Print Himanshu 4 Times

#Head Recursion
def func(count = 0):
    if count == 4:
        return
    print("Himanshu")
    func(count + 1)

func()

# Tail Recursion
def func(count = 0):
    if count == 4:
        return
    func(count + 1)
    print("Himanshu")
func()
