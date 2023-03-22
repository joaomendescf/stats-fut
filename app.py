import streamlit as st
from io import BytesIO
import pandas as pd
from pandas import json_normalize
#import xlsxwriter
import base64
from datetime import datetime, timedelta, date



st.title("Web App - Tips Futebol")

st.sidebar.header("Tabelas")
selected_league = st.sidebar.selectbox('Liga',['England','Germany','Italy','Spain','France'])

selected_season = st.sidebar.selectbox('Temporada', ['2021/2022','2020/2021','2019/2020'])

#=========================================================================

def load_data_flashScore(periodo, status):      

    df = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_FlashScore/"+str(periodo)+"_Jogos_do_Dia_FlashScore.csv?raw=true")

    agora = datetime.today()
    hora = agora.hour
    minuto = agora.minute
    hora_agora = f'{hora}:{minuto}'
    hora_agora_ajuste = f'{hora + 2}:{minuto}'

    df['Time_mod'] = pd.to_datetime(df['Time'])
    df['Time_mod'] = df['Time_mod'] + pd.Timedelta(hours=2)
    df['Time_mod'] = df['Time_mod'].dt.strftime('%H:%M')
    
    if status.upper() == 'PENDENTES':
        
        df_filtrado = df[pd.to_datetime(df['Time_mod']).dt.time > pd.to_datetime(hora_agora).time()]

        return df_filtrado
    
    elif status.upper() == 'LIVE':
    
        filtro = (
           pd.to_datetime(df['Time']).dt.time <= pd.to_datetime(hora_agora_ajuste).time()
           ) & (
           pd.to_datetime(df['Time_mod']).dt.time >= pd.to_datetime(hora_agora).time()
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

if opcao_selecionada == 'Data':
  periodo = st.sidebar.date_input("Data de Análise", date.today())


#=========================================================================

  
def load_data(league, season):
  
    if selected_league == 'England':
      league = 'E0'
    if selected_league == 'Germany':
      league = 'D1'
    if selected_league == 'Italy':
      league = 'I1'
    if selected_league == 'Spain':
      league = 'SP1'
    if selected_league == 'France':
      league = 'F1'
    
    if selected_season == '2021/2022':
      season = '2122'
    if selected_season == '2020/2021':
      season = '2021'
    if selected_season == '2019/2020':
      season = '1920'
      
    url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
    data = pd.read_csv(url)
    return data


if selected_season2 == 'Mostrar Jogos':
    status = 'Dia'

    if opcao_selecionada == 'Pendentes' or opcao_selecionada == 'Live':
        periodo = date.today()
        if opcao_selecionada == 'Pendentes':
          status = 'Pendentes'
        elif opcao_selecionada == 'Live':
           status = 'Live'
    
    df = load_data_flashScore(periodo, status)
    st.subheader(f"Dataframe: {selected_season2} - {opcao_selecionada} [{df.shape[0]}]")
else:
    df = load_data(selected_league, selected_season)
    st.subheader("Dataframe: "+selected_league)

st.dataframe(df)


def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="Base_de_Dados.csv">Download CSV File</a>'
    return href


output = BytesIO()

# Write files to in-memory strings using BytesIO
# See: https://xlsxwriter.readthedocs.io/workbook.html?highlight=BytesIO#constructor
workbook = xlsxwriter.Workbook(output, {'in_memory': True})
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello')
workbook.close()

st.download_button(
    label="Download Excel workbook",
    data=output.getvalue(),
    file_name="workbook.xlsx",
    mime="application/vnd.ms-excel"
)
    
st.markdown(filedownload(df), unsafe_allow_html=True)
