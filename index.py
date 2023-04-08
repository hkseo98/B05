from login_function import login
from register_function import register

def main():
    isLoggedIn = False 
    isStudent = True
    while True:
        print()
        print("=================시작=================")
        print()
        print("<계정 기반 수강신청 프로그램>")
        print("1. 로그인")
        print("2. 회원가입")
        print("3. 종료")
        selectedMainMenu = input("> ")
        if selectedMainMenu == "1":
            # 로그인 시작
            isLogged, isStu = login()
            isLoggedIn = isLogged
            isStudent = isStu
            # 로그인 성공 시 
            if isLoggedIn:
                if isStudent:
                    print("학생사용자 로그인 완료")
                    # 학생 사용자 로그인 이후 단계로 이동
                    return
                else:
                    print("교수사용자 로그인 완료")
                    # 교수 사용자 로그인 이후 단계로 이동
                    return
        elif selectedMainMenu == "2":
            # 회원가입 시작
            print("회원가입")
            register()
        elif selectedMainMenu == "3":
            # 종료
            print("프로그램을 종료합니다.")
            break
        else:
            print("문법에 맞지 않습니다. 다시 입력해주세요.")

            
main()



        