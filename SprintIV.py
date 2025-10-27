import random

produtos = [
    "Água Destilada", "Solução Salina", "Ácido Clorídrico", "Etanol 70%",
    "Glicerina", "Peróxido de Hidrogênio", "Fórmula X", "Máscara"
]

dias = 5
estoque_inicial = {p: random.randint(5, 15) for p in produtos}
max_estoque = 20

def simularConsumoDias(produtos, dias):
    return [[(p, random.randint(1, 8)) for p in produtos] for _ in range(dias)]

consumo_simulado = simularConsumoDias(produtos, dias)

def dp(dia, produto_idx, estoque, memo):
    if dia == dias:
        return 0
    chave = (dia, produto_idx, estoque)
    if chave in memo:
        return memo[chave]
    melhor = float('inf')
    consumo = consumo_simulado[dia][produto_idx][1]
    for repor in range(max_estoque - estoque + 1):
        novo_estoque = min(max_estoque, estoque + repor)
        falta = max(consumo - novo_estoque, 0)
        estoque_apos = max(0, novo_estoque - consumo)
        proximo = dp(dia + 1, produto_idx, estoque_apos, memo)
        melhor = min(melhor, falta + proximo)
    memo[chave] = melhor
    return melhor

def dp_iterativo():
    dp_table = [[[float('inf')] * (max_estoque+1) for _ in range(len(produtos))] for _ in range(dias+1)]
    for idx in range(len(produtos)):
        for est in range(max_estoque+1):
            dp_table[dias][idx][est] = 0
    for dia in range(dias-1, -1, -1):
        for idx in range(len(produtos)):
            consumo = consumo_simulado[dia][idx][1]
            for est in range(max_estoque+1):
                for repor in range(max_estoque - est + 1):
                    novo_estoque = min(max_estoque, est + repor)
                    falta = max(consumo - novo_estoque, 0)
                    estoque_apos = max(0, novo_estoque - consumo)
                    val = falta + dp_table[dia + 1][idx][estoque_apos]
                    if val < dp_table[dia][idx][est]:
                        dp_table[dia][idx][est] = val
    resultado = 0
    for idx, p in enumerate(produtos):
        resultado += dp_table[0][idx][estoque_inicial[p]]
    return resultado

resultado_recursivo = sum([dp(0, idx, estoque_inicial[p], {}) for idx, p in enumerate(produtos)])
resultado_iterativo = dp_iterativo()
print("\n============ Falta mínima em %d dias ===========" % dias)
print(f"Falta mínima recursivo: {resultado_recursivo}")
print(f"Falta mínima iterativo: {resultado_iterativo}")
assert resultado_recursivo == resultado_iterativo

def simularConsumo(produtos):
    consumos = []
    num_produtos_hoje = random.randint(2, len(produtos))
    produtos_hoje = random.sample(produtos, num_produtos_hoje)
    for p in produtos_hoje:
        valor = random.randint(1, 20)
        consumos.append((p, valor))
    return consumos

def buscaSequencial(lista, produto):
    for i in range(len(lista)):
        if lista[i][0] == produto:
            return i
    return -1

def mergeSort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = mergeSort(lista[:meio])
    direita = mergeSort(lista[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i][1] <= direita[j][1]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def quickSort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    menores = [x for x in lista[1:] if x[1] <= pivot[1]]
    maiores = [x for x in lista[1:] if x[1] > pivot[1]]
    return quickSort(menores) + [pivot] + quickSort(maiores)

consumos = simularConsumo(produtos)
fila = []
pilha = []

for c in consumos:
    fila.append(c)
    pilha.append(c)

print("\nProdutos utilizados hoje:")
for p in consumos:
    print(f"{p[0]} - Quantidade utilizada: {p[1]}")

produtos_para_pedir = []

while True:
    print("\nProdutos disponíveis para consulta hoje:")
    for p in [c[0] for c in consumos]:
        print("-", p)
    produto_busca = input("\nDigite o produto que deseja consultar: ")
    indice_produto = buscaSequencial(consumos, produto_busca)
    if indice_produto != -1:
        print(f"\nQuantidade de {produto_busca} consumida hoje: {consumos[indice_produto][1]}")
        while True:
            resposta = input(f"Deseja pedir mais {produto_busca}? (sim/não): ").lower()
            if resposta == "sim":
                while True:
                    try:
                        quantidade = int(input(f"Digite a quantidade que deseja pedir de {produto_busca}: "))
                        print(f"Pedido de {quantidade} unidades de {produto_busca} registrado.")
                        produtos_para_pedir.append(f"{produto_busca} ({quantidade})")
                        break
                    except ValueError:
                        print("Por favor, digite um número válido.")
                break
            elif resposta == "não":
                print("Nenhum pedido realizado.")
                break
            else:
                print("Resposta inválida. Digite 'sim' ou 'não'.")
        while True:
            continuar = input("\nDeseja consultar outro produto? (sim/não): ").lower()
            if continuar == "sim":
                break
            elif continuar == "não":
                sair_loop = True
                break
            else:
                print("Resposta inválida. Digite 'sim' ou 'não'.")
        if 'sair_loop' in locals() and sair_loop:
            break
    else:
        print("Produto não encontrado. Tente novamente.")

print("\nProdutos que deseja pedir mais:", produtos_para_pedir)

consumos_merge = mergeSort(consumos)
print("\nConsumos ordenados por quantidade (Merge Sort):")
for p in consumos_merge:
    print(f"{p[0]} - Quantidade utilizada: {p[1]}")

consumos_quick = quickSort(consumos)
print("\nConsumos ordenados por quantidade (Quick Sort):")
for p in consumos_quick:
    print(f"{p[0]} - Quantidade utilizada: {p[1]}")
