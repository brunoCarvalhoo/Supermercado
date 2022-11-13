#-----------------Sistema de Gestão de Supermercado--------------------

# Os itens registrados serão guardados no array items.
# Esta Array é uma array em que serão adicionados cada dicionário.
items = []

while True:
    display = input('Presione Enter para Continuar')
    print('------------------Bem Vindo ao Supermercado------------------')
    print('1. Listar Itens\n2. Adicionar Itens para Promoção\n3. Comprar Itens\n4. Pesquisar Itens \n5. Editar itens\n6. Sair do Programa')
    escolha = input('Digite o Número de sua escolha : ')

    if escolha == '1' :
        print('------------------Listar Itens------------------')

        # Na função abaixo, tem-se a quantidade de itens registradas

        print('A quantidade de Materiais Presentes no estoque é de: ',len(items))
        
        # Na função abaixo, mostramos todos os itens que foram registrados na array de dicionários e seus valores

        while len(items) != 0:
            print('Os Itens disponíveis no supermercado estão abaixo:')
            for item in items:
                # No Loop abaixo, exibimos todos os valores registrados em cada dicionário presente na Array item().
                for key, value in item.items():
                    print(key, ':', value)
                    print('--------------')
            break

    elif escolha == '2' :
        print('------------------Adicionar Itens para Promoção------------------')
        print('Para adicionar um item preencha os dados abaixo:')

        # Criou-se um dicionário chamado de item e através dele vamos adicionar informações como:
        # Nome do Item, Quantidade e Preço para que posteriormente possamos adicionar essas informações no Array Principal

        item = {}
        item['nome'] = input('Nome do Item : ')

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
        
        print('O Item foi adicionado com Sucesso.')
        # Através do Append() o item adicionado é adicionado no final da Array items[]
        items.append(item)

    elif escolha == '3' :

        print('------------------Comprar Itens------------------')
        print(items)
        item_de_compra = input('Qual Item você deseja Comprar? Insira o Nome : ')
        quantidade_de_compra = int(input('Qual a quantidade que você deseja? Digite o Nº:'))

        # No Loop abaixo nós localizamos o item com base no nome e substrai-se na quantidade presente do estoque

        for item in items:
            if item_de_compra.lower() == item['nome'].lower() :
                if (item['quantidade'] != 0 & item['quantidade'] > 0 & item['quantidade'] > quantidade_de_compra):
                    print('Pague ', quantidade_de_compra*item['preço'] , 'R$ no Balção.')
                    item['quantidade']-= quantidade_de_compra                    
                else:                     
                    print('Item fora de Estoque.')

    elif escolha == '4' :
        
        print('------------------Procurar Itens------------------')
        achar_item = input('Entre com o Nome do Item para Pesquisa : ')
        
        # Nesta etapa pesquisamos na base de dados na string se existe o registro do item
        
        for item in items:
            if item['nome'].lower() == achar_item.lower():
                
                print('O Item chamado: ' + achar_item + ' é exibido abaixo com seus detalhes')
                print(item)
            else:
                print('Item não foi Encontrado.')

    elif escolha == '5' :
        
        print('------------------Editar Itens------------------')
        item_mod = input('Digite o nome do item que deseja-se modificar: ')

        for item in items:
            if item_mod.lower() == item['nome'].lower():

                # Mostra-se as informações registradas sobre os itens.

                print('Abaixo estão os detalhes de ' + item_mod)
                print(item)

                # Abaixo desta linha são requisitadas as informações para modificar os valores atualmente registrados no item em questão

                item['nome'] = input('Nome do Item : ')

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
            else:
                print('Item não Encontrado')
                
    elif escolha == '6' :
        print('------------------Fechou o Programa------------------')
        break

    else: 
         print('Um valor inválido foi digitado. Por favor digite um valor válido')
