# დავალება1) შექმენით სია, რომელშიც შეიტანთ რიცხვებს 0-იდან 20-ის ჩათვლით (ხელით ჩაწერეთ, ციკლის გარეშე), ბოლოს დაპრინტეთ მთლიანი სია.
# Create an array which will include numbers from 0 to 20 (write it manually, without loops), then print whole array.

# დავალება2) შექმენით ახალი სია, რომელშიც შეიტანთ ლუწ რიცხვებს წინა სიიდან. ბოლოს დაპრინტეთ ეს სია.
# Create a new array, which will include even numbers from the first array. Then print this new array.

# დავალება3) შექმენით ახალი სია, შემდეგ 50-იდან 100-მდე ამ სიაში შეიტანეთ ყველა რიცხვი (დასერჩეთ python array append). ბოლოს დაპტინტეთ თქვენთვის სასურველი სიის ნაწილი უარყოფითი index-ების საშუალებით.
# Create an array, then add numbers from 50 to 100 to it. In the end, print the part of this array with negatives indexes.

# დავალება4) მომხმარებელს შეეკითხეთ ორი მთელი რიცხვი, შემდეგ ამ ორი ცვლადიდან for ციკლში უმცირესი ჩასვის start-ის, ხოლო უდიდესი end-ის პოზიციაზე, step არ გინდათ. ახლა ჩაურთეთ if statement და დაპრინტეთ მარტო ხუთის ჯერადები.
# Ask user for two inputs and store them as variables, their type has to be int. Then use for loop, use lower number from this two variables as start, Higher number as end, you do not need step. After that, you'll have to use if statement to only print multiples of five.

# დეგ მომხმარებელს შეეკითხეთ მისი ასაკი და თუ ასაკი 18-ზე მეტი იქნება, შეეკითხეთ მას სახელი. მეორე ინფუთის შემდეგ სახელი შეიტანეთ სიაში და დაპრინტეთ ის.
# Create a new array. Ask user his/her age and if it will be over 18, ask him/her name. Then add this name to already created array and print it.დავალება5) შექმენით ახალი სია. შემimport array

# numbers_array = array.array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# print(numbers_array)


even_numbers_list = [x for x in numbers_list if x % 2 == 0]
print(even_numbers_list)

even_numbers_array = array.array('i', [x for x in numbers_array if x % 2 == 0])
print(even_numbers_array)

none=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(none)

even_numbers_array = ( [x for x in none if x % 2 == 0])
print(even_numbers_array)



nonep=[]
nonep.extend(range(50,101))
print(nonep[-6])

wow=int(input("enter first number:"))
none=int(input("enter second number:"))
ror=min(wow, none)
pop=max(wow, none)
for i in range(ror, pop+1):
    if i %5 ==0:
        print(i)

name=[]
uou=int(input("enter you age :"))
if uou > 18:
    user=input("what is your name : ?")
    name.append(user)
print("name", name)