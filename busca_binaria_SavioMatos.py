# Savio Agusto de Oliveira Matos — Estrutura de Dados II

# Parte 1 
def busca_binaria_iterativa(L, x):
    ini = 0
    fim = len(L) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        valor = L[meio]
        if valor == x:
            return meio
        if valor < x:
            ini = meio + 1
        else:
            fim = meio - 1
    return -1


# Parte 2 
def busca_binaria_recursiva(L, x, ini, fim):
    if ini > fim:
        return -1

    meio = (ini + fim) // 2
    valor = L[meio]
    if valor == x:
        return meio
    if valor < x:
        return busca_binaria_recursiva(L, x, meio + 1, fim)
    return busca_binaria_recursiva(L, x, ini, meio - 1)


# Parte 3
# 

# TESTES
L = [3, 8, 15, 21, 30, 42, 57, 66, 74, 89]
casos = [(57, 6), (3, 0), (89, 9), (30, 4), (10, -1), (1, -1), (100, -1)]
for x, esperado in casos:
    assert busca_binaria_iterativa(L, x) == esperado, f"iterativa: x={x} deveria dar {esperado}"
    assert busca_binaria_recursiva(L, x, 0, len(L) - 1) == esperado, f"recursiva: x={x} deveria dar {esperado}"
assert busca_binaria_iterativa([], 5) == -1, "iterativa: lista vazia deveria dar -1"
assert busca_binaria_recursiva([], 5, 0, -1) == -1, "recursiva: lista vazia deveria dar -1"
assert busca_binaria_iterativa([42], 42) == 0, "iterativa: lista com um elemento"
assert busca_binaria_recursiva([42], 42, 0, 0) == 0, "recursiva: lista com um elemento"
grande = list(range(0, 2_000_000, 2))
assert busca_binaria_iterativa(grande, 1_999_998) == 999_999, "iterativa: lista grande"
assert busca_binaria_recursiva(grande, 1_999_998, 0, len(grande) - 1) == 999_999, "recursiva: lista grande"
assert busca_binaria_recursiva(grande, 7, 0, len(grande) - 1) == -1, "recursiva: ausente na lista grande"
print("Todos os testes passaram!")  
