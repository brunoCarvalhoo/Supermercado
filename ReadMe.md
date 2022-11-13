# Simulação de um sistema de Supermercado

Nesse projeto criou-se um sistema de gestão de um mercado.
O projeto em si apresenta 5 funcionalidades que estão listados abaixo:

## Listar Itens

Os itens que são registrados estão salvos na Array `items()` que é uma array de dicionários.
Por meio do loop abaixo esses dados são acessados:
```Python
 while len(items) != 0:
            print('Os Itens disponíveis no supermercado estão abaixo:')
            for item in items:
                for key, value in item.items():
                    print(key, ':', value)
                    print('--------------')
            break
```
Os valores registrados em cada chave para cada dicionário são printados.

## Adicionar Itens

O Item em promoção será registrado em um dicionário chamado `item`.

Esse dicionário tem 3 chaves: 
>nome, quantidade e preço.

Portanto, cada item da array `itens` será salvo como uma tabela.

|Nome|Quantidade|Preço|
|----|----------|-----|
|`not null`|Número `int`|Número `float`|

Esse valores serão, posteriormente, adicionados por meio de um `.append()` na array `items`

## Comprar Itens

Nessa etapa do código serão computadas as compras, portanto após o print de todos os registros presentes em `items`.

É requerido ao usuário que ele digite o `item_de_compra` e a `quantidade_de_compra`.

Por meio do nome do item de compra o dicionário é acessado.
```Python
 for item in items:
            if item_de_compra.lower() == item['nome'].lower() :
                if (item['quantidade'] != 0 & item['quantidade'] > 0 & item['quantidade'] > quantidade_de_compra):
                    print('Pague ', quantidade_de_compra*item['preço'] , 'R$ no Balção.')
                    item['quantidade']-= quantidade_de_compra                    
                else:                     
                    print('Item fora de Estoque.')
```
Uma vez dentro do dicionário em questão são realizadas as baixas nas quantidades que são compradas e calculado o valor que deve-se pagar no balcão. Caso não haja quantidade suficiente para satisfazer a compra é informado que o item está fora de estoque

## Pesquisar Itens

Toda array `items` será percorrida e comparada com o nome registado em `achar_item`.

Caso o item seja encontrado as informações deste item serão exibidas no terminal.

## Editar Itens

É requisitado o nome do item que deseja-se modificar.

Uma vez encontrado este `item` na array `items` são exibidos os valores atualmente registrados no dicionário em questão. Conforme o código abaixo:

```Python
for item in items:
            if item_mod.lower() == item['nome'].lower():

                print('Abaixo estão os detalhes de ' + item_mod)
                print(item)
```

Num processo análogo ao presente a _Adicionar Itens_ os valores registrados nas chaves são reescritos.
Após a atualização é informado no terminal que os dados foram atualizados.

```Python
    while True:
        try:
            item['quantidade'] = int(input('Quantidade do Item : '))
            break
        except ValueError:
            print('Quantidade do Item deve ser registrada como Nº Inteiro')
    
    while True:
        try:
            item['preço'] = float(input('Valor do Item R$ : '))
            break
        except ValueError:
            print('O Preço deve ser um Valor Numérico no formato xx.xx')
    print('O Item foi atualizado!!!')
    print(item)
```

## Fechar o Programa

Como o programa funciona num loop de `while True` é preciso de um break para "Fechar" o programa

**_Ao Digitar 6 o programa é finalizado_**