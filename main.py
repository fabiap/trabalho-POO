# Trabalho Avaliativo do 3º Bimestre
# Turma: 2º Ano Matutino de Informática
# Disciplina: Programação Orientada a Objetos
# Professora: Camila Serrão
# Alunos(as): Fábia Pinheiro, Kaiki Hounsell, Lucas Marinho e Maria Luísa


# é pra começar fazendo o cadrasto :d

# Importações das classes necessárias
<<<<<<< HEAD
from user import Admin, Aluno, Servidor, Reclamacao, Departamento, AtendenteReclamacao, Usuario, LoginInvalidoException, DepartamentoNaoDefinidoException, ColecaoDepartamentos
=======
from user import Admin, Aluno, Servidor, Reclamacao, Departamento, AtendenteReclamacao, Usuario,LoginInvalidoException, DepartamentoNaoDefinidoException,senhaInvalida, emailInvalido, NomeRepetido
>>>>>>> 72241d70d652fce260a7d6681e8a438a1557afe9
from datetime import date
from collections import deque

# "Banco de dados" falso

usuarios = {}
admin = Admin("admin", "1234", "admin@admin.com", "geral", "oi")
usuarios["admin"] = admin 
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
    

#funçao exceção
def validaremail(email):
     if "@" not in email or "." not in email:
         raise emailInvalido("email invalido")


def validarsenha(senha):
    if len(senha) < 4:
        raise senhaInvalida("a senha precisa de mais de 4 caracteres.")
    
    

# Função auxiliar para buscar o departamento pelo nome
def buscar_departamento(nome_departamento):
    for dep in departamentos:  # departamentos é a lista de objetos Departamento
        if dep.get_nome_departamento() == nome_departamento:
            return dep
    return None  # Retorna None caso o departamento não seja encontrado


# Função para cadastrar um novo usuário
def cadastrar_usuario():
    print("\n--- Cadastro de Novo Usuário ---")
    try:
        tipo = input("Digite o tipo de usuário (1-Alunos, 2- Servidores): ")
        
        nome = input("Digite o nome de usuário: ").strip()
        if nome in usuarios: 
            raise NomeRepetido(nome)
       
       #exceção para caso o usuario digite algo incorreto
        email = input("Digite o email(email valido): ").strip()
        validaremail(email)
        
        senha = input("Digite a senha(mais de 4 caracteres): ").strip()
        validarsenha(senha)

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
            
    except emailInvalido as e:
        print(e)
    except senhaInvalida as e:
        print(e)
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally: 
        print("usuario nao foi cadastrado")
 


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

# Reclamação sem departamento
def criar_reclamacao(usuario, departamento, descricao):
    try:
        if not departamento:
            raise DepartamentoNaoDefinidoException("Departamento não pode ser vazio.")
        reclamacao = Reclamacao(usuario, departamento, descricao)
        print("Reclamação criada com sucesso!")
    except DepartamentoNaoDefinidoException as e:
        print(e)

# Coleção para armazenar reclamações em ordem de chegada
fila_reclamacoes = deque()

def adicionar_reclamacao_na_fila(reclamacao):
    fila_reclamacoes.append(reclamacao)
    print("Reclamação adicionada na fila!")

def processar_reclamacoes():
    if not fila_reclamacoes:
        print("Nenhuma reclamação pendente na fila!")
        return

    print("\n--- Processando Reclamações ---")
    while fila_reclamacoes:
        reclamacao = fila_reclamacoes.popleft()
        reclamacao.dados_reclamacao()
        print("Reclamação processada e removida da fila!\n")


# Menu de opções para os Admins
def menu_admin(admin):
    while True:
        print("\n--- Menu Admin ---")
        print("1. Cadastrar usuário")
        print("2. Gerenciar reclamações")
        print("3. Listar todas as reclamações")
        print("4. Adicionar reclamação na fila")
        print("5. Processar reclamações na fila")
        print("6. Sair")
        escolha = input("Escolha uma opção: ").strip()


        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            gerenciar_reclamacoes(admin)
        elif escolha == "3":
            listar_todas_reclamacoes()
        elif escolha == "4":  # Adicionar reclamação na fila
            descricao = input("Digite a descrição da reclamação: ").strip()
            nome_departamento = input("Digite o nome do departamento: ").strip()

            # Buscar o departamento correto
            departamento = buscar_departamento(nome_departamento)
            
            if departamento:  # Departamento encontrado
                reclamacao = Reclamacao(admin, departamento, descricao)
                adicionar_reclamacao_na_fila(reclamacao)
            else:
                print("Departamento não encontrado! Verifique o nome e tente novamente.")
        elif escolha == "5":
            processar_reclamacoes()
        elif escolha == "6":
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


