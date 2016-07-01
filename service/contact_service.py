"""
이 모듈은 실행 모듈이 아니다

"""
def regist_contact(contact):
    """
    contact.dat 로 주소록을 관리한다.
    :param contact:
    :return:
    """
    #contact 객체를 스트링으로 변환
    # kim;010-0000-0000;em@nate.com;seoul 변환해서  contact.dat 반환
    contect_str = contact.to_string()
    with open('contact.dat','a') as f:
        f.write(contect_str + '\n')


def view_all_contact():
    """
    전체 주소록을 보여주는 것 배열 형식으로 넘김
    데이터를 라인 바이 라인으로 읽어서 리스트로 넘김다.
    [
        {
            "name" = name,
            "hpnum" = hpnum,
            "email" = email,
            "addr" = addr
        },
        {
            ...
        }
    ]
    :return: []
    """
    contact_list = []

    with open('contact.dat', 'r') as f:
        while True:
            line = f.readline()
            if not line: break;
            a_dic = _to_dic(line)
            contact_list.append(a_dic)

    return contact_list

def _to_dic(line):
    line = line[:-1] #맨마지막 \n 제거
    dic = {}
    list = line.split(';')

    dic['name']  = list[0]
    dic['hpnum'] = list[1]
    dic['email'] = list[2]
    dic['city']  = list[3]

    return dic



def modify_contact(contact):
    pass

def remove_contact(name):
    pass

def search_contact(name):
    pass


#이 코드는 제일 마지막에 위치한다
if __name__ =="__main__":
    print("실행 모듈이 아닙니다.")