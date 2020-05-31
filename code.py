#HARSH KUMAR AGARWAL
#a = ("{0:0%db}" % alen).format(a)       #converts to binary value(as a string of length alen)
#int("stirng of zeros and one", 2)                             #converts from string binary to int decimal

import math
def pow2c(a):           #this function finds if the given parameter is a power of 2 or not
    c=math.log2(a)      #finding the log base 2 value of a
    return(c.is_integer())          #checking if the log base 2 value is an integer or not

def size_of_word(n):
    return (len('{:b}'.format(n))<32)       #checks and return if the given value is less than 32 bit or not


def search_dm(addr,tag_f,c1):       #function to search the address using direct mapping technique
    nb_tf = len(tag_f[0])           #find the size of the tag field
    linno=int(addr[nb_tf:nb_tf+nb_cl],2)        #extract the relevant part from the given address
    stf=tag_f[linno]
    if(stf==addr[:nb_tf]):              #checking if the given location has the same tag field or not(if yes than cache hit)
        print("CACHE HIT")
        r=int(math.log2(len(c1[0])))        # r stores the number of bit in which cache is stored
        bi=int(addr[-r:] ,2)                # slicing the address from the given address and then converting it to decimal form
        print("the value found at the given location is : ",c1[linno][bi])      #printing the value at the given location
    else:
        print("cache miss,address not found")


def load_cache_dm(rd,tag_f,c1,sd):          #function to load data into the cache using direct mapping technique
    nb_tf = len(tag_f[0])                   #finding the length of the bit required to store the tag field
    linno = int(rd[nb_tf:nb_tf + nb_cl], 2)     #slicing the part needed from the given address
    print("befor changing ,cache = ",c1)
    print("befor changing ,tag fields=",tag_f)
    tag_f[linno]=rd[:nb_tf]                     #changing the data in tag field
    c1[linno]=sd                                #changing the data in the cache
    print("After changing the cache, the new cache : ",c1)
    print("After changing the tag fields",tag_f)

def search_am(addr,tag_f,c1):       #function to search the address using associative mapping technique
    nb_tf = len(tag_f[0])               #finding the length of the bit required to store the tag field
    se=addr[:nb_tf]                 #slicing the part needed from the given address
    flag=0
    for i in range(len(c1)):            #start searching on each line of the cache
        if(se==tag_f[i]):               #checking if the given location has the same tag field or not(if yes than cache hit)
            flag=1
            print("CACHE HIT")
            r = int(math.log2(len(c1[0])))          # r stores the number of bit in which cache is stored
            bi = int(addr[-r:], 2)               # slicing the address from the given address and then converting it to decimal form
            print("the value found at the given location is : ", c1[i][bi])         #printing the value at the given location
            break
    if(flag==0):
        print("cache miss,address not found")


def load_cache_am(rd,tag_f,c1,sd,wheretocopy):      #function to load data into the cache using associative mapping technique
    print("befor changing ,cache = ", c1)                #rd is the value of the tagfield
    print("befor changing ,tag fields=", tag_f)
    tag_f[wheretocopy]=rd                            #changing the data in tag field
    c1[wheretocopy]=sd                                  #changing the data in the cache
    print("After changing the cache, the new cache : ", c1)
    print("After changing the tag fields", tag_f)


def search_nam(n,addr,tag_f,c1):            #function to search the address using n was associative mapping technique
    no_sets=int(cl/n)
    noofbit_for_sets=int(math.log2(no_sets))                #finding the length of the bit required to sets
    nb_tf = len(tag_f[0])                                    #finding the length of the bit required to store the tag field
    setno = int(addr[nb_tf:nb_tf + noofbit_for_sets], 2)        #slicing the part needed from the given address and converting it to decimal form
    se = addr[:nb_tf]                               #slicing the tag field part needed from the given address
    flag = 0
    for i in range(n*setno,n*setno+n):
        if(se==tag_f[i]):                       #checking if the given location has the same tag field or not(if yes than cache hit)
            flag = 1
            print("CACHE HIT")
            r = int(math.log2(len(c1[0])))           # r stores the number of bit in which cache is stored
            bi = int(addr[-r:], 2)                  # slicing the address from the given address and then converting it to decimal form
            print("the value found at the given location is : ", c1[i][bi])         #printing the value at the given location
            break
    if (flag == 0):
        print("cache miss,address not found")

