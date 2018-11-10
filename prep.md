![](media/image1.jpeg){width="1.4875in" height="0.6819444444444445in"}

UNIVERSITÉ DU QUÉBÈC A TROIS-RIVIÈRES

DÉPARTEMENT DE MATHÉMATIQUES ET D\'INFORMATIQUE

APPLIQUÉES

Laboratoire de Mathématiques et Informatique Appliquées (LAMIA)

Préparation de la demande PRIME-VERT

Étudiant : Mohamed Amine BOUHEDADJA

Étudiant : Charles Sirois

Directeur de recherche : François Meunier

Automne 2018

 {#section .En-ttedetabledesmatires}

Problématique et objectifs (section 5.1)

La présente demande aborde la problématique de la détection automatique
des mauvaises herbes comme, par exemple : le cornouiller du Canada
(quatre-temps), la comptonie voyageuse (fougère douce) ou le kalmia à
feuilles étroites (crevard de mouton), dans les champs de bleuets nains.
Le principal objectif de ce projet de recherche consiste alors a
développer une méthode de détection automatique de mauvaises herbes dans
les champs de bleuets nains permettant de cibler plus précisément les
zones infestées par les mauvaises herbes et ainsi orienter les
opérations d'éradication manuelles dans les cultures biologiques ou
phytosanitaires (arrosage par herbicide) dans les cultures
conventionnelles (non biologiques). L'objectif de cette recherche
rejoint donc directement une des préoccupations exprimées par le MAPAQ ,
soit de : «Mettre au point de nouvelles techniques ou de nouvelles
méthodes à moindres risques contre les mauvaises herbes dans la culture
de bleuets nains». Cette approche de détection automatique des mauvaises
herbres aura alors des répercussions positives tant sur le plan
environnemental que sur le plan économique. En ciblant à priori les
zones de champs à arroser aux herbicides dans les parcelles sous culture
conventionnelle, la quantité d'herbicide requise pour l'éradication des
mauvaises herbes pourra ainsi être réduite puisque les parcelles
n'auraient plus à être arrosées systématiquement sur leur pleine
surface, diminuant ainsi l'empreinte environnementale des arrosages
d'herbicide et l'exposition massive à ces herbicides ainsi que leurs
coûts d'achat. Cette approche de détection ciblée des mauvaises herbes
pourrait aussi avoir une incidence directe sur l'efficacité de
l'éradication manuelle des mauvaises herbes dans les cultures
biologiques puisque cette opération manuelle serait alors orientée de
façon à être dirigée vers les zones infestées, permettant ainsi de
minimiser les omissions visuelles et aussi diminuer le coût
d'éradication puisque le temps requis pour la recherche visuelle des
mauvaises herbes et le nombre de passages avec la machinerie, serait
ainsi réduit.

Méthodologie (Section 5.2)

**OBJECTIF PRINCIPAL **

Dans les cultures de bleuets nains conventionnelles de même que
biologiques il est indispensable d'éliminer les mauvaises herbes, que ce
soit par arrosage par herbicide ou par sarclage, mais pour optimiser ces
opérations une bonne détection préalable des mauvaises herbes est
primordiale, ce qui permettrait de faire d'importante économies et de
contribuer à l'apport écologique (réduction des herbicides comme
l'kexazinone dans les cultures traditionnelles ou augmentation de
l'efficacité au sarclage dans les cultures biologique).

Bien que les mauvaises herbes apparaissent de façon anarchique, on peut
néanmoins se baser sur certains paramètres pour optimiser leur détection
comme la connaissance à priori des espèces de mauvaises herbes de chaque
région, leurs descriptions (hauteur, forme des feuilles, couleur du
feuillage, couleur des fleurs), leurs stades de croissance.

**OBJECTIFS SPÉCIFIQUES ET MÉTODOLOGIE**

**Sélection des parcelles témoins**

Dans ce contexte, la première phase du projet consistera à sélectionner
des parcelles de bleuets nains ayant des problématiques de mauvaises
herbes comme par exemple, le kalmia à feuilles étroites. Les surfaces
infestées seront alors répertoriées et documentées avec pour chacune des
prises d'images couleur (Visible) géoréférencées, qui permettront
ulltérieurement à faire la validation des opérations de détection
automatisées de mauvaises herbes et aussi la validation de l'efficacité
des opérations phytosanitaires (arrosage aux herbicides) ciblées à
l'aide des outils de détection automatique.

**Extraction des propriétés optiques des mauvaises herbes et du bleuet
nain**

Après avoir inventorié les espèces de mauvaises herbes présentes dans
les parcelles témoins, des analyses du feuillage des mauvaises herbes et
du bleuet nain seront effectuées à l'aide de spectromètres dans le
UV-Visible et l'Infra-Rouge et ce pour déterminer les propriétés
optiques de ces plantes et principalement leur réflectance. Ces mesures
de réflectance permettront de déterminer la sensibilité du feuillage de
ces plantes au rayonnement et ainsi évaluer le potentiel discriminant de
la réflectance pour la différentiation entre les mauvaises herbes et le
bleuet nain. Ces mesures spectrophotométriques seront effectuées pendant
une saison de végétation complète, ce qui permettra de déterminer les
variations saisonnières de la réflectance des mauvaises herbes et du
bleuet nain.

**Détection et reconnaissance des mauvaises herbes**

Ces diverses connaissances pourront alors être mises en pratique par le
biais de techniques de détection automatique afin de pouvoir faire la
reconnaissance automatique géolocalisée des mauvaises herbes et ensuite
assister le processus d'éradication de ces mauvaises herbes.

Pour pouvoir faire la détection automatique géolocalisées des zones
infestées par des mauvaises herbes, il faudra d'abord faire la capture
d'images des parcelles de bleuets nains à l'aide de drones munies de
caméras sensibles à plusieurs bandes spectrales dans le visible et le
proche infrarouge. Le choix de ces capteurs sera basé sur l'analyse
préalable des données de réflectance effectuées sur les mauvaises herbes
ciblées et le bleuet nain. Les images ainsi capturées seront ensuite
analysées pour en extraire d'abord les surfaces ayant un couvert
végétal, ensuite, des caractéristiques extraites de ces surfaces
végétales permettront de faire l'identification du type de couvert
végétal. Cette phase d'identification sera basée principalement sur les
caractéristiques de croissance des mauvaises herbes en comparaison de
celles du bleuet nain.

Les résultats obtenus du processus de reconnaissance des mauvaises
herbes seront ensuite validés par des observations faites directement
aux champs de façon visuelle et par des captures d'images géoréférencées
à l'aide de caméras portatives dans le spectre visible.

La reconnaissance automatique géolocalisée des mauvaises herbes
s'effectue à partir des régions homogènes (ex : sol, mauvaises herbes,
bleuet nain) détectées dans les images. Un ensemble de caractérisques
seront calculées pour chaque région favorisant leur discrimination
mutuelle. Pour pouvoir bien exploiter tout le potentiel de ces images,
il faudra au préalable leur faire subir des prétraitements, ces étapes
servent entre autres à ajuster les contrastes de couleurs des images,
gérer l'ombrage et la non-uniformité de l'illumination. L'utilisation de
filtres numériques et des conversions de couleurs sont aussi utile dans
cette étape d'amélioration préalable des images.

