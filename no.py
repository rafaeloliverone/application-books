class No:
    def __init__(self, titulo = None, ano = None, left = None, right = None):
        self.titulo = titulo
        self.ano = ano
        self.left = left
        self.right = right

    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self, novatitulo):
        self.titulo = novatitulo

    def get_ano(self):
      return self.ano
    
    def set_ano(self, novoAno):
      self.ano = novoAno

    def get_left(self):
        return self.left
    
    def set_left(self, no):
        self.left = no
    
    def get_right(self):
        return self.right
    
    def set_right(self, no):
        self.right = no
    
    def __str__(self):
        return 'Titulo : {} \nAno : {}'.format(self.titulo,self.ano)



    ########### ÁRVORE AVL ##############

    def rotacaoDireita(self):
      #pegar os valores do nó raiz antes de serem alterados
      x = self.get_titulo()
      y = self.get_ano()
      #mudando os valores da raiz para os valores do filho esquerdo
      self.set_titulo(self.get_left().get_titulo()) 
      self.set_ano(self.get_left().get_ano())
      #mudando os valores do filho esq para o da raiz 
      self.get_left().set_titulo(x)
      self.get_left().set_ano(y) 

      old_direita = self.get_right()
      self.set_right(self.get_left())
      self.set_left(self.get_left().get_left())
      self.get_right().set_left(self.get_right().get_right())
      self.get_right().set_right(old_direita)
    
    def rotacaoEsquerda(self):
      x = self.get_titulo()
      y = self.get_ano()
      self.set_titulo(self.get_right().get_titulo())
      self.set_ano(self.get_right().get_ano())
      self.get_right().set_titulo(x)
      self.get_right().set_ano(y)

      old_esquerda = self.get_left()
      self.set_left(self.get_right())
      self.set_right(self.get_right().get_right())
      self.get_left().set_right(self.get_left().get_left())
      self.get_left().set_left(old_esquerda)
    
    def rotacaoEsquerdaDireita(self):
      self.get_left().rotacaoEsquerda()
      self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
      self.get_right().rotacaoDireita()
      self.rotacaoEsquerda()

    def executaBalanco(self):
      balanco = self.balanco()
      #quer girar para direita
      if balanco > 1:
        #mesmos sinais
        if self.get_left().balanco() >= 0:
          self.rotacaoDireita()
        #sinais diferentes
        else:
          self.rotacaoEsquerdaDireita()
      #quer girar para esquerda
      elif balanco < -1:
        #mesmos sinais 
        if self.get_right().balanco() < 0:
          self.rotacaoEsquerda()
        #sinais diferentes
        else:
          self.rotacaoDireitaEsquerda()

    #função que vai dar o fator de balanceamento 
    def balanco(self):
      prof_esq = 0 
      if self.get_left():
        prof_esq = self.get_left().profundidade()
      prof_dir = 0
      if self.get_right():
        prof_dir = self.get_right().profundidade()
      return prof_esq - prof_dir

    #função para ver o nível da árvore
    def profundidade(self):
      prof_esq = 0
      if self.get_left():
        prof_esq = self.get_left().profundidade()
      prof_dir = 0
      if self.get_right():
        prof_dir = self.get_right().profundidade()
      return 1 + max(prof_esq,prof_dir)