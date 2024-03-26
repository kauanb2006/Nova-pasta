from lib.funcoes import (
    ver_todos_times, ver_todos_jogadores, apagar_times, 
    consultar_jogadores_por_time, cadastrar_time, cadastrar_jogador, 
    apagar_jogador, atualizar_jogador, trocar_jogador_de_time, atualizar_time
)
from database import times, jogadores

def main():
    while True:
        print("Menu:")
        print("1. Cadastrar jogador")
        print("2. Apagar jogador")
        print("3. Atualizar jogador")
        print("4. Trocar jogador de time")
        print("5. Cadastrar time")
        print("6. Apagar time")
        print("7. Atualizar time")
        print("8. Emitir relatório: Jogadores de um time específico")
        print("9. Emitir relatório: Lista de todos os jogadores")
        print("10. Emitir relatório: Lista de todos os times")
        print("0. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            nome = input("Digite o nome do jogador: ")
            idade = input("Digite a idade do jogador: ")
            posicao = input("Digite a posição que o jogador joga: ")
            time_id = input("Digite o id do time: ")
            cadastrar_jogador(jogadores, nome, idade, posicao, time_id)

        elif opcao == '2':
            apagar_jogador(jogadores)

        elif opcao == '3':
            id_jogador = input("Digite o ID do jogador que deseja atualizar: ")
            novo_nome = input("Digite o novo nome (ou deixe em branco para manter o mesmo): ")
            nova_idade = input("Digite a nova idade (ou deixe em branco para manter a mesma): ")
            nova_posicao = input("Digite a nova posição (ou deixe em branco para manter a mesma): ")
            atualizar_jogador(jogadores, id_jogador, novo_nome, nova_idade, nova_posicao)

        elif opcao == '4':
            trocar_jogador_de_time(jogadores)

        elif opcao == '5':
            nome_time = input("Digite o nome do time: ")
            cidade_time = input("Digite a cidade do time: ")
            cadastrar_time(times, cidade_time, nome_time)

        elif opcao == '6':
            
            id_time_a_remover = input("Digite o ID do time para remover: ")
            apagar_times(times, jogadores, id_time_a_remover)

        elif opcao == '7':
            id_time = input("Digite o ID do time que deseja atualizar: ")
            novo_nome = input("Digite o novo nome do time (ou deixe em branco para manter o mesmo): ")
            nova_cidade = input("Digite a nova cidade do time (ou deixe em branco para manter a mesma): ")
            atualizar_time(times, id_time, novo_nome, nova_cidade)

        elif opcao == '8':
            consultar_jogadores_por_time(times, jogadores)

        elif opcao == '9':
            ver_todos_jogadores(jogadores)

        elif opcao == '10':
            ver_todos_times(times)

        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()