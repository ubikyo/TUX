#!/usr/bin/env python3
"""Comparaison temporaire des icônes configurées et des alternatives ASCII.

Exécution : /opt/TUX/venv/bin/python3 scripts/compare-icons.py
"""

from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    sys.exit("Utilise le Python de TUX : /opt/TUX/venv/bin/python3 scripts/compare-icons.py")

root = Path(__file__).resolve().parents[1]
config = yaml.safe_load(
    (root / "TUX.motd/ressources/tux_motd.yaml").read_text().replace("{services}", "{}")
)
alternatives = {
    "distro": "OS", "uptime": "UP", "processor": "CPU",
    "memory": "RAM", "disk": "DISK", "service": "SVC",
    "interface": "NET", "route": "->", "resolver": "DNS",
    "firewall": "FW", "user": "USER", "update": "UPD",
}


def display(label, icon, alternative):
    # L'icône reste hors des colonnes alignées : sa largeur dépend de la police.
    print(f"{label:24} ASCII : {alternative:6} Actuel : {icon}")


print("Comparaison TUX.motd — configuration locale\n")
for entry in config["modules"]:
    name, settings = next(iter(entry.items()))
    for item in settings.get("content", [{name: settings}]):
        method, options = next(iter(item.items()))
        icon = (options or {}).get("icon")
        if isinstance(icon, dict):
            for kind, value in icon.items():
                display(f"{method}.{kind}", value,
                        "#" if kind == "graph" else alternatives[method])
        elif icon is not None:
            display(method, icon, alternatives[method])

print("\nTUX.ps1\n")
display("Logo Ubuntu", "", "OS")
display("Séparateur", "", ">")
print("\nCadres :  ┌───┐  │  └───┘    ASCII :  +---+  |  +---+")
