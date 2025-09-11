#Created by Sam Stuyvenberg

standards = int(input("How many standards have been met?: "))
miss = int(input("How many standards have been missed?: "))

if standards == 57:
    print("A+")
elif 53 <= standards < 57:
    print("A")
elif 51 <= standards < 53:
    print("A-")
elif 49 <= standards < 51:
    print("B+")
elif 47 <= standards < 49 and miss == 0: 
    print("B")
elif 45 <= standards < 47 and miss == 0: 
    print("B-")
elif 43 <= standards < 45 and miss == 0:
    print("C+")
elif 40 <= standards < 43:
    print("C")
elif 35 <= standards < 40:
    print("D")
else:
    print("F")
