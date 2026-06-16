# Zero-Combustion AI Data Center — Pilot Brief

**Author:** Tomas Nelson | Former US Marine | 469-912-5150 | Carrollton, TX

Pilot concept for magnetic-assisted power + waterless cooling, with a runnable Texas summer heat-load simulation.

## Quick start (Windows 10 / Windows 11 / Linux / Chrome OS)

1. Install Python 3.9+ (on Windows check "Add Python to PATH")
2. Open a terminal in this folder
3. Install deps:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python simulation.py
   ```
   (On some systems use `python3` instead of `python`)

The script prints a 7-day simulation and saves `pue_simulation.png` in the folder. No GUI is required — it runs headless.

## Files
- `Tomas_Nelson_Data_Center_Brief.pdf` — printable briefcase
- `simulation.py` — Texas summer model (air vs liquid cooling)
- `requirements.txt` — `matplotlib>=3.5.0`
- `LICENSE` — MIT
- `.gitignore` — Python standard ignores
- `run.bat` / `run.sh` — one-click launchers
- `docs/brief_source.html` — editable source

## What the simulation does
- Models a 100 kW IT pilot over 7 days at 95–102°F ambient
- Air-cooled PUE: 1.50 + 0.25% per °F above 85°F
- Liquid-cooled PUE: 1.08 + 0.05% per °F above 85°F
- Reports total MWh, % energy saved, and estimated water saved (0.5 gal/kWh avoided)

License: MIT © 2026 Tomas Nelson
