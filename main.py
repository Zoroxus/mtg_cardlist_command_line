import requests
import json
import scrython


def get_cards_1(json_object):
	data_temp = []
	i = 0
	price_eur = 0.0
	price_usd = 0.0
	while i < len(json_object):
		if len(json_object[i])<4:
			card = scrython.cards.Collector(card_name=json_object[i][0], code=json_object[i][1], collector_number=json_object[i][2])
			data_temp.append([card.name(), card.set_name(), card.collector_number(), card.prices("eur"), card.prices("usd")])
			try:
				price_eur += float(card.prices("eur"))
				json_object[i].append(card.prices("eur"))
			except:
				price_eur += float(0.0)
				json_object[i].append(0.0)
			try:
				price_usd += float(card.prices("usd"))
				json_object[i].append(card.prices("usd"))
			except:
				price_usd += float(0.0)
				json_object[i].append(0.0)
			print(card.name(), "  |  ", card.set_code(), "  |  ", card.prices("eur"), "€  |  ", card.prices("usd"), "$")
			with open("local.json", "w") as outfile:
				json.dump(json_object, outfile)
		elif len(json_object[i])>3:
			print(json_object[i][0], "  |  ", json_object[i][1], "  |  ", json_object[i][2], "  |  ", json_object[i][3], "€  |  ", json_object[i][4], "$")
			price_eur += float(json_object[i][3])
			price_usd += float(json_object[i][4])
		i += 1
	print("Total price : ", round(price_eur, 2), "€  |  ", round(price_usd, 2), "$")


# Opening JSON file
def get_data(json_object):
	data = []
	for i in data:
		data.append(i)
	return data


if __name__ == '__main__':
	with open('local.json', 'r') as openfile:
		# Reading from json file
		json_object = json.load(openfile)
	while True:
		print("If you want to see your cards : 1")
		print("If you want to add a card : 2")
		choice = int(input())
		# print(data[1][1])
		match choice:
			case 1:
				print("Here's your collection :")
				get_cards_1(json_object)
				break
			case 2:
				card_name = input("Input the card's name :")
				card_code = input("Input the card's set code (The List = PLIST) :")
				card_num = input("Input the card's set number :")
				json_object.append([card_name, card_code, card_num])
				with open("local.json", "w") as outfile:
					json.dump(json_object, outfile)
				break
		#    case _:
        #        print("Nothing was chosen !")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
