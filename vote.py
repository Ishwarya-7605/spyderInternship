def vote():
    print("welcome to voting booth")
    TVK_count=0
    DMK_count=0
    ADMK_count=0
    NTK_count=0
    NOTA_count=0
    while True:
        print("do you have a veter id?(yes/no)")
        voter_id=input("enter your answer")
        if voter_id=="yes":
            print("show list of candidates \n1.TVK \n2.DMK \n3.ADMK \n4.NTK \n5.NOTA \n6.exit")
            choice=int(input("enter your candidates:"))
            if choice==1:
                print("voted successfully")
                TVK_count+=1
            elif choice==2:
                print("voted successfully")
                DMK_count+=1
            elif choice==3:
                print("voted successfully")
                ADMK_count+=1
            elif choice==4:
                print("voted successfully")
                NTK_count+=1
            elif choice==5:
                print("voted successfully")
                NOTA_count+=1
            elif choice==6:
                print("count the tvk votes:",TVK_count)
                print("count the  dmk votes:",DMK_count)
                print("count the admk votes:",ADMK_count)
                print("count the ntk votes:",NTK_count)
                print("count the nota votes:",NOTA_count)
                exit(0)
    else:
        print("not eligible to vote, bring your voter_id")        
vote()        
