import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="naman",
    passwd="naman",
    database='mydatabase'
)
mycursor = mydb.cursor()


def q_o_insert_mcq(qid, auth, op1, op2, op3, op4, ans, q):
    sql_insert_q = 'insert into questions(question_id,author,type,question) values(%s,%s,%s,%s)'
    sql_insert_o = 'insert into options(options_id,option1,option2,option3,option4,answer) values(%s,%s,%s,%s,%s,%s)'

    mycursor.execute(sql_insert_q, (qid, auth, "mcq", q))
    mycursor.execute(sql_insert_o, (qid, op1, op2, op3, op4, ans))

    mydb.commit()


def q_o_insert_sub(qid, auth, q):
    sql_insert_q = 'insert into questions(question_id,author,type,question) values(%s,%s,%s,%s)'
    mycursor.execute(sql_insert_q, (qid, auth, "subjective", q))
    mydb.commit()


def get_mcqs():
    sql_get_mcqs = "select * from (questions join options on question_id = options_id) where type = 'mcq'"
    mycursor.execute(sql_get_mcqs)
    for i in mycursor.fetchall():
        print(i)
    mycursor.execute(sql_get_mcqs)
    return mycursor.fetchall()


def get_subs():
    sql_get_subs = 'select * from questions where type = "subjective"'
    mycursor.execute(sql_get_subs)
    for i in mycursor.fetchall():
        print(i)
    mycursor.execute(sql_get_subs)
    return mycursor.fetchall()


def sub_ans_sub(qid, answerer, ans):
    sql_insert_ans = 'insert into answers(question_id,answerer,answer,type) values(%s,%s,%s,%s)'
    mycursor.execute(sql_insert_ans, (qid, answerer, ans, "subjective"))
    mydb.commit()


def sub_ans_mcq(qid, answerer, ans, marks):
    sql_insert_ans = 'insert into answers(question_id,answerer,answer,type,marks) values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql_insert_ans, (qid, answerer, ans, "mcq", marks))
    mydb.commit()


def add_marks_for_sub(aid, qid, evaluator, marks):
    sql_update = 'Update answers set marks=%s,evaluator=%s where ans_id=%s'
    data = [marks, evaluator, aid]
    mycursor.execute(sql_update, data)
    mydb.commit()


def get_subs_toeval():
    sql_get_subs = 'select * from (questions,answers) where questions.question_id=answers.question_id and answers.type="subjective" and marks =0'
    mycursor.execute(sql_get_subs)
    for i in mycursor.fetchall():
        print(i)
    mycursor.execute(sql_get_subs)
    return mycursor.fetchall()


get_subs_toeval()
