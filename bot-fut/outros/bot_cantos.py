import requests
# import pytz
from time import sleep
from datetime import datetime, timedelta
import telegram
import asyncio


def obter_dados(url):
	response = requests.get(url)
	if response.status_code == 200:
		return response.json()

async def send(msg, chat_id, token):
    bot = telegram.Bot(token=token)
    await bot.sendMessage(chat_id=chat_id, text=msg, parse_mode = "Markdown") 

def extract_game_statistics(data, tipo, token, chat_id, qtd_escanteios):
	today = datetime.today().strftime('%d/%m/%Y')
	message = f'TENDENCIA DE CANTOS DIA {today}\n'
	games = []
	qtd_partidas = 0

	for match in data['data']:

		try:
			fav = match['favorite']
			country_name = match['country_name']
			league_name = match['league_name']
			starting_time = match['starting_time']
			dt = datetime.strptime(starting_time, '%Y-%m-%d %H:%M:%S')
			offset = timedelta(hours=-3)
			dt = dt + offset
			
			time = dt.strftime('%H:%M')
			hora_agora = datetime.today().strftime('%H:%M')
			
			localTeam = match['localTeam']['name']
			visitorTeam = match['visitorTeam']['name']
			# goals05ht = match['goals05ht']
			# goals15ht = match['goals15ht']
			# goals15ft = match['goals15ft']
			# goals25ft = match['goals25ft']
			# goals35ft = match['goals35ft']
			cornerprediction = match['cornerprediction']
			# corners_potential = cornerprediction - 3
			corners_potential = cornerprediction
			# spectedcorner = cornerprediction * 5

			if fav == 1:
				favorite = f'Time da casa -> {localTeam}'
			elif fav == 2:
				favorite = f'Time de fora -> {visitorTeam}'
			else:
				favorite = f'Sem definição de favorito'

			# qtd_escanteios = 8

			if corners_potential >= qtd_escanteios:

				lst_time = time.split(':')
				time_hora = int(lst_time[0])
				time_min = int(lst_time[1])

				lst_hora_agora = hora_agora.split(':')
				hora_agora_hora = int(lst_hora_agora[0])
				hora_agora_min = int(lst_hora_agora[1])

				if time_hora >= hora_agora_hora:
					
					if time_min >= hora_agora_min: 
					
						probabilidade = (corners_potential * 100)/(qtd_escanteios+qtd_escanteios)

						if probabilidade >= 80:
							qtd_partidas += 1	

							# print(f'TIME: {time_hora} - {time_min}')
							# print(f'HORA AGORA: {hora_agora_hora} - {hora_agora_min}')
							txt0 = '===================================================\n'
							txt1 = f'*🌍{country_name} | ⚽{league_name}*'
							txt2 = f'\n\n✅*{localTeam} x {visitorTeam} - ⏰ {time}*'
							# txt2 = f'\n🔥*Favorito:* {favorite}\n'
							# txt3 = f'\n🎲*[Probabilidades]*\n- {goals05ht}% para Over 0.5HT\n- {goals15ht}% para Over 1.5HT\n- {goals15ft}% para Over 1.5FT\n- {goals25ft}% para Over 2.5FT\n- {goals35ft}% para Over 3.5FT\n\n'
							# txt4 = f'\n🚩*[Cantos]*\nMédia: {corners_potential :.2f} por partida\nProbabilidade: {spectedcorner :.2f}% para Over 9.5 cantos\n\n'
					
							txt4 = f'\n\n🚩*[Cantos]*\n*Média:* {corners_potential} por partida\n*Probabilidade:* {probabilidade :.2f}% para Over {qtd_escanteios-0.5} cantos'
							lst_casa = localTeam.split(' ')
							casa = lst_casa[0]
							casa = casa.replace(' ','%20')
							
							lst_fora = visitorTeam.split(' ')
							fora = lst_fora[0]
							fora = fora.replace(' ','%20')
						
							txt5 = f'\n\n💸*Link:* https://www.bet365.com/#/AX/K%5E{casa}%20{fora} 🎰\n'

							# games.append(game_info)
							# message += '\n'.join(games)
							# print(message)
							
							print('-----------------------')
							# game_info = txt0 + txt1 + txt2 + txt3 + txt4 + txt5
							game_info = txt0 + txt1 + txt2 + txt4 + txt5
							print(game_info)
						
							if tipo == 'telegram':
								# game_info = txt1 + txt2 + txt3 + txt4 + txt5
								game_info = txt1 + txt2 + txt4 + txt5

								asyncio.run(send(game_info, chat_id, token)) # Goes to Selection_Testing
								# telegram_bot = telegram.Bot(token=token)
								# telegram_bot.send_message(chat_id=chat_id, text=game_info)
								# url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={game_info}'
								# results = requests.get(url_base)

		except:
			pass
				
	if qtd_partidas >= 1:
		texto_total = f'\n\nTotal de partidas: {qtd_partidas}'
		print(texto_total)

		if tipo == 'telegram':
			url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto_total}'
			results = requests.get(url_base)

	else:
		texto_total = f'\nSem partidas para Over {qtd_escanteios-0.5} cantos!\n'
		print('-'*30)
		print(texto_total)
