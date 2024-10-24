#!/usr/bin/python3


from random import randint
import time
from math import ceil

solde = 0.0
jouer = 1

def initialiser(montant_initial):
    global solde
    solde = montant_initial

def retirer(montant):
    global solde
    solde -= montant
    print(f"[INFO] {montant} € retiré. Nouveau solde : {solde} €")

def ajouter(montant):
    global solde
    solde += montant
    print(f"[INFO] {montant} € ajouté. Nouveau solde : {solde} €")

def afficher_solde():
    print(f"[INFO] Votre solde actuel est de {solde} €")

def return_solde():
	global solde
	return solde

def choixnumero():
	while True:
	    try:
	    	while True:
		        numero = int(input("[Croupier]: Sur quel numéro voulez vous misez [1-50]: "))
		        if 0 < numero <= 50:
			        print(f"[INFO] Vous avez miser sur le numéro {numero}")
			        return numero 
	    except ValueError:
	        print("[INFO] Veuillez entrer un nombre entier")


def miseargent():
    global solde
    while True:
        try:
            argentmiser = float(input("[Croupier] Et maintenant combien d'argent voulez-vous miser ?: "))
            if 0 < argentmiser <= solde:
                return argentmiser
            else:
                print("[INFO] La mise doit être supérieure à 0 et ne pas dépasser votre solde.")
        except ValueError:
            print("[INFO] Veuillez entrer un nombre ou bien un nombre à virgule (séparé d'un point) seulement")


def randomnum():
	return randint(1,50)


def casino():
	initialiser(1000)
	global jouer
	while jouer == 1:
		afficher_solde()
		numero = choixnumero()
		if numero % 2 == 0:
			couleur1 = "rouge"
		else:
			couleur1 = "noir"
		print(f"[INFO] Vous avez choisie le numéro {numero} qui est de couleur {couleur1}")
		argentmiser = miseargent()
		retirer(argentmiser)
		print("[INFO] Lancement de la roue !")
		print("....")
		time.sleep(1)
		print("...")
		time.sleep(1)
		print("..")
		time.sleep(1)
		random = randomnum()
		if random % 2 == 0:
			couleur = "rouge"
		else:
			couleur = "noir"
		print(f"[INFO] C'est tombé sur le numéro {random} qui est de couleur {couleur}")
		if numero == random:
			print("[Croupier] Vous êtes tombé sur le numéro juste !!!")
			print("[INFO] Vous avez gagner !")
			ajouter(ceil( argentmiser + argentmiser * 3))
		elif couleur1 == couleur:
			print("[Croupier] Vous n'avez pas gagner mais vous êtes tombé sur la même couleur")
			print(".. Vous repartez donc avec la moitié de votre mise initial.")
			ajouter(ceil(argentmiser / 2))
		else:
			print("[Croupier] Vous avez perdu cette fois.")

		if return_solde() > 0:
			while True:
				try:
					choix = str(input("[INFO] Voulez vous continuer de jouer ? (O(ui) - N(on)? "))
					if choix == "O" or choix == "Oui" or choix == "o":
						jouer = 1
						break
					elif choix == "N" or choix == "Non" or choix == "n":
						jouer = 0	
						break
					else: 
						raise ValueError
				except ValueError:
					print("[INFO] Je n'ai pas bien compris.")
		else:
			jouer = 0
			print("[INFO] Vous avez perdu l'entièreter de votre argent.")

	else:
		print("[INFO] Fin.")


if __name__ == "__main__":
    resultat = casino()
    print(resultat)
