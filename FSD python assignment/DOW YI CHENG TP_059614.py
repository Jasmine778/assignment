#DOW YI CHENG
#TP059614
#register part 
def register():
    cnt1 = 1
    ptlist = []
    mylist = []
    ptname= str(input("\nEnter patient name:"))
    r=open("patient.txt","r")    
    for list1 in r:
        sp = list1.split("><")
        ptlist.append(str(sp[0]))
    r.close()
    ptnumber = int(ptlist[-1])
    ptnumber = ptnumber + 1
    ptcontact = str(input("Enter patient contact number or email address :"))
    print("Select one patient group(ATO/ACC/AEO/SID/AHS) in below:\nA.ATO\nB.ACC\nC.AEO\nD.SID\nE.AHS")
    ptgroup = str(input("Enter Patient group:"))        
    while (ptgroup!= "ATO" and ptgroup!="ACC" and ptgroup!="AEO" and ptgroup!="SID" and ptgroup!="AHS"):
            print ("Invalid group name")
            ptgroup = str(input("Please type again:"))

    print("\nPatient name is :",ptname,
            "\nPatient id numebr is :",ptnumber,
            "\nPatient personal contact number or email address is:",ptcontact,
            "\nPatient group is :",ptgroup,"\n")

    f=open("patient.txt","a")
    f.write(str(ptnumber)+"><"+str(ptname)+"><"+str(ptcontact)+"><"+str(ptgroup)+"\n")
    f.close ()
    zone()
#catogory zone
def zone():
    mylist=[]
    r=open("patient.txt","r")
    for list1 in r:
        sp = list1.split("><")
        mylist.append(int(sp[0]))
    table1 = []
    table2 = []
    table3 = []
    table4 = []
    cnt2 = 0
    for cnt2 in mylist:
        if (cnt2%4==1):
            table1.append(cnt2)
        elif (cnt2%4==2):
            table2.append(cnt2)
        elif (cnt2%4==3):
            table3.append(cnt2)
        else:
            table4.append(cnt2)
                    
    print ("Patient ID in Zone A are: ",table,
            "\nPatient ID in Zone B are: ",table2,
            "\nPatient ID in Zone C are: ",table3,
            "\nPatient ID in Zone D are: ",table4 )
    print ("Total patient ID list that have in hospital : ",mylist)
    r.close()
    function()
    
