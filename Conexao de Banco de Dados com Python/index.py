#IMPORTAR AS BIBLIOTECAS
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import databases

# CONFIGURAÇÃO DA JANELA
janela = Tk()   #PASSANDO A INFORMAÇÃO PARA A VARIAVEL 
janela.title('Nome da Janela de Testes')  #INFORMANDO O NOME DA JANELA
janela.geometry('600x300')  # INFO O QUANTIDADE DE PIXELS PARA CADA LADO
janela.config(background= 'white') #  COR DE FUNDO  
janela.resizable(width=False, height=False)  # INFO QUE É UMA JANELA NÃO RESPONSIVEL
janela.attributes('-alpha',0.9)  # FAZ COM QUE A JANELA FIQUE MAIS TRANSPARENTE 
janela.iconbitmap(default="images/logoicon.ico") #ICONE DA PAGINA

#=========  Images ======================
logo = PhotoImage(file="images/logo.png") # coloca a imagem na variavel

#=========  Widgets ======================
#CONF LADO ESQUERDO
leftFrame = Frame(janela, width= 200, height= 300, bg= "green", relief='raise')  #Conf Left chama a variavel Janela informa a quantidade de pixels de altura e largura, info a cor e a conf basica "relief = 'raise' "
leftFrame.pack(side=LEFT)   #inf a Biblioteca 
#CONF LADO DIREITO
rightFrame = Frame(janela,width= 395, height= 300, bg='green',relief='raise')   #Conf Rigth chama a variavel Janela informa a quantidade de pixels de altura e largura, info a cor e a conf basica "relief = 'raise' "
rightFrame.pack(side=RIGHT)     #inf a Biblioteca

#CONF A LOGO NO LADO ESQUERDO
LogoLabel = Label(leftFrame, image=logo, bg="green")  # faz a conf da imagem informando o BackGround e aonde vai se posicionar no caso lado Esquerdo
LogoLabel.place(x=50, y=100)  # Info as coordenadas que vai se posicionar no lado Esquerdo

#CONF DOS LAYOYTS = NOME

UserLabel = Label(rightFrame, text="Username:", font=('Century Gothic', 18), bg="Darkgreen", fg="snow" )  # INFO O CAIXA DE TEXTO =  LADO DIREITO, O TEXTO, FONTE, O BACKGROUND E A COR DA LETRA
UserLabel.place(x=5, y=100) #INFO AONDE ESTÁ LOCALIZADO

UserEntry = ttk.Entry(rightFrame, width="28")  # INFO A ENTRADA DE DADOS = O NOME 
UserEntry.place(x=150, y=110) #INFO AONDE ESTÁ LOCALIZADO

#CONF DOS LAYOYTS = SENHA 
PassLabel = Label(rightFrame, text="Password:", font=('Century Gothic', 18), bg='Darkgreen', fg='snow') # INFO O CAIXA DE TEXTO =  LADO DIREITO, O TEXTO, FONTE, O BACKGROUND E A COR DA LETRA
PassLabel.place(x=5, y=140)  #INFO AONDE ESTÁ LOCALIZADO

PassEntry= ttk.Entry(rightFrame, width='30', show='*') #INFO A ENTRADA DE DADOS  =  A SENHA 
PassEntry.place(x=140, y=148) #INFO AONDE ESTÁ LOCALIZADO

def login():
    User = UserEntry.get()
    Pass = PassEntry.get()
    
    databases.cursor.execute('''
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    ''',(User, Pass))
    
    print ('SELECIONOU') 
    verifyLogin = databases.cursor.fetchone()
    try:
        if (User in verifyLogin and Pass in verifyLogin):
            messagebox.showinfo(title='Logind info', message='Acesso confirmado, Bem vindo')
    except:
        messagebox.showinfo(title='Login Info', message='Acesso Negado, Verifique se está no cadastro')

#BOTAOS
LoginButton = Button(rightFrame, text="Login", font=('Century Gothic', 15), bg="Darkgreen", fg="snow",command= login)  # INFO O BOTAO DE LOGIN  = CARACTERISTICAS 
LoginButton.place(x=130, y=200)  # BOTAO DE LOGIN = INFO AONDE ESTÁ LOCALIZADO  


def Register () :
#REMOVENDO WIDGETS DE LOGIN
    LoginButton.place (x=5000)
    RegisterButton.place (x=5000)
    
#INSERINDO WIDGETS DE CADASTRO
    #REGISTRANDO O NOME
    nomelabel = Label(rightFrame, text="Name:", font=('Century Gothic', 18), bg="Darkgreen", fg='snow')
    nomelabel.place(x=5,y=20)
    
    nomeentry = ttk.Entry(rightFrame, width= 35)
    nomeentry.place(x=110, y=30)
    
    #REGISTRANDO O E-MAIL
    emaillabel = Label(rightFrame, text="E-mail:",font=('Century Gothic', 18), bg="Darkgreen", fg='snow')
    emaillabel.place(x=5,y=60)
    
    emailentry = ttk.Entry(rightFrame,width= 35)
    emailentry.place(x=110, y=70)
    
    #BOTAO DE REGISTRAR NO BANCO DE DADOS
    def resgisterdatabase () :
        Name = nomeentry.get()
        email = emailentry.get() 
        User = UserEntry.get()
        Pass = PassEntry.get()

        #VERIFICAR SE OS DADOS NOME E EMAIL ESTÃO PREENCHIDO
        if (Name == '' and email == ''and User == '' and Pass == ''):
            messagebox.showerror(title='Register Erro', message='Verifique Se Todos Os Campos Estão Preenchidos')
        else:    
            databases.cursor.execute('''        
            INSERT INTO Users (Name, Email, User,Password) 
            VALUES (?, ?, ?, ?)
        ''', (Name,email,User,Pass))
            databases.conn.commit()
            messagebox.showinfo(title='Register info', message='account created successfully')
        
    
    Register= Button(rightFrame, text="Register", font=('Century Gothic', 15), bg="Darkgreen", fg='snow', command= resgisterdatabase) # INFO O BOTAO DE RESGISTRAR NO BD  = CARACTERISTICAS
    Register.place(x=120, y=200)  # BOTAO DE REGISTRO NO BD = INFO AONDE ESTÁ LOCALIZADO
    
    def backtologin () :
        #REMOVENDO WIDGETS DE CADASTRO 
        nomelabel.place(x=5000)
        nomeentry.place(x=5000)
        emaillabel.place(x=5000)
        emailentry.place(x=5000)
        Register.place(x=5000)
        back.place(x=5000)
        
        LoginButton.place(x=130, y=200)  # BOTAO DE LOGIN = INFO AONDE ESTÁ LOCALIZADO  
        RegisterButton.place(x=230, y=200)  # BOTAO DE REGISTRO = INFO AONDE ESTÁ LOCALIZADO
        
    back = Button(rightFrame,text='Back', font=('Century Gothic', 15), bg="Darkgreen", fg='snow', command=backtologin)
    back.place (x=230,y=200)
    
RegisterButton = Button(rightFrame, text="Register", font=('Century Gothic', 15), bg="Darkgreen", fg='snow', command=Register) # INFO O BOTAO DE RESGISTRO  = CARACTERISTICAS
RegisterButton.place(x=230, y=200)  # BOTAO DE REGISTRO = INFO AONDE ESTÁ LOCALIZADO

janela.mainloop()  #  FIM DA JANELA