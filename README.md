# PO3L_Ecosystem


par Edouard d.S.d.L. 18072
## Introduction
L'objectif du projet est de créer une simulation d'un Ecosystème contenant des Animaux (des prédateurs et des proies) et des plantes, lesquelles se nourissent des matières organiques des animaux décédés. Pour effectuer ce projet j'ai choisi d'utiliser le language python et d'utiliser pygame pour créer une simulation dans lesquelles nos objets se promeneront de manière aléatoire.

## Les classes
Pour pouvoir créer cette simulation devons utiliser des classes pour créer nos différents éléments:

Lifeforms:

Nous commencons donc par créer la classe principale qui est appelé "lifeforms" de celle-ci déscendent toute les autres classes. Elle indique tout les paramètres qu'une forme de vie contient. C'est-à-dire points de vies, niveau d'énergie, la taille de celle-ci dans notre simulateur ainsi que son état actuel: la position X et Y dans notre monde virtuel.

Animals:

Cette classe sert à initialiser les différents paramètres de nos animaux comme le sexe, la vitesse à laquelle il peut se déplacer ainsi que de voir si il est enceinte ou pas. De cette classe nous pouvons alors déscendre vers nos deux types d'animaux les prédateurs et les proies qui se déplaceront dans notre ecosystème.

Predator and Herbivore:

Ces deux classes-ci représentent nos deux sortes d'animaux dans notre écosystème les deux éléments sont surtout important car ils contiennent une fonction appelée update() qui va indiquer un déplacement random au prédateurs ou proies en fonction de si oui ou non ils sont encore en vie.

Plants:

Notre dernière classe qui déscend de lifeforms est la classe plante qui reprends les éléments de base d'une lifeform c'est à dire le niveau d'énergie et le niveau de points de vie, mais qui contrairement au animaux ne se déplacera pas dans notre écosystème. 

Fonctionnement:

Dans notre onglet pygame qui sera ouvert une fois la simulation lancé nous verrons 3 types d'objets qui ont été crée: en Blanc nos prédateurs en Vert Foncé nos herbivores et en vert nos plantes. Nous verrons alors que nos deux types d'animaux se promennent de manière aléatoire dans notre simulation et qu'ils meurent une fois que leurs HP est à zéro.
Nos plantes ne se déplacent pas et se nourissent de la matière organique laissé par des cadavres des animaux décédé.

## Diagramme de classes
![Ceci est le diagramme de classes correspondant](https://raw.githubusercontent.com/ELophem/POOprojet2021/main/Diagramme%20de%20classe%20ECOSYSTEM.png?token=AOPPNMEHYZAYJLFI43ESTDDB2LLPS)







## Principes SOLID

Pour pouvoir programmer notre simulation de manière compréhensible nous avons utilisé la méthode SOLID.

Par exemple:

Le S (Single responsibility principle) nous indique qu'une classe ou une méthode doit avoir une seule résponsabilité. Si nous prennons l"exemple de notre classe Herbivore nous voyons que cette classe a comme unique objectif de créer notre type d'animal (herbivore). Et rien d'autre les attributs plus généraux de cet objet sont pris à la classe animal et lifeforms. (hp,energy,speed ...)

Le O (Open/Closed principle) indique que notre programme doit être fermée à la modification directe mais ouvert à l'extension. C'est à dire que nous pouvons devoir ajouter un objet sans devoir réecrire tout le code. Ceci est le cas car si nous voulions rajouter un type d'animal nous créerons simplement une nouvelle classe qui déscendra de la classe Animal. En faisant par exemple: class Fish(Animals):