#TEST 1
def test1():
    flag = 1
    ptlist =[]
    while (flag == 1 or flag == 2 or flag == 3 or flag==4 or flag ==5):
        ptnumber = int(input("\nEnter patient ID:"))
        flag = 0
        r1 = open ("patient.txt","r") # checking range of patient
        for list1 in r1:
            a = list1.split("><")
            ptlist.append (a[0])
        for a in ptlist:
            if (ptnumber != int(a)):
                flag = 1
            elif (ptnumber == int(a)):
                flag = 0
                break
        r1.close()
        r3 = open ("negativecase1.txt","r") # checking overlapping in negative
        for list3 in r3:
            a = list3.strip()
            if (ptnumber == int(a)):
                flag = 3
                break
        r3.close()
        
        r2 = open ("positivecase.txt","r") # checking overlapping in positive
        for list2 in r2:
            list2 = list2.split("\t")
            a = list2[0].strip()
            if (ptnumber == int(a)):
                flag = 2
                break
        r2.close()
        
        r4 = open ("recover.txt","r")
        for list4 in r4:
            a = list4.strip()
            if (ptnumber ==int(a)):
                flag = 4
                break
        r4.close()
        r5 = open ("dead.txt","r")
        for list5 in r5:
            a = list5.strip()
            if (ptnumber ==int(a)):
                flag = 5
                break
        r5.close()
        if flag == 1:
            print ("This patient id haven't register\nPlease enter again")
            testinput()
        elif flag == 2:
            print ("This patient id already has been tested positive\nPlease enter again")
            testinput()
        elif flag == 3:
            print ("This patient id already has been tested negative,preparing for test 2\nPlease enter again")
            testinput()
        elif flag == 4:
            print ("This patient id already recovered\nPlease enter again")
            testinput()
        elif flag == 5:
            print ("This patient id already dead\nPlease enter again")
            testinput()
        else :
            r=open("patient.txt","r")    
            for list1 in r:
                sp = list1.split("><")
                if (ptnumber == int(sp[0])):
                    ptgroup = str(sp[3].strip("\n"))
                    ptname = str(sp[1])
                    ptcontact = str(sp[2])
                    if (ptnumber%4==1):
                        zone = str("zone A")
                    elif (ptnumber%4==2):
                        zone = str("zone B")
                    elif (ptnumber%4==3):
                        zone = str("zone C")
                    else:
                        zone = str("zone D")
                    print ("Patient name is:",ptname,"\nPatient id is:",ptnumber,"\nPatient contact is:",ptcontact,"\nPatient group is:",ptgroup,"\nPatient zone is:",zone)
                    positivelist=[]
                    totallist=[]
                    r2 = open ("positivecase.txt","r")
                    for cnt in r2:
                        a = cnt.split("\t")
                        b = a[0].strip()
                        totallist.append (b.strip())
                    r2.close()
            if(ptgroup == "ATO" or ptgroup=="ACC" or ptgroup=="AEO"):
                test1= int(input("\nEnter patient test 1 result :\n0.Return to option menu\n1.Positive \n2.Negative\nPlease select your option:"))
                if(test1 == 1):
                    print ("Advise patient QHNF")
                    place = str(input("Stay at ICU/NW :"))
                    while place != "ICU" and place != "NW":
                        print ("Invalid input")
                        place = str(input("Stay at ICU/NW :"))
                    positivelist.append(ptnumber)
                    for positive in positivelist:
                        totallist.append (str(ptnumber))
                    w=open ("positivecase.txt","a")
                    w.write (str(ptnumber)+"\t"+place+"\n")
                    w.close()
                        
                elif(test1 == 2):
                    print ("Advise patient QDFR and preparing for test 2")
                    w = open ("negativecase1.txt","a")
                    w.write (str(ptnumber)+"\n")
                    w.close()
                    
                elif(test1 == 0):
                    function()
                else:
                    print ("Invalid input ")
                    test1= int(input("Please type again :"))
                    testinput()
                    
            elif(ptgroup =="SID"):
                test1= int(input("\nEnter patient test 1 result :\n0.Return to option menu\n1.Positive \n2.Negative\nPlease select your option:"))
                if(test1 == 1):
                    print ("Advise patient QHNF")
                    place = str(input("Stay at ICU/NW :"))
                    if place != "ICU" and place != "NW":
                        print ("Invalid input")
                        function()
                    positivelist.append(ptnumber)
                    for positive in positivelist:
                        totallist.append (str(ptnumber))
                    w=open ("positivecase.txt","a")
                    w.write (str(ptnumber)+"\t"+place+"\n")
                    w.close()
                        
                elif(test1 == 2):
                    print ("Advise patient HQFR and preparing for test 2")
                    w = open ("negativecase1.txt","a")
                    w.write (str(ptnumber)+"\n")
                    w.close()
                elif(test1 == 0):
                    function()
                else:
                    print ("Invalid input ")
                    test1= int(input("Please type again :"))
                    testinput ()

            elif(ptgroup =="AHS"):
                test1= int(input("\nEnter patient test 1 result :\n0.Return to option menu\n1.Positive \n2.Negative\nPlease select your option:"))
                if(test1 == 1):
                    print ("Advise patient HQNF")
                    positivelist.append(ptnumber)
                    for positive in positivelist:
                        a = positive
                        totallist.append (str(ptnumber))
                    w=open ("positivecase.txt","a")
                    w.write (str(ptnumber)+"\t"+"-"+"\n")
                    w.close()
                        
                elif(test1 == 2):
                    print ("Advise patient CWFR and preparing for test 2")
                    w = open ("negativecase1.txt","a")
                    w.write (str(ptnumber)+"\n")
                    w.close()             
                elif(test1 == 0):
                    function()
                else:
                    print ("Invalid input ")
                    test1= int(input("Please type again :"))
                    testinput()
            
            caseidlist = []
            if test1== 1:
                r = open ("caseactive.txt","r")
                for cnt in r:
                    a=cnt.split("\t")
                    b=a[0].split()
                    caseidlist.append (b)
                idc = len(caseidlist)
                p1 = open ("caseactive.txt","a")
                p1.write(str(idc)+"\t"+str(ptnumber)+"\t"+"ACTIVE"+"\n") 
                print ("Case id for patient id",ptnumber,"is:",idc)
                p1.close ()
                r.close()
            print("\n")
            print("ˇ" * 70)
            print ("Patient ID in active case is :",totallist,"\nTotal number of active case is :",len(totallist))
            print ("Patient information has been updated suscessful")
            testinput()
        
