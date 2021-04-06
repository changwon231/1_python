def profile(name, age, main_lang):
    print(name, age, main_lang)
# 변수가 지정이 되면 순서가 꼬여 있어도 함수 호출이 된다.
profile(name="유재석", main_lang="파이썬", age=20)
profile(age=10, main_lang = "자바", name = "김태호")
