import instaloader
X = '\033[1;33m'
F = '\033[2;32m'
C = '\033[2;35m'
B = '\033[2;36m'
st=0
username=input(f'{X}[+]{C} -{F} ادخل يوزر حسابك  :{F} ')
password=input(f'{X}[+]{C} -{F} ادخل باسورد حسابك  :{F} ')
targe=input(f' {X}ادخل يوزر الي تريد تسوي لسته يوزرات منه للفحص :{B} ')
L = instaloader.Instaloader()
L.login(username,password)
profile = instaloader.Profile.from_username(L.context, targe)
follow_list = []
for i in profile.get_followers():
 user=str(i)
 use= user.split('<Profile ')[1].split('(')[0]
 st+=1
 print(f'''{X} 𓊆 {st} 𓊇 {F}{use}''')
 use2=use+'@gmail.com'
 username=use2.replace(" ","")
 file = open("username.txt","a+")
 file.write(username)
 file.write("\n")
 file.close()