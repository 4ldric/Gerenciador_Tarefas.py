# GERENCIADOR DE TAREFAS EM PYTHON

def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "concluida": False}
    tarefas.append(tarefa)
    print(f'A tarefa {nome_tarefa} foi adicionada com sucesso!')
    return


def visualizar_tarefa():
    print("\n Lista de tarefas")
    for indice, tarefa in enumerate(tarefas, start = 1):
        status = "✓" if tarefa["concluida"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f'{indice}. [{status}] {nome_tarefa}')
    return


def atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_ajustado = indice_tarefa - 1
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Tarefa não existe!!")
    return

def concluir_tarefa(tarefas, indice_tarefa):
    indice_ajustado = indice_tarefa - 1
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        tarefas[indice_ajustado]["concluida"] = True 
        print(f'Tarefa: {tarefas[indice_ajustado]["tarefa"]} foi marcada como concluida')
    else:
        print("Tarefa não existe!!")
    return

tarefas = []

print("==Menu do gerenciador==")

while True:
    comando = int(input("""
[1] Adicionar uma tarefa
[2] Visualizar lista de tarefas
[3] Atualizar uma tarefa
[4] Marcar tarefa como concluida
[5] Limpar tarefas concluidas
[6] Sair
                        
Digite o numero de um comando: """))

    if comando == 1:
        nome_tarefa = input("Adicione uma tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif comando == 2:
        visualizar_tarefa()
    elif comando == 3:
        visualizar_tarefa()
        indice_tarefa = int(input("Digite o numero da tarefa: "))
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, indice_tarefa, novo_nome)
    elif comando == 4:
        visualizar_tarefa()
        indice_tarefa = int(input("Digite o numero da tarefa: "))
        concluir_tarefa(tarefas, indice_tarefa)
    elif comando == 6:
        break

print("Programa Finalizado")