#TEST 2
def test2():
    flag = 1
    ptlist =[]
    while (flag == 1 or flag == 2 or flag == 3 or flag == 5):
        ptnumber = int(input("\nEnter patient ID:"))
        flag = 0
        r1 = open ("patient.txt","r") # checking range of patient
        for list1 in r1:
            a = list1.split("><")
            ptlist.append (a[0])
        for a in ptlist:
            if (ptnumber != int(a)):
                flag = 1
            elif (ptnumber == int(a)):
                flag = 0
                break
        r1.close()
        r4 = open ("negativecase1.txt","r")
        for list4 in r4:
            a = list4.strip()
            if (ptnumber == int(a)):
                flag = 4
                break

        r3 = open ("negativecase2.txt","r") # checking overlapping in negative
        for list3 in r3:
            a = list3.strip()
            if (ptnumber == int(a)):
                flag = 3
                break
        r3.close()

        r2 = open ("positivecase.txt","r") # checking overlapping in positive
        for list2 in r2:
            list2 = list2.split("\t")
            a = list2[0].strip()
            if (ptnumber == int(a)):
                flag = 2
                break
        r2.close()

        r5 = open ("recover.txt","r")
        for list5 in r5:
            a = list5.strip()
            if (ptnumber ==int(a)):
                flag = 5
                break
        r5.close()

        r6 = open ("dead.txt","r")
        for list6 in r6:
            a = list6.strip()
            if (ptnumber ==int(a)):
                flag = 6
                break
        r6.close()
        if flag == 1:
            print ("This patient id haven't register\nPlease enter again")
            testinput()
        elif flag == 2:
            print ("This patient id already has tested positive\nPlease enter again")
            testinput()
        elif flag == 3:
            print ("This patient id already has tested negative,preparing for test 3\nPlease enter again")
            testinput()
        elif flag == 5:
            print ("This patient id already recovered\nPlease enter again")
            testinput()
        elif flag == 6:
            print ("This patient id already dead\nPlease enter again")
            testinput()
        elif flag == 4: 
            r=open("patient.txt","r")    
            for list1 in r:
                sp = list1.split("><")
                if (ptnumber == int(sp[0])):
                    ptgroup = str(sp[3].strip("\n"))
                    ptname = str(sp[1])
                    ptcontact = str(sp[2])
                    if (ptnumber%4==1):
                        zone = str("zone A")
                    elif (ptnumber%4==2):
                        zone = str("zone B")
                    elif (ptnumber%4==3):
                        zone = str("zone C")
                    else:
                        zone = str("zone D")
            
                    print ("Patient name is:",ptname,"\nPatient id is :",ptnumber,"\nPatient contact is :",ptcontact,"\nPatient group is :",ptgroup,"\nPatient zone is:",zone)
                    positivelist=[]
                    totallist=[]
                    r2 = open ("positivecase.txt","r")
                    for cnt in r2:
                        a = cnt.split("\t")
                        b = a[0].strip()
                        totallist.append (b.strip())
                    r2.close()
            if(ptgroup == "ATO" or ptgroup=="ACC" or ptgroup=="AEO"):
                test1= int(input("\nEnter patient test 1 result :\n0.Return to option menu\n1.Positive \n2.Negative\nPlease select your option:"))
                if(test1 == 1):
                    print ("Advise patient QHNF")
                    place = str(input("Stay at ICU/NW :"))
                    while place != "ICU" and place != "NW":
                        print ("Invalid input")
                        function()
                    positivelist.append(ptnumber)
                    for positive in positivelist:
                        totallist.append (str(ptnumber))
                    w=open ("positivecase.txt","a")
                    w.write (str(ptnumber)+"\t"+place+"\n")
                    w.close()
                elif(test1 == 2):
                    print ("Advise patient QDFR and preparing for test 3")
                    w = open ("negativecase2.txt","a")
                    w.write (str(ptnumber)+"\n")
                    w.close()

                elif(test1 == 0):
                    function()                            

                else:
                    print ("Invalid input ")
                    test1= int(input("Please type again :"))
                    testinput()
                    
            elif(ptgroup =="SID"):
                test1= int(input("\nEnter patient test 1 result :\n0.Return to option menu\n1.Positive \n2.Negative\nPlease select your option:"))
                if(test1 == 1):
                    print ("Advise patient QHNF")
                    place = str(input("Stay at ICU/NW :"))
                    while place != "ICU" and place != "NW":
                        print ("Invalid input")
                        function()
                    positivelist.append(ptnumber)
                    for positive in positivelist:
                        totallist.append (str(ptnumber))
                    w=open ("positivecase.txt","a")
                    w.write (str(ptnumber)+"\t"+place+"\n")
                    w.close()
                    
                elif(test1 == 2):
                    print ("Advise patient HQFR and preparing for test 3")
                    w = open ("negativecase2.txt","a")
                    w.write (str(ptnumber)+"\n")
                    w.close()

                elif(test1 == 0):
                    function()                        
                        
                else:
                    print ("Invalid input ")
                    test1= int(input("Please type again :"))
                    testinput()

            elif(ptgroup =="AHS"):
                test1= int(input("\nEnter patient test 1 result :\n0.Return to option menu\n1.Positive \n2.Negative\nPlease select your option:"))
                if(test1 == 1):
                    print ("Advise patient HQNF")
                    positivelist.append(ptnumber)
                    for positive in positivelist:
                        a = positive
                        totallist.append (str(ptnumber))
                    w=open ("positivecase.txt","a")
                    w.write (str(ptnumber)+"\t"+"-"+"\n")
                    w.close()
                        
                elif(test1 == 2):
                    print ("Advise patient CWFR and preparing for test 3")
                    w = open ("negativecase2.txt","a")
                    w.write (str(ptnumber)+"\n")
                    w.close()

                elif(test1 == 0):
                    function()                                

                else:
                    print ("Invalid input ")
                    test1= int(input("Please type again :"))
                    testinput()
            r.close()
            caseidlist = []
            if test1== 1:
                r = open ("caseactive.txt","r")
                for cnt in r:
                    a=cnt.split("\t")
                    b=a[0].split()
                    caseidlist.append (b)
                idc = len(caseidlist)
                p1 = open ("caseactive.txt","a")
                p1.write(str(idc)+"\t"+str(ptnumber)+"\t"+"ACTIVE"+"\n") 
                print ("Case id for patient id",ptnumber,"is:",idc)
                p1.close ()
                r.close()
            print("\n")
            print("ˇ" * 70)
            print ("Patient ID in active case is :",totallist,"\nTotal number of active case is :",len(totallist))
            print ("Patient information has been updated suscessful")
            function()

        else:
            print ("This patient haven't enter test 1 result ")
            testinput()
                    
