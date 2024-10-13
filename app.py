from cal_func import do_addition, do_subtraction, do_division, do_multiplication

def main():
    print("welcome to the calculator app")
    print("""
          \nSelect the function from the given options
          1. Add
          2. subtract
          3. multiply
          4. division
          """)
    user_input= input('select the function')
    a= int(input('value of a'))
    b= int(input('value of b'))

    if user_input== '1':
        result= do_addition(a,b)
    elif user_input== '2':
        result= do_subtraction(a,b)
    elif user_input== '3':
        result= do_multiplication(a,b)
    elif user_input== '4':
        result= do_division(a,b)
    print('result', result)
if __name__ == "__main__":
    main()
