from creat_subject import creatSubject
from subject_manager import manageSub
from subject_revise import reviseSubject

def Menu():

    print("\n-----------------------------------<교수메뉴>-----------------------------------")
    print("1 -- 과목개설")
    print("2 -- 개설과목 조회/철회")
    print("3 -- 개설과목 정보 수정")
    print("4 -- 로그아웃")
    print("--------------------------------------------------------------------------------")

def logout():
    print("\n로그아웃 합니다. 시작 화면으로 돌아갑니다.")
    print("================================================================================\n")

def professorManger(id):   
    while True:

        Menu()

        print("메뉴를 입력하시오 > ", end = "")
        select = input()

        if (select == "1"):
            creatSubject(id)

        elif (select == "2"):
            manageSub(id)

        elif (select == "3"):
            reviseSubject(id)
        
        elif (select == "4"):
            logout()
            return

        else:
            print("메뉴번호를 확인 후 다시 입력해 주세요.")
