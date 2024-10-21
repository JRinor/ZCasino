#!/usr/bin/python3

from random import randint
import time


defaultargent = 1000
defaultgain = 0.0

def mise():
	while True:
	    try:
	        mise = int(input("[Croupier]: Sur quel numéro voulez vous misez [1-50]: "))
	        print(f"[INFO] Vous avez miser sur le numéro {mise}")
	        return mise 
	    except ValueError:
	        print("[INFO] Veuillez entrer un nombre entier")


def miseargent():
    while True:
        try:
            miseargent = float(input("[Croupier] Et maintenant combien d'argent voulez-vous miser ?: "))
            return miseargent
        except ValueError:
            print("[INFO] Veuillez entrer un nombre ou bien un nombre à virgule (séparé d'un point) seulement")

def casino():
	global defaultargent
	global defaultgain
	print(f"[INFO] Vous avez {defaultargent} euro dans votre compte")
	jouer = 1
	while jouer == 1:
		print(f"[INFO] Vous avez {defaultargent} euro dans votre compte")
		mise1 = mise()
		mise2 = miseargent()
		print("[INFO] Lancement de la roue !")
		print("....")
		time.sleep(1)
		print("...")
		time.sleep(1)
		print("..")
		time.sleep(1)
		random = randint(1,50)
		if random % 2 == 0:
			couleur = "rouge"
		else:
			couleur = "noir"
		print(f"[INFO] C'est tombé sur le numéro {random} qui est de couleur {couleur}")
		if mise1 == random:
			print("[Croupier] Vous êtes tombé sur le numéro juste !!!")
			print("[INFO] Vous avez gagner !")
			gain = mise2 * 3
			# argent += gain
		elif mise1 % 2 == 0 and random % 2 == 0: 
			print("[Croupier] Vous n'avez pas gagner mais vous êtes tombé sur la même couleur")
			print(".. Vous repartez donc avec la moitié de votre mise initial.")
			gain = mise2 / 2
			# argent += gain
		else:
			print("[Croupier] Vous avez perdu cette fois.")
			gain -= mise2
			# argent -= mise2

		print(f"[INFO] Vous avez {defaultargent} euro dans votre compte")
		
		while True:
			try:
				choix = str(input("[INFO] Voulez vous continuer de jouer ? (O(ui) - N(on)? "))
				if choix == "O" or choix == "Oui":
					jouer = 1
					defaultargent += gain
					break
				elif choix == "N" or choix == "Non":
					jouer = 0
					break
				else: 
					raise ValueError
			except ValueError:
				print("[INFO] Je n'ai pas bien compris.")



# Test de la fonction principale
if __name__ == "__main__":
    resultat = casino()
    print(resultat)
