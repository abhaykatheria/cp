def timeConversion(string):
    l=len(string)
    temp1=int(string[0]+string[1])
    string1=string[2:]
    string3=string[l-2:]
    temp2=temp1+12
    if temp2 <24 and string3 !="AM":
        string=str(temp2)+string1
        string=string[:l-2]
    elif temp2 <24 and string3=="AM":
        string=string[:l-2]
    elif temp2==24 and string3=="PM":
        string=string[:l-2]
    else:
        string="00"+string1
        string=string[:l-2]
    print (string)
string=str(input())
timeConversion(string)