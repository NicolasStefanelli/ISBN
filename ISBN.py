class InValidNumberError(Exception):
    pass
class NonNumberError(Exception):
    pass
class AttemptedExitError(Exception):
    pass

def isbn(num):
    num_list = []
    count = 0
    sums = 0
    for n in num:
        if n == "e":
            raise AttemptedExitError
        if n not in "0123456789":
            raise NonNumberError("The entered ISBN contains character(s) which are not valid numbers.")
        num_list.append(n)
        count = count + 1
    if count == 10:
        for num in num_list:
            product = int(num) * count
            sums = sums + int(product)
            count = count - 1
        if (sums % 11) == 0:
            print("%s is a valid ISBN number." % (num))
            
        else:
            print("%s is not a valid ISBN number." % (num))
            
    elif count == 13:
        for num in num_list:
            pass
            # determine number's posistion (odd or even)
            # multiply by 1 or 3 respectively 
            # add to total 
            # divide by 10 and if the remainder is 0, the IBSN is valid
    else:
        raise InValidNumberError("%s is not a valid ISBN number. A Valid ISBN number must be either 10 or 13 digits" % (num))
        

    



        
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



