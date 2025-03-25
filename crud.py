usuarios = []
proximo_id = 1 # Contador para gerar ID

def criar_usuarios(nome, idade, altura, peso, cor_olhos): 
  global proximo_id # Permite alterar a variável global 
  usuario = {
    "id": proximo_id,
    "nome": nome, 
    "idade": idade,
    "altura": altura,
    "peso": peso,
    "cor_olhos": cor_olhos,
    }
  usuarios.append(usuario)
  print(f"Usuário criado com sucesso! ID: {proximo_id}")
  proximo_id += 1 # incrementa o ID para o próximo usuário

def listar_usuarios():
  if not usuarios: # Verifica se a lista está vazia
    print('Nenhum usuário cadastrado')
  else:
    for u in usuarios: # Passa por cada usuário da lista
      id = u['id'] # Aqui a gente esta colocando por nome, ou seja vai pegar o 'id' de cada usuário
      nome = u['nome']
      idade = u['idade']
      altura = u['altura']
      peso = u['peso']
      cor_olhos = u['cor_olhos']
      print(f'Protocolo: {id} - Nome: {nome} \n\n idade: {idade} \n altura: {altura} \n peso: {peso} \n cor dos olhos: {cor_olhos} \n\n')

def buscar_usuario(id):
  for u in usuarios: # Aqui percorremos a lista
    if u['id'] == id: # Se o id for igual ao mencionado, mostra o usuário abaixo
      print(f"ID: {u['id']} - Nome: {u['nome']} \n\n idade: {u['idade']} \n altura: {u['altura']} \n peso: {u ['peso']} \n cor dos olhos: {u['cor_olhos']}")
      return # encerra a função após encontrar
  print('Usuário não encontrado') # Caso o ID não exista

# o =None, define que se não for passado nada, será um valor None, ou seja, não altera
def atualizar_usuario(id, nome=None, idade=None, altura=None, peso=None, cor_olhos=None):
  for u in usuarios:
    if u['id'] == id: # se o id for igual o passado
      if nome: # Se o valor for diferente de None, ou seja, se ele existir, ele entra aqui, nos demais
        u['nome'] = nome
      if idade:
        u['idade'] = idade
      if altura:
        u['altura'] = altura
      if peso: 
        u['peso'] = peso
      if cor_olhos:
        u['cor_olhos'] = cor_olhos
      print('Usuário Atualizado')
      return
    print('Usuário não encontrado')

def deletar_usuarios(id): # Esse aqui tu manja
  for u in usuarios: 
    if u['id'] == id:
      usuarios.remove(u)
      print('Usuário deletado')
      return
  print("usuários não encontrado")

while True: # Aqui tu manja 
  print('--MENU--')
  print('1. Criar Usuário')
  print('2. Listar usuários')
  print('3. Buscar usuário por ID') 
  print('4. Atualizar usuário')
  print('5. Deletar usuário')
  print('0 - Sair') 

  opcao = input('Escolha uma opção')
  # Recebe os dados do usuário e chama a função 
  if opcao == '1':
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    altura = int(input('Altura (somente numeros): '))
    peso = int(input('Peso (somente numeros): '))
    cor_olhos = input('Cor dos olhos: ')
    criar_usuarios(nome, idade, altura, peso, cor_olhos)

  # Somente chama a função para executar
  elif opcao == '2':
      listar_usuarios()

  # Busca pelo ID "Protocolo" e mostra o usuário
  elif opcao == '3': 
    id = int(input('protocolo do paciente (somente numero): '))
    buscar_usuario(id)

  # Aqui a lógica é simples, avisamos o usuario para deixar em branco oque não for alterar, e depois usamos um if inline
  # if inline, ele verifica se o valor recebido tem algum dado, se tiver ele usa o dado, se ele não tiver usa o None
  elif opcao == '4':
    id = int(input('Protocolo do paciente (somente numero): '))
    print('**ATENÇÃO**')
    print('Deixe em branco os dados que não serão alterados')
    novo_nome = input('Novo nome: ')
    nova_idade = input('Nova idade: ')
    nova_altura = input('Nova altura:')
    novo_peso = input('Novo peso:')
    novo_cor_olhos = input('Nova cor do olhos: ')
    nome = novo_nome if novo_nome else None
    idade = int(nova_idade) if nova_idade else None
    altura = int(nova_altura) if nova_altura else None
    peso = int(novo_peso) if novo_peso else None
    cor_olhos = novo_cor_olhos if novo_cor_olhos else None
    atualizar_usuario(id, nome, idade, altura, peso, cor_olhos)

  # aqui tu manja
  elif opcao == '5': 
    id = int(input('Protocolo do paciente: '))
    deletar_usuarios(id)

  elif opcao == '0':
    break

  else:
    print('Opção Inválida')