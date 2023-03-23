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
									
def estrategia_modelo(casa_time, fora_time, league, minuto, segundo, temperature, clouds, humidity, wind, casa_time_score, fora_time_score, exg_home, exg_away, dangerousAttacks_home, dangerousAttacks_away, shotsOngoal_home, shotsOngoal_away, shotsOffgoal_home, shotsOffgoal_away, corners_home, corners_away, appm1_home, appm1_away, appm2_home, appm2_away, mh1_away, mh1_home, mh2_away, mh2_home, mh3_away, mh3_home, yellowredcards_away, yellowredcards_home, home_vencer, fora_vencer, empate, ambas_marcam, ht_over_05, ht_under_05, ht_over_15, ht_under_15, over_05, under_05, over_15, under_15, over_25, under_25, over_35, under_35, posse_de_bola_casa, posse_de_bola_fora, redcards_home, redcards_away, yellowcards_home, yellowcards_away, ataque_momento_away, ataque_momento_home, attacks_away, attacks_home, chat_id, token):
	
	regra1 = 85 <= minuto <= 90
	regra2 = (fora_time_score - 1) == casa_time_score or (fora_time_score - 2) == casa_time_score
	regra3 = 1.2 <= exg_home <= 2
	regra4 = 8 <= dangerousAttacks_home <= 100 
	regra5 = 6 <= shotsOngoal_home <= 100
	regra6 = 0 <= shotsOffgoal_home <= 100
	regra7 = 10 <= (shotsOngoal_home + shotsOffgoal_home) <= 100
	regra8 =  30 <= attacks_home <= 500
	regra9 = 1 <= appm1_home <= 5  
	regra10 = 1.5 <= appm2_home <= 5  
	regra11 = 5 <= corners_home <= 20

	# print(posse_de_bola_casa)
	# input('valor posse de bola casa')

	regra12 = 55 <= posse_de_bola_casa <= 100
	regra13 = 60 <= home_vencer <= 100
	regra14 = 60 <= over_05 <= 100
	regra15 = 1 <= 2 <= 5 
	regra16 = 1 <= 2 <= 5
	regra17 = 1 <= 2 <= 5
	regra18 = 1 <= 2 <= 5
	regra19 = 1 <= 2 <= 5
	regra20 = 1 <= 2 <= 5
	regra21 = 1 <= 2 <= 5
	regra22 = 1 <= 2 <= 5
	regra23 = 1 <= 2 <= 5
	regra24 = 1 <= 2 <= 5
	regra25 = 1 <= 2 <= 5
	
	result = criar_sequencia_and(regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9, regra10, regra11, regra12, regra13, regra14, regra15, regra16, regra17,regra18, regra19, regra20, regra21, regra22, regra23, regra24, regra25)

	# print(result)

	if eval(result):
	
		text1 = f'\n🚨ALERTA TIPS🚨\n💰1º tempo: mais 1 canto💰\n\n'       
		
		text2 = f'✅ {casa_time} ({casa_time_score}) v ({fora_time_score}) {fora_time}\n🏆 {league}\n⏰ {minuto} min {segundo} seg\n\n'

		text3 = f'❗️Informações do clima da partida\n🌡 {temperature}°C | ☁️  {clouds} | 💧 {humidity} | 💨 {wind}\n\n'
		
		text4 = f'❗️Estatísticas (Últimos 10 minutos)\n🌡Pressão(Exp Gol): {exg_home} - {exg_away}\n🌡Pressão(Ata P/ Min): {appm2_home} - {appm2_away}\n\n❗️Estatísticas (Todo o jogo)\n🔥 Ataques Perigosos: {dangerousAttacks_home} - {dangerousAttacks_away}\n🎯 Chutes ao gol: {shotsOngoal_home} - {shotsOngoal_away}\n💥 Chutes fora do gol: {shotsOffgoal_home} - {shotsOffgoal_away}\n🕹 Escanteios: {corners_home} - {corners_away}\n🟡 Cartões amarelos: {yellowcards_home} - {yellowcards_away}\n🔴 Cartões vermelhos: {redcards_home} - {redcards_away}\n\n'
		# \n Pré-Live\nOdds: {odds_home} - {odds_draw} - {odds_away}

		lst_casa = casa_time.split(' ')
		casa = lst_casa[0]
		casa = casa.replace(' ','%20')
		
		lst_fora = fora_time.split(' ')
		fora = lst_fora[0]
		fora = fora.replace(' ','%20')
		
		text5 = f'💸Link: https://www.bet365.com/#/AX/K%5E{casa}%20{fora} 🎰'

		texto = text1 + text2 + text3 + text4 + text5
		
		print(texto)
		print('-'*30)
		
		asyncio.run(send(texto, chat_id, token))