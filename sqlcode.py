import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="naman",
    passwd="naman",
    database='mydatabase'
)
mycursor = mydb.cursor()
sql = "create table questions (question_id INT PRIMARY KEY, author VARCHAR(255))"
sql2 = "create table options (options_id INT PRIMARY KEY ,  option1 VARCHAR(255), option2 VARCHAR(255), option3 VARCHAR(255), option4 VARCHAR(255),answer VARCHAR(255))"


def q_o_insert(qid, auth, op1, op2, op3, op4, ans):
    sql_insert_q = f'insert into questions(question_id,author) values(%s,%s)'
    sql_insert_o = f'insert into options(options_id,option1,option2,option3,option4,answer) values(%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql_insert_o, (qid, op1, op2, op3, op4, ans))
    print("1 record inserted, ID:", mycursor.lastrowid)

    mycursor.execute(sql_insert_q, (qid, auth))
    print("1 record inserted, ID:", mycursor.lastrowid)
    mydb.commit()
