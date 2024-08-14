# random seige operator
# Emilio Ortiz
# created 12/21/23

import random

def pick_random():
	attackers = ["RAM", "BRAVA","GRIM","SENS","OSA","FLORES","ZERO","ACE",
	"IANA","KALI","AMARU","NOKK","GRIDLOCK","NOMAD","MAVERICK","LION",
	"FINKA","DOKKAEBI","ZOFIA","YING","JACKAL","HIBANA","CAPITAO","BLACKBEARD",
	"BUCK","SLEDGE","THATCHER","ASH","THERMITE","MONTAGE","TWITCH", "BLITZ",
	"IQ","FUZE","GLAZ"]

	defenders = ["TUBARAO","FENRIR","SOLIS","AZAMI","THORN","THUNDERBIRD","ARUNI",
	"MELUSI","ORYX","WAMAI","GOYO","WARDEN","MOZZIE","KAID","CLASH","MASETRO",
	"ALIBI","VIGIL","ELA","LESION","MIRA","ECHO","CAVERIA","VALKYRIE","FROST",
	"MUTE","SMOKE","CASTLE","PULSE","DOC","ROOK","JAGER","BANDIT","TACHANKA","KAPKAN"]

	try:
		user_input = int(input("1: for Attcking 2: for Defending? "))
	except ValueError:
		return

	if user_input == 1:
		choice = attackers
	elif user_input == 2:
		choice = defenders
	else:
		return

	return random.choice(choice)

print(pick_random())
