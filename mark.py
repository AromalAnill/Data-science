def result(m1,m2,m3):
    total=m1+m2+m3
    percentage=total/3

    if percentage>=90:
        grade="A"
    elif percentage>=80:
        grade="B"
    elif percentage>=70:
        grade="C"
    else:
        grade="D"
    print("total marks=",total)
    print("percentage marks=",percentage)
    print("grade=",grade)

m1=int(input("enter the mark1:"))
m2=int(input("enter the mark2:"))
m3=int(input("enter the mark3:"))

result(m1,m2,m3)


