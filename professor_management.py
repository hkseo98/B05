from creat_subject import creatSubject
from subject_manager import manageSub

def Menu():

    print("--------------------------------------------------")
    print("1 -- 과목 개설")
    print("2 -- 개설 과목 조회/철회")
    print("3 -- 로그아웃")
    print("--------------------------------------------------")

def logout():
    print("로그아웃 합니다.\n곧 로그인 화면으로 돌아갑니다.")

def professorManger(id):   
    while True:

        Menu()

        print("메뉴를 입력하시오: ", end = "")
        select = input()

        if (select == "1"):
            creatSubject(id)

        elif (select == "2"):
            manageSub(id)

        elif (select == "3"):
            logout()
            return 

        else:
            print("메뉴번호를 확인 후 다시 입력해 주세요.")
