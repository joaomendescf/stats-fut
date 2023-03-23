import requests
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import datetime
import keyboard
from datetime import datetime, timedelta			

from bot_cantos import extract_game_statistics
from bot_cantos import obter_dados

from estrategia_funil_ft_casa import estrategia_funil_ft_casa
from estrategia_escanteio_final_jogo import estrategia_escanteio_final_jogo
from estrategia_modelo import estrategia_modelo
from estrategia_under_gol_ft import estrategia_under_gol_ft 
from estrategia_over_05_ht import estrategia_over_05_ht 

# 🏁🏴‍☠🏴🏳
# 👁‍🗨🔅🌡💰💸💵💷💴💶💳🪪🕹🚨🎯🎰♟🎲💥🔥
# ❌⭕️🚫❗️📳✅
# 📢🔊📣🕧🕟🕓🕢🕒☑️⏰⏱🏆
# 💧💨☁️🔥💦

def ler_pagina(url):
	# Faz a requisição HTTP GET para a página
	headers = {
	  "cookie": "route=94206abd7dc66948dc67e8b90e588983; SRVGROUP=common",
	  "authority": "api.sportsanalytics.com.br",
	  "accept": "application/json, text/plain, */*",
	  "accept-language": "pt-BR, pt;q=0.9,en-US;q=0.8,en;q=0.7",
	  "origin": "https://playscores.com",
	  "referer": "https://playscores.com",
	  "sec-ch-ua": "^\^Google",
	  "sec-ch-ua-mobile": "?0",
	  "sec-fetch-platform": "^\^Windows",
	  "sec-fetch-dest": "empty",
	  "sec-fetch-mode": "cor$",
	  "sec-fetch-site": "cross-site",
	  "user-agent": "Mozzila/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.35 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
	}
	sleep(3)

	response = requests.request("GET", url, headers=headers)
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	dic_response = response.json()

	return dic_response