#test3
def test3():
    flag = 1
    ptlist =[]
    while (flag == 1 or flag == 2 or flag == 3 or flag == 5):
        ptnumber = int(input("\nEnter patient ID:"))
        flag = 0
        r1 = open ("patient.txt","r") # checking range of patient
        for list1 in r1:
            a = list1.split("><")
            ptlist.append (a[0])
        for a in ptlist:
            if (ptnumber != int(a)):
                flag = 1
            elif (ptnumber == int(a)):
                flag = 0
                break
        r1.close()
        r4 = open ("negativecase2.txt","r")
        for list4 in r4:
            a = list4.strip()
            if (ptnumber == int(a)):
                flag = 4
                break
        r4.close()
        r3 = open ("negativecase3.txt","r") # checking overlapping in negative
        for list3 in r3:
            a = list3.strip()
            if (ptnumber == int(a)):
                flag = 3
                break
        r3.close()

        r2 = open ("positivecase.txt","r") # checking overlapping in positive
        for list2 in r2:
            list2 = list2.split("\t")
            a = list2[0].strip()
            if (ptnumber == int(a)):
                flag = 2
                break
        r2.close()

        r5 = open ("recover.txt","r")
        for list5 in r5:
            a = list5.strip()
            if (ptnumber ==int(a)):
                flag = 5
                break
        r5.close()
        r6 = open ("dead.txt","r")
        for list6 in r6:
            a = list6.strip()
            if (ptnumber ==int(a)):
                flag = 6
                break
        r6.close()
        if flag == 1:
            print ("This patient id haven't register\nPlease enter again")
            testinput()
            
        elif flag == 2:
            print ("This patient id already tested positive\nPlease enter again")
            testinput()
            
        elif flag == 3:
            print ("Patient already advised RU or CW\nPlease enter again")
            testinput()
            
        elif flag == 5:
            print ("Patient has already recovered")
            testinput()

        elif flag == 6:
            print ("This patient id already dead\nPlease enter again")
            testinput()           

        elif flag == 4: 
            r=open("patient.txt","r")    
            for list1 in r:
                sp = list1.split("><")
                if (ptnumber == int(sp[0])):
                    ptgroup = str(sp[3].strip("\n"))
                    ptname = str(sp[1])
                    ptcontact = str(sp[2])
                    if (ptnumber%4==1):
                        zone = str("zone A")
                    elif (ptnumber%4==2):
                        zone = str("zone B")
                    elif (ptnumber%4==3):
                        zone = str("zone C")
                    else:
                        zone = str("zone D")

                    print ("Patient name is:",ptname,"\nPatient id is :",ptnumber,"\nPatient contact is :",ptcontact,"\nPatient group is :",ptgroup,"\nPatient zone is:",zone)
                    positivelist=[]
                    totallist=[]
                    r2 = open ("positivecase.txt","r")
                    for cnt in r2:
                        a = cnt.split("\t")
                        b = a[0].strip()
                        totallist.append (b.strip())
                    r2.close()
            if(ptgroup == "ATO" or ptgroup=="ACC" or ptgroup=="AEO"):
                test1= int(input("\nEnter patient test 1 result :\n0.Return to option menu\n1.Positive \n2.Negative\nPlease select your option:"))
                if(test1 == 1):
                    print ("Advise patient QHNF")
                    place = str(input("Stay at ICU/NW :"))
                    while place != "ICU" and place != "NW":
                        print ("Invalid input")
                    positivelist.append(ptnumber)
                    for positive in positivelist:
                        totallist.append (str(ptnumber))
                    w=open ("positivecase.txt","a")
                    w.write (str(ptnumber)+"\t"+place+"\n")
                    w.close()

                elif(test1 == 2):
                    print ("Advise patient RU")
                    w = open ("negativecase3.txt","a")
                    w.write (str(ptnumber)+"\n")
                    w.close()

                elif(test1 == 0):
                    function()                            

                else:
                    print ("Invalid input ")
                    test1= int(input("Please type again :"))
                    function ()
                    
            elif(ptgroup =="SID"):
                test1= int(input("\nEnter patient test 1 result :\n0.Return to option menu\n1.Positive \n2.Negative\nPlease select your option:"))
                if(test1 == 1):
                    print ("Advise patient QHNF")
                    place = str(input("Stay at ICU/NW :"))
                    while place != "ICU" and place != "NW":
                        print ("Invalid input")
                    w=open ("positivecase.txt","a")
                    w.write (str(ptnumber)+"\t"+place+"\n")
                    w.close()
                        
                elif(test1 == 2):
                    print ("Advise patient RU")
                    w = open ("negativecase3.txt","a")
                    w.write (str(ptnumber)+"\n")
                    w.close()
                        

                elif(test1 == 0):
                    function()                        
                        
                else:
                    print ("Invalid input ")
                    test1= int(input("Please type again :"))
                    function ()

            elif(ptgroup =="AHS"):
                test1= int(input("\nEnter patient test 1 result :\n0.Return to option menu\n1.Positive \n2.Negative\nPlease select your option:"))
                if(test1 == 1):
                    print ("Advise patient HQNF")
                    positivelist.append(ptnumber)
                    for positive in positivelist:
                        a = positive
                        totallist.append (str(ptnumber))
                    w=open ("positivecase.txt","a")
                    w.write (str(ptnumber)+"\t"+"-"+"\n")
                    w.close ()
                        
                elif(test1 == 2):
                    print ("Advise patient CW")
                    w = open ("negativecase3.txt","a")
                    w.write (str(ptnumber)+"\n")
                    w.close ()

                elif(test1 == 0):
                    function()                                

                else:
                    print ("Invalid input ")
                    test1= int(input("Please type again :"))
                    function ()
            r.close()
            caseidlist = []
            if test1== 1:
                r = open ("caseactive.txt","r")
                for cnt in r:
                    a=cnt.split("\t")
                    b=a[0].split()
                    caseidlist.append (b)
                idc = len(caseidlist)
                p1 = open ("caseactive.txt","a")
                p1.write(str(idc)+"\t"+str(ptnumber)+"\t"+"ACTIVE"+"\n") 
                print ("Case id for patient id",ptnumber,"is:",idc)
                p1.close ()
                r.close()
            print("\n")
            print("ˇ" * 70)
            print ("Patient ID in active case is :",totallist,"\nTotal number of active case is :",len(totallist))
            print ("Patient information has been updated suscessful")
            testinput()

        else:
            print ("This patient haven't enter test 1 or test 2 result ")
            testinput()

