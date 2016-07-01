"""
main executable module

_ini 앞에 언더바는 내부에서 사용하는 함수라는 뜻으로 사용된다.
"""
from model.contact import Contact
import service.contact_service as svc

import sqlite3

def main():
    create_talble_query = \
        'create table contact(name text, hpnum text, email text, age int);'
    insert_query = "insert into contact values (?,?,?,?)"
    #1. establich connection
    con = sqlite3.connect('contact.db')
    #2. get cursor form the db
    cur = con.cursor()
    #3. send SQL the to db from cursor
    cur.execute('selet * from contact')
    a_record = cur.fetchone()
    prin(a_record[0])
    #4. transaction
    con.commit()
    #5.release resource
    con.close()

#def _init_contact():
#    f = open("contact.dat","w")
#    f.close()
"""
def main():
 #   _init_contact()

    #주소 객체 생성
    #c = Contact('park', '000000000', 'ds@kt.co.kr', 'seoul')
    #svc.regist_contact(c)

    #print('주소 등록 성공')

    list = svc.view_all_contact()
    print(list)
"""

# 아래 코드는 모듈 제일 마지막에 위치한다
if __name__ == "__main__":
    main()