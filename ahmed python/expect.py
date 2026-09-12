def main():
   x = get_int()
   print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("what is x:"))
        except ValueError:
            print("x must be a whole number")



main()