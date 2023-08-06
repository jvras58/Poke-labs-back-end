from models.modelos import Pokemon,Tipo_Pokemon,Habilidade

class dadosfakes:
    def pokemon():
        # pokes
        pikachu =    Pokemon(
                            name='Pikachu',
                            altura=0.4,
                            peso=6.0
        )

        charmander = Pokemon(
                            name='Charmander',
                            altura=0.6, 
                            peso=8.5
        )

        bulbasaur =  Pokemon(
                        name='Bulbasaur',
                        altura=0.7,
                        peso=6.9
        )

        # tipos
        eletrico = Tipo_Pokemon(
                            name='Elétrico'
        )

        fogo =     Tipo_Pokemon(
                            name='Fogo'
        )

        planta = Tipo_Pokemon(
                            name='Planta'
        )

        # poderes
        choque_do_trovao = Habilidade(
                                        name='Choque do Trovão',
                                        descricao='Um ataque elétrico famoso peita lendario'
        )

        lanca_chamas = Habilidade(
                                        name='Lança-Chamas',
                                        descricao='Um ataque de fogo'
        )

        raio_solar = Habilidade(
                                        name='Raio Solar',
                                        descricao='Um ataque de planta'
        )

        #associa os objetos usando os atributos de relacionamento
        #como não vai ser igual a o pcctec eu não consigo fazer o append direto quando eu pego um tipo por exemplo ja que são dados fakes...
        pikachu.tipo.append(eletrico)
        charmander.tipo.append(fogo)
        bulbasaur.tipo.append(planta)

        pikachu.habilidades.append(choque_do_trovao)
        charmander.habilidades.append(lanca_chamas)
        bulbasaur.habilidades.append(raio_solar)

