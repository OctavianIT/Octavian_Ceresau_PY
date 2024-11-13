
while True:
    cittàorigine = input("\nDove abiti: ")

    animaledomestico = input("Nome del tuo animale domestico: ")

    print(f"Il tuo nome è: {cittàorigine}{animaledomestico}")

    risposta = input ("\nTi piace questo nome?(si/no) ")


    if (risposta == "si"):
        print("Hai trovato il tuo nome!")
        break
        
    else:
        print("\nMi dispiace, Riprova\n")
        continue