def testinput():
    check = 0
    cnt = 1
    while (cnt == 1):
        print("\nSelect test (0,1,2,3) result that you want upload\n0.Return to main option\n1.Enter test 1 result\n2.Enter test 2 result\n3.Enter test 3 result")
        check = int(input("Please select your command :"))
        while (check >3 or check<0):
            print("\nInvalid value")
            check = int(input("Please insert your value again:"))
        if (check >= 1 and check <=3):
            if (check == 1):
                test1()
            elif (check == 2):
                test2()
            elif (check == 3):
                test3()
            elif (check == 0):
                function()
            else:
                cnt=1
        else:
            cnt=1
#changing active list to RECOVERED / DECEASED
def edit():
    totallist = []
    ptlist = []
    k = open ("positivecase.txt","r")
    for u in k:
        u = u.split("\t")
        totallist.append(int(u[0].strip()))
    k.close()
    caseid = int(input("Enter patient case ID:"))
    if (caseid>len(totallist)):
        print ("Invalid case ID")
        function()
    ptnumber = int(totallist[caseid-1])
    r1 = open ("patient.txt","r") # checking range of patient
    for list1 in r1:
        a = list1.split("><")
        ptlist.append (a[0])
    for a in ptlist:
        if (ptnumber != int(a)):
            flag = 1
        elif (ptnumber == int(a)):
            flag = 0
            break
    r1.close()
    if (flag == 1):
        print ("This patient ID haven't register")
        function ()

    with open ("caseactive.txt","r")as f:
        for line in f:
            a=line.split("\t")
            if (str(caseid) == a[0]):
                if(a[2].strip() != "ACTIVE"):                
                    flag = 0
                    break
                else:
                    flag = 1

    if flag == 0:
        print ("This ACTIVE case status already changed\nPlease enter again:")
        function()
    
    r=open("patient.txt","r")
    for list1 in r:
        sp = list1.split("><")
        if (ptnumber == int(sp[0])):
            ptgroup = str(sp[3].strip("\n"))
            ptname = str(sp[1])
            ptcontact = str(sp[2])
            if (ptnumber%4==1):
                zone = str("zone A")
            elif (ptnumber%4==2):
                zone = str("zone B")
            elif (ptnumber%4==3):
                zone = str("zone C")
            else:
                zone = str("zone D")
    r.close()
    positivelist = []
    print ("Patient name is:",ptname,"\nPatient id is :",ptnumber,"\nPatient contact is :",ptcontact,"\nPatient group is :",ptgroup,"\nPatient zone is:",zone)
    h = open ("positivecase.txt","r")
    for list1 in h:
        list1 = list1.split("\t") 
        positivelist.append(list1[0].strip("\n")) #read value to positive list
    h.close()
    for cnt in positivelist: #checking positivelist    
        cnt = cnt.split("\t")
        cnt = cnt[0].strip()
        if(ptnumber == int(cnt)):
            print("\nChanging status to RECOVERED = 1\nChanging status to DECEASED = 2")
            status = int(input("Please enter your command :"))
            while (status < 1 or status > 2):
                status = int(input("Please enter your command :"))
            if (status == 1 or status == 2):
                if(status == 1):
                    r = open ("recover.txt","a")
                    r.write (str(ptnumber)+"\n")
                    r.close()
                    filedata = ""
                    with open ("caseactive.txt","r")as f:
                        for line in f:
                            a=line.split("\t")
                            if (str(caseid) == a[0] ):
                                new = a[2].replace("ACTIVE","RECOVERED")
                                newdata = str(caseid)+"\t"+a[1]+"\t"+new
                                filedata = filedata + newdata
                            else:
                                filedata = filedata + line

                    with open("caseactive.txt","w") as f:
                        f.write(filedata)
                        
                    print ("Caseid :",caseid,"\tStatus : RECOVERED","\tPatient ID:",ptnumber)
                    print ("Cases of patient ID infected:",positivelist)
                    print ("Total case of infected status:",len(positivelist))
                    print ("Patient information has been updated suscessful")
                    function()
                        
          
                elif(status == 2):
                    r = open ("dead.txt","a")
                    r.write (str(ptnumber)+"\n")
                    r.close()
                    file_data = ""
                    with open ("caseactive.txt","r")as f:
                        for line in f:
                            a=line.split("\t")
                            if (str(caseid) == a[0] ):
                                new = a[2].replace("ACTIVE","DECEASED")
                                newdata = str(caseid)+"\t"+a[1]+"\t"+new
                                file_data = file_data + newdata
                            else:
                                file_data = file_data + line

                    with open("caseactive.txt","w") as f:
                        f.write(file_data)
                        
                    print ("Caseid :",caseid,"\tStatus : DECEASED","\tPatient ID:",ptnumber)
                    print ("Cases of patient ID infected:",positivelist)
                    print ("Total case of infected status:",len(positivelist))
                    print ("Patient information has been updated suscessful")
                    function()
            
    print ("\nInvalid input\nThis patient ID havent insert to ACTICE case")
    function()