def organizar_dados(game):
   
	# data = game['date']

	#team
	fora_time = game['awayTeam']['name']
	casa_time = game['homeTeam']['name']
	league = game['league']['name']

	#currentTime
	minuto = game['currentTime']['minute']
	segundo = game['currentTime']['second']
	if segundo == None:
		segundo = '00'

	#scores
	casa_time_score = game['scores']['homeTeamScore']
	fora_time_score = game['scores']['awayTeamScore']

	try:
	#corners
		corners_home = game['stats']['corners']['home']
		corners_away = game['stats']['corners']['away']
	except:
		corners_home = 0
		corners_away = 0

	if corners_away == None:
		corners_away = 0

	if corners_home == None:
		corners_home = 0

	#dangerousAttacks
	try:
		dangerousAttacks_away = game['stats']['dangerousAttacks']['away']
		dangerousAttacks_home = game['stats']['dangerousAttacks']['home']
	except:
		dangerousAttacks_away = 0  
		dangerousAttacks_home = 0

	if dangerousAttacks_away == None:
		dangerousAttacks_away = 0
	if dangerousAttacks_home == None:
		dangerousAttacks_home = 0
   
	try:
		attacks_away = game['stats']['attacks']['away']
		attacks_home = game['stats']['attacks']['home']
	except:
		attacks_away = 0  
		attacks_home = 0

	if attacks_away == None:
		attacks_away = 0
	if attacks_home == None:
		attacks_home = 0

	#shotsOngoal
	try:
		shotsOngoal_away = game['stats']['shotsOngoal']['away']
		shotsOngoal_home = game['stats']['shotsOngoal']['home']
	except:
		shotsOngoal_away = 0
		shotsOngoal_home = 0
	
	#shotsOffgoal
	try:
		shotsOffgoal_away = game['stats']['shotsOffgoal']['away']
		shotsOffgoal_home = game['stats']['shotsOffgoal']['home']
	except:
		shotsOffgoal_away = 0
		shotsOffgoal_home = 0

	#yellowredcards
	try:
		yellowredcards_away = game['stats']['yellowredcards']['away']
		yellowredcards_home = game['stats']['yellowredcards']['home']
	except:
		yellowredcards_away = 0
		yellowredcards_home = 0

	#appm1
	try:
		appm1_away = game['pressureStats']['appm1']['away']
		appm1_home = game['pressureStats']['appm1']['home']
	except:
		appm1_away = 0
		appm1_home = 0
	
	#appm2
	try:
		appm2_away = game['pressureStats']['appm2']['away']
		appm2_home = game['pressureStats']['appm2']['home']
	except:
		appm2_away = 0
		appm2_home = 0
			
	try:
		ataque_momento_away = game['pressureStats']['attack_momentum']['away']
		ataque_momento_home = game['pressureStats']['attack_momentum']['home']
	except:
		ataque_momento_away = 0
		ataque_momento_home = 0
			
	#exg
	try:
		exg_away = game['pressureStats']['exg']['away']
		exg_home = game['pressureStats']['exg']['home']
	except:
		exg_away = 0
		exg_home = 0
			
	#mh1
	try:
		mh1_away = game['pressureStats']['mh1']['away']
		mh1_home = game['pressureStats']['mh1']['home']
	except:
		mh1_away = 0
		mh1_home = 0
	
	#mh2
	try:
		mh2_away = game['pressureStats']['mh2']['away']
		mh2_home = game['pressureStats']['mh2']['home']
	except:
		mh2_away = 0
		mh2_home = 0
	
	#mh3
	try:
		mh3_away = game['pressureStats']['mh3']['away']
		mh3_home = game['pressureStats']['mh3']['home']
	except:
		mh3_away = 0
		mh3_home = 0
			
	#wearther
	try:
		temperature = game['weatherReport']['temperature']
	except:
		temperature = 0

	try:   
		clouds = game['weatherReport']['clouds']
	except:
		clouds = 0

	try:    
		humidity = game['weatherReport']['humidity']
	except:
		humidity = 0
	
	try:
		wind = game['weatherReport']['wind']
	except:
		wind = 0

	#mercado vitoria
	try:
		home_vencer = game['probabilities']['home']
		fora_vencer = game['probabilities']['away']
		empate = game['probabilities']['draw']
	except:
		home_vencer = 0
		fora_vencer = 0
		empate = 0

	#mercado gols
	try:
		ambas_marcam = game['probabilities']['btts']
		ht_over_05 = game['probabilities']['HT_over_0_5']
		ht_under_05 = game['probabilities']['HT_under_0_5']
		ht_over_15 = game['probabilities']['HT_over_1_5']
		ht_under_15 = game['probabilities']['HT_under_1_5']
		over_05 = game['probabilities']['over_0_5']
		under_05 = game['probabilities']['under_0_5']
		over_15 = game['probabilities']['over_1_5']
		under_15 = game['probabilities']['under_1_5']
		over_25 = game['probabilities']['over_2_5']
		under_25 = game['probabilities']['under_2_5']
		over_35 = game['probabilities']['over_3_5']
		under_35 = game['probabilities']['under_3_5']
	except:
		ambas_marcam = 0
		ht_over_05 = 0
		ht_under_05 = 0
		ht_over_15 = 0
		ht_under_15 = 0
		over_05 = 0
		under_05 = 0
		over_15 = 0
		under_15 = 0
		over_25 = 0
		under_25 = 0
		over_35 = 0
		under_35 = 0

	try:
		posse_de_bola_casa = game['stats']['possessiontime']['home']
		posse_de_bola_fora = game['stats']['possessiontime']['away']
	except:
		posse_de_bola_casa = 0
		posse_de_bola_fora = 0

	if posse_de_bola_casa == None:
		posse_de_bola_casa = 0
	if posse_de_bola_fora == None:
		posse_de_bola_fora = 0
	

	try:
		redcards_home = game['stats']['redcards']['home']
		redcards_away = game['stats']['redcards']['away']
	except:
		redcards_home = 0
		redcards_away = 0

	try:
		yellowcards_home = game['stats']['yellowcards']['home']
		yellowcards_away = game['stats']['yellowcards']['away']
	except:
		yellowcards_home = 0
		yellowcards_away = 0
	 
	return casa_time, fora_time, league, minuto, segundo, temperature, clouds, humidity, wind, casa_time_score, fora_time_score, exg_home, exg_away, dangerousAttacks_home, dangerousAttacks_away, shotsOngoal_home, shotsOngoal_away, shotsOffgoal_home, shotsOffgoal_away, corners_home, corners_away, appm1_home, appm1_away, appm2_home, appm2_away, mh1_away, mh1_home, mh2_away, mh2_home, mh3_away, mh3_home, yellowredcards_away, yellowredcards_home, home_vencer, fora_vencer, empate, ambas_marcam, ht_over_05, ht_under_05, ht_over_15, ht_under_15, over_05, under_05, over_15, under_15, over_25, under_25, over_35, under_35, posse_de_bola_casa, posse_de_bola_fora, redcards_home, redcards_away, yellowcards_home, yellowcards_away, ataque_momento_away, ataque_momento_home, attacks_away, attacks_home

