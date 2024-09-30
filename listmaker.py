import os

def listadd(m):
    n=m+".txt"
    b=os.path.isfile(n)
    if b== True:
        return "The list already exists"
    if b== False:
        open(n,'w')
        return "The List Is Created"
def elementadd(n,k):
     l=k+".txt"
     print(l)
     filename=open(l,'a')
     filename.write("{}\n".format(n))
def elementremove(f,g):
 # f= Element to remove
 # g= List name
 j=g+".txt"


 with open(j, "r") as input:
    with open("temp.txt", "w") as output:
        # iterate all lines from file
        for line in input:
            # if text matches then don't write it
            if line.strip("\n") != f:
                output.write(line)

 # replace file with original name
 os.replace('temp.txt', j)



  