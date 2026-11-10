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

#recuper le temps et la vitesse

timeDriver1 = telemetryDriver1["Time"]
speedDriver1 = telemetryDriver1["Speed"]
timeDriver2 = telemetryDriver2["Time"]
speedDriver2 = telemetryDriver2["Speed"]

# recuperer la couleur des drivers

colorDriver1 = fastf1.plotting.get_driver_color("VER", session)
colorDriver2 = fastf1.plotting.get_driver_color("HAM", session)

#recuper la distance

distanceDriver1 = telemetryDriver1["Distance"]
distanceDriver2 = telemetryDriver2["Distance"]

fig, ax = plt.subplots()

ax.plot(distanceDriver1,speedDriver1,color=colorDriver1, label="VER")
ax.plot(distanceDriver2,speedDriver2,color=colorDriver2, label="HAM")
#       donnée x          donnée y     couleur             nom affiché dans la legende
#definir les titres du graphique

ax.set_title("Comparaison vitesse tour VER-HAM")
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Vitesse (Km/h)")
ax.legend()
plt.savefig("graphique.png")
plt.show()