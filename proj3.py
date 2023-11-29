import hashlib



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
class Quebrado():
    def __init__(self, login, senha, nome, data):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.data = data
#%%
countusers = 0
countpasswd = len(passwds)
for i in range(len(users)):
    if (users[i] == '---\n'):
        countusers = countusers + 1
        
users_list = []


for i in range(len(users)-1):
    first_user = users[i]


    if len(first_user) > 0:
        
        modified_user = first_user[:-1]

        
        users[i] = modified_user
newusers = []
for i in range(len(users)):
    if(users[i] != '---'):
        newusers.append(users[i])

for i in range(0, len(newusers), 5):
    useri = Usuario(newusers[i+0], newusers[i+1], newusers[i+2], newusers[i+3], newusers[i+4])
    users_list.append(useri)
    
#%%
for i in range(len(passwds)-1):
    fs = passwds[i]
    if len(fs) > 0:
        mod = fs[:-1]
        passwds[i] = mod

hashs = []

for i in range(countpasswd):
    hashs.append(hashlib.sha256(passwds[i].encode()).hexdigest())

#%%
final = []
relcount = 0


for i in range(countusers + 1):
    for j in range(countpasswd ):
        if(users_list[i].passwd == hashs[j]):
            relcount = relcount + 1
            rel = Quebrado(users_list[i].login, passwds[j], users_list[i].name, users_list[i].birth)
            final.append(rel)

#%%
with open('final.txt', 'w') as f:
    for i in range(relcount):
        f.write(final[i].login)
        f.write('\n')
        f.write(final[i].senha)
        f.write('\n')
        f.write(final[i].nome)
        f.write('\n')
        f.write(final[i].data)
        f.write('\n')
        f.write('---')
        if i != relcount - 1:
            f.write('\n')