def menu():
	os.system('cls' if os.name=='nt' else 'clear')
	print('='*25)
	print('Apostas Esportivas')
	print('='*25)
	print('[1] Jogos in Live -> .txt')
	print('[2] Bot estrategias')
	print('[3] Escanteios e Over/Under gols')
	print('-'*25)
	print('[4] Sair')
	print('='*25)
	print('Escolha a opção: ', end=' ')

def op2():
	os.system('cls' if os.name=='nt' else 'clear')
	print('='*25)
	print('Bot!')
	print('='*25)

def op3():
	os.system('cls' if os.name=='nt' else 'clear')
	print('='*25)
	print('PREVISÃO DE ESCANTEIOS')
	print('='*25)



def inicio():

	pasta = os.getcwd()
	agora = datetime.now()
	datahora_str = agora.strftime('%d-%m_%H-%M')

	arquivo = f'{pasta}/probabilidades{datahora_str}.txt'
	chat_id = '1236729658'
	token = '6075826453:AAG1PLHWmwAni_qAdfOVescVoJuufMI8MQ4'

	url = 'https://api.sportsanalytics.com.br/api/v1/fixtures-svc/fixtures/livescores?include=weatherReport,additionalInfo,league,stats,pressureStats,probabilities'


	while True:
		menu()
		op = input()

		if op == '1':

			dict_dados = ler_pagina(url)

			texto_placar = ''
			cont = 1
			
			for game in dict_dados['data']:

				casa_time, fora_time, league, minuto, segundo, temperature, clouds, humidity, wind, casa_time_score, fora_time_score, exg_home, exg_away, dangerousAttacks_home, dangerousAttacks_away, shotsOngoal_home, shotsOngoal_away, shotsOffgoal_home, shotsOffgoal_away, corners_home, corners_away, appm1_home, appm1_away, appm2_home, appm2_away, mh1_away, mh1_home, mh2_away, mh2_home, mh3_away, mh3_home, yellowredcards_away, yellowredcards_home, home_vencer, fora_vencer, empate, ambas_marcam, ht_over_05, ht_under_05, ht_over_15, ht_under_15, over_05, under_05, over_15, under_15, over_25, under_25, over_35, under_35, posse_de_bola_casa, posse_de_bola_fora, redcards_home, redcards_away, yellowcards_home, yellowcards_away, ataque_momento_away, ataque_momento_home, attacks_away, attacks_home = organizar_dados(game)

				casa = casa_time.replace(' ','%20')
				fora = fora_time.replace(' ','%20')

				link = f'https://www.bet365.com/#/AX/K%5E{casa}%20{fora}'
				texto_placar += f'✅JOGO {cont}: {casa_time} ({casa_time_score}) v ({fora_time_score}) {fora_time}\n⏰Tempo: {minuto} minutos\n\n{casa_time} - {home_vencer :.2f} %\nEmpate - {empate :.2f} %\n{fora_time} - {fora_vencer :.2f} %\n\nAmbas marcam {ambas_marcam :.2f} %\n\n1° tempo\n>0,5 gol {ht_over_05 :.2f} % | <0,5 gol{ht_under_05 :.2f} %\n>1,5 gol {ht_over_15 :.2f} % | <1,5 gol {ht_under_15 :.2f} % \n\nJogo Completo\n>0,5 gol {over_05 :.2f} % | <0,5 gol {under_05 :.2f} % \n>1,5 gol {over_15 :.2f} % | <1,5 gol {under_15 :.2f} %\n>2,5 gol {over_25 :.2f} % | <2,5 gol {under_25 :.2f} % \n>3,5 gol {over_35 :.2f} % | <3,5 gol {under_35 :.2f} %\n\n💸Link: {link} 🎰\n\n==================================================\n\n'
				
				# print(f'JOGO: {casa_time} ({casa_time_score}) v ({fora_time_score}) {fora_time}\n⏰Tempo: {minuto} minutos\n\n💸Link: https://www.bet365.com/#/AX/K%5E{casa}%20{fora} 🎰\n\n')

				cont += 1

			with open(arquivo, 'w', encoding='utf-8') as arquivo:
				arquivo.write(texto_placar)

		elif op == '2':

			while True:

				os.system('cls' if os.name=='nt' else 'clear')
				op2()
	
				dict_dados = ler_pagina(url)

				for game in dict_dados['data']:
			
					casa_time, fora_time, league, minuto, segundo, temperature, clouds, humidity, wind, casa_time_score, fora_time_score, exg_home, exg_away, dangerousAttacks_home, dangerousAttacks_away, shotsOngoal_home, shotsOngoal_away, shotsOffgoal_home, shotsOffgoal_away, corners_home, corners_away, appm1_home, appm1_away, appm2_home, appm2_away, mh1_away, mh1_home, mh2_away, mh2_home, mh3_away, mh3_home, yellowredcards_away, yellowredcards_home, home_vencer, fora_vencer, empate, ambas_marcam, ht_over_05, ht_under_05, ht_over_15, ht_under_15, over_05, under_05, over_15, under_15, over_25, under_25, over_35, under_35, posse_de_bola_casa, posse_de_bola_fora, redcards_home, redcards_away, yellowcards_home, yellowcards_away, ataque_momento_away, ataque_momento_home, attacks_away, attacks_home = organizar_dados(game)

					print(f'🅰️ {casa_time} ({casa_time_score})\n🅱️ {fora_time} ({fora_time_score}) ')
					print(f'⏰ {minuto}:{segundo}')

					print('-'*25)

					try:
						estrategia_escanteio_final_jogo(casa_time, fora_time, league, minuto, segundo, temperature, clouds, humidity, wind, casa_time_score, fora_time_score, exg_home, exg_away, shotsOngoal_home, shotsOngoal_away, shotsOffgoal_home, shotsOffgoal_away, corners_home, corners_away, appm1_home, appm1_away, appm2_home, appm2_away, redcards_home, redcards_away, yellowcards_home, yellowcards_away,home_vencer, fora_vencer, chat_id, token)
					except:
						pass

					try:
						estrategia_funil_ft_casa(casa_time, fora_time, league, minuto, segundo, temperature, clouds, humidity, wind, casa_time_score, fora_time_score, exg_home, exg_away, shotsOngoal_home, shotsOngoal_away, shotsOffgoal_home, shotsOffgoal_away, corners_home, corners_away, appm1_home, appm1_away, appm2_home, appm2_away, redcards_home, redcards_away, yellowcards_home, yellowcards_away,home_vencer, chat_id, token)
					except:
						pass

					# try:
					estrategia_under_gol_ft(casa_time, fora_time, league, minuto, segundo, temperature, clouds, humidity, wind, casa_time_score, fora_time_score, exg_home, exg_away, dangerousAttacks_home, dangerousAttacks_away, shotsOngoal_home, shotsOngoal_away, shotsOffgoal_home, shotsOffgoal_away, corners_home, corners_away, appm1_home, appm1_away, appm2_home, appm2_away, mh1_away, mh1_home, mh2_away, mh2_home, mh3_away, mh3_home, yellowredcards_away, yellowredcards_home, home_vencer, fora_vencer, empate, ambas_marcam, ht_over_05, ht_under_05, ht_over_15, ht_under_15, over_05, under_05, over_15, under_15, over_25, under_25, over_35, under_35, posse_de_bola_casa, posse_de_bola_fora, redcards_home, redcards_away, yellowcards_home, yellowcards_away, ataque_momento_away, ataque_momento_home, attacks_away, attacks_home, chat_id, token)
					
					# estrategia_over_05_ht(casa_time, fora_time, league, minuto, segundo, temperature, clouds, humidity, wind, casa_time_score, fora_time_score, exg_home, exg_away, dangerousAttacks_home, dangerousAttacks_away, shotsOngoal_home, shotsOngoal_away, shotsOffgoal_home, shotsOffgoal_away, corners_home, corners_away, appm1_home, appm1_away, appm2_home, appm2_away, mh1_away, mh1_home, mh2_away, mh2_home, mh3_away, mh3_home, yellowredcards_away, yellowredcards_home, home_vencer, fora_vencer, empate, ambas_marcam, ht_over_05, ht_under_05, ht_over_15, ht_under_15, over_05, under_05, over_15, under_15, over_25, under_25, over_35, under_35, posse_de_bola_casa, posse_de_bola_fora, redcards_home, redcards_away, yellowcards_home, yellowcards_away, ataque_momento_away, ataque_momento_home, attacks_away, attacks_home, chat_id, token)
					# except:
						# pass
					

					# estrategia_modelo(casa_time, fora_time, league, minuto, segundo, temperature, clouds, humidity, wind, casa_time_score, fora_time_score, exg_home, exg_away, dangerousAttacks_home, dangerousAttacks_away, shotsOngoal_home, shotsOngoal_away, shotsOffgoal_home, shotsOffgoal_away, corners_home, corners_away, appm1_home, appm1_away, appm2_home, appm2_away, mh1_away, mh1_home, mh2_away, mh2_home, mh3_away, mh3_home, yellowredcards_away, yellowredcards_home, home_vencer, fora_vencer, empate, ambas_marcam, ht_over_05, ht_under_05, ht_over_15, ht_under_15, over_05, under_05, over_15, under_15, over_25, under_25, over_35, under_35, posse_de_bola_casa, posse_de_bola_fora, redcards_home, redcards_away, yellowcards_home, yellowcards_away, ataque_momento_away, ataque_momento_home, attacks_away, attacks_home, chat_id, token)
											
				sleep(30)

				if keyboard.is_pressed('q'):
					print('Saindo do loop...')
					break

		elif op == '3':
			op3()

			today = datetime.now().strftime('%Y-%m-%d')

			url = f'https://api.sokkerpro.net/eventApi/{today}/-180/web_ndcco5njxy2mjklo'
		
			data = obter_dados(url) 
			print('Digite a quantidade mínima de escanteios: ', end=' ')
			qtd_escanteios = int(input())
			print('Deseja enviar para o BOT-TELETRAM? [S / N]: ', end=' ')
			op = input()

			if op.upper() == 'S':
				while True:
					extract_game_statistics(data, 'telegram', token, chat_id, qtd_escanteios)
					sleep(40)
					
			elif op.upper() == 'N':
				while True:
					extract_game_statistics(data, 'prompt', token, chat_id, qtd_escanteios)
					sleep(40)
					
			print('Pressione qualquer tecla para finalizar... ', end='')
			input()
			        
			menu()            
		
		elif op == '4':
			exit()        

		


inicio()


