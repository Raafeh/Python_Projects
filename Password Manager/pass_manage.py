
from cryptography.fernet import Fernet


# def write_key():
#     key= Fernet.generate_key()
#     with open('key.key','wb') as key_file:
#         key_file.write(key)
# write_key()

def load_key():
    file= open('key.key','rb')
    key= file.read()
    file.close()
    return key

m_pwd=input('What is the master password? :')

key =load_key() + m_pwd.encode() 
fer=Fernet(key)

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user , password = data.split('|')
            psw=password.encode()
            print("User: ",user,"| Password :",fer.decrypt(psw).decode())

def add():
    name= input('Account Name: ')
    pwd= input('Password : ')

    with open('passwords.txt','a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() +'\n')



while True:
    mode= input("Would you like to view existing password or add a new password (view,add),press q to quit!").lower()
    if mode=='q':
        break
    if mode=='view':
        view()
    elif mode=='add':
        add()
    else:
        print('Invalid Mode!')
        continue 

