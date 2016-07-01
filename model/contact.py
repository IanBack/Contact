"""
이 모듈은 실행 모듈이 아니다
 Line 11 : 클래스 안에 함수를 만들때는 반드시 self 가 들어가야 한다
 Lint 13 : 개행을 할때는 위에 \ 를 붙여준다
"""
class Contact(object):
    def __init__(self, name, hpnum, email, addr):
        self.name = name
        self.hpnum = hpnum
        self.email = email
        self.addr = addr

    def to_string(self):
        return  self.name + ";" + self.hpnum + ";" \
                + self.email+ ";" + self.addr

#이 코드는 제일 마지막에 위치한다
if __name__ =="__main__":
    print("실행 모듈이 아닙니다.")