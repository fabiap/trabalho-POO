from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nomeUser, senha):
        self.__nomeUser = nomeUser
        self.__senha = senha

    
    def get_nomeUser(self):
        return self.__nomeUser

    def set_nomeUser(self, nomeUser):
        self.__nomeUser = nomeUser

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha

    def checar_senha(self, senha):
        return self.__senha == senha

    @abstractmethod
    def get_user_type(self):
        pass


class Admin(Usuario):
    def __init__(self, nomeUsuario, senha, permissoes):
        super().__init__(nomeUsuario, senha)
        self.__permissoes = permissoes

    def get_user_type(self):
        return "Admin"

   
    def get_permissoes(self):
        return self.__permissoes

    def set_permissoes(self, permissoes):
        self.__permissoes = permissoes

    def add_permissao(self, permissao):
        self.__permissoes.append(permissao)

    def remove_permissao(self, permissao):
        if permissao in self.__permissoes:
            self.__permissoes.remove(permissao)
            print(f"Permissão '{permissao}' removida.")
        else:
            print(f"Permissão '{permissao}' não encontrada.")

    def listar_permissoes(self):
        print(f"Permissões de {self.get_nomeUser()}: {', '.join(self.__permissoes)}")


class Alunos(Usuario):
    def __init__(self, nomeUsuario, senha, matricula):
        super().__init__(nomeUsuario, senha)
        self.__matricula = matricula

    def get_user_type(self):
        return "Alunos"

   
    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

  
    def exibir_informacoes(self):
        print(f"Nome: {self.get_nomeUser()}, Matrícula: {self.get_matricula()}")

  
    def atualizar_matricula(self, nova_matricula):
        self.set_matricula(nova_matricula)
        print(f"Matrícula atualizada para: {self.get_matricula()}")


class Servidores(Usuario):
    def __init__(self, nomeUser, senha, email):
        super().__init__(nomeUser, senha)
        self.__email = email

    def get_user_type(self):
        return "Servidores"

    
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    
    def exibir_informacoes(self):
        print(f"Nome: {self.get_nomeUser()}, E-mail: {self.get_email()}")

    
    def atualizar_email(self, novo_email):
        self.set_email(novo_email)
        print(f"E-mail atualizado para: {self.get_email()}")


class SuperUsuario(Admin):
    def __init__(self, nomeUsuario, senha, permissoes, nivel_acesso):
        super().__init__(nomeUsuario, senha, permissoes)
        self.__nivel_acesso = nivel_acesso

    def get_user_type(self, detalhe=False):
        if detalhe:
            return f"SuperUsuario com acesso nível {self.get_nivel_acesso()}"
        return "SuperUsuario"

    
    def get_nivel_acesso(self):
        return self.__nivel_acesso

    def set_nivel_acesso(self, nivel_acesso):
        self.__nivel_acesso = nivel_acesso

   
    def redefinir_senha(self, usuario, nova_senha):
        if isinstance(usuario, Usuario):
            usuario.set_senha(nova_senha)
            print(f"A senha de {usuario.get_nomeUser()} foi redefinida.")
        else:
            print("Usuário inválido.")

    
    def aumentar_nivel_acesso(self):
        self.set_nivel_acesso(self.get_nivel_acesso() + 1)
        print(f"Nível de acesso de {self.get_nomeUser()} agora é {self.get_nivel_acesso()}")
