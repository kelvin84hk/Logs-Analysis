#!/usr/bin/env python
import psycopg2

q1 = "What are the most popular three articles of all time?"
q2 = "Who are the most popular article authors of all time?"
q3 = "On which days did more than 1% of requests lead to errors?"
dbname = "dbname=news"


def loadSQL(q):
    try:
        db = psycopg2.connect(dbname)
    except psycopg2.Error:
        print psycopg2.Error.pgerror
        return None
    c = db.cursor()
    c.execute(q)
    d = c.fetchall()
    db.close()
    return d


def load_q1():
    sql = "select articles.title, article_view.view_num from articles "
    sql += "right join (select substr(path,10) "
    sql += "as slug,count(path) as view_num "
    sql += "from log where path like '%article%' group by slug order by "
    sql += "view_num desc limit 3) as article_view "
    sql += "on articles.slug = article_view.slug "
    sql += "order by article_view.view_num desc;"
    data = loadSQL(sql)
    print(q1)
    print('\n')
    print('1. "' + data[0][0] + '" with ' + str(data[0][1]) + ' views')
    print('2. "' + data[1][0] + '" with ' + str(data[1][1]) + ' views')
    print('3. "' + data[2][0] + '" with ' + str(data[2][1]) + ' views')
    print('\n')


def load_q2():
    sql = "select author_view.name as names, "
    sql += "count(author_view.name) as num from "
    sql += "(select authors.name , articles.slug "
    sql += "from authors right join articles on "
    sql += "authors.id = articles.author) as author_view "
    sql += "join (select substr(path,10) as slug "
    sql += "from log where path like '%article%') as article_view "
    sql += "on author_view.slug = article_view.slug "
    sql += "group by names order by num desc;"
    data = loadSQL(sql)
    print(q2)
    print('\n')
    for i in range(len(data)):
        print(str(i + 1) + '. "' + data[i][0] +
              '" with ' + str(data[i][1]) + ' views')
    print('\n')


def load_q3():
    sql = "select stats.d,100.0*stats.e/stats.c as error "
    sql += "from (select distinct date(time) as d, "
    sql += "sum(case when status like '4%' "
    sql += "or status like '5%' then 1 else 0 end) as e, "
    sql += "count(status) as c from log group by d ) as stats "
    sql += "where 100.0*stats.e/stats.c >1.0;"
    data = loadSQL(sql)
    print(q3)
    print('\n')
    for i in range(len(data)):
        print(str(i + 1) + '. ' + data[i][0].strftime('%b/%d/%Y') +
              ' with ' + str(round(data[i][1], 2)) + '% error')
    print('\n')


if __name__ == '__main__':
    load_q1()
    load_q2()
    load_q3()
