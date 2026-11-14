import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt
import numpy as np

session = fastf1.get_session(2026,20,"Q")

session.load()

#recuperer le pilote voulu

driver1 = session.laps.pick_drivers('VER')
driver2 = session.laps.pick_drivers("HAM")

#recuperer son meilleur tour

driver1Lap = driver1.pick_fastest()
driver2Lap = driver2.pick_fastest()

#recuperer la telemetrie de son tour

telemetryDriver1 = driver1Lap.get_telemetry()
telemetryDriver2 = driver2Lap.get_telemetry()

#recuper le temps, la vitesse et la distance

timeDriver1 = telemetryDriver1["Time"]
speedDriver1 = telemetryDriver1["Speed"]
timeDriver2 = telemetryDriver2["Time"]
speedDriver2 = telemetryDriver2["Speed"]
distanceDriver1 = telemetryDriver1["Distance"]
distanceDriver2 = telemetryDriver2["Distance"]

# recuperer la couleur des drivers

colorDriver1 = fastf1.plotting.get_driver_color("VER", session)
colorDriver2 = fastf1.plotting.get_driver_color("HAM", session)

#distance du tour pour avoir le meme pour les 2 driver
distanceTour = min(distanceDriver1.max(), distanceDriver2.max()) 

#Points de distance communs pour comparer au meme endroit
grille = np.linspace(0,distanceTour,500)

#temps de chaque pilote a chaque distance de la grille
tempsDriver1 = np.interp(grille,distanceDriver1,timeDriver1.dt.total_seconds())
tempsDriver2 = np.interp(grille,distanceDriver2,timeDriver2.dt.total_seconds())

# on calcule l'ecart dans une liste pour tracé un nouveau graphique
ecart = []
for i in range(len(tempsDriver1)):
    ecart.append(tempsDriver2[i] - tempsDriver1[i])

# création des graphique et de leur données

fig, ax = plt.subplots()

fig2, ax2 = plt.subplots()

fig3, ax3 = plt.subplots()

#graphique 1 (vitesse en fonction de distance)

ax.plot(distanceDriver1,speedDriver1,color=colorDriver1, label="VER")
ax.plot(distanceDriver2,speedDriver2,color=colorDriver2, label="HAM")
#       donnée x          donnée y     couleur             nom affiché dans la legende

#graphique 2 (temps en fonction de distance)

ax2.plot(distanceDriver1, timeDriver1.dt.total_seconds(), color=colorDriver1, label="VER")
ax2.plot(distanceDriver2,timeDriver2.dt.total_seconds(),color=colorDriver2, label="HAM")

#graphique 3 (ecart de temps des 2 driver)

ax3.plot(grille, ecart)

#definir les titres du graphique

ax.set_title("Comparaison vitesse tour VER-HAM")
ax2.set_title("Comparaison de temps au tour VER-HAM")
ax3.set_title("Ecart de temps entre VER-HAM")

ax.set_xlabel("Distance (m)")
ax.set_ylabel("Vitesse (Km/h)")

ax2.set_xlabel("Distance (m)")
ax2.set_ylabel("Temps (s)")

ax3.set_xlabel("Distance (m)")
ax3.set_ylabel("Delta (s)")

ax.legend()
ax2.legend()
fig.savefig("vitesse.png")
fig2.savefig("temps.png")
fig3.savefig("delta.png")
plt.show()