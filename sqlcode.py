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
    sql_get_subs = 'select * from (questions,answers) where questions.question_id=answers.question_id and answers.type="subjective" and marks is NULL'
    mycursor.execute(sql_get_subs)
    for i in mycursor.fetchall():
        print(i)
    mycursor.execute(sql_get_subs)
    return mycursor.fetchall()


def get_all_students():
    sql_get_students = 'select distinct(answerer) from answers'
    mycursor.execute(sql_get_students)
    for i in mycursor.fetchall():
        print(i)
    mycursor.execute(sql_get_students)
    return mycursor.fetchall()


def get_student_marks(stud):
    sql_get_student_marks = 'select SUM(marks) from answers where answerer = %s'
    mycursor.execute(sql_get_student_marks, (stud,))
    return mycursor.fetchone()


def get_student_qs(stud):
    sql_get_student_qs = 'select Distinct(question) from answers,questions where answers.answerer = %s and answers.question_id=questions.question_id'
    mycursor.execute(sql_get_student_qs, (stud,))
    return mycursor.fetchall()


def set_answerer(answerer):
    sqlmake = 'insert into answerers (answerer) Select %s Where not exists(select * from answerers where answerer=%s)'
    mycursor.execute(sqlmake, (answerer, answerer))
    mydb.commit()


def set_answerer(answerer):
    sqlmake = 'insert into answerers (answerer) Select %s Where not exists(select * from answerers where answerer=%s)'
    mycursor.execute(sqlmake, (answerer, answerer))
    mydb.commit()


def set_setter(setter):
    sqlmake = 'insert into setters (setter) Select %s Where not exists(select * from setters where setter=%s)'
    mycursor.execute(sqlmake, (setter, setter))
    mydb.commit()


def set_evaluator(evaluator):
    sqlmake = 'insert into evaluators (evaluator) Select %s Where not exists(select * from evaluators where evaluator=%s)'
    mycursor.execute(sqlmake, (evaluator, evaluator))
    mydb.commit()


print(get_student_qs('rodeo'))
set_setter('rodeo')
