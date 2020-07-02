from no import No

# Função para adicionar um novo nó
def inserir(T, titulo, ano):
  if buscaTitulo(T, titulo) is None:
    if T is None:
      return No(titulo, ano)

    elif titulo < T.titulo:
      T.set_left(inserir(T.left, titulo, ano))
      return T

    elif titulo > T.titulo:
      T.set_right(inserir(T.right, titulo, ano))
      return T
  else:
    return T


# Função para excluir um nó
def excluir(t, titulo):
  if t is None:
    return None

  elif t.titulo == titulo:
    # caso 1 - no folha
    if ehFolha(t):
      return None
    
    # caso 2 A - no tem apenas filho esquerdo
    elif t.left is not None and t.right is None:
      return t.left
    
    # caso 2 B - no tem apenas filho direito
    elif t.right is not None and t.left is None:
      return t.right
    
    # caso 3
    else:
      # encontrar predecessor
      p = predecessor(t)
      # trocar os valores
      q = t.titulo
      r = t.ano

      t.titulo = p.titulo
      t.ano = p.ano

      p.titulo = q
      p.ano = r

      t.right = excluir(t.right, titulo)

  elif t.titulo > titulo:
    t.left = excluir(t.left, titulo)
  
  elif t.titulo < titulo:
    t.right = excluir(t.right, titulo)

  return t


# Função para buscar um determinado nó
def buscaTitulo(T, titulo):
  if T is None or T.titulo == titulo:
    return T

  elif T.titulo > titulo:
    return buscaTitulo(T.left, titulo)

  else:
    return buscaTitulo(T.right, titulo)


# Funções para gerar uma lista com todos os registros de um determinado ano
def buscaAno(T, ano):
  vetor = []
  return anoList(T, vetor, ano)

def anoList(t, vetor, ano):
  if t != None:
    anoList(t.left, vetor, ano)
    if t.ano == ano:
      vetor.append(t.titulo)
    anoList(t.right, vetor, ano)
    return vetor


# Função para encontrar o predecessor de um nó
def predecessor(t):
  if t is None:
    return None
  
  elif ehFolha(t):
    return t
  
  else:
    aux = t.right

    while aux.left is not None:
      aux = aux.left
    return aux


# Funções para gerar uma lista com todos os registros
def transfere(t):
  vetor = []
  return emOrdem(vetor, t)

def emOrdem(vetor, t):
  if t != None:
    emOrdem(vetor, t.left)
    vetor.append(t.titulo)
    emOrdem(vetor, t.right)
    return vetor
  

# Função para saber se um nó é folha
def ehFolha(T):
  if T.left is None and T.right is None:
    return True
  else:
    return False


# Função para balancear cada nó
def balancear(T):
  if T != None:
    balancear(T.left)
    T.executaBalanco()
    balancear(T.right)


