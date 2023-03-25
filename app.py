import streamlit as st
import pandas as pd
from pandas import json_normalize
from datetime import datetime, date
import json
import pandas as pd
# import cfscrape
import io
# from github import Github


# def upload_to_github(token, repo_name, file_path, commit_message):
#     g = Github(token)
#     repo = g.get_repo(repo_name)

#     #excluir arquivo existente no github
#     file = repo.get_contents('dados-stats.csv')
#     repo.delete_file(file.path, commit_message, file.sha)
    
#     #upload de novo arquivo
#     repo.create_file('dados-stats.csv', commit_message, file_path)

# def data(tipo): 
#     if tipo == 'dataframe':
#         today = datetime.today().strftime('%d_%m_%H_%M')
#     elif tipo == 'dia':
#         today = datetime.today().strftime('%Y-%m-%d')
#     return today

# def odd_frac_dec(odd_frac):
#     ##odds decimais
#     partes = odd_frac.split("/")
#     numerador = int(partes[0])
#     denominador = int(partes[1])
    
#     return (numerador / denominador) + 1

# def odd_dec_prob(odd_dec):
#     return 1/odd_dec *100

# def jogos_do_dia(dia):
#     url = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{dia}"

#     payload = ""
#     headers = {
#         "authority": "api.sofascore.com",
#         "accept": "*/*",
#         "accept-language": "pt-BR,pt-PT;q=0.9,pt;q=0.8,en-US;q=0.7,en;q=0.6",
#         "cache-control": "max-age=0",
#         "dnt": "1",
#         "if-none-match": "W/'52d773b869'",
#         "origin": "https://www.sofascore.com",
#         "referer": "https://www.sofascore.com/",
#         "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": '"Windows"',
#         "sec-fetch-dest": "empty",
#         "sec-fetch-mode": "cors",
#         "sec-fetch-site": "same-site",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
#     }
    
    #evitar o erro 403
#     scraper = cfscrape.create_scraper()
#     response = scraper.request("GET", url, data=payload, headers=headers)

#     response = requests.request("GET", url, data=payload, headers=headers)
    
    
#     json_data = json.loads(response.text)

#     df = pd.json_normalize(json_data, record_path=['events'])

#     df_modificado = df.drop(columns=['winnerCode', 'hasGlobalHighlights', 'hasEventPlayerHeatMap', 'detailId', 'finalResultOnly', 'tournament.category.sport.name', 'tournament.category.sport.slug', 'tournament.category.sport.id', 'tournament.category.flag', 'tournament.uniqueTournament.name', 'tournament.slug', 'tournament.uniqueTournament.category.name', 'tournament.uniqueTournament.category.slug', 'tournament.uniqueTournament.category.sport.name', 'tournament.uniqueTournament.category.sport.slug', 'tournament.uniqueTournament.category.sport.id', 'tournament.uniqueTournament.category.id', 'tournament.uniqueTournament.category.flag', 'tournament.uniqueTournament.userCount', 'hasEventPlayerStatistics', 'tournament.uniqueTournament.crowdsourcingEnabled', 'tournament.uniqueTournament.hasPerformanceGraphFeature', 'tournament.uniqueTournament.displayInverseHomeAwayTeams', 'tournament.priority', 'roundInfo.round', 'status.code', 'status.type', 'homeTeam.slug', 'homeTeam.shortName', 'homeTeam.sport.name', 'homeTeam.sport.slug', 'homeTeam.sport.id', 'homeTeam.userCount', 'homeTeam.type', 'homeTeam.subTeams', 'homeTeam.teamColors.primary', 'homeTeam.teamColors.secondary', 'homeTeam.teamColors.text', 'awayTeam.slug', 'awayTeam.sport.name', 'awayTeam.shortName', 'awayTeam.sport.slug', 'awayTeam.sport.id', 'awayTeam.userCount', 'awayTeam.type', 'awayTeam.subTeams', 'awayTeam.teamColors.secondary', 'awayTeam.teamColors.primary', 'awayTeam.teamColors.text', 'homeScore.display', 'awayScore.display', 'changes.changes', 'roundInfo.name', 'roundInfo.cupRoundType', 'homeTeam.disabled', 'awayTeam.disabled', 'time.initial', 'time.max', 'time.extra', 'statusTime.prefix', 'statusTime.max', 'statusTime.initial', 'tournament.category.alpha2', 'tournament.uniqueTournament.category.alpha2','tournament.category.slug','tournament.category.id', 'lastPeriod', 'statusTime.timestamp', 'statusTime.extra','time.currentPeriodStartTimestamp', 'changes.changeTimestamp'])

