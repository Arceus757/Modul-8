# 1. Gör ett program som skriver ut dagens datum och tid

import time
import datetime

# now = datetime.datetime.now()

# print("Dagens datum och tid är:")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# # 2. Prova olika sätt att skriva ut tid/datum
# time_objekt = time.localtime()
# print(time_objekt)
# local_time = time.strftime("%B %d-%Y *%H:%M:%S*", time_objekt)
# print(local_time)

# # andra sättet (Här kan man ange tid och datum på egen hand):
# time_tuple = (2023, 11, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# 3. Gör så klockan uppdateras automatiskt
# from datetime import datetime

# while True:
#     # Aktuell tid
#     nu = datetime.now()

#     # Uppdateras var 0.0001 sekund
#     print(nu)

#     time.sleep(0.0001)

# 4. Gör ett tidtagarur

# def tidtagarur():
#     start_tid = time.time()

#     while True:
#         nu_tid = time.time()
#         passerad_tid = nu_tid - start_tid

#         timmar, rest = divmod(passerad_tid, 3600)
#         minuter, sekunder = divmod(rest, 60)

#         tid_str = "{:0>2}:{:0>2}:{:05.2f}".format(int(timmar), int(minuter), sekunder)
#         print(tid_str, end="\r")  # Skriv över samma rad i konsolen

#         try:
#             time.sleep(0.001)  # Uppdateras var 0.0001 sekund
#         except KeyboardInterrupt:
#             sluta_tidtagarur()
#             break

# def sluta_tidtagarur():
#     print("\nTidtagaruret avslutat.")

# print("Tryck på Ctrl+C för att avsluta.")
# tidtagarur()


# 5. Lägg till klockan i ett annat program/spel du har skapat
import time
import random

def rock_paper_scissors():
    alternativ = ["Rock", "Paper", "Scissors"]
    start_tid = time.time()

    while True:
        spelare_val = input("Välj Rock, Paper eller Scissors (q för att avsluta): ").capitalize()

        if spelare_val == 'Q':
            break

        dator_val = random.choice(alternativ)
        print("Datorn valde:", dator_val)

        # Uppdatera klockan
        nu_tid = time.time()
        passerad_tid = nu_tid - start_tid

        timmar, rest = divmod(passerad_tid, 3600)
        minuter, sekunder = divmod(rest, 60)

        tid_str = "{:0>2}:{:0>2}:{:05.2f}".format(int(timmar), int(minuter), sekunder)
        print("Aktuell tid:", tid_str)

        # vinnare och förlorare
        if spelare_val == dator_val:
            print("Oavgjort!")
        elif (spelare_val == "Rock" and dator_val == "Scissors") or \
             (spelare_val == "Paper" and dator_val == "Rock") or \
             (spelare_val == "Scissors" and dator_val == "Paper"):
            print("Du vann!")
        else:
            print("Du förlorade!")

    print("Spelet avslutat.")

rock_paper_scissors()


# 6. ÖVERKURS: Skriv ett program som frågar användaren efter ett specifikt datum (månad, dag och år) och sedan beräknar antalet dagar mellan det datumet och dagens datum.

# 7. ÖVERKURS: Gör en larmklocka eller timer där man kan ställa in tid för nedräkning. Något ska hända när tiden är ute
