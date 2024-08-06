# lista
cidades = ['Brasília', 'Taguatinga', ' Planaltina', 'Ceilândia', 'Samambaia', 'Riacho Fundo', 'Canadangolândia', 'Núcleo bandeirante', 'Gama', 'Santa maria', 'Sobradinho', 'Planaltina', 'Recanto das emas', 'Guará', 'Valparaíso', 'Novo gama', 'Céu azul', 'Lago do sul', 'Formosa', 'Sol nascente', 'Estrutural', 'Águas claras', 'Arniqueiras', 'Arial', 'Sol nascente', 'Dvo', 'São sebastião', 'Dvo'] 

# cidade a ser pesquisada
cidade_pesquisada = input('Cidade a ser pesquisada: ').capitalize()

# conta a quantidade de ocorrências da palavra
cont = cidades.count(cidade_pesquisada)

# exibe o resultado 
print(f'{cidade_pesquisada} foi encontrada {cont} vezes.')