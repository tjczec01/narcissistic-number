def nexp(num):
    n_int = int(num)
    nn = len(str(n_int))
    digits = []
    for i in range(nn):
        digits.append(int(str(n_int)[i]))
    digits_exp = [n**nn for n in digits]
    total = sum(digits_exp)
    # print(num, total)
    # print(n_int == total)
    return(n_int == total)




end_num = int(input("Input number to find all narcissistic numbers under: "))  # Range of numbers to look through

numbs = []

for i in range(0, end_num + 1, 1):
    if nexp(i) is True:
        #print(i, nexp(i))
        numbs.append(i)
    else:
        pass
    
print(numbs)
