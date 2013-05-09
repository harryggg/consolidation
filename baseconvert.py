def baseconvert(n,frombase,tobase=10):
    
    #convert to decimal form
    decimal_form=0
    counter = 0
    for element in list(str(n))[::-1]:
        decimal_form += int(todec[element])*(frombase**counter)
        counter += 1

    if tobase == 10: return decimal_form
    #to the target base
    if decimal_form < tobase: return base[decimal_form]
    
    result =""
    while decimal_form >= tobase:
        result += base[decimal_form % tobase]
        decimal_form = decimal_form // tobase
    result += base[decimal_form % tobase]
    return result[::-1]
        
    
todec={}
base={}

for i in range(10):
    base[i]=str(i)
    todec[str(i)]=i


for i in range(10,16):
    base[i]=chr(55+i)
    todec[chr(55+i)]=i
