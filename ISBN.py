class InValidNumberError(Exception):
    pass
class NonNumberError(Exception):
    pass
class AttemptedExitError(Exception):
    pass

def isbn(isbn_num):
    num_list = []
    count = 0
    sums = 0
    for n in isbn_num:
        if n == "e":
            raise AttemptedExitError
        elif n not in "0123456789":
            raise NonNumberError("The entered ISBN contains character(s) which are not valid numbers.")
        else:
            num_list.append(n)
            count = count + 1
    if count == 10:
        for num in num_list:
            product = int(num) * count
            sums = sums + int(product)
            count = count - 1
        if (sums % 11) == 0:
            print("%s is a valid ISBN number." % (isbn_num))
            
        else:
            print("%s is not a valid ISBN number." % (isbn_num))
            
    elif count == 13:
        for num in num_list:
            posistion = num_list.index(num) + 1
            
            if posistion % 2 == 0:
                product = int(num) * 3
            else:
                product = int(num) * 1
            sums = sums + product
        if int(sums) % 10 == 0:
            print("%s is a valid ISBN number." % (isbn_num))
        else:
            print("%s is not a valid ISBN number." % (isbn_num))

    else:
        raise InValidNumberError("%s is not a valid ISBN number. A Valid ISBN number must be either 10 or 13 digits" % (isbn_num))
        

    



        
def main():
    num = None
    while num != "E":
        try:
            num = input("Please input an ISBN to test or input 'E' to exit :")
            if num == "E":
                continue 
            isbn(num)
        except InValidNumberError as err:
            print(err)
        except NonNumberError as err:
            print(err)
        except AttemptedExitError:
            print("Thank you for using the ISBN tester.")
            return
    print("Thank you for using the ISBN tester.")




main()



