# def criar_arquivo(nome_arquivo: str, conteudo: str):
#  """Cria um arquivo com nome e conteúdo fornecidos"""
#    with open(nome_arquivo, 'w') as arquivo:
#        arquivo.write(conteudo)
#        print('Arquivo criado com sucesso"')

# nome = input('Digite o nome do arquivo:  ')
# criar_arquivo(f'./Aula05/arquivos/{nome}.txt', 'Este é um exemplo de arquivo criado com python.')

# Ler o arquivo

# def ler_arquivo(nome_arquivo: str) -> str:
#    """lê um arquivo com nome e conteúdo fornecidos"""
#   with open(nome_arquivo, 'r') as arquivo:
#       return arquivo.read()

# nome = input("Digite o nome do arquivo: ")
# print(ler_arquivo(f'./Aula05/arquivos/{nome}.txt'))

# Adicionar conteúdo

# def adicionar_arquivo(nome_arquivo: str, conteudo: str):
#     """adicona um Conteúdo ao final de um arquivo."""
#     with open(nome_arquivo, 'a') as arquivo:
#          arquivo.write('\n' + conteudo)
#          print("Arquivo criado com sucesso")

# nome = input("Digite o nome do arquivo: ")
# conteudo=input("Digite um texo a ser adicionado: ")
# adicionar_arquivo(f'./Aula05/arquivos/{nome}.txt', conteudo)

# Remover arquivo


# import os
# def remover_arquivo(nome_arquivo: str):
#     """exclui o arquivo se ele existir."""
#     if os.path.exists(nome_arquivo):
#          os.remove(nome_arquivo)
#          print("Arquivo removido com sucesso")
#     else:
#         print("esse arquivo nao existe")

# nome = input("Digite o nome do arquivo que deseja remover: ")
# remover_arquivo(f'./Aula05/arquivos/{nome}.txt')

# def contar_linhas(nome_arquivo: str) -> int:
#      """conta as linhas de um arquivo."""
#      with open(nome_arquivo, 'r') as arquivo:
#         return   len(arquivo.readlines())
           
# nome = input("Digite o nome do arquivo: ")
# print(contar_linhas(f'./Aula05/arquivos/{nome}.txt'))


# def verifica_palavra(nome_arquivo: str, palavra: str) -> bool:
#      """Verifica se a palavra existe."""
#      with open(nome_arquivo, 'r') as arquivo:
#         return palavra in arquivo.read()

# nome=input("Informe o nome do arquivo: ")
# print(verifica_palavra(f'./Aula05/arquivos/{nome}.txt', 'oi'))


def atualizar_linha(nome_arquivo: str, novo_conteudo: str, linha_alv: int):
      """Atualiza uma linha especifica de um arquivo."""
      with open(nome_arquivo, 'r') as arquivo:
         linhas = arquivo.readlines()
         if 0 <= linha_alv < len(linhas):
            linhas[linha_alv] = novo_conteudo + '\n'
      with open(nome_arquivo, 'w') as arq:
            arq.writelines(linhas)


nome=input("Informe o nome do arquivo: ")
conteudo=input("Informe o conteudo do arquivo: ")
linha=int(input("Informe o numero da linha do arquivo: "))
print(atualizar_linha(f'./Aula05/arquivos/{nome}.txt', conteudo, linha))