def load_cache_nam(n,rd,tag_f,c1,sd,wheretocopy):                #function to load data into the cache using n way associative mapping technique
    no_sets = int(cl / n)                                       #calculating the number of sets from the given data
    noofbit_for_sets = int(math.log2(no_sets))                   #finding the length of the bit required to sets
    nb_tf = len(tag_f[0])
    setno = int(rd[nb_tf:nb_tf + noofbit_for_sets], 2)           #slicing the part needed from the given address and converting it to decimal form
    print("befor changing ,cache = ", c1)
    print("befor changing ,tag fields=", tag_f)
    tag_f[(setno*n+wheretocopy)]=rd[:nb_tf]                     #changing the data in tag field
    c1[(setno*n+wheretocopy)]=sd                                 #changing the data in the cache
    print("After changing the cache, the new cache : ", c1)
    print("After changing the tag fields", tag_f)

N=64        #predifining total size of main memory
cl=4            #predifing cache line size
b=4             #predifing size of block
majchoice=int(input("\nEnter 1 if you want to use predefined values or 2 if you want to enter your own value :\t"))
if(majchoice==2):
    cl = int(input("enter numbers of cache lines size :\t"))
    b=int(input("enter block size :\t"))
    N=int(input("enter the total number of blocks in the main memory as a power of 2\t"))

s=cl*b     #s is the total cache size
nb=int(N/b)  #number of blocks
nb_cl=int(math.log2(cl))  #store number of bits for cache line
nb_b=int(math.log2(b))      #store number of bits for block size
nb_nb=int(math.log2(nb))        #store number of bits for number of blocks
mm = []                     #initializing main memory(instead not used in the program)
cac=[]                      #initializing cache memory
tf=[]                       #initializing tag field(part with cache to see the address part)
if(not pow2c(s*N)):                 #checking if the given values are of power 2 or not
    print("THE GIVEN VALUES ARE NOT OF POWERS OF 2 PLEASE RERUN THE PROGRAM AND TRY AGAIN!!")
