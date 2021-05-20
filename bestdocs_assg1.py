import requests
import json
import schedule
import time
import mysql.connector
# ******** collecting from database******
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="bestdoc")
mycursor=mydb.cursor()

def check_word(word,negative_words,positive_words):
    for i in range(len(negative_words)):
        if negative_words[i] in word:
            return "negative"
    for i in range(len(positive_words)):
        if positive_words[i] in word:
            return "positive"

questions=[
    "Did you get a room of your requirements?",
    "How well were your queries addressed at the admission center?",
    "How properly were you explained about the treatment and its corresponding expenses?",
    "How would you rate the waiting time for admission process?",
    "Any Comments (Admission Process):",
    "How well were you informed about the treatment and medication?",
    "How would you rate the promptness and responses in the services?",
    "How would you rate the courtesy of the staff in attending to your queries?",
    "Any Comments (Nursing Care):",
    "Did the doctor visit you daily and on time?",
    "How well did the doctor explain the diagnosis and treatment?",
    "How would you assess the care and promptness of doctors in attending to your queries?",
    "Any Comments (Doctor): ",
    "How well was your room cleaned and maintained?",
    "How was your room environment for a peaceful stay?",
    "How was the facility in the room and Hospital?",
    "How was the quality of the food served?",
    "Any comments (Facility):",
    "How promptly were you given the discharge bill?",
    "Were your bills transparent and easily understandable?",
    "Were you able to pay your bills easily?",
    "Were you given the discharge summary and discharge medication in a timely manner?",
    "How well were your insurance claims handled?",
    "Any comments (Billing & Discharge):",
    "Admitted from:",
    "How likely are you to choose this hospital for your care again?",
    "How likely is it that you would recommend this hospital to others?",
    "Wish to compliment any staff for their outstanding care?"
]

negative_words=["not good","bad experience","never recommend","worst experience","not good for women","not clean","untidy","not well responded"]
positive_words=["[very good","good experience","i would recommend","best experience","good for females","cleaniness","well responding"]
print(len(questions))

# hospitals=["sunshine","mydoctor","image","yashoda","medicover","doctor.com","archana"]
# areas=["kozhikode","miyapur","lingampally","munnar","calicut","kochi","medhipatnam"]

print("1. Rate    2.Looking for doctor\n")
option=int(input("Option: "))
administration=[]
nursing=[]
doctor=[]
facility=[]
bd=[]
services=[]
if option==2:
    area=input("In which area are you looking for hospital: ")
    sql="select name from hospital_rating where area=%s group by area order by doctor desc,bd desc,services desc,nursing desc,administration desc"
    name=(area,)
    mycursor.execute(sql,name)
    result=mycursor.fetchall()
    try:
        hospital_name=result[0][0]
        print()
        print(hospital_name+" hospital is the best for you in the area which you are looking for")
    except:
        print("Sorry No hospital's in the area you are looking for")
