from login_function import login
from register_function import register
from professor_management import professorManger
from student_management import studentmanager

def main():
    isLoggedIn = False 
    isStudent = True
    
    print("\n=====================================<시작>=====================================")
    print("                           계정 기반 수강신청 프로그램")
    print("================================================================================\n")
    
    while True:
        print("\n-----------------------------------<메인메뉴>-----------------------------------")
        print("1 -- 로그인")
        print("2 -- 회원가입")
        print("3 -- 종료")
        print("--------------------------------------------------------------------------------")

        selectedMainMenu = input("메뉴를 입력하시오 > ")

        if selectedMainMenu == "1":
            # 로그인 시작
            isLogged, isStu, id = login()
            isLoggedIn = isLogged
            isStudent = isStu
            # 로그인 성공 시 
            if isLoggedIn:
                if isStudent:
                    print("학생사용자 로그인 완료")
                    studentmanager(id)
                    continue
                
                else:
                    print("교수사용자 로그인 완료")
                    professorManger(id)
                    continue
                    
        elif selectedMainMenu == "2":
            # 회원가입 시작
            register()

        elif selectedMainMenu == "3":
            # 종료
            print("프로그램을 종료합니다.")
            break
        else:
            print("문법에 맞지 않습니다. 다시 입력해주세요.")

            
main()



        