Les images des parcelles témoins étant capturées à l'aide d'un drone,
ces séquences d'images devront en plus des prétraitements cités
auparavant subir une orthorectification et un assemblage pour en déduire
une mosaïque (image complète des parcelles). Des outils comme Photoscan
Pro, Pix4D, ou Microsoft Image Composite Editor pourraient être utilisés
pour faire cet assemblage d'images.

Afin de faire la détection des mauvaises herbes, il faut détecter
(segmenter) la végétation dans les images. Plusieurs techniques de
segmentation sont basées sur des indices de végétation calculés sur
chaque pixel des images des parcelles. Les indices les plus prometteurs
dans le contexte de la détection de mauvaises herbes pourraient être :
l'indice d'excès de vert ExG, l'indice d'excès de rouge (ExR), l'indice
ExGR, l'indice NDI, l'indice NDVI, ou l'indice GNDVI. La segmentation
permet alors sur la base de ces indices de végétation calculés, de
subdiviser l'image d'une parcelle en régions distinctes (ex : sol,
végétation). Le résultat obtenu permettra aussi d'observer une
classification des divers types de couverts végétaux qu'ils soient du
bleuet nain ou des mauvaises herbes.

Étant donné que les résultats de classification (identification) peuvent
être présentés sous forme d'images géoréférencées, chaque pixel
correspondant à des surfaces infestées par des mauvaises herbes pourra
ainsi être facilement géolocalisé. Ces images seront en fait des cartes
d'occupation du sol à partir desquelles la localisation des surfaces
infestées par des mauvaises herbes sera explicite.

