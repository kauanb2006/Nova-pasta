


            # print("1. Cadastrar jogador)

def cadastrar_jogador(jogadores, idade,nome,posicao,time_id):
    novo_jogador={
        "id" : len (jogadores) + 1,
        "idade" : idade,
        "nome" : nome,
        "posicao" :posicao ,
        "time_id" : time_id

    }
    jogadores.append(novo_jogador)
    print("Jogador cadastrado com sucesso.")

# -----------------------fim----------------------------------
    

            # print("2. Apagar jogador")
def apagar_jogador(jogadores):
    print("\nApagar Jogador")
    jogador_id = int(input("Digite o ID do jogador a ser apagado: "))

    for index, jogador in enumerate(jogadores):
        if jogador["id"] == jogador_id:
            del jogadores[index]
            print("Jogador apagado com sucesso!\n")
            break
    else:
        print("Jogador não encontrado.\n")

#-------------------------- fim-------------------------------------
        
        
            # print("3. Atualizar jogador")
def atualizar_jogador(jogadores, id_jogador, novo_nome=None, nova_idade=None, nova_posicao=None):
    for jogador in jogadores:
        if int(jogador['id']) == int( id_jogador):
            if novo_nome:
                jogador['nome'] = novo_nome
            if nova_idade:
                jogador['idade'] = nova_idade
            if nova_posicao:
                jogador['posicao'] = nova_posicao
            print(f"Perfil do jogador com ID {id_jogador} atualizado com sucesso.")
            return
    print(f"Jogador com ID {id_jogador} não encontrado.")

#--------------------------------- fim------------------------------------
            #print("4. Trocar jogador de time")
def trocar_jogador_de_time(jogadores):
    print("\nTrocar Jogador de Time")
    id_jogador = int(input("Digite o ID do jogador a ter o time alterado: "))
    novo_time_id = int(input("Digite o novo ID do time para o jogador: "))

    for jogador in jogadores:
        if jogador["id"] == id_jogador:
            jogador["time_id"] = novo_time_id
            print("Time do jogador atualizado com sucesso!\n")
            break
    else:
        print("Jogador não encontrado.\n")

# ------------------------------------fim-------------------------------------------------


                # print("5. Cadastrar time")
        
def cadastrar_time(times,cidade,nome,):
    novo_time={
        "id" : len (times) + 1,
        "nome" : nome,
        "cidade" : cidade
        }
    times.append(novo_time)
    print("time cadastrado com sucesso.")

 # ----------------------------------fim-----------------------------------
                     # print("6. Apagar time")
    

def apagar_times(times, jogadores, id_time):
    time_removido = None
    for time in times:
        if int(time["id"]) == int(id_time):
            time_removido = time
            times.remove(time)
            break

    if time_removido:
        jogadores_restantes = [jogador for jogador in jogadores if int(jogador["time_id"]) != int(id_time)]
        jogadores.clear()
        jogadores.extend(jogadores_restantes)
        print(f"Time com ID {id_time} e todos os jogadores associados foram removidos com sucesso.")
    else:
        print(f"Time com ID {id_time} não encontrado.")



#---------------------------------fim----------------------------------


                    #print("7. Atualizar time")
    
def atualizar_time(times,id_time , novo_nome = None , nova_cidade = None):
    for time in times:
        if str(time['id']) == str(id_time):
            if novo_nome:
                time['nome'] = novo_nome
            if nova_cidade:
                time['cidade'] = nova_cidade
            
        print(f" perfil do time com ID {id_time} atualizado com sucesso")
        return times
    print(f"Time com ID {id_time} não encontrada")
#--------------------------------- fim------------------------------------
      
def consultar_jogadores_por_time(times, jogadores):
    print("\nConsultar Jogadores por Time")
    time_id = int(input("Digite o ID do time que deseja consultar os jogadores: "))

    # Verifica se o time existe na lista de times
    time_existente = False
    for time in times:
        if time["id"] == time_id:
            time_existente = True
            break
  

    if time_existente == True:
        jogadores_time = [jogador for jogador in jogadores if jogador["time_id"] == time_id]

        if len(jogadores_time) > 0:
            print(f"\nJogadores do Time ID {time_id}:")
            for jogador in jogadores_time:
                print(f"ID: {jogador['id']}")
                print(f"Nome: {jogador['nome']}")
                print(f"Idade: {jogador['idade']}")
                print(f"Posição: {jogador['posicao']}")
                print("----------------------")
        else:
            print("Não há jogadores cadastrados para este time.\n")
    else:
        print("Time não encontrado.\n")

#--------------------------------fim ------------------------------------
        # print("9. Emitir relatório: Lista de todos os jogadores")
def ver_todos_jogadores(jogadores):
    print("\nLista de Todos os Jogadores:")
    if len(jogadores) > 0:
        for jogador in jogadores:
            print(f"ID: {jogador['id']}")
            print(f"Nome: {jogador['nome']}")
            print(f"Idade: {jogador['idade']}")
            print(f"Posição: {jogador['posicao']}")
            print(f"Time ID: {jogador['time_id']}")
            print("----------------------")
    else:
        print("Não há jogadores cadastrados.\n")

#--------------------------------fim-------------------------------------------
        #print("10. Emitir relatório: Lista de todos os times")

def ver_todos_times(times):
    print("\nLista de Todos os Times:")
    if len(times) > 0:
        for time in times:
            print(f"ID: {time['id']}")
            print(f"Nome: {time['nome']}")
            print(f"Cidade: {time['cidade']}")
            print("----------------------")
    else:
        print("Não há times cadastrados.\n")

#---------------------------------fim -------------------------------------------------
