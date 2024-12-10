'''
classes-Referente a caracteres, seguir o mesmo padrão de variáveis e objetos.
Sempre iniciar as classes com caracteres maiúsculos, inclusive as iniciais de nomes compostos:
Exemplo: MinhaClasse()

Variaveis ou objetos-Utilizar somente caracteres e letras minúsculas.
No caso de variáveis com nome composto, utilizar o underline para separação das palavras.
Não iniciar o nome com números (podemos utilizar números no nome, mas não devemos iniciar com eles).
Não utilizar caracteres especiais.
Não utilizar espaçamento em branco.
Evitar utilizar os caracteres I e O.

pacotes,modulos e metodos-Utilizar nomes pequenos.
Utilizar sempre caracteres minúsculos.
Utilizar o underline para unir nomes compostos.

Atributos
Os atributos armazenam as características de uma classe.

Os atributos são as declarações de variáveis da classe.

Métodos
São ações da classe, suas funções.

Representam os estados e ações dos objetos quando instanciados.
'''

class Cliente:
    def __init__(self, n, fone):

        self._nome = n
        self._telefone = fone

    #Método Get
    def get_nome(self):
        return self._nome
    
    #Método Set
    def set_nome(self, nome):
        self._nome = nome
        

'''
Para definir o construtor adicionamos: underline, underline __, a palavra reservada 'init', underline, underline. O init() é um método especial que será chamado sempre que criarmos um objeto da classe.

Todo método Python tem self como primeiro parâmetro.

A palavra reservada representa o objeto em si, portanto, sempre que quisermos especificar atributos de objetos, devemos associá-lo à palavra reservada self.

Com o parâmetro self são passados os parâmetros que serão utilizados para inicialização dos atributos

Inicializamos os atributos com os valores passados por parâmetro..

'''
'''De forma geral, todas as linguagens de programação que utilizam orientação a objetos usam modificadores de acesso para alterar a visibilidade de classes, atributos e métodos.

Para a implementação do encapsulamento é fundamental alterarmos a visibilidade dos atributos de uma classe. Para isso, utilizamos os modificadores de acesso.

Diferentemente de outras linguagens, como o Java e o C#, que utilizam palavras reservadas, a linguagem Python utiliza o símbolo underscore ”_”.

Dentro da orientação a objetos temos os modificadores Public, Protected e Private.

A seguir, vamos conhecer as principais características de cada um deles.

PUBLICA - É o mais comum entre os modificadores.
Ele permite acesso tanto de dentro, quanto de fora de uma classe.
Sua implementação se dá por meio do uso do underline ”_” na frente do nome.

PROTECTED - Utilizando o modificador protegido, somente suas classes e subclasses terão acesso ao atributo ou método.
Para sua implementação adicione um underline ”_” antes do nome.

PRIVATE - É o modificador mais restrito do desenvolvimento orientado a objetos.
Ele permite que somente a sua classe (onde foi definido) tenha acesso a um determinado atributo ou método.
Para definir o método private adicionamos underline duplo ”__” na frente do nome.


Para permitir o acesso aos atributos de forma controlada, a prática mais comum é a utilização de dois métodos de acesso: um retornando valor e outro que muda valor.

Getters e Setters são usados na maioria das linguagens de programação orientada a objetos com o objetivo de garantir o princípio de encapsulamento de dados.

Os métodos são utilizados para implementações que alteram os valores internos da classe ou que retornam valores dela.'''
