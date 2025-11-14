# first attempt
# def create_phone_number(n):
#     #your code here
#     # => returns "(123) 456-7890"
#     # iterate through list and append each number to string output
#     # format output       
                                                          
#    return (f'({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}')


# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# second attempt

def create_phone_number(n):
    str1 = ""
    str2 = "" 
    str3 = ""

    for number in n[0:3]:
        str1 += str(number)
    for number in n[3:6]:
        str2 += str(number)
    for number in n[6:10]:
        str3 += str(number)

    return(f'({str1}) {str2}-{str3}')

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

