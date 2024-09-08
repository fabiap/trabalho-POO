#Trabalho Avaliativo do 2º Bimestre
#Turma: 2º Ano Matutino de Informática
#Disciplina: Programação Orientada a Objetos
#Professora: Camila Serrão
#Alunos(as): Fábia Pinheiro, Kaiki Hounsell, Lucas Marinho e Maria Luísa
#:(

from user import Admin, Alunos, Servidores, SuperUsuario

def cadastrar_usuario():
    print("\n--- Cadastro de Novo Usuário ---")
    tipo = input("Digite o tipo de usuário (1-Alunos, 2- Servidores): ")
    nome = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()

    if tipo == "1":
        matricula = input("Digite a matrícula: ").strip()
        novo_usuario = Alunos(nome, senha, matricula)
    elif tipo == "2":
        email = input("Digite o e-mail: ").strip()
        novo_usuario = Servidores(nome, senha, email)
    else:
        print("Tipo de usuário inválido!")
        return None

    if nome in usuarios:
        print("Usuário já existe!")
    else:
        usuarios[nome] = novo_usuario
        print(f"Usuário {nome} cadastrado com sucesso!")

def login(usuario, senha):
    if usuario.checar_senha(senha):
        print(f"Bem-vindo {usuario.get_nomeUser()}! Você está logado como {usuario.get_user_type()}.")

        if isinstance(usuario, Alunos):
            matricula = input("Digite sua matrícula: ")
            if usuario.get_matricula() == matricula: 
                print(f"Matrícula confirmada: {matricula}")
            else:
                print("Matrícula incorreta!")

        elif isinstance(usuario, Servidores):
            email = input("Digite seu e-mail: ")
            if usuario.get_email() == email:  
                print(f"E-mail confirmado: {email}")
            else:
                print("E-mail incorreto!")

        elif isinstance(usuario, Admin):
            print("Você está logado como Admin.")

        if isinstance(usuario, SuperUsuario):
            print(usuario.get_user_type(detalhe=True))

    else:
        print("Senha Inválida!")


admin1 = Admin("adminkaiki", "123", ["create", "delete"])
admin2 = Admin("adminmaria", "321", ["create", "delete"])
admin3 = Admin("adminfabia", "231", ["create", "delete"])
admin4 = Admin("adminlucas", "312", ["create", "delete"])
aluno1 = Alunos("fabia", "123", "2023106060025")
aluno2 = Alunos("maria", "321", "2023106060026")
aluno3 = Alunos("lucas", "213", "2023106060027")
aluno4 = Alunos("kaiki", "312", "2023106060028")
servidor1 = Servidores("camila", "123", "camila@gmail.com")
servidor2 = Servidores("dani", "321", "dani@gmail.com")
servidor3 = Servidores("ozemar", "213", "ozemar@gmail.com")
servidor4 = Servidores("silvio", "312", "silvio@gmail.com")
superuser1 = SuperUsuario("paula", "123", ["create", "delete", "modify"], 5)
superuser2 = SuperUsuario("hounsel", "321", ["create", "delete", "modify"], 6)
superuser3 = SuperUsuario("luisa", "213", ["create", "delete", "modify"], 7)
superuser4 = SuperUsuario("marinho", "312", ["create", "delete", "modify"], 8)

# "banco de dados"
usuarios = {
    "adminkaiki": admin1,
    "adminfabia": admin2,
    "adminmaria": admin3,
    "adminlucas": admin4,
    "fabia": aluno1,
    "maria": aluno2,
    "lucas": aluno3,
    "kaiki": aluno4,
    "camila": servidor1,
    "dani": servidor2,
    "ozemar": servidor3,
    "silvio": servidor4,
    "paula": superuser1, 
    "hounsel": superuser2,
    "luisa": superuser3,
    "marinho": superuser4,
}

def iniciar_sistema():
    while True:
        print("\n--- Sistema de Login ---")
        escolha = input("Digite '1' para fazer login, '2' para cadastrar um novo usuário, ou '3' para encerrar: ")

        if escolha == "1":
            nome = input("Digite o nome de usuário: ").strip()
            senha = input("Digite a senha: ").strip()
            
            usuario = usuarios.get(nome)
            if usuario:
                login(usuario, senha)
            else:
                print("Usuário não encontrado!")

        elif escolha == "2":
            cadastrar_usuario()

        elif escolha == "3":
            print("Encerrando o sistema...")
            break

        else:
            print("Escolha inválida! Tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()

