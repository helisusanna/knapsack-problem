# Knapsack problem
import sys
import queue as Q
hh_Q = Q.PriorityQueue()

# objektit ja niiden ominaisuudet joukossa S={(a, b, c),..(..)}
# a on objektin nimi
# b on objektin hyötyluku
# c on objektin paino (kustannus)
#hh_S={('Työasemat',6600,58400),
 # ('Huonekalut',3700,30000),
 # ('Mobiililaitteet',5700,58400),
 # ('Osuus vapaa-ajan mökistä',3200,50000)}

hh_S={(sys.argv[1],int(sys.argv[2]),int(sys.argv[3])),(sys.argv[4],int(sys.argv[5]),int(sys.argv[6])),
   (sys.argv[7],int(sys.argv[8]),int(sys.argv[9])),(sys.argv[10],int(sys.argv[11]),int(sys.argv[12]))}
# B on kokonaisbudjetti
hh_B = int(sys.argv[13])

#hh_S={(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))}
#hh_B = int(sys.argv[4])

def Yreppu(hh_S, hh_B):
    hh_Reppu = set() # joukko Reppu, johon lisätään objektien nimet
    hh_H_list = [] # lista, johon lisätään reppuun lisättävien objektien hyötyluvut
    hh_K_list = [] # lista, johon lisätään reppuun lisättävien objektien painoluvut / kustannusluvut
    # käydään joukko S läpi ja lasketaan objektien suhdeluvut 
    # Si[b] / Si[c] (objektin hyötyluku jaettuna painoluvulla)
    for i in hh_S:
        # lisätään suhdeluvut prioriteettijonoon Q negatiivisena,
        # jotta saadaan isoin luku (positiivisena) jonon ensimmäiseksi, toinen arvo on objektin nimi
        hh_Q.put((-i[1]/i[2],i[0]))

    # käydään prioriteettijono läpi
    # kun jonosta otetaan arvo, se poistuu jonosta. joten toistetaan tätä kunnes jono on tyhjä
    while not hh_Q.empty():
        object_name = hh_Q.get()[1] # jonon ensimmäisen objektin nimi
        for i in hh_S:
            if object_name in i: # jos objektin nimi on jossakin joukon S tuplassa
                hh_K = sum(hh_K_list) + i[2] # lasketaan uusi kokonaispaino (kustannus)
                if hh_K <= hh_B: # jos uusi kokonaispaino, eli kustannus, ei ylitä budjettia
                    #x = 1, esimerkin vuoksi, boolean-muuttuja x on true objektin kohdalla
                    hh_Reppu.add(i[0]) # lisätään objekti reppuun
                    hh_K_list.append(i[2]) # lisätään painoluku listaan, jonka summaa käytetään taas seuraavalla kierroksella
                    hh_H_list.append(i[1]) # lisätään hyötyluku sille varattuun listaan
               #else:
                     #x = 0, esimerkin vuoksi, boolean-muuttuja x on false objektin kohdalla, jos budjetti ylittyy
    hh_K = sum(hh_K_list)
    hh_H = sum(hh_H_list)
    reppu = ', '.join(hh_Reppu)
    print({'sisalto':reppu,'kokonaishyoty':str(hh_H),'kokonaiskustannus':str(hh_K)})

Yreppu(hh_S, hh_B)