Ces cartes pourraient ensuite être utilisées lors des opérations
d'arrosage aux herbicides pour ainsi ciblées plus précisément les
surfaces où doivent être appliquées les traitements (arrosage). Un
opérateur d'un tracteur munie d'un GPS, pourrais utiliser la carte de
répartition des mauvaises herbes géoréférencées pour actionner
l'arrosage dans les zones strictement infestées.

État des connaissancs actuelles (SECTION 5.3)

Durant la saison de végétation 2018, certaines études exploratoires ont
été effectuées par le demandeur principal et un étudiant de maîtrise en
informatique, sur des bleuetières situées au nord de La Tuque. Ces
études ont portées sur l'évaluation comparative des propriétés de
réflectance du feuillage du bleuet nain et du kalmia à feuilles
étroites. Comme les expérimentations faites par Yang \[1\], des mesures
de réflectance ont été prise sur le feuillage du bleuet nain et le
kalmia à l'aide de spectromètres UV-VIS (Cary-60 UV-Vis, Agilent
Technologies) et Infrarouge (Nicolet iS10 FT-IR, Thermo Fischer
Scientific). Ces observations ont permis de confirmer certaines des
observations faites par le producteur propriétaire des bleuetières et
des données déjà repertoriées dans la littérature à l'effet que entres
autres le kalmia est une plante dont le feuillage est persistant même
tard à l'automne lorsque le feuillage du bleuet est déjà tombé depuis
quelques semaines \[2\]. Cette observation pourrait ainsi favoriser la
discrimination entre le bleuet et le kalmia, sachant que lors de la
chute des feuilles du bleuet en octobre, le kalmia a encore un feuillage
vert.

Ces études préliminaires ont aussi permis de tester des équipements de
capture d'images portés sur drone pour l'acquisition de séries d'images
des bleuetières étudiées. Comme plusieurs auteurs dans la litérature
\[3-5\], certains indices de végétation, dont l'indice ExG, ont été
calculés à partir de ces images permettant d'évaluer leur potentiel
discriminant pour faire la reconnaissance des mauvaises herbes comme le
kalmia.

D'autre part, plusieurs publications portant sur la détection de la
végétation en général et aussi plus spécifiquement sur la détection des
mauvaises herbes dans les cultures sont accessibles dans la littérature
\[6-8\]. La plupart des études publiées utilisent les indices de
végétation comme facteur discriminant pour la détection des mauvaises
herbes et basent donc le processus de classification (détection) sur ces
indices et ce pour détecter la présence ou l'absence de mauvaises herbes
dans les cultures en rang comme le mais et le soya \[9\]. Peu d'études
pourtant sur la détection des mauvaises herbes dans les bleuetières sont
répertoriées dans la littérature.

Les cartes de répartition des mauvaises herbes produites par le
processus de détection automatique pourrraient devenir des cartes
d'épandage d'herbicide permettant ainsi un arrosage localisé.
L'automatisation de la production des cartes d'épandage découlant du
système de détection automatique des mauvaises herbes développé,
pourrait être greffé à un outil d'arrosage localisé dont les cartes
d'épandage sont produites manuellement \[10-11\].

Aspects novateurs du projet (SECTION 5.4)

