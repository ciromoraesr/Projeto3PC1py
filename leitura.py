with open('usuarios.txt') as f:
    users = f.readlines()
with open('senhas.txt') as c:
    passwds = c.readlines()
class Usuario():
    def __init__(self, name, birth, login, passwd, lchange):
        self.name = name
        self.birth = birth
        self.login = login
        self.passwd = passwd
        self.lchange = lchange

countusers = 0
countpassswd = len(passwds)
for i in range(len(users)):
    if (users[i] == '---\n'):
        countusers = countusers + 1
        
users_list = []
for a in users:
    a.replace("\n","")
for i in range(0, countusers*5, 6):
    user_instance = Usuario(users[i+0], users[i+1], users[i+2], users[i+3], users[i+4])
    
    users_list.append(user_instance)
print(users_list)


    