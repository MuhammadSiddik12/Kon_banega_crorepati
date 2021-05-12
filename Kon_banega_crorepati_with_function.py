print("Welcome To you in KBC, \nLets Start The Game...\n")
questions=[
    "How many continents in the world?",
    "Which day is observed as the world standard day?",
    "Who is the author of the epic 'Magdoot'?",             # Questions
    "September 27 is celebrated every year as?",
    "How many planets are there in our solar system?",
    "Who is the president of America?",
    "Where is the Navgurukul's girls campus in India?",]
options=[
    ["1","5","4","7","50:50"],
    ["June 26","Oct 14","Nov 15","Dec 2","50:50"],
    ["Vamlmiki","Banabhata","Kalidas","Vishal","50:50"],            # Options
    ["Teacher,s Day","Natinal Integretion Day","World Tourism Day","International Day","50:50"],
    ["5","8","9","6","50:50"],
    ["Joe Biden","Donald Trump","Emmanuel Macron","Barack Obama","50:50"],
    ["Pune","Banglore","Delhi","Gurugram","50:50"],]
solutions=[4,2,3,3,2,1,2]           # solutions
solution_for_50_50=[[2,4],[2,3],[2,3],[3,1],[4,2],[1,4],[2,1]]  # solution for 50 50 option

def kbc_body(questions,options,solutions,solution_for_50_50):
    total_score,total_lose,n,k,d=0,0,0,1,0
    for i in questions:
        print(i)
        print("Here Is Your Options...")
        for i in options[n]:
            if k==6: k=1
            print(k,':', i)     
            k+=1
        inp=int(input("Choose The Correct Answer:"))
        if inp==solutions[n]: 
            print("Congratulation! You Won\n")     # condition for checking user put right nswer or not
            total_score+=1
        elif inp==5:
            if d==1: print("Sorry!! You Already Choosed This option\n")
            else:
                for i in range(1): print("option Number", solution_for_50_50[n])
                inp=int(input("Enter Your Option Number:"))
                if inp==solutions[n]:                           # condition 50 50 option
                    print("Congratulation! You Won Again\n")
                    total_score+=1
                    d+=1
                else:
                    print("Your Answer Is Wrong.\n")
                    total_lose+=1
        else:
            print("Your Answer Is Wrong.\n")
            total_lose+=1
        n+=1
    print(total_score,"Correct answer")
    print(total_lose,"Wrong answer")
kbc_body(questions,options,solutions,solution_for_50_50)