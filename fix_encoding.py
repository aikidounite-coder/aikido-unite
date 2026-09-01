#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# Fichier à corriger
html_file = r'd:\AikidoUnite\GitHub\aikido-unite\www.aikido-unite.com\inscriptions.html'

# Lire le fichier en UTF-8
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Compteur de remplacements
replacements = []

# Problème 1: "Ã¢â‚¬â€¹" -> "«" (guillemet français ouvrant)
if 'Ã¢â‚¬â€¹' in content:
    count = content.count('Ã¢â‚¬â€¹')
    content = content.replace('Ã¢â‚¬â€¹', '«')
    replacements.append(f"Ã¢â‚¬â€¹ -> « ({count} occurrences)")

# Problème 2: "Ã¢â‚¬Â»" -> "»" (guillemet français fermant)
if 'Ã¢â‚¬Â»' in content:
    count = content.count('Ã¢â‚¬Â»')
    content = content.replace('Ã¢â‚¬Â»', '»')
    replacements.append(f"Ã¢â‚¬Â» -> » ({count} occurrences)")

# Problème 3: "Ã¢â‚¬â„¢" -> "'" (apostrophe courbe)
if 'Ã¢â‚¬â„¢' in content:
    count = content.count('Ã¢â‚¬â„¢')
    content = content.replace('Ã¢â‚¬â„¢', ''')
    replacements.append(f"Ã¢â‚¬â„¢ -> ' ({count} occurrences)")

# Problème 4: "Ã¢â‚¬â€" -> "–" (tiret demi-cadratine)
if 'Ã¢â‚¬â€' in content:
    count = content.count('Ã¢â‚¬â€')
    content = content.replace('Ã¢â‚¬â€', '–')
    replacements.append(f"Ã¢â‚¬â€ -> – ({count} occurrences)")

# Sauvegarder le fichier corrigé
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

# Afficher les résultats
print("✓ Fichier corrigé avec succès!")
print("\nRemplacements effectués:")
for replacement in replacements:
    print(f"  - {replacement}")

if not replacements:
    print("  Aucun caractère corrompu trouvé.")