#     df_renomeado = df_modificado.rename(columns={'id':'Id_Evento','startTimestamp': 'Data_Hora', 'slug': 'Evento_Slug', 'tournament.name': 'Torneio', 'tournament.category.name': 'Pais', 'tournament.category.slug': 'Pais_Slug', 'tournament.uniqueTournament.slug': 'Torneio_Slug', 'tournament.uniqueTournament.id': 'Id_Unico_Torneio', 'tournament.uniqueTournament.hasEventPlayerStatistics': 'Evento_com_Estats', 'tournament.id': 'Id_Torneio', 'status.description': 'Status_Partida', 'homeTeam.name': 'Time_Casa', 'homeTeam.id': 'Id_Time_Casa', 'awayTeam.name': 'Time_Fora', 'awayTeam.id': 'Id_Time_Fora', 'homeScore.current': 'Gols_Casa', 'homeScore.period1': 'Gols_Casa_1T', 'homeScore.period2': 'Gols_Casa_2T', 'homeScore.normaltime': 'Gols_Casa_Tempo_Normal','awayScore.current': 'Gols_Fora', 'awayScore.period1': 'Gols_Fora_1T', 'awayScore.period2': 'Gols_Fora_2T', 'awayScore.normaltime': 'Gols_Fora_Tempo_Normal', 'time.injuryTime1': 'Tempo_Extra_1T','time.injuryTime2': 'Tempo_Extra_2T', 'awayRedCards': 'Cartao_Vermelho_Fora', 'homeRedCards': 'Cartao_Vermelho_Casa'})

#     df_renomeado['Data_Hora'] = df_renomeado['Data_Hora'].fillna(0)

#     df_renomeado['Data_Hora'] = pd.to_datetime(df_renomeado
#     ['Data_Hora'], unit='s').apply(lambda x: datetime.fromtimestamp(x.timestamp()).strftime('%d/%m/%Y %H:%M'))
   
#     #ordenar dataframe de acordo com a coluna Data_Hora
#     df_renomeado['Data_Hora'] = pd.to_datetime(df_renomeado['Data_Hora'])

#     df_renomeado['link_temp'] = 'https://www.sofascore.com/'+df_renomeado['Evento_Slug'] + '/'+ df_renomeado['customId']

#     df_renomeado.insert(0, 'Link', df_renomeado['link_temp'])
    
#     df_final = df_renomeado.drop(columns=['link_temp'])

#     df_final = df_final.sort_values(by='Data_Hora')

#     return df_final
        
# def odds_do_dia(dia):
    
#     url = f"https://api.sofascore.com/api/v1/sport/football/odds/1/{dia}"

#     payload = ""
#     headers = {
#         "authority": "api.sofascore.com",
#         "accept": "*/*",
#         "accept-language": "pt-BR,pt-PT;q=0.9,pt;q=0.8,en-US;q=0.7,en;q=0.6",
#         "cache-control": "max-age=0",
#         "dnt": "1",
#         "if-none-match": 'W/"de620a01cd"',
#         "origin": "https://www.sofascore.com",
#         "referer": "https://www.sofascore.com/",
#         "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": '"Windows"',
#         "sec-fetch-dest": "empty",
#         "sec-fetch-mode": "cors",
#         "sec-fetch-site": "same-site",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
#     }

#     scraper = cfscrape.create_scraper()

#     response = scraper.request("GET", url, data=payload, headers=headers)

#     response = requests.request("GET", url, data=payload, headers=headers)

#     json_data = json.loads(response.text)

