import requests
import json
import pandas as pd


def jogos_do_dia():
    import requests

    url = "https://api.sofascore.com/api/v1/sport/football/scheduled-events/2023-03-22"

    payload = ""
    headers = {
        "authority": "api.sofascore.com",
        "accept": "*/*",
        "accept-language": "pt-BR,pt-PT;q=0.9,pt;q=0.8,en-US;q=0.7,en;q=0.6",
        "cache-control": "max-age=0",
        "dnt": "1",
        "if-none-match": "W/'52d773b869'",
        "origin": "https://www.sofascore.com",
        "referer": "https://www.sofascore.com/",
        "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }

    response = requests.request("GET", url, data=payload, headers=headers)

    json_data = json.loads(response.text)

    # df = pd.json_normalize(json_data, record_path=['tournament'], meta=[['name','slug',['category', 'name']]])

    df = pd.json_normalize(json_data, record_path=['events'])

    df.to_excel('dados_stats.xlsx', index=False)
    # df = pd.json_normalize(json_data, record_path=[['events','tournament', 'name'], ['events','tournament','category', 'name'],])

    # print(df)

    # def qq():
    #     lst_torneio = []
    #     lst_pais = []
    #     lst_pais_slug = []
    #     lst_torneio_slug = []
    #     lst_tem_estatistica1 = []
    #     lst_tem_grafico = []
    #     lst_prioridade = []
    #     lst_id = []
    #     lst_cod = []
    #     lst_time_casa = []
    #     lst_time_fora = []
    #     lst_score_time_casa = []
    #     lst_score_time_fora = []
    #     lst_tempo_extra1 = []
    #     lst_tempo_extra2 = []
    #     lst_tempo_agora = []
    #     lst_prev_termino = []
    #     lst_tem_estatistica2 = []
    #     lst_id_evento = []
    #     lst_data_hora_inicio_jogo = []
    #     lst_evento_slug = []

    # for game in json_data['events']:
    #     torneio = game['tournament']['name']
    #     pais = game['tournament']['category']['name']
    #     pais_slug = game['tournament']['category']['slug']
    #     torneio_slug = game['tournament']['uniqueTournament']['slug']
    #     tem_estatistica1 = game['tournament']['uniqueTournament']['hasEventPlayerStatistics']
    #     tem_grafico = game['tournament']['uniqueTournament']['hasPerformanceGraphFeature']
    #     prioridade = game['tournament']['priority']
    #     id = game['tournament']['id']
    #     cod = game['customId']
    #     time_casa = game['homeTeam']['name']
    #     time_fora = game['awayTeam']['name']
        
    #     score_time_casa = None
    #     score_time_fora = None
    #     try:
    #         score_time_casa = game['homeScore']['display']
    #         score_time_fora = game['awayScore']['display']
    #     except:
    #         pass

    #     tempo_extra_1 = None
    #     tempo_extra_2 = None
    #     try:
    #         tempo_extra_1 = game['time']['injuryTime1']
    #     except:
    #         pass
    #     try:
    #         tempo_extra_2 = game['time']['injuryTime2']
    #     except:    
    #         pass
    #     try:       
    #         tempo_agora = game['time']['currentPeriodStartTimestamp']
    #     except:
    #         tempo_agora = None
        
    #     prev_termino = game['changes']['changeTimestamp']
        
    #     tem_estatistica2 = None
    #     try:
    #         tem_estatistica2 = game['hasEventPlayerStatistics']
    #     except:
    #         tem_estatistica2 = None

    #     id_evento = game['id']
    #     data_hora_inicio_jogo = game['startTimestamp']
    #     evento_slug = game['slug']
        
    #     lst_torneio.append(torneio)
    #     lst_pais.append(pais)
    #     lst_pais_slug.append(pais_slug)
    #     lst_torneio_slug.append(torneio_slug)
    #     lst_tem_estatistica1.append(tem_estatistica1)
    #     lst_tem_grafico.append(tem_grafico)
    #     lst_prioridade.append(prioridade)
    #     lst_id.append(id)
    #     lst_cod.append(cod)
    #     lst_time_casa.append(time_casa)
    #     lst_time_fora.append(time_fora)
    #     lst_score_time_casa.append(score_time_casa)
    #     lst_score_time_fora.append(score_time_fora)
    #     lst_tempo_extra1.append(tempo_extra_1)
    #     lst_tempo_extra2.append(tempo_extra_2)
    #     lst_tempo_agora.append(tempo_agora)
    #     lst_prev_termino.append(prev_termino)
    #     lst_tem_estatistica2.append(tem_estatistica2)
    #     lst_id_evento.append(id_evento)
    #     lst_data_hora_inicio_jogo.append(data_hora_inicio_jogo)
    #     lst_evento_slug.append(evento_slug)
        

    # dados = {'torneio': lst_torneio,'pais': lst_pais,'pais_slug': ,'torneio_slug': ,'tem_estatistica1': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': ,'': }

    # .append()
    # .append()
    # lst_pais_slug.append()
    # lst_torneio_slug.append()
    # lst_tem_estatistica1.append()
    # lst_tem_grafico.append(tem_grafico)
    # lst_prioridade.append(prioridade)
    # lst_id.append(id)
    # lst_cod.append(cod)
    # lst_time_casa.append(time_casa)
    # lst_time_fora.append(time_fora)
    # lst_score_time_casa.append(score_time_casa)
    # lst_score_time_fora.append(score_time_fora)
    # lst_tempo_extra1.append(tempo_extra_1)
    # lst_tempo_extra2.append(tempo_extra_2)
    # lst_tempo_agora.append(tempo_agora)
    # lst_prev_termino.append(prev_termino)
    # lst_tem_estatistica2.append(tem_estatistica2)
    # lst_id_evento.append(id_evento)
    # lst_data_hora_inicio_jogo.append(data_hora_inicio_jogo)
    # lst_evento_slug.append(evento_slug)


        # print(pais,' | ', time_casa, score_time_casa, ' x ',score_time_fora, time_fora)

    # print(json_data)

    
jogos_do_dia()