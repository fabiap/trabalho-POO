# Trabalho Avaliativo do 3º Bimestre
# Turma: 2º Ano Matutino de Informática
# Disciplina: Programação Orientada a Objetos
# Professora: Camila Serrão
# Alunos(as): Fábia Pinheiro, Kaiki Hounsell, Lucas Marinho e Maria Luísa


# é pra começar fazendo o cadrasto :d

# Importações das classes necessárias
from user import Admin, Aluno, Servidor, Reclamacao, Departamento, AtendenteReclamacao, Usuario, LoginInvalidoException, DepartamentoNaoDefinidoException
from datetime import date


# "Banco de dados" falso
usuarios = {}
usuarios["admin"] = Admin("fabia", "1234", "2023", "fabia@admin.com", "tudo")

# Lista para armazenar reclamações
reclamacoes = []
# Dicionário para armazenar departamentos e seus atendentes
departamentos = {}


# Lista de administradores predefinidos com nome de usuário e senha
administradores_predefinidos = {
    "fabia": "senha123",
    "admin2": "senha456"
}


# Função para inicializar os departamentos com seus respectivos atendentes
def inicializar_departamentos():
    dep_comida = Departamento("Comida", AtendenteReclamacao("fabia", "Comida"))
    dep_limpeza = Departamento("Limpeza", AtendenteReclamacao("paula", "Limpeza"))
    dep_infraestrutura = Departamento("Infraestrutura", AtendenteReclamacao("pinheiro", "Infraestrutura"))
    departamentos["1"] = dep_comida
    departamentos["2"] = dep_limpeza
    departamentos["3"] = dep_infraestrutura


# Função para cadastrar um novo usuário
def cadastrar_usuario():
    print("\n--- Cadastro de Novo Usuário ---")
    tipo = input("Digite o tipo de usuário (1-Alunos, 2- Servidores): ")
    nome = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()


    # Verifica o tipo de usuário para cadastrar corretamente
    if tipo == "1":
        matricula = input("Digite a matrícula: ").strip()
        novo_usuario = Aluno(nome, senha, matricula)
    elif tipo == "2":
        email = input("Digite o e-mail: ").strip()
        novo_usuario = Servidor(nome, senha, email)
    else:
        print("Tipo de usuário inválido!")
        return None


    # Verifica se o usuário já existe
    if nome in usuarios:
        print("Usuário já existe!")
    else:
        usuarios[nome] = novo_usuario
        print(f"Usuário {nome} cadastrado com sucesso!")


# Função para fazer uma reclamação vinculada a um departamento
def fazer_reclamacao(usuario):
    print("\n--- Fazer Reclamação ---")
    dep_nome = input("Nome do departamento (Ex: 1 - Comida, 2- Limpeza, 3 - Infraestrutura): ")
    descricao = input("Descreva o problema: ").strip()


    # Busca o departamento no dicionário de departamentos
    departamento = departamentos.get(dep_nome)
    if departamento:
        nova_reclamacao = Reclamacao(usuario, departamento, descricao)
        reclamacoes.append(nova_reclamacao)
        print("Reclamação registrada com sucesso!")
    else:
        print("Departamento não encontrado!")


# Função para listar as reclamações de um usuário
def listar_reclamacoes(usuario):
    print("\n--- Minhas Reclamações ---")
    for reclamacao in reclamacoes:
        if reclamacao.get_usuario() == usuario.get_nomeUser():
            reclamacao.dados_reclamacao()        


# Função de login para validar credenciais e direcionar o usuário ao menu apropriado
def login(usuario, senha):
    if usuario.checar_senha(senha):
        print(f"Bem-vindo {usuario.get_nomeUser()}! Você está logado como {usuario.get_user_type()}.")


        # Verificação e direcionamento baseado no tipo de usuário
        if isinstance(usuario, Aluno):
            matricula = input("Digite sua matrícula: ")
            if usuario.get_matricula() == matricula:
                print(f"Matrícula confirmada: {matricula}")
                menu_aluno(usuario)
            else:
                print("Matrícula incorreta!")


        elif isinstance(usuario, Servidor):
            email = input("Digite seu e-mail: ")
            if usuario.get_email() == email:  
                print(f"E-mail confirmado: {email}")
                menu_servidor(usuario)
            else:
                print("E-mail incorreto!")

        elif isinstance(usuario, Admin):
            menu_admin(usuario)

        elif isinstance(usuario, AtendenteReclamacao):
            menu_atendente(usuario)
        
    try:
        if usuario.get_senha() != senha:
            raise LoginInvalidoException("Senha errasdvgv!")
        print(f"Login bem-sucedido! Bem-vindo, {usuario.get_nomeUser()}.")
    except LoginInvalidoException as e:
            print(e)



     
