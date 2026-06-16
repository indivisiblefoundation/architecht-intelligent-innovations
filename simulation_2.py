import matplotlib
matplotlib.use('Agg')  # headless — works on Windows, Linux, Chrome OS
import random
import matplotlib.pyplot as plt

IT_KW = 100
DAYS = 7
temps = [random.randint(95, 102) for _ in range(DAYS)]

def pue_air(t): return 1.50 * (1 + 0.0025 * max(0, t - 85))
def pue_liquid(t): return 1.08 * (1 + 0.0005 * max(0, t - 85))

air = [IT_KW * 24 * pue_air(t) / 1000 for t in temps]
liq = [IT_KW * 24 * pue_liquid(t) / 1000 for t in temps]

print(f"Texas Summer {DAYS}-Day | Temps: {temps}")
print(f"Air total: {sum(air):.1f} MWh | Liquid total: {sum(liq):.1f} MWh")
print(f"Saved: {sum(air)-sum(liq):.1f} MWh ({(sum(air)-sum(liq))/sum(air)*100:.1f}%)")

plt.figure(figsize=(8,4))
plt.plot(range(1, DAYS+1), air, marker='o', label='Air-cooled')
plt.plot(range(1, DAYS+1), liq, marker='o', label='Liquid-cooled')
plt.title('Texas Summer Pilot — Daily Energy')
plt.xlabel('Day'); plt.ylabel('MWh'); plt.legend(); plt.tight_layout()
plt.savefig('pue_simulation.png')
print('Saved pue_simulation.png')