#4.1
def testoutput ():
    ptlist = []
    ptlist1 = []
    ptlist2 = []
    ptlist3 = []
    ptlist4 = []
    print("ˇ" * 70 )

    r = open ("positivecase.txt","r")
    print ("\n\n\t\t-----$$$ ALL POSITIVE TEST $$$------")
    for cnt in r:
        a = cnt.split("\t")
        a = a[0].strip("\n")
        ptlist.append (a)
        ptlist4.append (a)
    print ("\n\tAll patient id in active case are ",ptlist)
    print ("\n\tTotal number tested carry out in active case are ",len(ptlist))
    r.close ()

    print("\n\t\t------$$$ NEGATIVE TEST 1 $$$-------")
    r = open ("negativecase1.txt","r")
    for cnt in r:
        a = cnt.strip("\n")
        ptlist1.append (a)
        ptlist4.append (a)
    print ("\n\tAll patient id tested negetive in test 1 ",ptlist1)
    print ("\n\tNumber of tests carried out in NEGATIVE TEST 1 ",len(ptlist1))
    r.close ()

    print("\n\t\t------$$$ NEGATIVE TEST 2 $$$-------")
    r = open ("negativecase2.txt","r")
    for cnt in r:
        a = cnt.strip("\n")
        ptlist2.append (a)
        ptlist4.append (a)
    print ("\n\tAll patient id tested negetive in test 2 ",ptlist2)
    print ("\n\tNumber of tests carried out in NEGATIVE TEST 2 ",len(ptlist2))
    r.close ()

    print("\n\t\t------$$$ NEGATIVE TEST 3 $$$-------")
    r = open ("negativecase3.txt","r")
    for cnt in r:
        a = cnt.strip("\n")
        ptlist3.append (a)
        ptlist4.append (a)
    print ("\n\tAll patient id tested negetive in test 3 ",ptlist3)
    print ("\n\tNumber of tests carried out in NEGATIVE TEST 3 ",len(ptlist3))
    r.close ()
    print ("\n\t\tTotal number of tested carry out",len(ptlist4))

#4.2
def patient():
    ptlist = []
    ptlist1 = []
    print("ˇ" * 70 )

    r = open ("positivecase.txt","r")
    print ("\n\n\t\t-----$$$ TOTAL OF PATIENT TESTED $$$------")
    for cnt in r:
        a = cnt.strip("\n")
        a = a[0].strip("\n")
        ptlist.append (a)

    r.close ()
    r = open ("negativecase1.txt","r")
    for cnt in r:
        a = cnt.strip("\n")
        ptlist.append (a)

    r.close ()

    for cnt in ptlist:
        if cnt not in ptlist1:
            ptlist1.append (cnt)
    print ("\n\t\tTotal number of patient tested is",len(ptlist1))
