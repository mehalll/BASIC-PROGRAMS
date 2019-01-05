sub1 = int(input("Enter the marks of chemistry: "))
sub2 = int(input("Enter the marks of urdu:"))
sub3 = int(input("Enter the marks of english:"))
sub4 = int(input("Enter the marks of physics:"))
sub5 = int(input("Enter the marks of ict:"))

avg = (sub1+sub2+sub3+sub4+sub5) /5
if avg >= 90:
    print("grade A")
elif avg >= 80:
    print("grade B")
elif avg >= 70:
    print("grade C")
elif avg >= 60:
    print("grade D")
else:
    print(" grade F")
    
