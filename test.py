s1="0 1 2 3 4 5 6 7 8 9"
s3="0 1 2 3 4 5 6 7 8 9"
s4="0 1 2 3 4 5 6 7 8 9"
s1=s1.strip().split()
s3=s3.strip().split()
s4=s4.strip().split()
s1[4]="7"
s2=[]
s2.append(s1)
s2.append(s3)
s2.append(s4)



fi = open("test.txt","w")
for el in s2:
    el=str(el)
    el=el.strip("[']")
    el=el.replace("', '"," ")
    print(el)
    fi.write(el)
    fi.write("\n")
# s5="".join(s2)
