# GERENCIADOR DE TAREFAS EM PYTHON

sair = 0

print("Menu do gerenciador")
while sair != 6:
    comando = int(input("""Gerenciador de tarefas
                    [1] Adicionar uma tarefa
                    [2] Atualizar uma tarefa
                    [3] Visualizar lista de tarefas
                    [4] Marcar tarefa como concluida
                    [5] Limpar tarefas concluidas
                    [6] Sair
                    Digite o numero de um comando
                    """))
    
    if comando > 6 or comando != int:
        print("Comando inexistente!!")
    elif 