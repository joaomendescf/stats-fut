import telegram
import asyncio


async def send(msg, chat_id, token):
	bot = telegram.Bot(token=token)
	await bot.sendMessage(chat_id=chat_id, text=msg, parse_mode = "Markdown") 

def criar_sequencia_and(*args):
	if len(args) == 0:
		return ""
	elif len(args) == 1:
		return str(args[0])
	else:
		return " and ".join(str(arg) for arg in args[:-1]) + " and " + str(args[-1])

def estrategia_funil_ft_casa(casa_time, fora_time, league, minuto, segundo, temperature, clouds, humidity, wind, casa_time_score, fora_time_score, exg_home, exg_away, shotsOngoal_home, shotsOngoal_away, shotsOffgoal_home, shotsOffgoal_away, corners_home, corners_away, appm1_home, appm1_away, appm2_home, appm2_away, redcards_home, redcards_away, yellowcards_home, yellowcards_away,home_vencer, chat_id, token):
	
	regra1 = appm1_home >= 1  
	regra2 = home_vencer >= 60  
	regra3 = minuto >= 80 and minuto <= 90
	chance_de_gol = shotsOngoal_home + shotsOffgoal_home + corners_home		
	regra4 = chance_de_gol >= 20
	score_difference = fora_time_score - casa_time_score
	regra5 = (casa_time_score == fora_time_score) or (score_difference == 1)
	regra6 = 1.5 <= appm2_home <= 5  
	regra7 = 5 <= corners_home <= 20
	regra8 = exg_home >= 1.2
	regra9 = 0 <= 1 <= 100
	regra10 = 0 <= 1 <= 100
	regra11 =  0 <= 1 <= 100		
	regra12 = 0 <= 1 <= 100
	regra13 = 0 <= 1 <= 100
	regra14 = 0 <= 1 <= 100
	
	result = criar_sequencia_and(regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9, regra10, regra11, regra12, regra13, regra14)

	if eval(result):

		text1 = f'\n🚨*ALERTA TIPS🚨 - 💰 ZOIAO + GOL* 💰\n\n🎰*APOSTA: + 1 GOL + 1 ESCANTEIO*'       
		
		text2 = f'✅ *{casa_time} v {fora_time}\n🏆 {league}\n⏰ {minuto} min {segundo} seg*\n\n'

		text3 = f'❗️*Clima da partida*\n🌡 {temperature}°C | ☁️  {clouds} | 💧 {humidity} | 💨 {wind}\n\n'
		
		text4 = f'❗️*Estatísticas (Últimos 10 minutos)*\n🌡Pressão(ExG): {exg_home} - {exg_away}\n🔥Pressão(APPM 10"): {appm2_home} - {appm2_away}'
		
		text5 = f'\n\n❗️*Estatísticas (Todo o jogo)*\n🌡Pressão(APPM): {appm1_home} - {appm1_away}\n🎯 Chutes ao gol: {shotsOngoal_home} - {shotsOngoal_away}\n💥Chutes fora do gol: {shotsOffgoal_home} - {shotsOffgoal_away}\n⛳ Escanteios: {corners_home} - {corners_away}\n⚽*Chances de gol do {casa_time}:* {chance_de_gol}'
		
		text6 = f'\n\n🟡 Cartões amarelos: {yellowcards_home} - {yellowcards_away}\n🔴 Cartões vermelhos: {redcards_home} - {redcards_away}\n\n'
		
		lst_casa = casa_time.split(' ')
		casa = lst_casa[0]
		casa = casa.replace(' ','%20')
		
		lst_fora = fora_time.split(' ')
		fora = lst_fora[0]
		fora = fora.replace(' ','%20')
	
		bet365 = f'💸\n*Link:* https://www.bet365.com/#/AX/K%5E{casa}%20{fora}'
		
		site = 'sofascore'
		google = f'\n🎲\n*Link:* https://www.google.com/search?q={site}+{casa}+{fora}'

		texto = text1 + text2 + text3 + text4 + text5 + text6 + bet365 + google
		
		print(texto)
		print('-'*30)

		asyncio.run(send(texto, chat_id, token))