#     dict_rows = {}

#     for key, value in json_data['odds'].items():
#         market_id = key
#         # market_name = value['marketName']
#         # is_live = value['isLive']

#         dados = {}

#         for choice in value['choices']:
#             choice_name = choice['name']
#             fractional_value = choice['fractionalValue']
#             # source_id = choice['sourceId']
#             # winning = choice['winning']

#             dados[choice_name] = fractional_value
#             # rows.append([market_id, market_name, is_live, choice_name, fractional_value, source_id, winning])
        
#         dict_rows[market_id] = dados

#     df = pd.DataFrame([dict_rows[k] for k in dict_rows], index=dict_rows.keys())

#     df.reset_index(inplace=True)

#     df['index'] = df['index'].astype('int64')
        
#     df_renomeado = df.rename(columns={'1':'Odd_Frac_Casa', 'X':'Odd_Frac_Empate', '2':'Odd_Frac_Fora'})
    
#     df_renomeado["Odds_Decimais_Casa"] = df_renomeado["Odd_Frac_Casa"].apply(odd_frac_dec).round(2)
#     df_renomeado["Odds_Decimais_Empate"] = df_renomeado["Odd_Frac_Empate"].apply(odd_frac_dec).round(2)
#     df_renomeado["Odds_Decimais_Fora"] = df_renomeado["Odd_Frac_Fora"].apply(odd_frac_dec).round(2)

#     df_renomeado["Prob_Casa"] = df_renomeado["Odds_Decimais_Casa"].apply(odd_dec_prob).round(2)
#     df_renomeado["Prob_Empate"] = df_renomeado["Odds_Decimais_Empate"].apply(odd_dec_prob).round(2)
#     df_renomeado["Prob_Fora"] = df_renomeado["Odds_Decimais_Fora"].apply(odd_dec_prob).round(2)


#     df_renomeado = df_renomeado.reindex(columns=['index', 'Odd_Frac_Casa', 'Odds_Decimais_Casa', 'Prob_Casa', 'Odd_Frac_Empate', 'Odds_Decimais_Empate', 'Prob_Empate', 'Odd_Frac_Fora', 'Odds_Decimais_Fora', 'Prob_Fora'])

#     return df_renomeado
    
    
# def salvar_arquivo(df_jogos, df_odds, hoje):

#     df = pd.merge(df_jogos, df_odds, left_on='Id_Evento', right_on='index')
#     df_final = df.drop(columns=['index'])

#     doc_csv = f'stats-{hoje}.csv'
#     doc_xlsx = f'stats-{hoje}.xlsx'

#     df_final.to_csv(doc_csv, index=False)
#     df_final.to_excel(doc_xlsx, index=False)

#     #salvar na memoria
#     output = io.StringIO()
#     df_final.to_csv(output, index=False)
#     csv_file = output.getvalue()

#     print(f'Documentos {doc_csv} e {doc_xlsx} salvos com sucesso!')

#     return csv_file


# def atualizar_bd():

#     hoje = data('dataframe')
#     dia = data('dia')

#     df_jogos = jogos_do_dia(dia)
#     df_odds = odds_do_dia(dia)    

#     csv_file = salvar_arquivo(df_jogos, df_odds, hoje)
#     # csv_file = f'stats-{dia}.xlsx'
#     # csv_file = f'dados_stats_inicio.xlsx'

#     token = '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'
#     repo_name = 'joaomendescf/stats-fut'
#     commit_message = 'Adicionando arquivo stats'
    
#     upload_to_github(token, repo_name, csv_file, commit_message)
#     # update_file_github(token, repo_name, csv_file, commit_message)





st.title("Web App - Tips Futebol")

# st.sidebar.header("Tabelas")
# selected_league = st.sidebar.selectbox('Liga',['England','Germany','Italy','Spain','France'])

# selected_season = st.sidebar.selectbox('Temporada', ['2021/2022','2020/2021','2019/2020'])

#=========================================================================