#4.3   
def recovered ():
    ptlist=[]
    r = open ("recover.txt","r")
    for cnt in r:
        a = cnt.strip("\n")
        ptlist.append (a)
    print ("\n\n\t\t-----$$$ RECOVERED CASE $$$------")
    print ("\tAll patient id that had been recovered are",ptlist)
    print ("\tTotal number case of patient that had been recovered are",len(ptlist))
    r.close()
#4.4
def positive():
    caselist = []
    ato = []
    acc = []
    aeo = []
    sid = []
    ahs = []
    r = open ("positivecase.txt","r")
    for cnt in r:
        a = cnt.strip("\n")
        a = a[0].strip("\n")
        caselist.append(a)
    r.close()
    caselist.sort
    r1 = open ("patient.txt","r")
    for cnt2 in r1:
        for cnt in caselist:     
            a = cnt2.split("><")
            b = a[3].strip()
            if cnt == a[0]:                
                if b == "ATO":
                    a[0]=int(a[0])
                    ato.append (a[0])
                elif b == "ACC":
                    a[0]=int(a[0])
                    acc.append (a[0])
                elif b == "AEO":
                    a[0]=int(a[0])
                    aeo.append (a[0])
                elif b == "SID":
                    a[0]=int(a[0])
                    sid.append (a[0])
                elif b == "AHS":
                    a[0]=int(a[0])
                    ahs.append (a[0])
        
    print("\n\n\t\t --------$$$ TOTAL POSITIVE CASE $$$---------")
    print("\t\t  Total cases if positive tested patient are",len(caselist))
    print("\n\n\t\t-----$$$ TOTAL POSITIVE CASE IN ATO GROUP $$$------")
    print("\n\t\t\tTotal cases in ATO group are",len(ato))
    print("\n\n\t\t-----$$$ TOTAL POSITIVE CASE IN ATO GROUP $$$------")
    print("\n\t\t\tTotal cases in ACC group are",len(acc))
    print("\n\n\t\t-----$$$ TOTAL POSITIVE CASE IN ATO GROUP $$$------")
    print("\n\t\t\tTotal cases in AEO group are",len(aeo))
    print("\n\n\t\t-----$$$ TOTAL POSITIVE CASE IN ATO GROUP $$$------")
    print("\n\t\t\tTotal cases in SID group are",len(sid))
    print("\n\n\t\t-----$$$ TOTAL POSITIVE CASE IN ATO GROUP $$$------")
    print("\n\t\t\tTotal cases in AHS group are",len(ahs))
    r1.close()
#4.5
def activezone():
    plist = []
    f =open ("caseactive.txt","r")
    for cnt in f:
        b = cnt.split("\t")
        status = b[2].strip("\n")
        if (status == "ACTIVE"):
            plist.append (int(b[0])) 
    table1 = []
    table2 = []
    table3 = []
    table4 = []
    for cnt2 in plist:
        if (cnt2%4==1):
            table1.append(cnt2)
        elif (cnt2%4==2):
            table2.append(cnt2)
        elif (cnt2%4==3):
            table3.append(cnt2)
        else:
            table4.append(cnt2)
    print("\n\n\t-----$$$ ACTIVE CASE AVAILABLE IN SPECIFIC ZONE $$$------")
    print ("\t\t  ACTIVE case in ZONE A",table1)
    print ("\t\t  ACTIVE case in ZONE B",table2)
    print ("\t\t  ACTIVE case in ZONE C",table3)
    print ("\t\t  ACTIVE case in ZONE D",table4)
    f.close()    
        
#4    
def additional ():
    cnt = 1
    while (cnt == 1):
        print ("\n")
        print("ˇ" * 70)
        print("Enter (0/1/2/3/4) to select system function\n0.Return to main option\n1.Total of Test(1,2,3) carried out\n2.Total patients tested\n"
              "3.Total recovered cases\n4.Total patients test positive for COVID-19 group wise\n5.Total active cases zone wise")
        print("ˇ" * 70)
        check = int(input("Please select your command :"))
        while (check >5 or check<0):
            print("\nInvalid value")
            check = int(input("Please insert your value again:"))
        if (check >= 0 and check <=5):
            if (check == 1):
                testoutput()
            elif (check == 2):
                patient()
            elif (check == 3):
                recovered()
            elif (check == 4):
                positive()
            elif (check == 5):
                activezone()
            elif (check == 0):
                function()
            else:
                cnt=1
        else:
            cnt=1
