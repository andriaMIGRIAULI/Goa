# დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვს (გამოიყენეთ შეყვანა). თუ რიცხვი ლუწია, დაბეჭდეთ ეს რიცხვი ლუწი. წინააღმდეგ შემთხვევაში დაბეჭდეთ ეს რიცხვი არ არის ლუწი, ასევე დაბეჭდეთ შემდეგი ლუწი რიცხვი, მაგალითად, თუ შეყვანილია 15, დაბეჭდეთ 16.

# შექმენით while loop, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. განაგრძეთ კითხვა, სანამ არ შეიყვანენ სწორ პაროლს "Goa best". ასევე დაბეჭდეთ არასწორი პაროლების რაოდენობა.

# დაწერეთ ალგორითმი, რომელიც იღებს სტრიქონს შეყვანად და აბრუნებს True-ს, თუ ამ სტრიქონის პირველი სიმბოლოა "G".

# სთხოვეთ მომხმარებელს ხუთი სახელი (გამოიყენეთ შეყვანა ხუთჯერ). დაამატეთ ყველა მათგანი ერთ სიაში და დაბეჭდეთ მხოლოდ პირველი სამი სახელი.

# დაწერეთ ალგორითმი, რომელიც ამოწმებს, არის თუ არა მოცემული რიცხვი მარტივი (პირველ რიცხვს აქვს მხოლოდ ორი გამყოფი) გამოიყენეთ for loop ამ ამოცანისთვის.

# შექმენით while მარყუჟი, რომელიც ბეჭდავს ციფრებს 10-დან 0-მდე (10-დან 0-მდე).

# დანერგეთ მარტივი კალკულატორი, რომელიც იღებს ორ რიცხვს და ოპერატორს (+, რც შეყვან-, *, /), როგოის მომხმარებლისგან და ასრულებს შესაბამის ოპერაციას. ბონუს დავალება თუ გინდა, არ არის საჭირო - დაამატეთ ხარისხი, გამოიყენეთ ** ოპერატორი ამისთვის.

# სთხოვეთ მომხმარებელს შეიყვანოს სახელი და დაბეჭდოს ამ სტრიქონის ბოლო სიმბოლო.

# loop-ის გამოყენებით, სთხოვეთ მომხმარებელს ნომერი. შემდეგ შექმენით სია, რომელსაც ექნება ლუწი რიცხვები შემდეგ დიაპაზონში: 0-დან მომხმარებლის ნომრამდე. და ბოლოს, ამობეჭდეთ მთელი სია.

# სთხოვეთ მომხმარებელს მთელი ნომერი. შემდეგ შექმენით ფაქტორიალი ამ რიცხვისთვის და ამობეჭდეთ (თუ არ იცით რა არის ფაქტორიალი, დაგუგლდით).



# none=int(input("enter number :"))
#     if i %2 ==0:
#         print("even")
# else:
#     print("odd")



# pasword="goa best"
# attempt=0
# while True: 
#     andria=input("enter your pasword:")
#     if andria== pasword:
#         print("pasword matched")
#         break
#     else:
#         print("incorrect pasword")
#         attempt+=1
#         if attempt >= 5:
#             print("password attempts was reached")
#             break
# print("number of failed attempts:", attempt)



# def byge(string):
#     if string[0]=="G":
#         return True
#     else:
#         return False
    

# tot=input("enter string:")
# none=byge(tot)
# print(none)




# names=[]
# for i in range(5):
#     name=input("enter your name :")
#     names.append(name)
# print("enter your first 3 names :")
# for name in names[:3]:
#     print(name)




# def none(num):
#     if num < 2:
#         return False
#     for i in range(2, num // 2+1):
#         if num % i==0:
#             return False
#     return True
# number=int(input("enter number :"))
# if none(number):
#     print("this is simple number :", number)
# else:
#     print("this is not simple number", number)


# none=10
# while none >= 0:
#     print(none)
#     none-=1


def calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, , /, **): ")
    num2 = float(input("Enter the second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero."
    elif operator == '':
        result = num1 ** num2
    else:
        return "Invalid operator."

    return result

print("Result:", calculator())


# name=input("what is your name :")
# if len(name)>0:
#     print(name[-1])





# number=int(input("what is your number :"))
# even_number=[]
# for num in range(number + 1):
#     if num %2 == 0:
#         even_number. append(num)
# print(number, even_number)



# def none(num):
#     if num == 0:
#         return 1
#     else:
#         result=1
#         for i in range(1, num+ 1):
#             result *= i
#         return result
# nonu=int(input("enter number :"))   
# result=none(nonu)
# print(nonu, result)




def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number = int(input("Enter a whole number: "))

result = factorial(number)

print("Factorial of", number, "is", result)
