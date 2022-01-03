# PO3L_Ecosystem


par Edouard d.S.d.L. 18072
## Introduction
#### L'objectif du projet était de créer une simulation d'un Ecosystème contenant des Animaux (des prédateurs et des proies) et des plantes, lesquelles se nourissent des matières organiques des animaux décédés. Pour effectuer ce projet j'ai choisi d'utiliser le language python et d'utiliser pygame pour créer une simulation dans lesquelles nos objets se promeneront de manière aléatoire.

## Les classes
Pour pouvoir créer cette simulation devons utiliser des classes pour créer nos différents éléments:

##Lifeforms
Nous commencons donc par créer la classe principale qui est appelé "lifeforms" de celle-ci déscendent toute les autres classes. Elle indique tout les paramètres qu'une forme de vie contient. C'est-à-dire points de vies, niveau d'énergie, la taille de celle-ci dans notre simulateur ainsi que son état actuel: la position X et Y dans notre monde virtuel.

##Animals
Cette classe sert à initialiser les différents paramètres de nos animaux comme le sexe, la vitesse à laquelle il peut se déplacer ainsi que de voir si il est enceinte ou pas. De cette classe nous pouvons alors déscendre vers nos deux types d'animaux les prédateurs et les proies qui se déplaceront dans notre ecosystème.

## Predator and Herbivore
Ces deux classes-ci représentent nos deux sortes d'animaux dans notre écosystème les deux éléments sont surtout important car ils contiennent une fonction appelée update() qui va indiquer un déplacement random au prédateurs ou proies en fonction de si oui ou non ils sont encore en vie.

##Plants
Notre dernière classe qui déscend de lifeforms est la classe plante qui reprends les éléments de base d'une lifeform c'est à dire le niveau d'énergie et le niveau de points de vie, mais qui contrairement au animaux ne se déplacera pas dans notre écosystème. 



## Diagramme de classes