else:
    print("\t ENTER THE OPTIONS")
    print("1. Direct mapping ")
    print("2. Associative memory")
    print("3. n-way set associative memory where n is a power of 2.")

    for i in range(nb):
        row = []
        for j in range(b):
            row.append(i+j)             #putting some values in the main memory before our code start though not used in the program
        mm.append(row)

    for i in range(cl):
        row = []
        for j in range(b):
            row.append(i+j)             #putting some values in the cache before our code start
        cac.append(row)

    o=int(input("Your choice: "))       #asking for the choice
    wanttocont = 1
    if(o==1):
        nb_tf=nb_nb-nb_cl           #finding the number of bits required for tag field with the given data
        for i in range(cl):
            row=("{0:0%db}" % nb_tf).format(i)          #initialsing tag values with some data each in binary format of length find earlier
            tf.append(row)

        while(wanttocont==1):
            choi=int(input("Enter 1 if you want to search ,2 if you want to load : "))
            if(choi==1):
                print("Enter the address first ",nb_tf,"for tag field. Next ",nb_cl,"for line no. and next", nb_b,"for block offset")
                s=input("Enter the address to be fetched in binary format :\t")
                search_dm(s, tf, cac)                   #calling the function for searching the given address
                wanttocont = int(input("Enter 1 if you want to continue :\t"))
            elif(choi==2):
                print ("Enter first",nb_tf,"bit for tag field and next ",nb_cl,"bits for the cache line")
                r_add = input("Enter here: ")
                print("Enter",b,"values you want to store in cache")
                sentdata=[]
                for i in range(b):
                    t=int(input())                  #taking values to be stored in the cache
                    if(not size_of_word(t)):    #checking each word is less than 32 bit or not
                        print("The entered value is of greater size")
                        break
                    sentdata.append(t)
                load_cache_dm(r_add, tf, cac, sentdata)             #calling the fuction for loading of  the given data
                wanttocont = int(input("Enter 1 if you want to continue : "))
            else:
                print("Invalid choice ")
                wanttocont = int(input("Enter 1 if you want to continue : "))
    elif(o==2):
        counter = 0
        nb_tf = nb_nb                           #finding the number of bits required for tag field with the given data
        for i in range(cl):
            row=("{0:0%db}" % nb_tf).format(i)      #initialsing tag values with some data each in binary format of length find earlier
            tf.append(row)

        while (wanttocont == 1):
            choi = int(input("Enter 1 if you want to search ,2 if you want to load : "))
            if (choi == 1):
                print("Enter the address first ", nb_tf, "for tag field and next", nb_b,"for block offset")
                s = input("Enter the address to be fetched in binary format :  ")
                search_am(s, tf, cac)                                       #calling the function for searching the given address
                wanttocont = int(input("Enter 1 if you want to continue : "))
            elif (choi == 2):
                print("Enter", b, "values you want to store in cache")
                sentdata = []
                for i in range(b):
                    t = int(input())                            #taking values to be stored in the cache
                    if (not size_of_word(t)):                               #checking each word is less than 32 bit or not
                        print("The entered value is of greater size")
                        break
                    sentdata.append(t)
                print ("Enter first", nb_tf, "bit for tag field")
                r_add = input("Enter here: ")
                load_cache_am(r_add, tf, cac, sentdata, counter)                         #calling the fuction for loading of  the given data
                counter=counter+1
                counter = counter % cl                              #mainting the counter so that we know where to store next data
                wanttocont = int(input("Enter 1 if you want to continue : "))
            else:
                print("Invalid choice ")
                wanttocont = int(input("Enter 1 if you want to continue : "))
    elif(o==3):
        n=int(input("Enter the value of n: "))
        if(not pow2c(n)):
            print("THE GIVEN VALUES ARE NOT OF POWERS OF 2 PLEASE RERUN THE PROGRAM AND TRY AGAIN!!")
        else:
            counter = 0
            no_sets = int(cl / n)
            noofbit_for_sets = int(math.log2(no_sets))
            nb_tf=nb_nb-noofbit_for_sets        #finding the number of bits required for tag field with the given data
            for i in range(cl):
                row = ("{0:0%db}" % nb_tf).format(i)        #initialsing tag values with some data each in binary format of length found earlier
                tf.append(row)
            while (wanttocont == 1):
                choi = int(input("Enter 1 if you want to search ,2 if you want to load : "))
                if (choi == 1):
                    print("Enter the address first ", nb_tf, "for tag field. Next ", noofbit_for_sets , "for set line", nb_b,"for block offset")
                    s = input("Enter the address to be fetched in binary format : ")
                    search_nam(n, s, tf, cac)                           #calling the function for searching the given address
                    wanttocont = int(input("Enter 1 if you want to continue : "))
                elif (choi == 2):
                    print ("Enter first", nb_tf, "bit for tag field and next ", noofbit_for_sets, "bits for set line")
                    r_add = input("Enter here: ")
                    print("Enter", b, "values you want to store in cache")
                    sentdata = []
                    for i in range(b):
                        t = int(input())                                        #taking values to be stored in the cache
                        if (not size_of_word(t)):                   #checking each word is less than 32 bit or not
                            print("The entered value is of greater size")
                            break
                        sentdata.append(t)
                    load_cache_nam(n, r_add, tf, cac, sentdata, counter)                 #calling the fuction for loading of  the given data
                    counter = (counter + 1) % n                                              #mainting the counter so that we know where to store next data
                    wanttocont = int(input("Enter 1 if you want to continue : "))
                else:
                    print("Invalid choice ")
                    wanttocont = int(input("Enter 1 if you want to continue : "))

    else:
        print("INVALID OPTION SELECTED")
        print("PLEASE RERUN THE PROGRAM")



