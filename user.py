
from abc import ABC, abstractmethod
from datetime import date
#OIIIIIII

# Classe base abstrata para todos os tipos de usuário
class Usuario(ABC):
    def __init__(self, nomeUser, senha, matricula=None, email=None):
        # Atributos encapsulados para garantir segurança
        self.__nomeUser = nomeUser
        self.__senha = senha
        self.__matricula = matricula
        self.__email = email

    # Métodos de acesso e modificação com encapsulamento
    def get_nomeUser(self):
        return self.__nomeUser

    def set_nomeUser(self, nomeUser: str) -> None:
        self.__nomeUser = nomeUser

    # Verificação de senha, respeitando a privacidade dos dados
    def checar_senha(self, senha):
        return self.__senha == senha

    # Métodos para acessar e modificar matrícula e email
    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email
        
    def get_senha(self):
        return self.__senha
    
    def set_senha(self, senha):
        self.__senha = senha


    # Método abstrato para ser implementado por subclasses
    @abstractmethod
    def get_user_type(self):
        pass


# Subclasse Admin que herda de Usuario
class Admin(Usuario):
    def __init__(self, nomeUser, senha, matricula, email, departamento):
        super().__init__(nomeUser, senha, matricula, email)
        self.__departamento = departamento  # Atributo adicional para admins

    def get_user_type(self):
        return "Admin"
    
    def __str__(self):
        return f"Admin: {self._Usuario__nomeUser}, Matricula: {self._Usuario__matricula}, Email: {self._Usuario__email}, Departamento: {self.__departamento}"


    # Método específico para acessar permissões
    def get_permissoes(self):
        return self.__permissoes


# Subclasse Aluno
class Aluno(Usuario):
    def __init__(self, nomeUser, senha, matricula):
        super().__init__(nomeUser, senha, matricula)
        self.senha = senha
        self.__matricula = matricula
        
        
    def get_matricula(self):
        return self.__matricula
    
    def get_senha(self):
        return self.senha

    # Aluno implementa o método abstrato
    def get_user_type(self):
        return "Aluno"


# Subclasse Servidor
class Servidor(Usuario):
    def __init__(self, nomeUser, senha, email):
        super().__init__(nomeUser, senha, email=email)

    # Servidor implementa o método abstrato
    def get_user_type(self):
        return "Servidor"


# Classe Departamento representa a agregação de um AtendenteReclamacao
class Departamento:
    def __init__(self, nome_departamento, responsavel):
        # Nome do departamento e o responsável
        self.__nome_departamento = nome_departamento
        self.__responsavel = responsavel


    # Métodos para acessar informações do departamento
    def get_nome_departamento(self):
        return self.__nome_departamento


    def get_responsavel(self):
        return self.__responsavel


# Classe Reclamacao representa a associação entre Usuario e Departamento
class Reclamacao:
    def __init__(self, usuario, departamento, descricao):
        # Relaciona a reclamação a um usuário e um departamento
        self.__usuario = usuario
        self.__departamento = departamento
        self.__descricao = descricao
        self.__status = "Pendente"
        self.__data_registro = date.today()


    # Métodos para acessar detalhes da reclamação
    def get_usuario(self):
        return self.__usuario.get_nomeUser()


    def get_departamento(self):
        return self.__departamento.get_nome_departamento()


    def get_descricao(self):
        return self.__descricao


    def get_status(self):
        return self.__status


    def get_data(self) -> date:
        return self.__data_registro


    # Atualiza o status da reclamação
    def set_status(self, status: str) -> None:
        self.__status = status


    # Exibe os detalhes da reclamação
    def dados_reclamacao(self) -> None:
        print(f"Reclamacao feita por {self.get_usuario()} no departamento {self.get_departamento()}")
        print(f"Descrição: {self.__descricao}")
        print(f"Status: {self.__status}")
        print(f"Data de Registro: {self.__data_registro}")


# Classe AtendenteReclamacao lida com reclamações de um departamento específico
class AtendenteReclamacao:
    def __init__(self, nome_responsavel, departamento):
        # Nome do atendente e o departamento que ele gerencia
        self.__nome_responsavel = nome_responsavel
        self.__departamento = departamento


    # Métodos para acessar detalhes do atendente
    def get_nome_responsavel(self):
        return self.__nome_responsavel


    def get_nome_departamento(self) -> str:
        return self.__departamento


    # Método para responder reclamações atribuídas ao departamento do atendente
    def responder_reclamacao(self, reclamacao: Reclamacao, resposta: str) -> str:
        if reclamacao.get_departamento() == self.get_nome_departamento():
            reclamacao.set_status("Respondida")
            return f"Reclamacao respondida por {self.__nome_responsavel}: {resposta}"
        return "Reclamacao pertence a outro departamento."


    # Exibe detalhes do atendente
    def dados_responsavel(self) -> None:
        print(f"Responsável: {self.__nome_responsavel}")
        print(f"Departamento: {self.get_nome_departamento()}")

class LoginInvalidoException(Exception):
    pass

class DepartamentoNaoDefinidoException(Exception):
    pass

class DepartamentoNaoEncontradoException(Exception):
    """Exceção personalizada para departamentos inexistentes."""
    def _init_(self, departamento_nome):
        super()._init_(f"Erro: O departamento '{departamento_nome}' não foi encontrado no sistema.")



class ColecaoDepartamentos:
    """Classe responsável por gerenciar uma coleção de departamentos."""
    def _init_(self):
        self.departamentos = {}

    def adicionar_departamento(self, nome_departamento):
        """Adiciona um departamento à coleção."""
        if nome_departamento not in self.departamentos:
            self.departamentos[nome_departamento] = Departamento(nome_departamento)

    def listar_departamentos(self):
        """Lista todos os departamentos e suas reclamações associadas."""
        if not self.departamentos:
            print("Nenhum departamento cadastrado.")
            return

        for nome, departamento in self.departamentos.items():
            print(f"\nDepartamento: {nome}")
            if departamento.reclamacoes:
                print("Reclamações:")
                for reclamacao in departamento.reclamacoes:
                    print(f"  - Título: {reclamacao.titulo}")
                    print(f"    Descrição: {reclamacao.descricao}")
            else:
                print("Sem reclamações associadas.")

    def contar_departamentos(self):
        """Retorna o número de departamentos na coleção."""
        return len(self.departamentos)

    def contar_reclamacoes(self):
        """Retorna o número total de reclamações em todos os departamentos."""
        total_reclamacoes = 0
        for departamento in self.departamentos.values():
            total_reclamacoes += departamento.contar_reclamacoes()
        return total_reclamacoes

    def buscar_departamento(self, nome_parcial):
        """Busca um departamento pelo nome ou parte do nome."""
        for nome, departamento in self.departamentos.items():
            if nome_parcial.lower() in nome.lower():
                return departamento
        raise DepartamentoNaoEncontradoException(nome_parcial)