else:
    hospital=input("hospital name: ")
    sql="select id from hospital_details where name=%s"
    name=(hospital,)
    mycursor.execute(sql,name)
    result=mycursor.fetchall()
    id=result[0][0]

    for i in range(len(questions)):
        if i<=4:
            if i!=0 and i!=4:
                administration.append(int(input(questions[i])))
            else:
                administration.append(input(questions[i]))
        elif i<=8:
            if i==8:
                nursing.append(input(questions[i]))
            else:
                nursing.append(int(input(questions[i])))
        elif i<=12:
            if i==9 or i==12:
                print("mawa")
                doctor.append(input(questions[i]))
            else:
                doctor.append(int(input(questions[i])))
        elif i<=17:
            if i==17:
                facility.append(input(questions[i]))
            else:
                facility.append(int(input(questions[i])))
        elif i<=23:
            if i==23:
                bd.append(input(questions[i]))
            else:
                bd.append(int(input(questions[i])))
        elif i<=27:
            if i==27:
                services.append(input(questions[i]))
            else:
                services.append(int(input(questions[i])))

    if check_word(administration[4],negative_words,positive_words)=="negative":
        administration[4]=-1
    else:
        administration[4]=1
    if administration[0]=='yes':
        administration[0]=1
    else:
        administration[0]=-1

    if check_word(nursing[3],negative_words,positive_words)=="negative":
        nursing[3]=-1
    else:
        nursing[3]=1

    if check_word(doctor[3],negative_words,positive_words)=="negative":
        doctor[3]=-1
    else:
        doctor[3]=1
    if doctor[0]=='yes':
        doctor[0]=1
    else:
        doctor[0]=-1



    if check_word(facility[4],negative_words,positive_words)=="negative":
        facility[4]=-1
    else:
        facility[4]=1

    if check_word(bd[5],negative_words,positive_words)=="negative":
        bd[5]=-1
    else:
        bd[5]=1

    if check_word(services[3],negative_words,positive_words)=="negative":
        services[3]=-1
    else:
        services[3]=1

    ############## administration UPDATE ######################
    sql="select * from hospital_rating_administration where id=%s"
    name=(int(id),)
    mycursor.execute(sql,name)
    result=mycursor.fetchall()
    # print(result)
    var1=result[0][1]+administration[0]
    var2=float((result[0][2]+administration[1])/2)
    var3=float((result[0][3]+administration[2])/2)
    var4=float((result[0][4]+administration[3])/2)
    var5=result[0][5]+administration[4]

    sql="update hospital_rating_administration set question1=%s,question2=%s,question3=%s,question4=%s,question5=%s where id=%s"
    name=(var1,var2,var3,var4,var5,id,)
    mycursor.execute(sql,name)
    mydb.commit()

    sql="update hospital_rating set administration=%s where id=%s"
    name=(var1+var2+var3+var4+var5,id,)
    mycursor.execute(sql,name)
    mydb.commit()


    ############## nursing UPDATE ######################
    sql="select * from hospital_rating_nursing where id=%s"
    name=(int(id),)
    mycursor.execute(sql,name)
    result=mycursor.fetchall()
    # print(result)
    var1=float((result[0][1]+nursing[0])/2)
    var2=float((result[0][2]+nursing[1])/2)
    var3=float((result[0][3]+nursing[2])/2)
    var4=result[0][4]+nursing[3]

    sql="update hospital_rating_nursing set question1=%s,question2=%s,question3=%s,question4=%s where id=%s"
    name=(var1,var2,var3,var4,id,)
    mycursor.execute(sql,name)
    mydb.commit()

    sql="update hospital_rating set nursing=%s where id=%s"
    name=(var1+var2+var3+var4,id,)
    mycursor.execute(sql,name)
    mydb.commit()

    ############## BILLING UPDATE ######################
    sql="select * from hospital_rating_bd where id=%s"
    name=(int(id),)
    mycursor.execute(sql,name)
    result=mycursor.fetchall()
    # print(result)
    var1=float((result[0][1]+bd[0])/2)
    var2=float((result[0][2]+bd[1])/2)
    var3=float((result[0][3]+bd[2])/2)
    var4=float((result[0][4]+bd[3])/2)
    var5=float((result[0][5]+bd[4])/2)
    var6=result[0][6]+bd[5]


    sql="update hospital_rating_bd set question1=%s,question2=%s,question3=%s,question4=%s,question5=%s,question6=%s where id=%s"
    name=(var1,var2,var3,var4,var5,var6,id,)
    mycursor.execute(sql,name)
    mydb.commit()

    sql="update hospital_rating set bd=%s where id=%s"
    name=(var1+var2+var3+var4+var5+var6,id,)
    mycursor.execute(sql,name)
    mydb.commit()

    ############## services UPDATE ######################
    sql="select * from hospital_rating_services where id=%s"
    name=(int(id),)
    mycursor.execute(sql,name)
    result=mycursor.fetchall()
    # print(result)
    var1=float((result[0][1]+services[0])/2)
    var2=float((result[0][2]+services[1])/2)
    var3=float((result[0][3]+services[2])/2)
    var4=result[0][4]+services[3]

    sql="update hospital_rating_services set question1=%s,question2=%s,question3=%s,question4=%s where id=%s"
    name=(var1,var2,var3,var4,id,)
    mycursor.execute(sql,name)
    mydb.commit()

    sql="update hospital_rating set services=%s where id=%s"
    name=(var1+var2+var3+var4,id,)
    mycursor.execute(sql,name)
    mydb.commit()

    ############## Facility UPDATE ######################
    sql="select * from hospital_rating_facility where id=%s"
    name=(int(id),)
    mycursor.execute(sql,name)
    result=mycursor.fetchall()
    # print(result)
    var1=float((result[0][1]+facility[0]/2))
    var2=float((result[0][2]+facility[1])/2)
    var3=float((result[0][3]+facility[2])/2)
    var4=float((result[0][4]+facility[3])/2)
    var5=result[0][5]+facility[4]

    sql="update hospital_rating_facility set question1=%s,question2=%s,question3=%s,question4=%s,question5=%s where id=%s"
    name=(var1,var2,var3,var4,var5,id,)
    mycursor.execute(sql,name)
    mydb.commit()

    sql="update hospital_rating set facility=%s where id=%s"
    name=(var1+var2+var3+var4+var5,id,)
    mycursor.execute(sql,name)
    mydb.commit()

    ############## doctor UPDATE ######################
    sql="select * from hospital_rating_doctor where id=%s"
    name=(int(id),)
    mycursor.execute(sql,name)
    result=mycursor.fetchall()
    # print(result)
    var1=(result[0][1]+doctor[0])/2
    var2=float((result[0][2]+doctor[1])/2)
    var3=float((result[0][3]+doctor[2])/2)
    var4=result[0][4]+doctor[3]

    sql="update hospital_rating_doctor set question1=%s,question2=%s,question3=%s,question4=%s where id=%s"
    name=(var1,var2,var3,var4,id,)
    mycursor.execute(sql,name)
    mydb.commit()

    sql="update hospital_rating set doctor=%s where id=%s"
    name=(var1+var2+var3+var4,id,)
    mycursor.execute(sql,name)
    mydb.commit()