# Menu de opções para os Alunos
def menu_aluno(aluno):
    while True:
        print("\n--- Menu Aluno ---")
        print("1. Fazer reclamação")
        print("2. Listar minhas reclamações")
        print("3. Sair")
        escolha = input("Escolha uma opção: ").strip()


        if escolha == "1":
            fazer_reclamacao(aluno)
        elif escolha == "2":
            listar_reclamacoes(aluno)
        elif escolha == "3":
            break
        else:
            print("Escolha inválida. Tente novamente.")
           
# Menu de opções para os Servidores
def menu_servidor(servidor):
    while True:
        print("\n--- Menu Servidor ---")
        print("1. Fazer reclamação")
        print("2. Listar minhas reclamações")
        print("3. Sair")
        escolha = input("Escolha uma opção: ").strip()


        if escolha == "1":
            fazer_reclamacao(servidor)
        elif escolha == "2":
            listar_reclamacoes(servidor)
        elif escolha == "3":
            break
        else:
            print("Escolha inválida. Tente novamente.")


# Função para o admin gerenciar as reclamações
def gerenciar_reclamacoes(admin):
    for reclamacao in reclamacoes:
        reclamacao.dados_reclamacao()
        resposta = input("Digite a resposta (ou pressione Enter para pular): ").strip()
        if resposta:
            reclamacao.set_status("Respondida")
            print(f"Resposta registrada pelo Admin {admin.get_nomeUser()}: {resposta}")


# Menu de opções para os Admins
def menu_admin(admin):
    while True:
        print("\n--- Menu Admin ---")
        print("1. Cadastrar usuário")
        print("2. Gerenciar reclamações")
        print("3. Listar todas as reclamações")
        print("4. Sair")
        escolha = input("Escolha uma opção: ").strip()


        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            gerenciar_reclamacoes(admin)
        elif escolha == "3":
            listar_todas_reclamacoes()
        elif escolha == "4":
            break
        else:
            print("Escolha inválida. Tente novamente.")


# Função para listar todas as reclamações registradas
def listar_todas_reclamacoes():
    print("\n--- Todas as Reclamações ---")
    for reclamacao in reclamacoes:
        reclamacao.dados_reclamacao()


# Função principal para iniciar o sistema
def iniciar_sistema():
    inicializar_departamentos()
    while True:
        print("\n--- Sistema Principal ---")
        escolha = input("Digite '1' para login, '2' para cadastrar usuário, ou '3' para encerrar: ").strip()


        if escolha == "1":
            nome = input("Nome de usuário: ").strip()
            senha = input("Senha: ").strip()


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
            print("Escolha inválida. Tente novamente.")


# Ponto de entrada do programa
if __name__ == "__main__":
    iniciar_sistema()


#pedencias no código: uma maneira do atendente responder a reclamaçao; acessar o admin. - feitas.
#fazer excessoes de email e senha


#menu atendente (admin)
def menu_atendente(atendente):
    while True:
        print("\n--- Menu Atendente ---")
        print("1. Responder reclamações do meu departamento")
        print("2. Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            for reclamacao in reclamacoes:
                if reclamacao.get_departamento() == atendente.get_nome_departamento() and reclamacao.get_status() == "Pendente":
                    reclamacao.dados_reclamacao()
                    resposta = input("Digite sua resposta: ").strip()
                    print(atendente.responder_reclamacao(reclamacao, resposta))
        elif escolha == "2":
            break
        else:
            print("Escolha inválida. Tente novamente.")
            


# Reclamação sem departamento
def criar_reclamacao(usuario, departamento, descricao):
    try:
        if not departamento:
            raise DepartamentoNaoDefinidoException("Departamento não pode ser vazio.")
        reclamacao = Reclamacao(usuario, departamento, descricao)
        print("Reclamação criada com sucesso!")
    except DepartamentoNaoDefinidoException as e:
        print(e)