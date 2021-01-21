from random import choice, shuffle
from string import (
                     ascii_letters as letters,
                     digits,
                    punctuation,) 
if __name__ == "__main__":
    le = input("Enter the length of your password and letters/digits/punctuation you want in password:: ")
    lngth=int(le.split(" ")[0])
    if(le.split(" ")[1:]):
        s=le.split(" ")[1:]
    else:
        s=[]
    password=[]
    length=lngth-len("".join(s))
    for i in range(5):
        if i==0 or i==2:
            if s:
                a=[ choice("@"+"#"+"$"+"&"+"("+")"+"?"+":"+"_"+digits+digits) for _ in range(length)]
                s.extend(a)
                password.append("".join(s))
                s=le.split(" ")[1:]
            else:
                a=[ choice(letters+digits+"@"+"#"+"$"+"&"+"("+")"+"?"+":"+"_") for _ in range(length)]
                s.extend(a)
                password.append("".join(s))

        elif i==1 or i==3:
            a=[ choice(letters+digits+"@"+"#"+"$"+"&"+"("+")"+"?"+":"+"_") for _ in range(length)]
            a.extend(le.split(" ")[1:])
            password.append("".join(a))
        else:
            a=[ choice(letters+digits+"@"+"#"+"$"+"&"+"("+")"+"?"+":"+"_") for _ in range(lngth)]
            shuffle(a)
            password.append("".join(a))

    print("Password generated!")
    for i,j in enumerate(password):
        print(f" ({i+1}) >>  {j} ") 
