# Evaluation de performance

Nous allons utiliser pour ce TP, le logiciel `fio` qui a pour but de générer des tâches I/O et de reporter dans un fichier de résultats les performances obtenues. Pour un système Ubuntu, l’installation se fait simplement à l’aide de la commande suivante. Pour les autres systèmes, veuillez vous référer à la documentation présente sur le dépôt.

```sh
apt-get install fio
```

L’utilisation de fio se fait en ligne de commande. Une manpage est disponible et vous décrit l’ensemble des arguments disponibles et le contenu des affichages de fin de tâche. fio peut prendre en argument le chemin d’un fichier de tâche, contenant les paramètres à utiliser. Des exemples sont disponibles sur le dépôt.

## Consigne :
En utilisant fio, vous allez devoir répondre à des énoncés vous demandant d’effectuer des comparaisons entre plusieurs tâches I/O en faisant varier un (ou plusieurs) paramètre(s). Ces comparaisons prendront la forme de graphes de bande-passante générés par vos soins et d’un texte mettant en avant les différences observées et présentant une réflexion sur la raison de ces différences. Pour l’énoncé 3, vous présenterez également un graphe de déciles des latences observées.

### Usage
Pour lancer les benchmarks :
```sh
sh scripts/bench.sh
```

Les scripts Python `.py` se situent dans le dossier `src` afin de générer les différents graphes dans le dossier `plots`.

Pour lancer la génération de tous les graphes, utilisez la commande :
```sh
sh scripts/plots.sh
```