# def load_data_flashScore(periodo, status):      
def load_data_github(status):      

    # df = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_FlashScore/"+str(periodo)+"_Jogos_do_Dia_FlashScore.csv?raw=true")
    # df = pd.read_csv("https://github.com/joaomendescf/stats-fut/blob/main/dados-stats.csv?raw=true")
    df = pd.read_csv("https://github.com/joaomendescf/stats-fut/blob/main/lista_jogos_dia.csv?raw=true")

    
    agora = datetime.today()
    ano = agora.year
    mes = agora.month
    dia = agora.day
    hora = agora.hour
    minuto = agora.minute
    segundo = agora.second
    hora_agora = f'{ano}-{mes}-{dia} {hora}:{minuto}:{segundo}'
    hora_agora_ajuste = f'{ano}-{mes}-{dia} {hora - 2}:{minuto}:{segundo}'

    df['Data_Hora_mod'] = pd.to_datetime(df['Data_Hora'])
    df['Data_Hora_mod'] = df['Data_Hora_mod'] + pd.Timedelta(hours=2)
    df['Data_Hora_mod'] = df['Data_Hora_mod'].dt.strftime('%H:%M')
    
    if status.upper() == 'PENDENTES':        
        df_filtrado = df[pd.to_datetime(df['Data_Hora_mod']).dt.time > pd.to_datetime(hora_agora).time()]
        return df_filtrado
    
    elif status.upper() == 'LIVE': 
        filtro = (
           pd.to_datetime(df['Data_Hora']).dt.time >= pd.to_datetime(hora_agora_ajuste).time()
           ) & (
           pd.to_datetime(df['Data_Hora']).dt.time <= pd.to_datetime(hora_agora).time()
           )     
           
        df_filtrado = df.loc[filtro]
        return df_filtrado
    
    else:
        return df

st.sidebar.header("Jogos do Dia")
lst_opcoes = ['Mostrar Jogos', 'Esconder' ]
selected_season2 = st.sidebar.selectbox('Jogos do Dia?', lst_opcoes)

opcoes = ['Live','Pendentes','Data']
opcao_selecionada = st.sidebar.radio('Status', opcoes)

if st.sidebar.button("Atualizar Base de Dados"):
#     if atualizar_bd():
    st.sidebar.write('Impossível atualizar no momento!')

if opcao_selecionada == 'Data':
  periodo = st.sidebar.date_input("Data de Análise", date.today())




#=========================================================================

  
# def load_data(league, season):
  
#     if selected_league == 'England':
#       league = 'E0'
#     if selected_league == 'Germany':
#       league = 'D1'
#     if selected_league == 'Italy':
#       league = 'I1'
#     if selected_league == 'Spain':
#       league = 'SP1'
#     if selected_league == 'France':
#       league = 'F1'
    
#     if selected_season == '2021/2022':
#       season = '2122'
#     if selected_season == '2020/2021':
#       season = '2021'
#     if selected_season == '2019/2020':
#       season = '1920'
      
#     url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
#     data = pd.read_csv(url)
#     return data


if selected_season2 == 'Mostrar Jogos':
    status = 'Dia'

    if opcao_selecionada == 'Pendentes' or opcao_selecionada == 'Live':
        periodo = date.today()
        if opcao_selecionada == 'Pendentes':
          status = 'Pendentes'
        elif opcao_selecionada == 'Live':
           status = 'Live'
    
    df = load_data_github(status)
    st.subheader(f"Dataframe: {selected_season2} - {opcao_selecionada} [{df.shape[0]}]")
else:
    # df = load_data(selected_league, selected_season)
    # st.subheader("Dataframe: "+selected_league)
    pass

st.dataframe(df)


# def convert_df_xlsx(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_excel('base-de-dados.xls',index=False)#.encode('utf-8')

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

 # -- DOWNLOAD SECTION

st.subheader('Downloads:')

# st.download_button(
#     label="Download data as XLS",
#     data=convert_df_xlsx(df),
#     file_name='base-de-dados.xls',
#     mime='text/xls',
# )

st.download_button(
    label="Download data as CSV",
    data=convert_df(df),
    file_name='base-de-dados.csv',
    mime='text/csv',
)
