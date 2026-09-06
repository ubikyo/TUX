# Suivi des corrections

- [x] Adapter l’installateur aux sous-modules Git : clonage récursif,
  synchronisation, versions référencées, chemins explicites, isolation et
  propagation des erreurs retournées par les installateurs.
- [ ] Corriger la modification et la restauration de la configuration SSH.
- [ ] Préserver les personnalisations YAML lors des réinstallations.
- [ ] Éviter les doublons du prompt dans les fichiers `.bashrc`.
- [ ] Déclarer les dépendances Python dans `pyproject.toml`.
- [ ] Corriger la lecture des routes et le traitement des règles du pare-feu.
- [ ] Corriger les informations CPU affichées.
- [ ] Corriger le code de sortie de `--help`.
- [ ] Mutualiser les fonctions Bash et ajouter des tests ciblés.

## Points complémentaires relevés pendant la revue

- [ ] Vérifier les erreurs internes des installateurs : le nettoyage MOTD
  appelle un `setup.py` absent et peut masquer cet échec avec une commande
  suivante réussie.
- [ ] Vérifier le lancement du MOTD lorsque le lien dans `/usr/local/bin`
  est refusé pendant l’installation interactive.
- [ ] Valider la compatibilité Ubuntu annoncée avec des tests reproductibles.
