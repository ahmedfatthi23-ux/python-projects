def main():
    n = int(input("what is n "))
    if is_even(n):
        print("n is even")
    else:
        print("n is odd")



def is_even(x):
    return x % 2 == 0

main()

def name(x):
    if x % 2 == 0:
        return True
    else:
        return False