#5.1
def searchpt():
    ptnumber =int(input("Enter patient ID that you want to search:"))
    r=open("patient.txt","r")    
    for list1 in r:
        sp = list1.split("><")
        if (ptnumber == int(sp[0])):
            ptgroup = str(sp[3].strip("\n"))
            ptname = str(sp[1])
            ptcontact = str(sp[2])
            if (ptnumber%4==1):
                zone = str("zone A")
            elif (ptnumber%4==2):
                zone = str("zone B")
            elif (ptnumber%4==3):
                zone = str("zone C")
            else:
                zone = str("zone D")
            print ("Patient name is:",ptname,"\nPatient id is:",ptnumber,"\nPatient contact is:",ptcontact,"\nPatient group is:",ptgroup,"\nPatient zone is:",zone)
            flag = 0
            break
        else:
            flag = 1
    if (flag == 1):
        print ("Invalid input")
    r.close()
    if flag == 0:
        r3 = open ("negativecase1.txt","r")
        for cnt in r3:
            n1 = cnt.strip()
            if n1 == str(ptnumber):
                flag = 1
                break
        r3.close () 
        if (flag == 0):
            r1 = open ("positivecase.txt","r")
            for cnt in r1:
                b = cnt.split("\t")
                if b[0] == str(ptnumber):
                    print ("Patient is tested positive")
                    print ("Patient is Quarantine in :",b[1].strip())
                    r2 = open ("caseactive.txt","r")
                    for cnt2 in r2:
                        c = cnt2.split ("\t")
                        if c[1] == str(ptnumber):
                            print ("Patient case id is :",c[0])
                            print ("Patient status is :",c[2].strip())
                            r2.close()
                            flag=2
                            break

            r1.close()
        if flag == 2:
            add()
        if flag == 1:
            print ("This patient is tested negative")
            add()
    if flag == 0:
        print ("This patient havent go through any test")
            
#5.2
def searchcase():
    caseid = int(input("Enter Case ID:"))
    r = open ("caseactive.txt","r")
    for cnt in r:
        a = cnt.split ("\t")
        ptnumber = a[1]
        if str(caseid) == a[0].strip():
            print ("Caseid :",caseid,"\nPatient ID:",a[1],"\nStatus : ",a[2].strip())
            flag = 0
            break
        else:
            flag = 1
    if flag == 1:
        print ("Invalid input")
    r.close()

    r2 = open ("patient.txt","r")
    for cnt in r2:
        b = cnt.split ("><")
        if ptnumber == b[0]:
            ptnumber = int(ptnumber)
            ptgroup = str(b[3].strip("\n"))
            ptname = str(b[1])
            ptcontact = str(b[2])
            if (ptnumber%4==1):
                zone = str("zone A")
            elif (ptnumber%4==2):
                zone = str("zone B")
            elif (ptnumber%4==3):
                zone = str("zone C")
            else:
                zone = str("zone D")
            print ("Patient name is:",ptname,"\nPatient id is:",ptnumber,"\nPatient contact is:",ptcontact,"\nPatient group is:",ptgroup,"\nPatient zone is:",zone)
    r2.close()      
#5.3
def searchggcase():
    total = []
    r = open ("dead.txt","r")
    for cnt in r:
        total.append (cnt.strip())
    print ("\n\n\t\t-----$$$ TOTAL DECEASED CASE $$$------")
    print ("\t\t  Total case of DECEASED case is",len(total))
    r.close()
    r = open ("patient.txt","r")
    total.sort()
    for cnt in r:
        a = cnt.split ("><")
        for h in total:      
            if a[0]== h:
                ptnumber = int(a[0])
                if (ptnumber%4==1):
                    zone = str("zone A")
                elif (ptnumber%4==2):
                    zone = str("zone B")
                elif (ptnumber%4==3):
                    zone = str("zone C")
                else:
                    zone = str("zone D")
                print ("\n\tPatient name is",a[1])
                print ("\tPatient ID is",a[0])
                print ("\tPatient email/contact is",a[2])
                print ("\tPatient group is",a[3].strip(),"\n")
                print ("\tPatient zone is",zone)
                
    r.close()
    
#5
def add():
    cnt = 1
    while (cnt == 1):
        print ("\n")
        print("ˇ" * 70)
        print("Enter (0/1/2/3) to select system function\n0.Return to main option\n1.Searching patient detail by insert patient ID\n2.Searching patient detail by insert case ID\n"
              "3.Total deceased cases")
        print("ˇ" * 70)
        check = int(input("Please select your command :"))
        while (check >3 or check<0):
            print("\nInvalid value")
            check = int(input("Please insert your value again:"))
        if (check >= 0 and check <=3):
            if (check == 1):
                searchpt()
            elif (check == 2):
                searchcase()
            elif (check == 3):
                searchggcase()
            elif (check == 0):
                function()
            else:
                cnt=1
        else:
            cnt=1

def function():
    print("ˇ" * 70)
    print("Enter (1/2/3/4/5) to select system function\n1.Register new list of patient\n2.Upload test (1,2,3) result\n3.Edit patient status""\n4.Additional function (1)\n5.Additional function (2)",)
    print("ˇ" * 70)
    check = int(input("Please select your command :"))
    while (check >5 or check<1):
        print("\nInvalid value")
        check = int(input("Please insert your value again:"))
    if (check >= 1 and check <=5):
        if (check == 1):
            register()
        elif (check == 2):
            testinput()
        elif (check == 3):
            edit()
        elif (check == 4):
            additional()
        elif (check == 5):
            add()
        else:
            cnt=1
    else:
        cnt=1

function()