Ce projet permettra d'abord d'atténuer grandement les problématiques
environnementales liées à l'application massive d'herbicide dans les
bleuetières de bleuets nains conventionnelles en permettant de cibler à
priori les zones infestées par des mauvaises herbes comme le Kalmia à
feuilles étroites et ainsi limiter les arrosages à ces zones infestées.
L'approche préconisée est originale en ce sens qu'elle est une des
premières tentatives pour réduire par la détection automatique par drone
des mauvaises herbes, les quantités d'herbicide appliqué tout en
éliminant la problématique de mauvaises herbes comme le kalmia.

Cette approche est aussi novatrice au niveau de la possibilité de
généralisation de l'approche de détection de mauvaises herbes dans les
cultures de bleuets nains biologiques. La production de cartes
géoréférencées de répartition des mauvaises herbes dans les cultures
biologiques pourrait permettre de mieux aiguiller les efforts
d'éradication manuelle par sarclage ou automatisée par fauchage.

La détection automatique géoréférencées de mauvaises herbes développée
pourra aussi être généralisée dans son application à d'autres types de
mauvaises herbes comme le quatre temps (Cornouillier du canada), la
comptonie voyageuse. La connaissance des spécificités des stades de
végétation de chaque espèce de mauvaises herbes favorisera leur
détection. En guise d'exemple, nos observations préliminaires et les
données colligées dans la littérature nous permettent d'envisager la
détection du quatre temps à bonne heure au printemps sachant
que l'émergence des premières feuilles de cette plante se fait avant
celles du bleuet nain.

BIBLIOGRAPHIE

\[1\] Yang, S., SPECTRAL ANALYSIS AND MULTISPECTRAL/HYPERSPECTRAL
IMAGING TO DETECT BLUEBERRY FRUIT MATURITY STAGES FOR EARLY BLUEBERRY
YIELD ESTIMATION, PhD. Thesis, 2013, pp. 1-134.

\[2\] Agriculture, Aquaculture et Pêches , NB Canada, Utilisation
automnale de glyphosate pour la lutte contre le crevard de moutons,
Feuillet de renseignements sur le bleuet sauvage C.4.7.0, Révisé 2015.

\[3\] Hamuda, E., Glavin, M., & Jones, E., A survey of image processing
techniques for plant extractionvand segmentation in the field, Computer
& Electronic in Agriculture, Vol. 125, July 2016, pp. 184-199.

\[4\] Meyer, G.E, & Carmago Neto, J., Verification of color vegetation
indices for automated crop imaging applications, Cpmputers and
Electronic in Agriculture, 63, 2008, pp. 282-293.

\[5\] Xue, J., Baofeng, S,. Significant Remote Sensing Vegetation Indices: A Review of Developments and Applications, Journal of Sensors, Vol, 2017. pp. 1-17.
--------------------------------------------------------------------------------------------------------------------------------------------------------------

\[6\] Chen, L., ZHANG, J., SU, H., & GUO, W., WEED IDENTIFICATION METHOD
BASED ON PROBABILISTIC NEURAL NETWORK IN THE CORN SEEDLINGS FIELD,
Proceedings of the Ninth International Conference on Machine Learning
and Cybernetics, Qingdao, July 2010, pp. 1528-1531

\[7\] Tang, T. L., Chen, X-Q, Miao, R-H, & Wang, D., Weed Detection
Using Image Processing Under Different Illumination for Site-Specific
Area Spraying, Computers and Electronics in Agriculture, 122, 2016, pp.
103-111.

\[8\] Jeom, H.Y., Tian, L-F, & Zhu, H., Robust Crop and Weed
Segmentation under Uncontrolled Outdoor Illumination , Sensors 2011, 11,
pp, 6270-6283.

\[9\] Dos Santos Ferreira, A., Matte Freitasa, D., Gonçalves da Silvaa,
G., Pistorib, H., & Theophilo Folhesc, M., Weed detection in soybean
crops using ConvNets, Computers and Electronics in Agriculture, 143,
2017, pp. 314-324.

\[10\] Gagnon, S.(Agrinova), Évaluation des pratiques ayant le meilleur
potentiel de réduction des herbicides dans la production du bleuet nain,
Rapport final, Janvier 2009

\[11\] Gagnon, S., Morissette, S., et Bouchard, B., Méthodologie pour
l'application localisée d'herbicide dans la production du bleuet nain
semi-cultivé : Fiche d'information.
