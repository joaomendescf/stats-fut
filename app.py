import streamlit as st
import pandas as pd
from pandas import json_normalize
import base64
from datetime import datetime, timedelta, date
import io
# import openpyxl



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



def convert_df_xlsx(df):
    # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

 # -- DOWNLOAD SECTION

st.subheader('Downloads:')
# generate_excel_download_link(df_grouped)
convert_df_xlsx(df)

st.download_button(
    label="Download data as CSV",
    data=convert_df(df),
    file_name='base-de-dados.csv',
    mime='text/csv',
)