#pedencias no código: uma maneira do atendente responder a reclamaçao; acessar o admin
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
            

# Demonstração de diferentes coleções
def demonstrar_colecoes():
    print("\n--- Demonstração de Coleções em Python ---")

<<<<<<< HEAD
#Reclamação sem departamento
def criar_reclamacao(usuario, departamento, descricao):
    try:
        if not departamento:
            raise DepartamentoNaoDefinidoException("Departamento não pode ser vazio.")
        reclamacao = Reclamacao(usuario, departamento, descricao)
        print("Reclamação criada com sucesso!")
    except DepartamentoNaoDefinidoException as e:
        print(e)

if _name_ == "_main_":
    sistema = ColecaoDepartamentos()

    # Adicionar departamentos ao sistema
    nomes_departamentos = [
        "Departamento de Apoio ao Ensino (dape)",
        "Direção de Ensino (de)",
        "Coordenação de Gestão de Tecnologia da Informação (cgti)",
        "Coordenação de Gestão de Pessoas (cgp)",
        "Coordenação de Comunicação e Eventos (ccom)",
        "Direção-Geral (dg)",
        "Biblioteca (cbib)",
        "Departamentos de Assistência Estudantil (depae)",
        "Departamento de Extensão (depex)",
        "Departamento de Pesquisa, Inovação e Pós-graduação (depesp)",
        "Coordenação de Patrimônio e Almoxarifado (cpalm)",
        "Coordenação de Orçamento e Finanças (cofin)",
        "Coordenação de Serviços Gerais (csg)",
        "Coordenação de Compras e Licitação (ccl)",
    ]

    for nome in nomes_departamentos:
        sistema.adicionar_departamento(nome)

    # Menu interativo
    while True:
        print("\n--- Sistema de Reclamações ---")
        print("1. Fazer uma reclamação")
        print("2. Listar todos os departamentos e suas reclamações")
        print("3. Contar departamentos e reclamações")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            sistema.listar_departamentos()
            nome_parcial = input("\nDigite o nome ou sigla do departamento que deseja reclamar: ")

            try:
                departamento = sistema.buscar_departamento(nome_parcial)
                titulo = input("Digite o título da reclamação: ")
                descricao = input("Digite a descrição da reclamação: ")

                reclamacao = Reclamacao(titulo, descricao)
                departamento.adicionar_reclamacao(reclamacao)

                print("Problema relatado com sucesso!")
            except Exception as e:
                print(e)

        elif opcao == "2":
            sistema.listar_departamentos()

        elif opcao == "3":
            total_departamentos = sistema.contar_departamentos()
            total_reclamacoes = sistema.contar_reclamacoes()

            print(f"\nTotal de departamentos cadastrados: {total_departamentos}")
            print(f"Total de reclamações registradas: {total_reclamacoes}")

        elif opcao == "4":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")
=======
    # List
    lista_usuarios = ["admin", "atendente1", "usuario1"]
    print("Lista de Usuários:", lista_usuarios)

    # Set
    conjunto_departamentos = {"Limpeza", "TI", "RH"}
    print("Conjunto de Departamentos:", conjunto_departamentos)

    # Tuple
    tupla_permissoes = ("Admin", "Atendente", "Usuario")
    print("Tupla de Permissões:", tupla_permissoes)

    # Dict
    dicionario_reclamacoes = {"Limpeza": 5, "TI": 10, "RH": 3}
    print("Dicionário de Reclamações:", dicionario_reclamacoes)

    # Deque (Fila)
    print("Fila de Reclamações (deque):", list(fila_reclamacoes))
>>>>>>> 72241d70d652fce260a7d6681e8a438a1557afe9
