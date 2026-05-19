**Partea I: un singur raspuns corect**

1.  Tipurile de probleme care pot fi rezolvate pe baza **calcului
    evolutiv** sunt: **Probleme de optimizare (1), Probleme de modelare
    (4), Probleme de simulare (6) -\> 1,4,6 (B).**

2.  Care din urmatorii operatori pot fi utilizati intr-un algoritm
    genetic care foloseste reprezentarea prin siruri reale? **Mutatia
    uniforma (5), Mutatia neuniforma cu -distributie fixata (6),
    Aritmetica simpla (18), Aritmetica singulara (19), Aritmetica totala
    (20), Unipunct (14), Multipunct(15), Uniforma(16) -\> (A)**

3.  In algoritmii genetici, reprezentarea prin siruri de numere intregi:
    **e preferabila atunci cand pentru fiecare gena sunt posibile mai
    mult de doua valori distincte (D).**

4.  In algoritmii genetici, reprezentarea prin permutari: **necesita
    operatori de variatie special definiti (D)**.

5.  Calculul evolutiv este inspirat de: **evolutia naturala biologica
    (A).**

6.  Algoritmul Hillclimbing: **se aplica asupra unui singur punct din
    spatiul de cautare (1), Aplicarea de poate repeta pentru mai multe
    puncte pentru a creste performantele (2), De obicei gaseste un punct
    de optim local (7), Gaseste uneori solutia optima (5)**

[**Later edit: nu gaseste mereu solutia optima.(closed) -
Cezar**]{.mark}

7.  In algoritmii genetici, reprezentarea binara: **(B) A fost primul
    tip de reprezentare a cromozomilor in algoritmii genetici**

8.  Caracteristicile unui algoritm genetic clasic: **(E)1,3,5,8
    \--1.Reprezentarea populatiei este realizata prin intermediul
    sirurilor binare, 3.Probabilitatea de selectie a unui individ in
    multisetul parintilor este proportionala cu valoarea functiei de
    evaluare pentru el; 5. Probabilitatea efectuarii unei mutatii este
    mica; 8.Probabilitatea efectuarii recombinarii este mare**

9.  Intr-un algoritm evolutiv, functia de tip calitate: **Evalueaza
    calitatea fiecarui candidat (2), Trebuie maximizata(4)** **(B)**

10. Componentele algoritmilor evolutivi sunt: **reprezentarea, functia
    de evaluare, populatia, mecanismul de selectare a parintilor,
    operatorii de variatie, mecanismul de selectare a membrilor
    generatiei urmatoare, definirea modului de initializare(populatia
    initiala) si definirea conditiei terminale =\> raspuns corect: (B)**

**PARTEA II - variante multiple(gen)**

1.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de mutatie:**

a\. Este utilizata doar in probleme cu constringeri

[b. Este realizata cu probabilitate mica]{.mark}

c\. Utilizeaza populatia curenta

[d. Utilizeaza populatia de copii]{.mark}

[e. Determina structura cromozomiala]{.mark}

[f. Este de tip neuniform]{.mark}

g\. Alege pentru mutatie in medie jumatate de indivizi

h\. Este efectuata o singura data pe parcursul unui algoritm

[i. Este efectuata iterativ]{.mark}

[j. Este efectuata imediat ce este disponibila o populatie de
copii]{.mark}

**2. In cadrul unui algoritm genetic operatia de recombinare:**

a\. Este efectuata o singura data dupa prima etapa de selectie a
parintilor

b\. Este utilizata cu probabilitate mica

c\. In general probabilitatea de recombinare nu conteaza in rezolvarea
problemelor prin algoritmi genetici

d\. Este efectuata o singura data pe parcursul unui algoritm genetic

e\. [Este efectuata imediat inaintea fiecare proceduri de
mutatie]{.mark}

[f. Este efectuata imediat dupa fiecare etapa de selectie a
parintilor]{.mark}

[g. Este utilizata cu probabilitate mare **(intre 0.5 si 1, pag.
79)**]{.mark}

[h. Este efectuata iterativ]{.mark}

i\. Este utilizata doar in probleme fara constrangeri

[j. Utilizeaza populatia de parinti **(recombinarea celor doi
parinti)**]{.mark}

**3. In cadrul unui algoritm evolutiv populatia initiala**

a\. Este generata la inceputul fiecarui ciclu evolutiv-nu, pentru ca
ciclu evolutiv inseamna fiecare generatie si nu e adevarat.

b\. Este generata utilizand distributia pe probabilitate normala

[c. Este generata inaintea inceperii evolutiei propriu-zise]{.mark}

d\. Este generata dupa fiecare ciclu evolutiv

e\. Este generata utilizant distributia de probabilitate uniforma

[f. Este generata aleator **(setul initial de candidati este generat
aleator, curs 1)**]{.mark}

g\. Este setata pe multimea vida

**4.** [rezolvat corect]{.comment-start id="0"
author="Cătălina-Teodora Ianuş" date="2018-05-28T11:41:00Z"}**Fie
urmatorii doi cromozomi de tip permutare {6, 3, 11,7, 14, 8, 5, 15, 1,
2, 4, 13, 9 ,10 ,12 } si {7, 1, 15,13,2, 14,6,10,12,11,4,8,3,9, 5}.
Aplicand operatorul de recombinare PMX, cu pozitile 4 si 8 se obtin
descendentii.**[]{.comment-end id="0"}

. **a. 5 3 15 13 2 14 6 10 12 8 4 7 9 11 1**

b\. 5 3 11 13 2 14 6 15 1 8 4 7 9 10 12

[c. 5 3 11 13 2 14 6 15 1 8 4 7 9 15 12 - al doilea copil]{.mark}

[d.13 1 10 [7 14 8 5 15]{.underline} 12 11 4 2 3 9 6 - primul
copil]{.mark}

e\. 5 3 15 13 2 14 6 10 1 8 4 7 9 11 12

f\. 13 1 15 7 14 8 5 10 12 11 4 2 3 9 6

g\. [13]{.underline} 12 11 [7 14 8 5 15]{.underline} 1 10 4 2 3 9 6

h\. [13]{.underline} 1 11 [7 14 8 5 15]{.underline} 12 10 4 2 3 9 6

i\. [13]{.underline} 12 11 [7 14 8 5 15]{.underline} 1 10 4 2 3 9 6

j\. 5 3 15 13 2 14 6 10 12 8 4 7 9 11 1

**5. In cadrul unui algoritm din clasa strategiilor evolutive, operatia
de recombinare:**

[a. Este de tip local sau global]{.mark}

b\. Este efectuata o singura data pe parcursul unui algoritm

c\. Alege pentru recombinare in medie jumatate de indivizi

d\. Este realizata cu probabilitate mica

e\. Determina structura cromozomiala

[f. Utilizeaza poplatia curenta]{.mark}

g\. Este efectuata o singura data, dupa prima etapa de generare a unei
populatii

h\. [Determina obtinerea unui multiset de copii in general de dimensiuni
mai mari comparativ cu populatia curenta.]{.mark}

i\. Este utilizata doar in probleme cu constrangeri

[j. Este efectuata iterativ]{.mark}

**6. In cadrul unui algoritm din clasa strategiilor evolutive,
reprezentarea cromozomilor**

> a\. Influenteaza tipul de recombinare folosit
>
> b\. Se alege in functie de problema care se rezolva
>
> c\. Poate fi numai de tip siruri de numere intregi sau reale
>
> d\. Poate fi oricare dintre: siruri binare, siruri de numere intregi,
> siruri de numere reale, permutari
>
> e\. Are influenta asupra mecanismului de selectie a generatiei
> urmatoare
>
> f\. [Nu influenteaza tipul de mutatie folosit(discreta/
> nediscreta)]{.mark}
>
> [g. Poate fi numai de siruri de numere reale]{.mark}
>
> h\. [Contine atat descrierea individului candidat cat si parametrii
> care controleaza evolutia sa.]{.mark}

**7. In cadrul unui algoritm genetic operatia de selectie a parintilor**

a\. Intotdeauna este bazata pe o distributie de probabilitate de
selectie

[b. Utilizeaza populatia curenta]{.mark}

c\. Este efectuata o singura data pe parcursul unui algoritm genetic

d\. Este utilizata doar in probleme cu constringeri

e\. Este efectuata imediat inaintea fiecarei proceduri de mutatie

[f. Este efectuata imediat ce este disponibila o populatie curenta
eva]{.mark}

[luata]{.mark}

g\. Este efectuata o singura data dupa prima etapa de generare a unei
populatii

h\. Alege in general indivizi pe baza factorului varsta

i\. Utilizeaza populatia de copii mutati

j\. Utilizeaza populatia de copii

[k. Este efectuata iterativ]{.mark}

[l. Poate fi realizata prin utilizarea unei distributii de probabilitate
de selectie]{.mark}

**8. Fie urmatorul cromozom de tip permutare {7, 6, 12, 14, 3, 10, 8,
15, 11, 5, 4, 1, 13, 2, 9} In urma aplicarii operatorului de mutatie
prin amestec s-a obitnut cromozomul {7, 14, 13, 12, 1, 15, 2, 8, 6, 3,
11, 5, 10, 4, 9 }. Cele doua pozitii utilizate pentru amestesc sunt:**

**7, [6, 12, 14, 3, 10, 8, 15, 11, 5, 4, 1, 13, 2,]{.underline} 9**

**7, 14, 13, 12, 1, 15, 2, 8, 6, 3, 11, 5, 10, 4, 9**

a\. 3 si 13

[b. 1 si 15]{.mark}

[c. 1 si 14]{.mark}

d\. 4 si 8

e\. 1 si 12

f\. 4 si 15

g\. 3 si 15

h\. 2 si 13

[i. 2 si 14]{.mark}

[j. 2 si 15]{.mark}

k\. 1 si 13

**9. In cadrul unui algoritm genetic operatia de mutatie**

[a.]{.mark} [Are probabilitate mica]{.mark}

b\. Se aplica doar daca divesitatea genetica scade sub un prag x dat

c\. Intotdeauna produce indivizi fezabili

[d. Se aplica asupra descendentilor produsi de operatia de
recombinare]{.mark}

e\. Se aplica asupra mutlisetului de parinti

f\. Se aplica asupra populatiei curente

g\. Se utilizeaza doar in probleme cu constrangeri

h\. [Poate sa produca indivizi nefezabili]{.mark}

i\. Se efectueaza o singura data, dupa generarea populatiei initiale
**(mutatia se face de mai multe ori; in cazul unui algoritm genetic,
mutatia se face in fiecare era)**

j\. Se aplica imediat inaintea fiecarei etape de selectie a generatiei
urmatoare **(cred ca dupa mutatie urmeaza evaluare si dupa aceea
selectia.- deci asta nu ar fi)**

k\. Se utilizeaza doar in problemele fara constrangeri

l\. Nu foloseste factori aleatori.

**10. In cadrul unui algoritm genetic operatia de seleXCCCCCCSCC**

[g. Se aplica asupra populatiei curente si asupra descendentilor
obtinuti]{.mark}

h\. Garanteaza obtinerea unei generatii cu calitate medie superioara.
Daca foloseste selectia bazata pe varsta. **(ASTA ESTE GENITOR, NU
VARSTA)**

i\. Se aplica asupra descendentilor. Asigura perpetuarea individului cu
calitate maxima din populatia curenta

[j. Alege generatia urmatoare dintre indivizii disponibili dupa operatia
de mutatie]{.mark}

k\. Se aplica asupra descendentilor obtinuti din populatia curenta

Grile PEAG:

1.  Fie X = \[6 1 8 10 5 7 9 3 4 2\] si Y = \[9 8 7 3 6 1 5 10 4 2\]
    permutari. Care urmasi sunt generati prin utilizarea operatorului
    CX?

Raspuns corect:

C1=\[6 8 7 10 5 1 9 3 4 2\], C2=\[9 1 8 3 6 7 5 10 4 2\]

2.  Intr-un algoritm evolutiv, functia de tip calitate:

<!-- -->

a.  Evalueaza calitatea algoritmului

b.  Evalueaza calitatea fiecarui candidat

c.  Evalueaza viteza de gasire a solutiei fata de consumul de resurse

d.  Trebuie maximizata

e.  Stabileste daca un descendent este acceptabil

f.  Selecteaza indivizii care se vor reproduce

g.  Selecteaza indivizii care trec in generatia urmatoare

h.  Contine un factor aleator

i.  Evalueaza calitatea populatiei curente

j.  Evalueaza calitatea populatiei curente fata de cea din generatia
    anterioara

> Raspuns corect:
>
> b, d

3.  In cadrul unui algoritm genetic operatia de selectia a parintilor

- Este efectuata iterative

- Utilizeaza populatia curenta

- Este efectuata imediat ce este disponibila o populatie curenta
  evaluate

- Poate fi realizata prin utilizarea unei distributii de probabilitate
  de selectie

4.  Componentele algortmilor evolutivi sunt:

<!-- -->

a.  Reprezentarea

b.  Probabilitatea de mutatie

c.  Functia de evaluare

d.  Probabilitatea de recombinare

e.  Populatia

f.  Generarea de numere aleatoare

g.  Mecanismul de selectie a parintilor

h.  Generarea de permutari

i.  Reprezentarea grafica a evolutiei calitatii

j.  Operatorii de variatie

k.  Stabilirea diversitatii genetice a populatiei

l.  Mecanismul de inlocuire a populatiei curente

m.  Hillclimbing

n.  Initializarea populatiei

o.  Conditia de terminare

> Raspuns corect:
>
> a, c, e, g, j, l, n, o

5.  Calculul evolutiv este inspirat din:

\-\--evolutia naturala biologica

6.  Fie urmatorii doi cromozomi de tip permutare {6, 3, 11 , 7, 14, 8,
    5, 15, 1, 2, 4, 13, 9, 10, 12} si {7, 1, 15, 13, 2, 14, 6, 10, 12,
    11, 4, 8, 3, 9, 5}. Aplicand operatorul de recombinare PMX, cu
    pozitiile 4 si 8 se obtin descendentii:

Raspuns corect:

h\. 13 1 10 7 14 8 5 15 12 11 4 2 3 9 6

i\. 5 3 11 13 2 14 6 10 1 8 4 7 9 15 12

7.  In cadrul uni algoritm genetic operatia de selectie a
    supravietuitorilor

- Se aplica asupra populatiei curente

- Indivizii alesi sunt intotdeauna fezabili

- Uneori utilizeaza factori aleatori

- In unele variante necesita calcularea unei distributii de
  probabilitate de selectie

- Se aplica asupra descendentilor obtinuti din populatia curenta

8.  Caracteristicile unui algoritm genetic clasic(canonic) sunt:

- Reprezentarea populatiei initiale este realizata prin intermediul
  sirurilor binare

- Probabilitatea de selectie a unui individ in multisetul parintilor
  este proportional cu valoarea functiei de evaluare pentru ei

- Probabilitatea efectuarii unei mutatii este mica

- Probabilitatea efectuarii recombinarii este mare

9.  In cadrul unui algoritm evolutiv populatia initiala

- Este generata aleator

- Este generata inaintea inceperii evolutiei propriu-zise

10. In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de recombinare:

- Este efectuata iterative

- Determina obtinerea unui multiset de copii in ..

- Utilizeaza populatia curenta

- Este de tip local sau global

11. Care dintre urmatorii operatori pot fi utilizati intr-un algoritm
    genetic care foloseste reprezentarea prin siruri de numere reale:

- Mutatia uniforma

- Mutatia neuniforma cu distributie fixata

- Unipunct

- Multipunct

- Uniforma

- Aritmetica simpla

- Aritmetica singulara

- Aritmetica totala

12. In cadrul unui algoritm genetic operatia de recombinare:

- Utilizeaza populatia de parinti

- Este efectuata imediat dupa fiecare etapa de selectie a parintilor

- Este efectuata imediat inaintea fiecarei procedure de mutatie

- Este efectuata iterative

- Este utilizata cu probabilitate mare

13. In algoritmii genetici, reprezentarea prin siruri de numere intregi

- E preferabila atunci cand pentru fiecare gena sunt posibile mai mult
  de doua valori distincte

14. In cadrul unui algoritm din clasa strategiilor evolutive,
    reprezentarea cromozomilor

- Poate fi numai de siruri de numere reale

- Nu influenteaza tipul de mutatie folosit(discrete/nediscreta)

- Contine atat descrierea individului candidat cat si parametrii care...

15. In cadrul unui algoritm genetic operatia de selectie a
    supravietuitorilor

- In unele variante necesita calcularea unei distributii de
  probabilitate de selectie

- Alege generatia urmatoare dintre indivizii disponibili dupa operatia
  de mutatie

- Indivizii alesi sunt intotdeauna fezabili

- Uneori utilizeaza factori aleatori

- Se aplica asupra populatiei curente si asupra descendentilor obtinuti
  din populatia curenta

16. Tipurile de probleme care pot fi rezolvate pe baza calculului
    evolutiv sunt:

- Probleme de cautare in spatial solutiilor

- Probleme de modelare

- Probleme de simulare

- Deplasarea autonoma a autovehiculelor

17. In algoritmii genetici, reprezentarea prin permutari

- Necesita operatori de variatie special definite

18. Intr-un algoritm evolutiv, functia fitness:

- Evalueaza calitatea fiecarui candidat

19. Fie urmatorul cromozom de tip permutare {7, 6, 12, 14, 3, 10, 8, 15,
    11, 5, 4, 1, 13, 2, 9}. In urma aplicarii operatorului de mutatie
    prin amestec s-a obtinut cromozomul {7, 14, 13, 12, 1, 15, 2, 8, 6,
    3, 11, 5, 10, 4, 9}. Cele doua pozitii utilizate pentru amestec
    sunt:

- 2 si 14

- 1 si 14

- 2 si 15

- 1 si 15

20. In algoritmii genetici, reprezentarea binara

- A fost primul tip de reprezentare a cromozomilor in algoritmi genetici

21. In cadrul unui algoritm genetic operatia de mutatie:

- Se aplica asupra descendetilor produsi de operatia de recombinare

- Poate sa produca indivizi refezabili

- Are probabilitate mica

22. In algorimii genetici, reprezentarea prin permutari

- Are nevoie de operatori speciali definite

23. In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de mutatie

- Utilizeaza populatia de copii

- Este efectuata iterative

- Este de tip neuniform

24. Algoritmul Hillclimbing

- Se aplica asupra unui singur punct din spatiul de cautare

- Aplicarea se poate repeat pentru mai multe puncte pentru a creste
  performantele

- Gaseste uneori solutia optima

- De obicei geseste un punct de optim local

25. care nu este un mecanism de selectie: -\> ruleta complicata

26. Ruleta multi-brat trebuie rotita doar o data pentru a executa
    intregul proces de selectie al parintilor

27. Care mecanism de selectie reproduce rezultate cat mai apropiate de
    distributia de probabilitate? -\> SUS(\...)

28. Mecanismul de selectie turnir -\> nu respecta distributia de
    probabilitate de selectie

29. Care din urmatoarele nu sunt modele de populatie? -\> cu generatii,
    cu dimensiune fixa, cu dimensiune variata, cu stari instabile

30. Care sunt modele de populatie? -\> cu stari stabile

31. In cadrul algoritmilor genetici, urmatoarea generatie este selectata
    dintre:

> -\> indivizii generatiei curente si descendentii obtinuti dupa etapa
> de mutatie

32. Care din urmatoarele este un dezavantaj pt distributia de
    probabilitate FPS? -\> convergenta premature

33. De cate ori tre rotit bratul ruletei simple pentru a executa
    intregul proces de selectie al parintilor pt o populatie cu tz
    cromozomi-\> de tz ori

34. In cadrul algoritmilor genetici, generatia urmatoare este selectata
    dintre:

-\> indivizii generatiei curente si descendentii obtinuti dupa etapa de
mutatie

35. Care din urmatoarele nu este un model de distributie folosit pt
    etapa de selectie:

-\> FPS cu alfa scalare

36. Care dintre urmatoarele este falsa pt modelul generational?

-\> nu tine cont de calitatea cromozomilor

37. Daca aplicarea unui operator de recombinare produce indivizi
    aberanti, atunci:

-\> se folosesc parintii ca descendenti

SAU

-\> algoritmul produce totusi rezultate corecte, ca urmare a
autoreglarii prin selectie

38. Mecanismul de selectie turnir -\> este intotdeauna un tip
    determinist

39. Pt pastrarea relatiilor comune din cromozomii parinti se foloseste
    operatorul de recombinare

-\> EXC (Edge crossover)

40. Recombinarea multipla

-\> produce rezultate mai bune doar in unele cazuri particulare

41. Schema generala de recombinare depinde de: -\> operatorul de
    recombinare folosit

42. In cazul reprezentarii cu siruri de numere intregi, recombinarile
    aritmetice:

-\> se pot aplica numai daca toate perechile de alele de pe pozitii
identice sunt fie pare, fie impare

43. Pt a pastra cat mai bine informatia referitoare la pozitiile
    absolute ale alelelor in cromozomii parinti se foloseste operatorul:

-\> CX (Cycle crossover)

44. Pentru problemele in care reprezentarea prin permutari semnifica
    ordinea de aparitie a unor evenimente, operatorul de recombinare
    folosit este

-\> OCX (Order crossover)

45. In algoritmii genetici, reprezentarea prin permutari:

-\> Necesita operatori de variatie special definite

46. Intr-un algoritm evolutiv, functia fitness: -\> Evalueaza calitatea
    fiecarui individ

47. In cadrul strategiilor evolutive: -\> Mutatia este aplicata cu
    probabilitate

48. In cadrul unui algoritm genetic, operatia de selectie a
    supravietuitorilor:

> -\>In unele variante necesita calcularea unei distributii de selectie
>
> -\>Alege generatia urmatoare dintre indivizii disponibili dupa
> operatia de mutatie
>
> -\>Indivizii alesi sunt intotdeauna fezabili (ce plm inseamna
> fezabil?)
>
> -\> Uneori utilizeaza factori aleatori
>
> -\> Se aplica asupra populatiei curente si asupra descendentilor
> obtinuti din populatia curenta

**Partea I:**

1.  În algoritmii genetici, **rerezentarea prin șiruri de numere
    întregi**

<!-- -->

1.  Este preferabila pentru probleme de optimizare

2.  Este doar un exercitiu de implementare, nefiind necesara

3.  E preferabila atunci cand pentru fiecare gena sunt posibile mai mult
    de doua valori distincte

4.  nu este utilizata in algoritmi genetici

5.  Nu poate fi utilizata in cazul atributelor ordinale

<!-- -->

2.  In algoritmii genetici, **reprezentarea prin permutări**

<!-- -->

1.  Nu permite utilizarea de operatori de mutatie

2.  Nu este utilizata

3.  Are nevoie de operatori special definiti **(Vezi cursul II: - Slide
    19)**

4.  Nu permite utilizarea de operatori de recombinare

5.  Nu permite mai mult de doua gene cu aceeasi valoare intr-un cromozom

<!-- -->

3.  **Tipurile de probleme care pot fi rezolvate pe baza calculului
    evolutiv **sînt: 1. Problemele de optimizare; 2.Probleme de cautare
    in spatiul solutilor; 3. Prelucrarea datelor de dimensiune
    mare(big-data); 4. Probleme de modelare; 5.Probleme de validare a
    datelor; 6. Probleme de simulare; 7 Alocarea dinamica a datelor in
    memoria calculatorului; 8. Deplasarea autonoma a vechiculelor

<!-- -->

1.  2,4,6

2.  1,4,6**(Vezi cursul I: Introducere: - Slide 9 si 10)**

3.  2,4,6,8

4.  1,3,5,7

5.  2,3,4

<!-- -->

4.  **Intr-un algoritm evolutiv**, functia de tip calitate: 1. Evalueaza
    calitatea algoritmului, 2. Evalueaza calitatea fiecarui candidat; 3.
    Evalueaza viteza de gasire a solutiei fata de consumul de
    resurse; 4. Trebuie maximizata; 5. Stabileste daca un descendent
    este acceptabil; 6. Selecteaza indivizii care se vor reproduce; 7.
    Selecteaza indivizii care trec in generatia urmatoare; 8. Contine un
    factor aleator; 9. Evalueaza calitatea populatiei curente; 10.
    Evalueaza calitatea populatiei curente fata de cea din generatia
    anterioara;

<!-- -->

1.  6,7,8

2.  5

3.  2,4**(Vezi cursul I: Introducere - Slide 11)**

4.  1,3

5.  9,10

<!-- -->

5.  **In algoritmii genetici, reprezentarea binara**

<!-- -->

1.  Este cea mai utilizata varianta de reprezentare a genotipurilor

2.  Nu e utilizata pentru algoritmi genetici

3.  A fost primul tip de reprezentare a cromozomilor in algoritmi
    genetici**(Vezi cursul 2: Slide 14)**

4.  Duce mereu la rezultate optime

5.  Nu depinde de problema rezolvata

<!-- -->

6.  **Componentele algoritmilor evolutivi sunt: **1. Reprezentarea; 2.
    Probabilitatea de mutatie; 3. Functia de evaluare; 4. Probabilitatea
    de recombinare; 5. Populatia; 6. Generarea de numere aleatoare; 7.
    Mecanismul de selectie a parintilor; 8. Generarea de permutari; 9.
    Reprezentarea grafica a evolutiei calitatii; 10; Operatorii de
    variatie; 11. Stabilirea diversitatii genetice a populatiei; 12.
    Mecanismul de inlocuire a populatiei curente; 13. Hillclimbing; 14;
    Initializarea populatiei; 15. Conditia de terminare;

<!-- -->

1.  1,2,5,6,7,14,15

2.  1,3,5,7,10,12,14,15

3.  2,4,6,8,11,13

4.  2,4,5,9,15

5.  1,3,5,6,10,13,14,15

<!-- -->

7.  **Calculul evolutiv este inspirat din**

<!-- -->

1.  Revolutia industriata

2.  Societatea cunoasterii

3.  Societatea informationala

4.  Noua revolutie agrara

5.  Evolutia naturala biologica**(Vezi cursul I: Introducere - Slide
    6)**

<!-- -->

8.  **Algoritmul Hillclimbing**: 1. Se aplica asupra unui singur punct
    din spatiul de cautare; 2. Aplicarea se poate repeta pentru mai
    multe puncte pentru a creste performantele; 3. Este inspirat din
    tehnicilie de alpinism; 4. Gaseste intotdeauna solutia optima; 5.
    Gaseste uneori solutia optima; 6. Calculele se incheie atunci cand
    temperatura sistemului devine 0; 7. De obicei gaseste un punct de
    optim local; 8. Se utilizeaza numai pentru reprezentarea cu siruri
    de numere reale;

<!-- -->

1.  1,2,5,7

2.  1,5,7,8

3.  1,2,4,7

4.  1,4,6,7

5.  3,4,6,8

<!-- -->

9.  **Caracteristicile unui algoritm genetic clasic(canonic) sunt**: 1.
    Reprezentarea populatiei este realizata prin intermediul sirurilor
    binare; 2. Reprezentarea populatiei este realizata prin intermediul
    sirurilor de numere naturale; 3. Probabilitatea de selectie a unui
    individ in multisetul parintilor este proportionala cu valoarea
    functiei de evaluare pentu el; 4. Probabilitatea de selectie a unui
    individ in multisetul parintilor este data de pozitia individului in
    erarhia populatiei, determinata pe baza functiei de evaluare; 5.
    Probabilitatea efectuarii unei mutatii este mica; 6. Probabilitatea
    efectuarii unei mutatii este mare; 7. Probabilitatea efectuarii
    recombinarii este mica; 8. Probabilitatea efectuarii recombinarii
    este mare; 9. Inlocuirea populatiei curente se face pe baza de
    varsta.

<!-- -->

1.  Nu exista algoritm genetic canonic

2.  2,4,6,7

3.  1,3,5,8(Speram, doamne ajuta)

4.  Nici una din variantele A,B,C,E

5.  2,3,6,7,9

<!-- -->

10. **Care din urmatorii operatori pot fi utilizati intr-un algoritm
    genetic care foloseste reprezentarea prin siruri de numere reale**:

> 1\. Negarea; 2. Negarea Fuzzy; 3. Resetarea aleatoare; 4. Fluaj; [5.
> Mutatia uniforma]{.mark}; [6. Mutatia neuniforma cu distributie
> fixata]{.mark}; 7. Mutatia locala; 8. Interschimbarea; 9. Inserarea;
> 10. Mutatia Rapida; 11. Amestecu; 12. Mutatia globala; 13.
> Inversiunea; [14. Unipunct]{.mark}; [15; Multipunct]{.mark}; [16.
> Uniforma]{.mark}; 17. Recombinarea radacinilor; [18; Aritmetica
> simpla]{.mark}; [19. Aritmetica singulara]{.mark}; [20 Aritmetica
> totala;]{.mark} 21. Recombinarea sirurilor maxima; 22. PMC; 23.
> Recombinare de ordine; 24. Recombinarea muchilor; 25. Recombinarea
> Ciclica

1.  Toti operatorii de mai sus

2.  2,7,10,12,17,21

3.  1,3,4,7,10,13,16,17,20

4.  3,4,5,6,7,12,18,19,21

5.  5,6,14,15,16,18,19,20

**Partea II:**

1.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de mutatie:**

<!-- -->

1.  Este utilizata doar in probleme cu constringeri

2.  Este realizata cu probabilitate mica

3.  Utilizeaza populatia curenta

4.  Utilizeaza populatia de copii

5.  Determina structura cromozomiala

6.  Este de tip neuniform

7.  Alege pentru mutatie in medie jumatate de indivizi

8.  Este efectuata o singura data pe parcursul unui algoritm

9.  Este efectuata iterativ

10. Este efectuata imediat ce este disponibila o populatie de copii

<!-- -->

2.  **In cadrul unui algoritm genetic operatia de recombinare:**

<!-- -->

1.  Este efectuata o singura data dupa prima etapa de selectie a
    parintilor

2.  Este utilizata cu probabilitate mica

3.  In general probabilitatea de recombinare nu conteaza in rezolvarea
    problemelor prin algoritmi genetici

4.  Este efectuata o singura data pe parcursul unui algoritm genetic

5.  Este efectuata imediat inaintea fiecare proceduri de mutatie

6.  Este efectuata imediat dupa fiecare etapa de selectie a parintilor

7.  Este utilziata cu probabilitate mare

8.  Este efectuata iterativ

9.  Este utilizata doar in probleme fara constrangeri

10. Utilizeaza populatia de parinti

<!-- -->

3.  **In cadrul unui algoritm evolutiv populatia initiala**

<!-- -->

1.  Este generata la inceputul fiecarui ciclu evolutiv

2.  Este generata utilizand distributia pe probabilitate normala

3.  Este generata inaintea inceperii evolutiei propriu-zise

4.  Este generata dupa fiecare ciclu evolutiv

5.  Este generata utilizand distributia de probabilitate uniforma

6.  Este generata aleator (Vezi cursul I: Introducere - Slide 11)

7.  Este setata pe multimea vida

<!-- -->

4.  **Fie urmatorii doi cromozomi de tip permutare {6, 3, 11,7, 14, 8,
    5, 15, 1, 2, 4, 13, 9 ,10 ,12 } si {7, 1, 15,13,2,
    14,6,10,12,11,4,8,3,9, 5}. Aplicand operatorul de recombinare PMX,
    cu pozitile 4 si 8 se obtin descendentii.**

<!-- -->

1.  Siruri de numere

> x2 = {13,1,10,7,14,8,5,15,12,11,4,2,3,9,6}
>
> y2 = {5,3,11,13,2,14,6,10,1,8,4,7,9,15,12}

5.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de recombinare:**

<!-- -->

1.  Este de tip local sau global

2.  Este efectuata o singura data pe parcursul unui algoritm

3.  Alege pentru recombinare in medie jumatate de indivizi

4.  Este realizata cu probabilitate mica

5.  Determina structura cromozomiala

6.  Utilizeaza poplatia curenta

7.  Este efectuata o singura data, dupa prima etapa de generare a unei
    populatii

8.  Determina obtinerea unui multiset de copii in ...

9.  Este utilizata doar in probleme cu constrangeri

10. Este efectuata iterativ

<!-- -->

6.  **In cadrul unui algoritm din clasa strategiilor evolutive,
    reprezentarea cromozomilor**

<!-- -->

1.  Influenteaza tipul de recombinare folosit

2.  Se alege in functie de problema care se rezolva

3.  Poate fi numai de tip siruri de numere intregi sau reale

4.  Poate fi oricare dintre: siruri binare, siruri de numere intregi,
    siruri de numere reale, permutari

5.  Are influenta asupra mecanismului de  selectie a generatiei
    urmatoare

6.  Nu influenteaza tipul de mutatie folosit(discreta/ nediscreta)

7.  Poate fi numai de siruri de numere reale

8.  Contine atat descrierea individului candidat cat si parametrii care
    ..

<!-- -->

7.  **In cadrul unui algoritm genetic operatia de selectie a
    parintilor**

<!-- -->

1.  Intotdeauna este bazata pe o distributie de probabilitate de
    selectie

2.  Utilizeaza populatia curenta

3.  Este efectuata o singura data pe parcursul unui algoritm genetic

4.  Este utilizata doar in probleme cu constringeri

5.  Este efectuata imediat inaintea fiecarei proceduri de mutatie

6.  Este efectuata imediat ce este disponibila o populatie curenta
    evaluata

7.  Este efectuata o singura data dupa prima etapa de generare a unei
    populatii

8.  Alege in general indivizi pe baza factorului varsta

9.  Utilizeaza populatia de copii mutati

10. Utilizeaza populatia de copii

11. Este efectuata iterativ

12. Poate fi realizata prin utilizarea unei distributii de probabilitate
    de selectie

<!-- -->

8.  **Fie urmatorul cromozom de tip permutare {7, 6, 12, 14, 3, 10, 8,
    15, 11, 5, 4, 1, 13, 2, 9} In urma aplicarii operatorului de mutatie
    prin amestec s-a obitnut cromozomul {7, 14, 13, 12, 1, 15, 2, 8, 6,
    3, 11, 5, 10, 4, 9 }. Cele doua pozitii utilizate pentru amestesc
    sunt:**

<!-- -->

1.  3 si 13

2.  1 si 15

3.  1 si 14

4.  4 si 8

5.  1 si 12

6.  4 si 15

7.  3 si 15

8.  2 si 13

9.  2 si 14

10. 2 si 15

11. 1 si 13

<!-- -->

9.  **In cadrul unui algoritm genetic operatia de mutatie**

<!-- -->

1.  Are probabilitate mica

2.  Se aplica doar daca divesitatea genetica scade sub un prag x dat

3.  Intotdeauna produce indivizi fezabili

4.  Se aplica asupra descendentilor produsi de operatia de recombinare

5.  Se aplica asupra mutlisetului de parinti

6.  Se aplica asupra populatiei curente

7.  Se utilizeaza doar in probleme cu constrangeri

8.  Poate sa produca indivizi nefezabili

9.  Se efectueaza o singura data, dupa generarea populatiei initiale

10. Se aplica imediat inaintea fiecarei etape de selectie a generatiei
    urmatoare

11. Se utilizeaza doar in problemele fara constrangeri

12. Nu foloseste factori aleatori.

<!-- -->

10. **In cadrul unui algoritm genetic operatia de selectie a
    supravietuitorilor**

<!-- -->

1.  Utilizeaza intotdeauna factori aleatori

2.  In unele variante necesita calcularea unei distributii de
    probabilitate de selectie

3.  Indivizii alesi sunt intotdeauna fezabili

4.  Duce la cresterea calitatii medii a populatiei curente

5.  Se aplica la inceputul fiecarei iteratii

6.  Uneori utilizeaza factori aleatori

7.  Se aplica asupra populatiei curente

8.  Garanteaza obtinerea unei generatii cu calitate medie superioara.
    Daca foloseste selectia bazata pe varsta.

9.  Asigura perpetuarea individului cu calitate maxima din populatia
    curenta

10. Alege generatia urmatoare dintre indivizii disponibili dupa operatia
    de mutatie

11. Se aplica asupra descendentilor obtinuti din populatia curenta

Grile PEAG:

1\. Pentru pastrarea relatiilor comune din cromozomii parinti se
foloseste operatorul de recombinare:

a\) PMX (Partially Mapped crossover)

b\) nu exista un operator pebntru acest scop

[c) ECX (Edge crossover)]{.mark}

d\) incrusisare de tip turneu

e\) incrucisare binara

2\. Care din urmatoarele este un dezavantaj al utilizatii distributiei
de probabilitate de selectie de tip FPS?

a\) Convergenta asimptomatica

b\) convergenta lenta

[c) convergenta prematura]{.mark}

d\) eliminarea indivizilor slabi

e\) selectarea celor mai buni indivizi

3\. Pentru problemele in care reprezentarea prin permutari semnifica
ordiea de aparitie a unor evenimente, operatorul de recombinare folosit
este:

a\) incrucisarea aritmetica singulara

b\) incrucisarea unipunct

c\) IPX

[d) OCX (Order crossover)]{.mark}

e\) incrucisare uniforma

4\. Mecanismul de selectie turnir:

a\) este intotdeauna de tip determinist

b\) acorda o sansa si celui mai slab inidvid

c\) nu exista un astfel de mecanism. Turniul este o competitie medievala

[d) nu respecta distributia de probabilitate de selectie]{.mark}

e\) este cel mai des folosit mecanism de selectie

5\. Pentru problemele cu dependenta de adiacente se foloseste operatorul
de recombinare:

a\) OCX

b\) niciunul din celelalte raspunsuri

c\) ECX

[d) PMX]{.mark}

e\) incrucisare aritmetica singulara

6\. Care din urmatoarele nu este un mecanism de selectie?

[a) Ruleta complicata]{.mark}

b\) genitor

c\) ruleta simpla

d\) ruleta multi-brat

e\) turnir

7\. Recombinarea multipla:

a\) nu se poate baza pe frecventa alelelor

b\) este o generealizare a operatiilor de recombinare pentru
reprezentarea cu permutari

c\) are echivalent bilogic

d\) este cea mai bun optiune pentru algoritmii genetici

[e) produce rezultate mai bune doar in unele cazuri particulare]{.mark}

8\. In cazul reprezentarii cu siruri de numere intregi, recombinarile
aritmetice:

[a) se pot aplica daca se face rotunjirea rezultatelor]{.mark}

b\) produc intotdeauna rezultate aberante

c\) nu exista notiunea de recombinare aritmetica

d\) sunt interzise

e\) se pot aplica numai daca toate perechile de alele de pe pozitii
identice sunt fie pare, fie impare

9\. Care din urmatoarele este un dezavantaj al utilizatii distributiei
de probabilitate de selectie tip FPS?

[a) Convergenta prematura]{.mark}

b\) convergenta asimptotica

c\) eliminarea indivizilor slabi

d\) selectarea celor mai buni indivizi

e\) convergenta lenta

10\. Schema generala de recombinare depinde de:

a\) numarul de indivizi din populatia initiala

b\) ooperatorul de recombinare folosit

[c) existenta constrangerilor in problema de rezolvat]{.mark}

d\) reprezentarea cromozomilor

e\) alegerea utilizatorului

11\. Recombinarea multipla:

a\) nu se poate baza pe frecventa alelelor

b\) este o generealizare a operatiilor de recombinare pentru
reprezentarea cu permutari

c\) are echivalent bilogic

d\) este cea mai buna optiune pentru algoritmii genetici

[e) produce rezultate mai bune doar in unele cazuri particulare]{.mark}

12\. In cadrul algoritmilor genetici, generatia urmatoare este selectata
dintre:

a\) parintii selectati

[b) indivizii generatiei curente si descndentii obtinuti dupa etape de
mutatie]{.mark}

c\) decendentii generatiei curente

d\) indivizii generatiei curente

e\) descendentii obtinuti din etapa de recombinare

13\. Care din urmatoarele este un model de populatie?

a\) cu dimensiune fixa

b\) cu dimensiune variabila

c\) cu generatii

d\) cu stari instabile

[e) cu stari stabile]{.mark}

14\. Care din urmatoarele nu este un model de distributie de
probabilitate folosit pentru etapa de selectie:

a\) FPS cu ferestre

b\) FPS

[c) FPS cu alfla scalare]{.mark}

d\) ranguri liniare

e\) FPS cu sigma scalare

15\. Care mecanism de selectie prroduce rezultate mai apropiate de
distributia de probabilitate de selectie calculata?

a\) toate produc rezultate la fel de apropiate

[b) SUS]{.mark}

c\) niciunul

d\) ruleta cu un brat

e\) turnirul

16\. Daca aplicarea unui operator de recombinare produce indivizi
aberanti atunci:

[a) se folosesc parintii ca descendenti]{.mark}

b\) se produce eroare la executie

c\) algoritmul produce totusi rezultate corecte, ca urmare a
autoreglarii prin selectie

d\) rezultatele sunt imprevizibile

e\) problema nu se poate rezolva prin algoritm genetic

17\. De cate ori trebuie rotit bratul ruletei multi-brat pentru a
executa intregul proces de selectie a parintilor, pentru o populatie cu
k indivizi?

a\) de 2\*k ori

b\) de k ori

[c) o data]{.mark}

d\) de k/2 ori

e\) nu este ruleta multi-brat

18\. Ce aritate are operatorul de recombinare in algorimtii genetici
(cati operazi utilizeaza)

a\) unar (un operand)

b\) depinde de problema dee rezolvat

c\) ternar (trei operanzi)

d\) nu exista operatori de recombinare in algoritmii genetici

[e) binar (doi operanzi)]{.mark}

19\. Pentru a pastra cat mai bine informatia referioare la pozitiile
absolute ale alelelor in cromozomi parinti se foloseste operatul:\
a) incrucisare multipunct

[b) CX]{.mark}

c\) ECX

d\) OCX

e\) PMX

20\. Care din urmatoarele afirmatii nu e adevarata petru modelul
generational?

a\) poate inlocui un singur cromozom din populatia curenta

[b) necesita urmarirea mai multor generatii consecutive]{.mark}

c\) nu tine cont de calitatea cromozomilor

d\) poate inlocui parial generatia curenta

e\) poate inlocui complet generatia curenta

**GRILE PE CARE LE SCRIU EU CA SA LE AM SA COPIEZ OK**

GRILE 1:

1\. Pentru pastrarea relatiilor comune din cromozomii parinti se
foloseste operatorul de recombinare:

a\) PMX (Partially Mapped crossover)

b\) nu exista un operator pebntru acest scop

[c) ECX (Edge crossover)]{.mark}

d\) incrusisare de tip turneu

e\) incrucisare binara

2\. Care din urmatoarele este un dezavantaj al utilizatii distributiei
de probabilitate de selectie de tip FPS?

a\) Convergenta asimptomatica

b\) convergenta lenta

[c) convergenta prematura]{.mark}

d\) eliminarea indivizilor slabi

e\) selectarea celor mai buni indivizi

3\. Pentru problemele in care reprezentarea prin permutari semnifica
ordiea de aparitie a unor evenimente, operatorul de recombinare folosit
este:

a\) incrucisarea aritmetica singulara

b\) incrucisarea unipunct

c\) IPX

[d) OCX (Order crossover)]{.mark}

e\) incrucisare uniforma

4\. Mecanismul de selectie turnir:

a\) este intotdeauna de tip determinist

b\) acorda o sansa si celui mai slab inidvid

c\) nu exista un astfel de mecanism. Turniul este o competitie medievala

[d) nu respecta distributia de probabilitate de selectie]{.mark}

e\) este cel mai des folosit mecanism de selectie

5\. Pentru problemele cu dependenta de adiacente se foloseste operatorul
de recombinare:

a\) OCX

b\) niciunul din celelalte raspunsuri

c\) ECX

[d) PMX]{.mark}

e\) incrucisare aritmetica singulara

6\. Care din urmatoarele nu este un mecanism de selectie?

[a) Ruleta complicata]{.mark}

b\) genitor

c\) ruleta simpla

d\) ruleta multi-brat

e\) turnir

7\. Recombinarea multipla:

a\) nu se poate baza pe frecventa alelelor

b\) este o generealizare a operatiilor de recombinare pentru
reprezentarea cu permutari

c\) are echivalent bilogic

d\) este cea mai bun optiune pentru algoritmii genetici

[e) produce rezultate mai bune doar in unele cazuri particulare]{.mark}

8\. In cazul reprezentarii cu siruri de numere intregi, recombinarile
aritmetice:

[a) se pot aplica daca se face rotunjirea rezultatelor]{.mark}

b\) produc intotdeauna rezultate aberante

c\) nu exista notiunea de recombinare aritmetica

d\) sunt interzise

e\) se pot aplica numai daca toate perechile de alele de pe pozitii
identice sunt fie pare, fie impare

9\. Care din urmatoarele este un dezavantaj al utilizatii distributiei
de probabilitate de selectie tip FPS?

[a) Convergenta prematura]{.mark}

b\) convergenta asimptotica

c\) eliminarea indivizilor slabi

d\) selectarea celor mai buni indivizi

e\) convergenta lenta

10\. Schema generala de recombinare depinde de:

a\) numarul de indivizi din populatia initiala

b\) ooperatorul de recombinare folosit

[c) existenta constrangerilor in problema de rezolvat]{.mark}

d\) reprezentarea cromozomilor

e\) alegerea utilizatorului

11\. Recombinarea multipla:

a\) nu se poate baza pe frecventa alelelor

b\) este o generealizare a operatiilor de recombinare pentru
reprezentarea cu permutari

c\) are echivalent bilogic

d\) este cea mai buna optiune pentru algoritmii genetici

[e) produce rezultate mai bune doar in unele cazuri particulare]{.mark}

12\. In cadrul algoritmilor genetici, generatia urmatoare este selectata
dintre:

a\) parintii selectati

[b) indivizii generatiei curente si descndentii obtinuti dupa etape de
mutatie]{.mark}

c\) decendentii generatiei curente

d\) indivizii generatiei curente

e\) descendentii obtinuti din etapa de recombinare

13\. Care din urmatoarele este un model de populatie?

a\) cu dimensiune fixa

b\) cu dimensiune variabila

c\) cu generatii

d\) cu stari instabile

[e) cu stari stabile]{.mark}

14\. Care din urmatoarele nu este un model de distributie de
probabilitate folosit pentru etapa de selectie:

a\) FPS cu ferestre

b\) FPS

[c) FPS cu alfla scalare]{.mark}

d\) ranguri liniare

e\) FPS cu sigma scalare

15\. Care mecanism de selectie prroduce rezultate mai apropiate de
distributia de probabilitate de selectie calculata?

a\) toate produc rezultate la fel de apropiate

[b) SUS]{.mark}

c\) niciunul

d\) ruleta cu un brat

e\) turnirul

16\. Daca aplicarea unui operator de recombinare produce indivizi
aberanti atunci:

[a) se folosesc parintii ca descendenti]{.mark}

b\) se produce eroare la executie

c\) algoritmul produce totusi rezultate corecte, ca urmare a
autoreglarii prin selectie

d\) rezultatele sunt imprevizibile

e\) problema nu se poate rezolva prin algoritm genetic

17\. De cate ori trebuie rotit bratul ruletei multi-brat pentru a
executa intregul proces de selectie a parintilor, pentru o populatie cu
k indivizi?

a\) de 2\*k ori

b\) de k ori

[c) o data]{.mark}

d\) de k/2 ori

e\) nu este ruleta multi-brat

18\. Ce aritate are operatorul de recombinare in algorimtii genetici
(cati operazi utilizeaza)

a\) unar (un operand)

b\) depinde de problema dee rezolvat

c\) ternar (trei operanzi)

d\) nu exista operatori de recombinare in algoritmii genetici

[e) binar (doi operanzi)]{.mark}

19\. Pentru a pastra cat mai bine informatia referioare la pozitiile
absolute ale alelelor in cromozomi parinti se foloseste operatul:\
a) incrucisare multipunct

[b) CX]{.mark}

c\) ECX

d\) OCX

e\) PMX

20\. Care din urmatoarele afirmatii nu e adevarata petru modelul
generational?

a\) poate inlocui un singur cromozom din populatia curenta

[b) necesita urmarirea mai multor generatii consecutive]{.mark}

c\) nu tine cont de calitatea cromozomilor

d\) poate inlocui parial generatia curenta

e\) poate inlocui complet generatia curenta

GRILE 2:

49. Fie X = \[6 1 8 10 5 7 9 3 4 2\] si Y = \[9 8 7 3 6 1 5 10 4 2\]
    permutari. Care urmasi sunt generati prin utilizarea operatorului
    CX?

Raspuns corect:

C1=\[6 8 7 10 5 1 9 3 4 2\], C2=\[9 1 8 3 6 7 5 10 4 2\]

50. Intr-un algoritm evolutiv, functia de tip calitate:

<!-- -->

k.  Evalueaza calitatea algoritmului

l.  Evalueaza calitatea fiecarui candidat

m.  Evalueaza viteza de gasire a solutiei fata de consumul de resurse

n.  Trebuie maximizata

o.  Stabileste daca un descendent este acceptabil

p.  Selecteaza indivizii care se vor reproduce

q.  Selecteaza indivizii care trec in generatia urmatoare

r.  Contine un factor aleator

s.  Evalueaza calitatea populatiei curente

t.  Evalueaza calitatea populatiei curente fata de cea din generatia
    anterioara

> Raspuns corect:
>
> b, d

51. In cadrul unui algoritm genetic operatia de selectia a parintilor

- Este efectuata iterative

- Utilizeaza populatia curenta

- Este efectuata imediat ce este disponibila o populatie curenta
  evaluate

- Poate fi realizata prin utilizarea unei distributii de probabilitate
  de selectie

52. Componentele algortmilor evolutivi sunt:

<!-- -->

p.  Reprezentarea

q.  Probabilitatea de mutatie

r.  Functia de evaluare

s.  Probabilitatea de recombinare

t.  Populatia

u.  Generarea de numere aleatoare

v.  Mecanismul de selectie a parintilor

w.  Generarea de permutari

x.  Reprezentarea grafica a evolutiei calitatii

y.  Operatorii de variatie

z.  Stabilirea diversitatii genetice a populatiei

a.  Mecanismul de inlocuire a populatiei curente

b.  Hillclimbing

c.  Initializarea populatiei

d.  Conditia de terminare

> Raspuns corect:
>
> a, c, e, g, j, l, n, o

53. Calculul evolutiv este inspirat din:

\-\--evolutia naturala biologica

54. Fie urmatorii doi cromozomi de tip permutare {6, 3, 11 , 7, 14, 8,
    5, 15, 1, 2, 4, 13, 9, 10, 12} si {7, 1, 15, 13, 2, 14, 6, 10, 12,
    11, 4, 8, 3, 9, 5}. Aplicand operatorul de recombinare PMX, cu
    pozitiile 4 si 8 se obtin descendentii:

Raspuns corect:

h\. 13 1 10 7 14 8 5 15 12 11 4 2 3 9 6

i\. 5 3 11 13 2 14 6 10 1 8 4 7 9 15 12

55. In cadrul uni algoritm genetic operatia de selectie a
    supravietuitorilor

- Se aplica asupra populatiei curente

- Indivizii alesi sunt intotdeauna fezabili

- Uneori utilizeaza factori aleatori

- In unele variante necesita calcularea unei distributii de
  probabilitate de selectie

- Se aplica asupra descendentilor obtinuti din populatia curenta

56. Caracteristicile unui algoritm genetic clasic(canonic) sunt:

- Reprezentarea populatiei initiale este realizata prin intermediul
  sirurilor binare

- Probabilitatea de selectie a unui individ in multisetul parintilor
  este proportional cu valoarea functiei de evaluare pentru ei

- Probabilitatea efectuarii unei mutatii este mica

- Probabilitatea efectuarii recombinarii este mare

57. In cadrul unui algoritm evolutiv populatia initiala

- Este generata aleator

- Este generata inaintea inceperii evolutiei propriu-zise

58. In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de recombinare:

- Este efectuata iterative

- Determina obtinerea unui multiset de copii in ..

- Utilizeaza populatia curenta

- Este de tip local sau global

59. Care dintre urmatorii operatori pot fi utilizati intr-un algoritm
    genetic care foloseste reprezentarea prin siruri de numere reale:

- Mutatia uniforma

- Mutatia neuniforma cu distributie fixata

- Unipunct

- Multipunct

- Uniforma

- Aritmetica simpla

- Aritmetica singulara

- Aritmetica totala

60. In cadrul unui algoritm genetic operatia de recombinare:

- Utilizeaza populatia de parinti

- Este efectuata imediat dupa fiecare etapa de selectie a parintilor

- Este efectuata imediat inaintea fiecarei procedure de mutatie

- Este efectuata iterative

- Este utilizata cu probabilitate mare

61. In algoritmii genetici, reprezentarea prin siruri de numere intregi

- E preferabila atunci cand pentru fiecare gena sunt posibile mai mult
  de doua valori distincte

62. In cadrul unui algoritm din clasa strategiilor evolutive,
    reprezentarea cromozomilor

- Poate fi numai de siruri de numere reale

- Nu influenteaza tipul de mutatie folosit(discrete/nediscreta)

- Contine atat descrierea individului candidat cat si parametrii care...

63. In cadrul unui algoritm genetic operatia de selectie a
    supravietuitorilor

- In unele variante necesita calcularea unei distributii de
  probabilitate de selectie

- Alege generatia urmatoare dintre indivizii disponibili dupa operatia
  de mutatie

- Indivizii alesi sunt intotdeauna fezabili

- Uneori utilizeaza factori aleatori

- Se aplica asupra populatiei curente si asupra descendentilor obtinuti
  din populatia curenta

64. Tipurile de probleme care pot fi rezolvate pe baza calculului
    evolutiv sunt:

- Probleme de cautare in spatial solutiilor

- Probleme de modelare

- Probleme de simulare

- Deplasarea autonoma a autovehiculelor

65. In algoritmii genetici, reprezentarea prin permutari

- Necesita operatori de variatie special definite

66. Intr-un algoritm evolutiv, functia fitness:

- Evalueaza calitatea fiecarui candidat

67. Fie urmatorul cromozom de tip permutare {7, 6, 12, 14, 3, 10, 8, 15,
    11, 5, 4, 1, 13, 2, 9}. In urma aplicarii operatorului de mutatie
    prin amestec s-a obtinut cromozomul {7, 14, 13, 12, 1, 15, 2, 8, 6,
    3, 11, 5, 10, 4, 9}. Cele doua pozitii utilizate pentru amestec
    sunt:

- 2 si 14

- 1 si 14

- 2 si 15

- 1 si 15

68. In algoritmii genetici, reprezentarea binara

- A fost primul tip de reprezentare a cromozomilor in algoritmi genetici

69. In cadrul unui algoritm genetic operatia de mutatie:

- Se aplica asupra descendetilor produsi de operatia de recombinare

- Poate sa produca indivizi refezabili

- Are probabilitate mica

70. In algorimii genetici, reprezentarea prin permutari

- Are nevoie de operatori speciali definite

71. In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de mutatie

- Utilizeaza populatia de copii

- Este efectuata iterative

- Este de tip neuniform

72. Algoritmul Hillclimbing

- Se aplica asupra unui singur punct din spatiul de cautare

- Aplicarea se poate repeat pentru mai multe puncte pentru a creste
  performantele

- Gaseste uneori solutia optima

- De obicei geseste un punct de optim local

73. care nu este un mecanism de selectie: -\> ruleta complicata

74. Ruleta multi-brat trebuie rotita doar o data pentru a executa
    intregul proces de selectie al parintilor

75. Care mecanism de selectie reproduce rezultate cat mai apropiate de
    distributia de probabilitate? -\> SUS(\...)

76. Mecanismul de selectie turnir -\> nu respecta distributia de
    probabilitate de selectie

77. Care din urmatoarele nu sunt modele de populatie? -\> cu generatii,
    cu dimensiune fixa, cu dimensiune variata, cu stari instabile

78. Care sunt modele de populatie? -\> cu stari stabile

79. In cadrul algoritmilor genetici, urmatoarea generatie este selectata
    dintre:

> -\> indivizii generatiei curente si descendentii obtinuti dupa etapa
> de mutatie

80. Care din urmatoarele este un dezavantaj pt distributia de
    probabilitate FPS? -\> convergenta premature

81. De cate ori tre rotit bratul ruletei simple pentru a executa
    intregul proces de selectie al parintilor pt o populatie cu tz
    cromozomi-\> de tz ori

82. In cadrul algoritmilor genetici, generatia urmatoare este selectata
    dintre:

-\> indivizii generatiei curente si descendentii obtinuti dupa etapa de
mutatie

83. Care din urmatoarele nu este un model de distributie folosit pt
    etapa de selectie:

-\> FPS cu alfa scalare

84. Care dintre urmatoarele este falsa pt modelul generational?

-\> nu tine cont de calitatea cromozomilor

85. Daca aplicarea unui operator de recombinare produce indivizi
    aberanti, atunci:

-\> se folosesc parintii ca descendenti

SAU

-\> algoritmul produce totusi rezultate corecte, ca urmare a
autoreglarii prin selectie

86. Mecanismul de selectie turnir -\> este intotdeauna un tip
    determinist

87. Pt pastrarea relatiilor comune din cromozomii parinti se foloseste
    operatorul de recombinare

-\> EXC (Edge crossover)

88. Recombinarea multipla

-\> produce rezultate mai bune doar in unele cazuri particulare

89. Schema generala de recombinare depinde de: -\> operatorul de
    recombinare folosit

90. In cazul reprezentarii cu siruri de numere intregi, recombinarile
    aritmetice:

-\> se pot aplica numai daca toate perechile de alele de pe pozitii
identice sunt fie pare, fie impare

91. Pt a pastra cat mai bine informatia referitoare la pozitiile
    absolute ale alelelor in cromozomii parinti se foloseste operatorul:

-\> CX (Cycle crossover)

92. Pentru problemele in care reprezentarea prin permutari semnifica
    ordinea de aparitie a unor evenimente, operatorul de recombinare
    folosit este

-\> OCX (Order crossover)

93. In algoritmii genetici, reprezentarea prin permutari:

-\> Necesita operatori de variatie special definite

94. Intr-un algoritm evolutiv, functia fitness: -\> Evalueaza calitatea
    fiecarui individ

95. In cadrul strategiilor evolutive: -\> Mutatia este aplicata cu
    probabilitate

96. In cadrul unui algoritm genetic, operatia de selectie a
    supravietuitorilor:

> -\>In unele variante necesita calcularea unei distributii de selectie
>
> -\>Alege generatia urmatoare dintre indivizii disponibili dupa
> operatia de mutatie
>
> -\>Indivizii alesi sunt intotdeauna fezabili (ce plm inseamna
> fezabil?)
>
> -\> Uneori utilizeaza factori aleatori
>
> -\> Se aplica asupra populatiei curente si asupra descendentilor
> obtinuti din populatia curenta

**Partea I:**

2.  În algoritmii genetici, **rerezentarea prin șiruri de numere
    întregi**

<!-- -->

6.  Este preferabila pentru probleme de optimizare

7.  Este doar un exercitiu de implementare, nefiind necesara

8.  E preferabila atunci cand pentru fiecare gena sunt posibile mai mult
    de doua valori distincte

9.  nu este utilizata in algoritmi genetici

10. Nu poate fi utilizata in cazul atributelor ordinale

<!-- -->

3.  In algoritmii genetici, **reprezentarea prin permutări**

<!-- -->

6.  Nu permite utilizarea de operatori de mutatie

7.  Nu este utilizata

8.  Are nevoie de operatori special definiti **(Vezi cursul II: - Slide
    19)**

9.  Nu permite utilizarea de operatori de recombinare

10. Nu permite mai mult de doua gene cu aceeasi valoare intr-un cromozom

<!-- -->

4.  **Tipurile de probleme care pot fi rezolvate pe baza calculului
    evolutiv **sînt: 1. Problemele de optimizare; 2.Probleme de cautare
    in spatiul solutilor; 3. Prelucrarea datelor de dimensiune
    mare(big-data); 4. Probleme de modelare; 5.Probleme de validare a
    datelor; 6. Probleme de simulare; 7 Alocarea dinamica a datelor in
    memoria calculatorului; 8. Deplasarea autonoma a vechiculelor

<!-- -->

6.  2,4,6

7.  1,4,6**(Vezi cursul I: Introducere: - Slide 9 si 10)**

8.  2,4,6,8

9.  1,3,5,7

10. 2,3,4

<!-- -->

5.  **Intr-un algoritm evolutiv**, functia de tip calitate: 1. Evalueaza
    calitatea algoritmului, 2. Evalueaza calitatea fiecarui candidat; 3.
    Evalueaza viteza de gasire a solutiei fata de consumul de
    resurse; 4. Trebuie maximizata; 5. Stabileste daca un descendent
    este acceptabil; 6. Selecteaza indivizii care se vor reproduce; 7.
    Selecteaza indivizii care trec in generatia urmatoare; 8. Contine un
    factor aleator; 9. Evalueaza calitatea populatiei curente; 10.
    Evalueaza calitatea populatiei curente fata de cea din generatia
    anterioara;

<!-- -->

6.  6,7,8

7.  5

8.  2,4**(Vezi cursul I: Introducere - Slide 11)**

9.  1,3

10. 9,10

<!-- -->

6.  **In algoritmii genetici, reprezentarea binara**

<!-- -->

6.  Este cea mai utilizata varianta de reprezentare a genotipurilor

7.  Nu e utilizata pentru algoritmi genetici

8.  A fost primul tip de reprezentare a cromozomilor in algoritmi
    genetici**(Vezi cursul 2: Slide 14)**

9.  Duce mereu la rezultate optime

10. Nu depinde de problema rezolvata

<!-- -->

7.  **Componentele algoritmilor evolutivi sunt: **1. Reprezentarea; 2.
    Probabilitatea de mutatie; 3. Functia de evaluare; 4. Probabilitatea
    de recombinare; 5. Populatia; 6. Generarea de numere aleatoare; 7.
    Mecanismul de selectie a parintilor; 8. Generarea de permutari; 9.
    Reprezentarea grafica a evolutiei calitatii; 10; Operatorii de
    variatie; 11. Stabilirea diversitatii genetice a populatiei; 12.
    Mecanismul de inlocuire a populatiei curente; 13. Hillclimbing; 14;
    Initializarea populatiei; 15. Conditia de terminare;

<!-- -->

6.  1,2,5,6,7,14,15

7.  1,3,5,7,10,12,14,15

8.  2,4,6,8,11,13

9.  2,4,5,9,15

10. 1,3,5,6,10,13,14,15

<!-- -->

8.  **Calculul evolutiv este inspirat din**

<!-- -->

6.  Revolutia industriata

7.  Societatea cunoasterii

8.  Societatea informationala

9.  Noua revolutie agrara

10. Evolutia naturala biologica**(Vezi cursul I: Introducere - Slide
    6)**

<!-- -->

9.  **Algoritmul Hillclimbing**: 1. Se aplica asupra unui singur punct
    din spatiul de cautare; 2. Aplicarea se poate repeta pentru mai
    multe puncte pentru a creste performantele; 3. Este inspirat din
    tehnicilie de alpinism; 4. Gaseste intotdeauna solutia optima; 5.
    Gaseste uneori solutia optima; 6. Calculele se incheie atunci cand
    temperatura sistemului devine 0; 7. De obicei gaseste un punct de
    optim local; 8. Se utilizeaza numai pentru reprezentarea cu siruri
    de numere reale;

<!-- -->

6.  1,2,5,7

7.  1,5,7,8

8.  1,2,4,7

9.  1,4,6,7

10. 3,4,6,8

<!-- -->

10. **Caracteristicile unui algoritm genetic clasic(canonic) sunt**: 1.
    Reprezentarea populatiei este realizata prin intermediul sirurilor
    binare; 2. Reprezentarea populatiei este realizata prin intermediul
    sirurilor de numere naturale; 3. Probabilitatea de selectie a unui
    individ in multisetul parintilor este proportionala cu valoarea
    functiei de evaluare pentu el; 4. Probabilitatea de selectie a unui
    individ in multisetul parintilor este data de pozitia individului in
    erarhia populatiei, determinata pe baza functiei de evaluare; 5.
    Probabilitatea efectuarii unei mutatii este mica; 6. Probabilitatea
    efectuarii unei mutatii este mare; 7. Probabilitatea efectuarii
    recombinarii este mica; 8. Probabilitatea efectuarii recombinarii
    este mare; 9. Inlocuirea populatiei curente se face pe baza de
    varsta.

<!-- -->

6.  Nu exista algoritm genetic canonic

7.  2,4,6,7

8.  1,3,5,8(Speram, doamne ajuta)

9.  Nici una din variantele A,B,C,E

10. 2,3,6,7,9

<!-- -->

11. **Care din urmatorii operatori pot fi utilizati intr-un algoritm
    genetic care foloseste reprezentarea prin siruri de numere reale**:

> 1\. Negarea; 2. Negarea Fuzzy; 3. Resetarea aleatoare; 4. Fluaj; [5.
> Mutatia uniforma]{.mark}; [6. Mutatia neuniforma cu distributie
> fixata]{.mark}; 7. Mutatia locala; 8. Interschimbarea; 9. Inserarea;
> 10. Mutatia Rapida; 11. Amestecu; 12. Mutatia globala; 13.
> Inversiunea; [14. Unipunct]{.mark}; [15; Multipunct]{.mark}; [16.
> Uniforma]{.mark}; 17. Recombinarea radacinilor; [18; Aritmetica
> simpla]{.mark}; [19. Aritmetica singulara]{.mark}; [20 Aritmetica
> totala;]{.mark} 21. Recombinarea sirurilor maxima; 22. PMC; 23.
> Recombinare de ordine; 24. Recombinarea muchilor; 25. Recombinarea
> Ciclica

6.  Toti operatorii de mai sus

7.  2,7,10,12,17,21

8.  1,3,4,7,10,13,16,17,20

9.  3,4,5,6,7,12,18,19,21

10. 5,6,14,15,16,18,19,20

**Partea II:**

2.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de mutatie:**

<!-- -->

11. Este utilizata doar in probleme cu constringeri

12. Este realizata cu probabilitate mica

13. Utilizeaza populatia curenta

14. Utilizeaza populatia de copii

15. Determina structura cromozomiala

16. Este de tip neuniform

17. Alege pentru mutatie in medie jumatate de indivizi

18. Este efectuata o singura data pe parcursul unui algoritm

19. Este efectuata iterativ

20. Este efectuata imediat ce este disponibila o populatie de copii

<!-- -->

3.  **In cadrul unui algoritm genetic operatia de recombinare:**

<!-- -->

11. Este efectuata o singura data dupa prima etapa de selectie a
    parintilor

12. Este utilizata cu probabilitate mica

13. In general probabilitatea de recombinare nu conteaza in rezolvarea
    problemelor prin algoritmi genetici

14. Este efectuata o singura data pe parcursul unui algoritm genetic

15. Este efectuata imediat inaintea fiecare proceduri de mutatie

16. Este efectuata imediat dupa fiecare etapa de selectie a parintilor

17. Este utilziata cu probabilitate mare

18. Este efectuata iterativ

19. Este utilizata doar in probleme fara constrangeri

20. Utilizeaza populatia de parinti

<!-- -->

4.  **In cadrul unui algoritm evolutiv populatia initiala**

<!-- -->

8.  Este generata la inceputul fiecarui ciclu evolutiv

9.  Este generata utilizand distributia pe probabilitate normala

10. Este generata inaintea inceperii evolutiei propriu-zise

11. Este generata dupa fiecare ciclu evolutiv

12. Este generata utilizand distributia de probabilitate uniforma

13. Este generata aleator (Vezi cursul I: Introducere - Slide 11)

14. Este setata pe multimea vida

<!-- -->

5.  **Fie urmatorii doi cromozomi de tip permutare {6, 3, 11,7, 14, 8,
    5, 15, 1, 2, 4, 13, 9 ,10 ,12 } si {7, 1, 15,13,2,
    14,6,10,12,11,4,8,3,9, 5}. Aplicand operatorul de recombinare PMX,
    cu pozitile 4 si 8 se obtin descendentii.**

<!-- -->

2.  Siruri de numere

> x2 = {13,1,10,7,14,8,5,15,12,11,4,2,3,9,6}
>
> y2 = {5,3,11,13,2,14,6,10,1,8,4,7,9,15,12}

6.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de recombinare:**

<!-- -->

11. Este de tip local sau global

12. Este efectuata o singura data pe parcursul unui algoritm

13. Alege pentru recombinare in medie jumatate de indivizi

14. Este realizata cu probabilitate mica

15. Determina structura cromozomiala

16. Utilizeaza poplatia curenta

17. Este efectuata o singura data, dupa prima etapa de generare a unei
    populatii

18. Determina obtinerea unui multiset de copii in ...

19. Este utilizata doar in probleme cu constrangeri

20. Este efectuata iterativ

<!-- -->

7.  **In cadrul unui algoritm din clasa strategiilor evolutive,
    reprezentarea cromozomilor**

<!-- -->

9.  Influenteaza tipul de recombinare folosit

10. Se alege in functie de problema care se rezolva

11. Poate fi numai de tip siruri de numere intregi sau reale

12. Poate fi oricare dintre: siruri binare, siruri de numere intregi,
    siruri de numere reale, permutari

13. Are influenta asupra mecanismului de  selectie a generatiei
    urmatoare

14. Nu influenteaza tipul de mutatie folosit(discreta/ nediscreta)

15. Poate fi numai de siruri de numere reale

16. Contine atat descrierea individului candidat cat si parametrii care
    ..

<!-- -->

8.  **In cadrul unui algoritm genetic operatia de selectie a
    parintilor**

<!-- -->

13. Intotdeauna este bazata pe o distributie de probabilitate de
    selectie

14. Utilizeaza populatia curenta

15. Este efectuata o singura data pe parcursul unui algoritm genetic

16. Este utilizata doar in probleme cu constringeri

17. Este efectuata imediat inaintea fiecarei proceduri de mutatie

18. Este efectuata imediat ce este disponibila o populatie curenta
    evaluata

19. Este efectuata o singura data dupa prima etapa de generare a unei
    populatii

20. Alege in general indivizi pe baza factorului varsta

21. Utilizeaza populatia de copii mutati

22. Utilizeaza populatia de copii

23. Este efectuata iterativ

24. Poate fi realizata prin utilizarea unei distributii de probabilitate
    de selectie

<!-- -->

9.  **Fie urmatorul cromozom de tip permutare {7, 6, 12, 14, 3, 10, 8,
    15, 11, 5, 4, 1, 13, 2, 9} In urma aplicarii operatorului de mutatie
    prin amestec s-a obitnut cromozomul {7, 14, 13, 12, 1, 15, 2, 8, 6,
    3, 11, 5, 10, 4, 9 }. Cele doua pozitii utilizate pentru amestesc
    sunt:**

<!-- -->

12. 3 si 13

13. 1 si 15

14. 1 si 14

15. 4 si 8

16. 1 si 12

17. 4 si 15

18. 3 si 15

19. 2 si 13

20. 2 si 14

21. 2 si 15

22. 1 si 13

<!-- -->

10. **In cadrul unui algoritm genetic operatia de mutatie**

<!-- -->

13. Are probabilitate mica

14. Se aplica doar daca divesitatea genetica scade sub un prag x dat

15. Intotdeauna produce indivizi fezabili

16. Se aplica asupra descendentilor produsi de operatia de recombinare

17. Se aplica asupra mutlisetului de parinti

18. Se aplica asupra populatiei curente

19. Se utilizeaza doar in probleme cu constrangeri

20. Poate sa produca indivizi nefezabili

21. Se efectueaza o singura data, dupa generarea populatiei initiale

22. Se aplica imediat inaintea fiecarei etape de selectie a generatiei
    urmatoare

23. Se utilizeaza doar in problemele fara constrangeri

24. Nu foloseste factori aleatori.

<!-- -->

11. **In cadrul unui algoritm genetic operatia de selectie a
    supravietuitorilor**

<!-- -->

12. Utilizeaza intotdeauna factori aleatori

13. In unele variante necesita calcularea unei distributii de
    probabilitate de selectie

14. Indivizii alesi sunt intotdeauna fezabili

15. Duce la cresterea calitatii medii a populatiei curente

16. Se aplica la inceputul fiecarei iteratii

17. Uneori utilizeaza factori aleatori

18. Se aplica asupra populatiei curente

19. Garanteaza obtinerea unei generatii cu calitate medie superioara.
    Daca foloseste selectia bazata pe varsta.

20. Asigura perpetuarea individului cu calitate maxima din populatia
    curenta

21. Alege generatia urmatoare dintre indivizii disponibili dupa operatia
    de mutatie

22. Se aplica asupra descendentilor obtinuti din populatia curenta

1\. Reprezentarea prin siruri de numere :

\- E preferabila atunci cand pentru fiecare gena sunt posibile mai mult
de doua valori distincte

2\. Reprezentarea prin permutari

\- Are nevoie de operatori special definiti

3\. Tipurile de problem care pot fi rezolvate pe baza calculului
evolutiv sunt:

\- Probleme de optimizare

\- Probleme de modelare sau identificare a sistemului

\- Probleme de simulare

4\. Intr-un algoritm evolutiv, functia de tip calitate/fitness/obiectiv:

\- Evalueaza calitatea fiecarui candidat

\- Este de maxim sau de minim ( de cele mai multe ori de maxim) /
trebuie maximizata

5\. Reprezentarea binara:

\- A fost primul tip de reprezentare a cromozomilor in algoritmi
genetici

\- Necesita operatori de variatie special definiti

\- Este eficienta in probleme in care solutia este un vector cu
componente logice

\- Determina ce tip de operatori de variatie trebuie folositi

6\. Componentele algoritmilor genetici sunt:

\- Reprezentarea

\- Functia de evaluare

\- Populatia

\- Mecanismul de selectie al parintilor

\- Operatorii de variatie

\- Mecanismul de inlocuire a populatiei curente

\- Initializarea populatiei

\- Conditia de terminare

7\. Calculul evolutiv este inspirat din:

\- Evolutia natural biologica

8\. Algoritmul Hillclimbing:

\- Se aplica unui singur punct din spatiul de cautare

\- Aplicarea se poate repeat pentru mai multe puncta pentru a creste
performantele

\- Gaseste uneori solutia optima

\- De obicei gaseste un punct de optim local

9\. Caracteristicile unui algoritm genetic classic (canonic) sunt:

\- Reprezentarea populatiei este realizata prin intermediul sirurilor
binare

\- Probabilitatea de selectie a unui individ in multisetul parintilor
este proportioanala cu valoarea functiei de evaluare pentru el

\- Probabilitatea efectuarii unei mutatii este mica

\- Probabilitatea efectuarii recombinarii este mare

10\. Operatorii care pot fi utilizati intr-un algoritm genetic care
foloseste reprezentarea prin siruri de numere reale:

\- Mutatia uniforma

\- Mutatia neuniforma cu distributie fixate

\- Unipunct

\- Multipunct

\- Uniforma

\- Aritmetica simpla

\- Aritmetica singular

\- Aritmetica totala

11\. In cadrul unui algoritm din clasa strategiilor evolutive, operatia
de mutatie:

\- Utilizeaza populatia curenta

\- Este de tip neuniform

\- Este efectuata iterative

12\. In cadrul unui algoritm genetic operatia de recombinare:

\- Este efectuata imediat inaintea fiecarei proceduri de mutatie

\- Este efectuata imediat dupa fiecare etapa de selectie a parintilor

\- Este utilizata cu probabilitate mare

\- Este efectuata iterativ

\- Utilizeaza populatia de parinti

13\. In cadrul unui algoritm evolutiv populatia initiala:

\- Este generate inaintea inceperii evolutiei propriu-zise

\- Este generata aleator

\- Este generata utilizand distributia de probabilitate uniforma

14\. Fie urmatorii cromozomi de tip permutare:
\[6,3,11,7,14,8,5,15,1,2,4,13,9,10,12\] si
\[7,1,15,13,2,14,6,10,12,11,4,8,3,9,5\]. Aplicand operatorul de
recombinare PMX, cu pozitiile 4 si 8 se obtin descendentii:

\- Sirurile de numere: x2=\[13,1,10,7,14,8,5,15,12,11,4,2,3,9,6\],
y2=\[5,3,11,13,2,14,6,10,1,8,4,7,9,15,12\]

15\. In cadrul unui algoritm din clasa strategiilor evolutive, operatia
de recombinare:

\- Este de tip local sau global

\- Utilizeaza populatia curenta

\- Determina obtinerea unui multiset de copii in ...

\- Este efectuata iterative

16\. In cadrul unui algoritm din clasa strategiilor evolutive,
reprezentarea cromozomilor

\- Nu influenteaza tipul de mutatie folosit (discrete/nediscreta)

\- Poate fi numai de siruri numere reale

\- Contine atat descrierea individului candidat cat si parametrii
care...

17\. In cadrul unui algoritm genetic operatia de selectie a parintilor:

\- Este efectuata imediat ce este disponibila

\- Utilizeaza populatia curenta

\- Este efectuata iterative

\- Poate fi realizata prin utilizarea unei distributii de probabilitate
de selectie

18\. Fie urmatorul cromozom de tip permutare
\[7,6,12,14,3,10,8,15,11,5,4,1,13,2,9\]. In urma aplicarii operatorului
de mutatie prin amestec s-a obtinut cromozomul
\[7,14,13,12,1,15,2,8,6,3,11,5,10,4,9\]. Cele doua pozitii utilizate
pentru amestec sunt:

\- 2 si 14 DAR AR PUTEA FI SI: 1 si 15; 1 si 14; 2 si 15 ( sa se fi
amestecat si poz 1 si 15 sa fi ramas la fel)

19\. In cadrul unui algoritm genetic operatia de mutatie:

\- Are probabilitate mica

\- Se aplica asupra descendentilor produsi din operatia de recombinare/
este efectuata imediat ce este disponibila o populatie de copii

\- Poate sa produca indivizi nefezabili

\- Este efectuata iterativ

\- Se aplica imediat inaintea fiecarei etape de selectie a generatiei
urmatoare

20\. In cadrul unui algoritm genetic operatia de selectie a
supravietuitorilor

\- In unele variante necesita calcularea unei distributii de
probabilitate de selectie

\- Alege generatia urmatoare dintre indivizii disponibili dupa operatia
de mutatie

\- Indivizii alesi sunt intotdeauna fezabili

\- Uneori utilizeaza factori aleatori

\- Se aplica asupra populatiei curente

\- Se aplica asupra descendentilor obtinuti din populatia curenta \<- nu
stiu daca e bine

\- Poate fi determinista sau cu factori aleatori

21\. Fie X=\[6 1 8 10 5 7 9 3 4 2 \] si Y=\[9 8 7 3 6 1 5 10 4 2 \]
permutari. Care urmasi sunt generate prin utilizarea operatorului CX?

\- C1=\[6 8 7 10 5 1 9 3 4 2\] si C2=\[9 1 8 3 6 7 5 10 4 2\]

22\. In cadrul unui algoritm genetic ce maximizeaza o functie (fitness):

\- Selectia parintilor este efectuata iterative

\- Mutatia este realizata cu probabilitate mica

\- Selectia supravietuitorilor este determinate de calitate si/sau
factorul varsta

\- Este intentionata determinarea unui punct de maxim global

23\. In cadrul unui algoritm genetic, reprezentarea cromozomilor:

\- Poate fi oricare dintre: siruri binare, siruri de numere intregi,
siruri de numere reale, permutari

\- Se alege in functie de problema care se rezolva

\- Influenteaza tipul de recombinare folosit

24\. Componente ale algoritmilor evolutivi sunt:

\- Reprezentarea

\- Functia de evaluare

\- Populatia

\- Mecanismul de selectie al parintilor

\- Operatorii de variatie

\- Mecanismul de inlocuirea apopulatiei curente

\- Initializarea populatiei

\- Conditia de terminare

25\. Calculul evolutiv este:

\- Tehnica de rezolvare a problemelor este de tip experiment-eroare

26\. Fie urmatorii 2 cromozomi de tip permutare
\[6,3,11,7,14,8,5,15,1,2,4,13,9,10,12\] si
\[7,1,15,13,2,14,6,10,12,11,4,8,3,9,5\]. Aplicand operatorul de
recombinare OCX, cu pozitiile 4 si 8 se obtin descendetii:

27\. In cadrul unui algoritm genetic conditia de oprire

\- Include in general controlul numarului de generatii simulate

\- Poate include controlul variabilitatii in cadrul populatiei nou
calculate

\- Nu depinde de reprezentarea cromozomiala

28\. Fie permutarile x=\[10 2 3 9 1 7 6 4 8 5\] si y=\[5 4 7 2 1 9 3 6 8
10\], un cromozom copil rezultat prin PMX este c=\[5 2 3 9 1 4 7 6 8
10\]. Atunci ordinea considerarii parintilor si respective punctele
crossover sunt:

\- X,y 2,5 - ei spun ca x,y 1,4

29\. In cadrul unui algoritm din clasa strategiilor evolutive,
autoadaptabilitatea se refera la:

\- Spatiul parametrilor

30\. De cate ori trebuie rotit bratul ruletei multi-brat pentru a
executa intregul process de selectie a parintilor, pentru o populatie de
k indivizi?

\- O data

31\. Care mecanism de selectie produce rezultate mai apropiate de
distributia de probabilitate de selectie cautata?

\- SUS (Stochastic Universal Sampling)

32\. Care din urmatoarele nu este mechanism de selectie?

\- Ruleta complicate

33\. Mecanismul de selectie turnir:

\- Nu respecta distributia de probabilitate de selectie

34\. Care din urmatoarele afirmatii nu este adevarata pentru modelul
generational?

\- Nu tine cont de calitatea cromozomilor

35\. Care din urmatoarele este un model de populatie?

\- Cu stari stabile

36\. In cazul algoritmilor genetici, generatia urmatoare este selectata
dintre:

\- Indivizii generatiei curente si descendentii obtinuti dupa etapa de
mutatie

37\. Care dintre urmatoarele este un dezavantaj al utilizarii
distributiei de probabilitate de selectie tip FPS?

\- Convergenta premature

38\. De cate ori trebuie rotit bratul ruletei simple pentru a executa
intregul process de selectie a parintilor, pentru o populatie cu tz
cromozomi?

\- De tz ori

39\. Care dintre urmatoarele nu este un model de distributie de
probabilitate folosit pentru etapa de selectie?

\- FPS cu alfa scalare

40\. Daca aplicarea unui operator de recombinare produce indivizi
aberanti atunci:

\- Se folosesc parintii descendenti

41\. Pentru pastrarea relatiilor commune din cromozomii parinti se
foloseste operatorul de recombinare:

\- ECX (Edge Crossover)

42\. Ce aritate are operatorul de recombinare in algoritmi genetici
(cati operanzi utilizeaza)?

\- Binar (doi operanzi)

43\. Recombinarea multipla:

\- Produce rezultate mai bune doar in unele cazuri particulare

44\. Schema generala de recombinare depinde de:

\- Operatorul de recombinare folosit

45\. In cazul reprezentarii cu siruri de numere intregi, recombinarile
aritmetice:

\- Ele se pot aplica numai daca toate perechile de allele de pe pozitii
identice sunt fie pare, fie impare

46\. Pentru a pastra cat mai bine informatia referitoare la pozitiile
absolute ale alelelor in cromozomii parinti se foloseste operatorul:

\- CX (Cycle crossover)

47\. Pentru problemele in care reprezentarea prin permutari semnifica
ordinea de aparitie a unor evenimente, operatorul de recombinare folosit
este:

\- OCX(Order Crossover)

**REPREZENTAREA BINARA:**

🡺Pentru problem cu variabile de decizie booleana

Ex: rucsac 0-1; drum cu bifurcatii-alegem stanga sau dreapta

**REPREZENTARE SIRURI NUMERE INTREGI:**

🡺Pentru problem cu mai mult de 2 valori posibile pentru o gena

**REPREZENTARE PRIN PERMUTARI:**

🡺Pentru problem unde ordinea evenimentelor e importanta

Ex: planificare activitati, cele n regine, comis voiajor

**MUTATII**

**Pt. reprezentare BINARA:** NEGARE

**Pt. reprezentare nr. INTREGI:** RESETARE ALEATOARE, FLUAJ

**Pt. reprezentare nr. REALE:** UNIFORMA, NEUNIFORMA

**Pt. reprezentare PERMUTARI:** INTRESCHIMBARE, INSERARE, AMESTEC,
INVERSIUNE -\> se aplica la nivel de cromozom nu de gena

NEGARE

Asupra genelor 2,3,8,12

1 1 0 1 0 0 0 1 1 1 0 1 0 1 1 0 -\> 1 0 1 0 0 0 0 1 1 0 0 0 1 1 0

RESETARE ALEATOARE

Pt siruri f mici

Modifica alela cu o valoare aleatoare: distributie uniforma

\*In general pt atribute de tip cardinal

-8 4 6 -5 2 10 7 -3 -\> -8 1 6 -5 2 10 7 -3

FLUAJ

Modifica alela cu o valoare mica(+-1 de obicei): distributie medie 0

\*In general pt atribute de tip ordinal

Codificarea trebuie stabilita

-odata cu alegerea reprezentarii

In algoritmii genetici reprezentarea binara:

-niciuna din celelalte variante

In algoritmii genetici reprezentarea prin permutari:

-este utilizata in probleme in care trebuie determinata ordinea
aparitiei unei secvente de evenimente

Daca aplicarea unui operator de recombinare produce indivizi aberanti
atunci:

-se folosesc parinti ca descendenti

Intr-un algoritm genetic populatia initiala:

-trebuie sa contina o diversitate genetica mare

b\.

In cadrul unui algoritm genetic operatia de selectie a parintilor:

-este efectuata imediat ce este disponibila o populatie curenta evaluata

-poate fi realizata prin utilizarea unei distributii de probabilitate de
selectie

-utilizeaza populatia curenta

d\. 3,6,8

Scopul unui algoritm memetic este:

-de a imbunatati informatia de la o populatie la alta

-de a imbunatati informatia din populatia curenta prin utilizarea de
algoritmi de cautare locala

2,4

(nicu cu iarba a zis ca e e.)

1.  In algoritmii genetici , alegerea unei anumite reprezentari

> -depinde de problema de rezolvat
>
> -influenteaza calitatea solutiei furnizate
>
> 2.In cadrul unui algoritm evolutiv conditia de terminare
>
> Este obligatorie
>
> Include obligatoriu direct sau indirect controlul numarului de
> iteratii.
>
> 3.in cadrul strategiei evolutive cu 2 membri (Es-2m)
>
> -la fiecare moment al evolutiei algoritmului este mentinut un singur
> candidat la solutie
>
> -calculul unui termen nou este realizat prin mutatie guassiana pentru
> fiecare component a vectorului current
>
> -sunt rezolvate problem de spatii continue
>
> -fiecare termen este calculate in maniera stohastica
>
> 4.in algoritmii genetici, reprezentarea prin siruri de numere intregi
>
> Este preferabila atunci cand pentru fiecare gena sunt posibile mai
> mult de doua valori distincte
>
> 5.in algoritmii genetici, opratia de selectie a parintilor
>
> Este utilizata in general in maniera nederminista
>
> 6.intr un algoritm evolutiv , functia de evaluare:
>
> Esetimeaza nivlul de afaptare a individului
>
> 7\. Fie X\[6 1 8 10 5 7 12 43 9 3 4 2\]o secventa de numere intregi ,
> in urma aplicarii mutatiei fluaj poate fi obtinuta urmatoarea variant
> mutanta
>
> Y=\[6 1 8 10 5 7 12 43 9 4 3 2 \]
>
> Y=7 1 8 10 5 7 12 43 9 3 4 2
>
> Y= 6 1 8 10 5 7 12 43 9 3 4 2
>
> Y= 6 1 8 10 5 7 12 42 9 3 4 2
>
> a.2,4,5,6
>
> 8Algoritmii genetici
>
> Sunt tehnici de cautaare stochastica bazate pe populatii.
>
> 9 algorimul ES2M
>
> Este algoritmul auto adaptiv primar
>
> 10.In cadrul unui algorit genetic operatia de selectie a
> supravietuitorilor
>
> In unele vairante necesita calcularea unei distributii de
> probabilitate de selectie
>
> Allege generatia urmatoare dintre indivizii disponibli dupa operatiune
> de mutatie
>
> Indivizii alesi sunt intotdeauna fezabil
>
> Uneori utilizeaza factori aleatori
>
> Se aplica asupra populatiei curente si asupra descendentilor obtinuti
> din populatia curenta
>
> 10.1 in cadrul unui algoritm genetic operatia de selectie a
> parintilor:
>
> Este utilizata in special maniera nedeterminista
>
> 11\. tipurile de probleme care pot fi rezolvate pe baza de calcul
> evolutiv sunt
>
> Problem de optimizare
>
> Problem de modelare
>
> Problem de simulare
>
> 12\. fie X= 6 1 8 10 5 7 9 3 4 2 \] o permutare , in uurma apicarii
> mutatiei prin inversiune pentru pozitiile 2 7 poate fi obtinuta
> urmatoare variant mutant
>
> Y= 6 9 75 10 8 1 3 4 2
>
> b.2
>
> 13\. fie permutarea x= 10 2 3 9 1 7 6 4 8 5 si y 5 4 7 2 1 9 3 6 8 10
> un cromozom copul rezultat prin PMX este c = 5 2 3 9 1 4 7 6 8 10.
> Atunci ordinea considerarii parintilor si respective punctelor d
> eincrucisare sunt
>
> (y x) (2,5)
>
> 14\. care din urmatoarele metode pot fi folosite in cadrul
> algoritmilor memetici pentru a imbunatati informatia in interiorul
> unei populatii
>
> Hillclimbing
>
> Strategie evolutiva cu 2 membri
>
> Metode exacte
>
> Metode euristice
>
> Metoda gradientului
>
> 15Decodificarea trebuie realizata
>
> Obligatoriu dupa extragerea celui mai bun individ din populatia finala
>
> 16.in algoritmii genetici, reprezentarea prin permutari
>
> Necesita operatori de variatie special definiti
>
> 17.in cadrul unui algoritm evolutiv populatia initiala
>
> Este generate inaintea inceperii evolutiei propriu zise
>
> Este generate aleator
>
> Este generate utilizant distributia de probabilitate uniforma
>
> 18.fie x =6 1 8 10 5 7 9 3 4 2 o permutare in urma aplicarii mutatiei
> prin amestec pt pozitiile 2 7 poate fi obtinuta urmatoare variant
> mutant
>
> 6 7 8 10 5 1 9 3 4 2
>
> 6 7 10 8 5 9 1 3 4 2
>
> 6 9 7 5 10 8 1 3 4 2
>
> 19\. in cadrul unui algoritm genetic operatia de recombinare
>
> Este efectuala imediat dupa fiecare etapa de selectie a parintilor
>
> Este efectuata inaintea fiecare procedure de mutatie
>
> Utilizeaza populatia de parinti
>
> Este utilizata cu probabilitate mare
>
> e.2,4,6,8
>
> 20\. calcul evolutiv este inspirit din
>
> Evolutia naturala biologica
>
> 21\. fie urmatorul cromozom de tip permutare{7 6 12 14 3 10 8 15 11 5
> 4 1 12 2 9}in urma aplicarii operatorului de mutatie prin amestec s a
> obtinut cromozomul
>
> {7 14 13 12 1 15 2 8 6 3 11 5 10 4 9 } cele doua pozitii utilizate
> pentru amestec sunt
>
> 1 si 14
>
> 2 si 15
>
> 2 si 14
>
> 1 si 15
>
> d.1,5,7,9
>
> 22 care din urmatorii operatori pot fi utilizati intr un algoritm
> genetic care foloseste reprezentarea prin siruri de numere reale ?
>
> Mutatia uniforma
>
> Mutatia neuniforma cu distributie fixa
>
> Recombinarea unipunct
>
> Recumbinarea multipunct
>
> Recombinarea uniforma
>
> Recombinarea aritmetica simpla
>
> Recombinarea aritmetica singular
>
> Recombinarea aritmetica totala
>
> b.5,6,14,15,16,18,19,20
>
> 23\. fie x = 6 1 8 10 5 7 9 3 4 2 si y= 9 8 7 3 6 1 5 10 4 2
> permutari. Care urmasi sunt generate prin utilizarea operatorului CX
>
> C1= 6 8 7 10 5 1 9 3 4 2
>
> C2 = 9 8 1 3 6 7 5 10 4 2
>
> b\.
>
> 24\. In cadrul unui algoritm genetic din clasa strategiilor evolutive
> , reprezentarea cromozomilor
>
> Poate fi numai de tip sururi de numere reale
>
> Nu influenteaza tipul de recombinare folosit( discrete\\ intermadiara)
>
> Contine atat descrierea individlui cat si parametric care controleaza
> evolutia sa.
>
> 25in cadrul unui algoritm din clasa strategiilor evolutive, operatia
> de mutatie
>
> Este efectuala imediat ce este disponibila o populatie de copuu
>
> Este de tip neunifor (flluaj)
>
> Determina structura cromozomiala
>
> Eset efectuata iterative
>
> a.2,5,9,11
>
> 26 in cadrul unui algoritm geneti care maximizeaza o functie (
> fitness)
>
> Mutatia este reaizata cu probabilitate mica
>
> Selectia supravietuitorilor este deternata de calitate sis au de
> factorul varsta
>
> Se urmareste determinarea unui punct de maxim global
>
> c\. 3,6,8
>
> 27.fie urmatorii doi cromozomi de tip permutare 6 3 7 8 5 1 2 4 9 si 7
> 2 8 5 6 9 4 1 3 . aplicand operatoruld e recombinare pmx cu pozitiile
> 3 si 5 se obtin descendentii
>
> 5 2 7 8 5 1 4 9 3
>
> 7 3 8 5 6 9 2 4 1
>
> c\. d,h
>
> 27.1 27.fie urmatorii doi cromozomi de tip permutare 6 3 7 8 5 1 2 4 9
> si 7 2 8 5 6 9 4 1 3 . aplicand operatoruld e recombinare pmx cu
> pozitiile 3 si 6 se obtin descendentii
>
> \-\-\-\-\-\-\--7 2 8 5 6 1 3 4 9
>
> 6 2 7 8 5 1 4 9 3
>
> 7 3 8 5 6 9 2 4 1

b\. d,h

> 28 componentele algorimilor evolutivi sunt
>
> Reprezentarea
>
> Functia de evaluare
>
> Populatia
>
> Mecanismul de selectie a parintilor
>
> Operatorii de variatie
>
> Mecanismul de inlocuire a populatiei curente
>
> Initializarea populatiei
>
> Conditia de terminare
>
> b\. 1,3,5,7,10,12,14,15
>
> 29.algoritmul Hillclimbing
>
> Se aplica asupra unui singur punct din spatial de cautare
>
> Aplicarea se poate repeat pentru mai multe puncte pentru a creste
> perfomantele
>
> Gaseste uneori solutia optima
>
> De obicei gaseste un punct de optim local
>
> d\. 1,2,5,7
>
> 30 intr un algoritm genetic populatia initiala
>
> Este contruita o singura data
>
> Contine exclisiv indivizi fezabili
>
> Este generate utilizant distributia de probabilitate uniforma
>
> d\. 2,5,7

31\. conditia terminala

??

1\. In algoritmii genetici, operatie de selectie a parintilor:

[a) este utilizata in general in maniera nedeterminista]{.mark}

b\) nu este utilizata

c\) este utilizata determinista

d\) este utilizata in functie de reprezentarea cromozomiala

e\) este doar un exercitiu de implementare, nefiind necesara

2\. In cadrul unui algoritm din clasa strategiilor evolutive,
reprezentarea cromozilor: 1. Poate fi oricare dintre: siruri binare,
siruri de numere intregi, siruri de numere reale, permutari, 2. Poate fi
numai de tip siruri de numere intregi sau reale, 3. Poate fi numai de
tip siruri de numere reale, 4. Nu influenteaza tipul de recombinare
folosit (discreta / indiscreta), 5. Se alege in functie de proble care
se rezolva, 6. Influenteaza tipul de recombinare folosit,7. Are
influenta asupra mecanismului de selectie a generatiei urmatoare, 8.
Contine atat descrierea individului candidat cat si parametrii care
controleaza evolutia sa.

a\) 2,4,5,6

b\) 1,3,4,8

[c)3,4,8]{.mark}

d)2,4,5,8

e)1,7,8

3\. In cadrul strategiei evolutive cu 2 membri (ES-2M): 1. Este generata
o populatie initiala aleator, din distributia normala, 2. La fiecare
moment al evolutiei algoritmul este mentinut un singur candidate la
solutie,3.Populatiile sunt de dimensiuni mari, 4. Calculul unui termen
nou este realizat prin mutatie gaussiana pentru fiecare componenta a
vectorului curent, 5. Sunt rezolvate problemele de spatii continue, 6.
Fiecare termen este calculat in maniera stochastica, 7. Calcul unui
termen nou este realizat prin mutatie gaussiana pentru o componenta
selectata aleator din vectorul curent, 8. Este intentionata cresterea
calitatii medii a populatiei curente, 9.Este garantata obtinerea unui
optim global, 10. La inceputul feicarei iterarii este testat dimensiunea
populatiei curente, 11. Sunt creati descendetini obtinuti din populatia
curenta prin recombinarea locala.

a\) 1,10

b\) 4,8,11

c)2,4,6,9

[d)2,4,5,6]{.mark}

e\) 6,8,11

4\. Fie X=\[6 1 8 10 5 7 12 43 9 3 4 2\] o secventa de numere intregi.
In urma aplicarii mutatiei fluaj poate fi obtinuta urmatoarea varianta
mutata: 1. Y=\[16, 1 8 10 5 7 12 43 9 3 4 2\], 2.Y=\[6 1 8 10 5 7 12 43
9 4 3 2\]

3\. Y=\[6 1 8 10 15 7 12 43 9 3 4 2\], 4. Y=\[7 1 8 10 5 7 12 43 9 3 4
2\], 5.Y=\[6 1 8 10 5 7 12 43 9 3 4 2\],

6\. Y=\[6 1 8 10 5 7 12 42 9 3 4 2\]

a\) 2, 4, 6

[b) 2,4,5,6]{.mark}

c)4,5,6

d\) 1,2,3,4,5,6

e\) 2,3,4,5,6

5\. In algoritmii genetici, reprezentarea prin permutari:

a\) nu este utilizata

b\) nu permite utlizarea de operatori de recombinare

[c) necesita operatori de variatie sepecial definiti]{.mark}

d\) nu permite utilizarea de operatori de mutatie

e\) nu permite mai mult de doua gene cu aceeasi valoare intr un cromozom

6\. Intr-un algoritm evolutiv, functia de evaluare:

a\) este o functie asimptotica

b\) se alege in functie de dimensiunea populatiei

[c) estimeaza nivelul de adpatate a individului]{.mark}

d\) este stabila de Holland

e\) este definita pe spatiul unidimensional

7\. In algoritmii genetici, alegerea unui anumite reprezentari 1. Este
independenta de problema de rezolvat, 2. .. problema de rezolvat, 3
poate fi facuta aleator, 4. Este imposibila, fiind folosita
reprezentarea prin numere reale, 5. Influenteaza calitatea solutiei
furnizate

a\) 4

b\) 1,3

[c) 2, 5]{.mark}

d\) 2,3

e\) 3,5

8\. Decodificarea trebuie realizata:

[a) obligatoriu dupa extragerea celui mai bun individ din populatia
finala]{.mark}

b\) nu depinde de reprezentarea aleasa

c\) nu e necesara in algoritmii genetici

d\) niciuna din celelalte variante

e\) garanteaza obtinerea de rezultate optime

9\. In cadrul unui algoritm din clasa strategiilor evolutive, operatie
de mutatie: 1. Este utilizata doar in probleme cu constrangeri, 2. Este
efectuata imediat ce este disponibila o populatie de copii, 3. Alege
pentru mutatie in medie jumatate de indivizi, 4. Utilizeaaza doua
multiseturi distincte de copii, 5. Este de tip neuniform (fluaj), 6.
Este efectuata o singura data, dupa prima etapa de genereare a unei
populatii, 7. Este realizata cu probabilitate mica, 8. Este efectuata o
singura data pe parcursul unui algoritm, 9. Determina structura
cromozomiala, 10. Utilizeaza populatia curenta, 11. Este efectuata
iterativ

[a)2,5,9,11]{.mark}

b)2,5,9,10

c)1,5,6,8

d)1,4,5,7

e)1,5,9,10

10\. Algoritmul Hillclimbing: 1. Se aplica asupra unui singur punct din
spatiul de cautare, 2. Aplicarea se poate repeta pentru mai multe puncte
pentru a creste performantele, 3. Este inspirat din tehnicile de
alpinism, 4. Gaseste intodeauna solutia optima, 5. Gaseste uneori
solutia optima, 6. Calculele se incheie atunci cand temeratura
sistemului devine 0, 7. De obicei gaseste un punct de optim local, 8. Se
utilieaza numai pentru reprezentarea cu siruri de numere reale

a\) 1,2,4,7

b)1,4,6,7

[c)1,2,5,7]{.mark}

d)1,5,7,8

e)3,4,6,8

11\. Algoritmul ES2M:

a\) nu este un algoritm auto-adaptiv

b\) nu este un algoritm evolutiv

c\) niciuna din celelalte variante

d\) este un algoritm determinist

[e) este algoritmul auto-adaptiv primar]{.mark}

12\. Fie permutarile x=\[10 2 3 9 1 7 6 4 8 5\] si y=\[5 4 7 2 1 9 3 6 8
10\], un cromozom copil rezultat prin PMX este c=\[5 2 3 9 1 4 7 6 8
10\]. Atunci ordinea considerarii parintilor si respectiv punctele de
incucisare sunt:

[a) (x,y) si (2,5)]{.mark}

b\) (y,x) si (1,4)

c\) (y,x) si (1,5)

d\) (x,y) si (1,4)

e)(y,x) si (2,5)

13\. Intr-un algoritm evolutiv, functia de evaluare:

[a) estimeaza nivelul de adaptare a individului']{.mark}

b\) este o functie asimptotica

c\) se alege in functie de dimensiunea populatiei

d\) este stabilita de Holland

e\) este deinita de spatiul unidemensional

14\. In cadrul unui algoritm genetic operatie de selectie a
supravietuitorilor: 1. Se aplica asupra populatitei curente, 2. In unele
variante necesita calcularea unei distributii de probabilitate de
selectie, 3. Utilizeaza intotdeauna factori aleatori, 4. Alege generatia
urmatoare dintre indivizii disponibili dupa operatia de mutatie, 5.
Indivizii alesi sunt intotdeauna fezabili, 6. Uneori utiliezeaza factori
aleatori, 7. Asigura perpetuarea individului cu calitatea maxima din
populatia curenta, 8. Duce la cresterea calitatii medii a populatiei
curente, 9. Gareanteaza obtinerea unui generatii cu calitate medie
superioara, daca foloseste selectia bazata pe varsta, 10. Se aplica la
inceputul fiecarei iteratii, 11. Se aplica asupra descendentilor
obtinuti din populatia curenta,12. Se aplica asupra populatiei curente
si asupra descendentilor obtinuti din populatia curenta.

a\) 2,3,4,5,6,11

[b)2,4,5,6,12]{.mark}

c)4,8,11

d)1,7

e)6,8,11

15\. Componentele algoritmilor evolutivi sunt: 1. Rerprezentarea, 2.
Probabilitatea de mutatie, 3. Functia de evaluare, 4. Probabilitatea de
recombinare, 5. Populatia, 6. Generearea de numere aleatoare, 7.
Mecanismul de selectia a parintilor, 8. Generarea de permutari, 9.
Reprezentarea grafica a evolutiei calitatii, 10. Operatorii de variatie,
11. Stabilitea diversitatii genetice a populatiei, 12. Mecanismul de
inlocuire a populatiei curente, 13. Hillclimbing, 14. Initializarea
populatiei, 15. Conditia de terminare

a\) 1,3,5,6,10,13,14,15

b)2,4,5,9,15

[c) 1,3,5,7,10,12,14,15]{.mark}

d\) 1,2,5,6,7,14,15

e\) 2,4,6,8,11,13

16\. In algoritmii genetici, reprezentarea prin siruri de numere intregi

a\) nu este utilizata in algoritmii genetici

b\) este preferabila pentru problemele de optimizare

c\) este doar un exercitiu de implementare, nefiind necesara

[d) este preferabila atunci cand pentru fiecare gena sunt posibile mai
mult de doua valori distincte]{.mark}

e\) nu poate fi utilizata in cazul atributelor ordinale

17\. In cadrul unui algoritm evoltiv conditia de terminare: 1. Este
obligatorie, 2. Nu este indicata, 3. Include obligatoriu, direct sau
indirect, controlul numarului de iteratii (numarul populatiilor
generate), 4. Nu poate fi implementata, 5. Este doar in cadrul GA, nu si
in cadrul ES

a\) 5

b\) 2,3,4

c\) 2,4

d\) 1,5

[e)1,3]{.mark}

18\. Tipurile de probleme care pot fi rezolvate pe baza calcului
evolutiv sunt: 1. Problema de optimizare, 2. Problemele de geometrie, 3.
Prelucrarea datelor de dimensiune mare (big-data), 4. Problemele de
modelare, 5. Problemele de validare a datelor, 6. Problemele de
simulare, 7. Alocarea dinamica a datelor in memoria calculatorului, 8.
Deplasarea autonoma a vehiculelor

[a) 1,4,6]{.mark}

b\) 2,4,6,8

c\) 2,3,4

d\) 2,4,6

e\) 1,3,5,7

19\. In cadrul unui algoritm genetic care maximizeaza o functie
(fitness): 1. Selectia generatiei urmatoare este obliatoriu bazata pe
varsta, 2. Sunt rezolvate doar problemele de constrangeri, 3. Mutatia
este realizata cu probabilitate mica, 4. Nu este recomandata utilizare
selectiei FPS, 5. Multisetul copiilor este fara duplicate, 6. Selectia
suprevietuitorilor este determinata de calitatea si/sau factorul varsta,
7. Recombinarea este realizata rareori, 8. Se urmareste determinarea
unui punct de maxim global, 9. Structura cormozomiala difera daca
functia este translatat

a\) 1,3,4,7

b\) 1,3,5,9

c\) 5,6,7

d\) 4,6,8

[e)3,6,8]{.mark}

20\. Algoritmii genetici:

a\) utlizeaza la fiecare moment de timp o varianta de solutie... prin
perturbare normala

[b) sunt tehnici de cautare stochastica bazate pe populatii]{.mark}

c\) folosesc exclusiv selectii deterministe

d\) sunt metode deterministe de cautare in spatiul solutiilor

e\) rezolva exclusiv probleme definite pe spatii continue

21\. In cadrul unui algoritm evolutiv populatia initiala: 1 . este
generata inaintea inceperii evolutiei propriu-zise, 2. Este generata
dupa fiecare cilcu evolutiv (care presupune efectuarea operatiilor de
selectie, recombinare, mutatie, evaluare), 3. Este generata la inceputul
fiecarui ciclu evolutiv, 4. Este genereata aleator, 5. Este generata
utilizand distributia de probabilitate uniforma, 6. Este generata
utilizand distribtuia de probabilitate normala, 7. Este setata pe
multimea vida

a\) 2,5,7

b\) 5,7

[c) 1,4,5]{.mark}

d\) 1,2,4,5,6

e\) 1,2,4,7

22\. Fie X=\[6 1 8 10 5 7 9 3 4 2\] o permutare. In urma aplicarii
mutatiei prin inversiune pentru pozitiile (2,7) poate fi obtinuta
urmatoarea varianta mutala: 1. Y=\[2 6 7 8 10 5 1 9 3 4\], 2. Y=\[6 7 8
10 5 1 9 3 4 2\], 3. Y=\[7 6 8 10 5 1 9 3 4 2\], 4. Y=\[6 7 10 8 5 9 1 3
4 2\], 5. Y=\[6 9 7 5 10 8 1 3 4 2\], 6=\[6 2 8 10 5 1 9 3 4 7\]

a\) 5

[b) 2]{.mark}

c\) 1, 5

d\) 2, 5

e\) 1

23\. Care dintre urmatoarele metode pot fi folosite in cadrul
algoritmilot memetici pentru a imbunatati infromatia in interiorul unei
populatii: 1. Recursivitatea, 2. Hillclimbing, 3. Divide ei impera, 4.
Strategie evolutiva cu doi memebri, 5. Backtracking, 6. Metode exact, 7.
Metode euristice, 8. Validarea datelor, 9. Metoda gradientului, 10. ECX

a\) 2,4,6,8,10

b)1,3,5,7,8

c)2,3,5,6,9

[d)2,4,6,7,9]{.mark}

e)1,3,6,7,10

24\. 22. Fie X=\[6 1 8 10 5 7 9 3 4 2\] o permutare. In urma aplicarii
mutatiei prin amestec pentru pozitiile (2,7) poate fi obtinuta
urmatoarea varianta mutala: 1. Y=\[2 6 7 8 10 5 1 9 3 4\], 2. Y=\[6 7 8
10 5 1 9 3 4 2\], 3. Y=\[7 6 8 10 5 1 9 3 4 2\], 4. Y=\[6 7 10 8 5 9 1 3
4 2\], 5. Y=\[6 9 7 5 10 8 1 3 4 2\], 6=\[6 2 8 10 5 1 9 3 4 7\]

a\) 1, 2,5

b\) 3, 4, 5

c\) 1, 2, 3

[d) 2, 4, 5]{.mark}

e\) 2,5, 6

25\. In cadrul unui algoritm genetic operatia de recombinare:

2\. Este efectuata o singura data dupa prima etapa de selectie a
parintilor

9\. Este utilizata cu probabilitate mica

3\. In general probabilitatea de recombinare nu conteaza in rezolvarea
problemelor prin algoritmi genetici

1\. Este efectuata o singura data pe parcursul unui algoritm genetic

4\. Este efectuata imediat inaintea fiecare proceduri de mutatie

5\. Este efectuata imediat dupa fiecare etapa de selectie a parintilor

8\. Este utilziata cu probabilitate mare

10\. Este efectuata iterativ

7\. Este utilizata doar in probleme fara constrangeri

6\. Utilizeaza populatia de parinti

a\) 2, 5, 7, 8

b\) 1, 2, 7, 8

c)4,8,9,10

d\) 2,3,4,7

[e) 2,4,6,8]{.mark}

26\. Calculul evolutiv este inspirat din:

[Fa) evolutia naturala bilogica]{.mark}

b\) revolutia industriala

c\) noua relutie agrara

d\) societatea cunoasterii

e\) societatea informationala

27\. Fie urmatorul comozom de tip premuare: {7,6, 12, 14, 3, 10, 8, 15,
11, 5 , 4, 1 , 13, 2, 9}. In urma aplicarii operatorului de mutatie prin
amestec s-a obtinut cromozumul: {7, 14, 13, 12, 1, 15, 2, 8, 6, 3, 11,
5, 10, 4, 9}. Cele doua pozitii utilizate pentru ameste sunt 1. 1 si 14,
2. 4 si 15, 3. 3 si 15, 4. 4 si 8, 5. 2 si 15, 6. 1 si 12, 7. 2 si 14,
8. 2 si 13, 9. 1 si 15, 10. 1 si 13, 11. 3 si 13

a)6

b\) 2

c\) 6, 7, 9

[d) 1, 5, 7, 9]{.mark}

e\) 5, 10

28\. Care din urmatorii operatori pot fi utilizati intr-un algoritm
genetic care foloseste reprezentatrea prin siruri de numere reale?

1.Negarea, 2. Megarea fuzzy, 3. Resetarea pseudo-aleatore, 4. Resetarea
determinista, 5. Mutatia uniforma, 6. Mutatita neunfiroma cu mestributie
fixata, 7. Mutatia locala, 8. Interschimabrea, 9. Inserarea, 10. Mutatia
rapida, 11. Amestecul, 12. Mutatia globala, 13. Inversiunea, 14.
Recombinarea unipunct, 15. Recombinarea multipunct, 16. Recombinarea
unfiorma, 17. Recombinarea radacinilor, 18. Recombinarea artmetica
simpla, 19. Recombinarea aritmetica singulara, 20. Recombinarea
arimetica toatla, 21. Recombinarea sirurilor maxime, 22. Partially
mapped crossover, 23. Recombinarea de ordine, 24. Recombinarea
muchiilor, 25. Recombinare ciclica

a\) toti operatorii de mai sus

[b) 5,6,14,15,16,18,19,20]{.mark}

c)1,3,4,7,10,13,16,17,20

d)2,7,10,12,17,21

e)3,4,5,6,7,12,18,19,21

29\. Fie X=\[6 1 8 10 5 7 9 3 4 2\] si Y=\[9 8 7 3 6 1 5 10 4 2\]
permutari. Care urmasisunt generati prin utilizarea operatorului CX?

a\) C1=\[ 6 7 8 10 5 1 9 3 4 2\], C2=\[9 8 1 3 6 7 5 10 4 2\]

[b) C1=\[6 8 7 10 5 1 9 3 4 2\] , C2=\[9 1 8 3 6 7 5 10 4 2\]]{.mark}

30\. Fie urmatorii doi cromozomi de tip permutare: {6, 3, 7, 8, 5 , 1, 2
, 4, 9} si { 7, 2, 8, 5, 6,9, 4 , 1 ,3}. Aplicand operatorul de
recombinare PMX, cu pozitiile 3 si 6 se obtin descendentii:

a\. 6,3,7,8,5,9,4,1,2

b.7,4,6,8,5,1,2,9,3

c.8,3,7,8,5,9,4,2,1

d\. 6,2,7,8,5,1,4,9,3

e.7,2,8,5,6,1,3,4,9

f.6,2,7,8,5,9,4,1,3

g\. 7,9,8,6,5,1,2,4,3

h.7,3,8,5,6,9,2,4,1

i.7,3,8,5,6,1,2,4,9

j.5,3,7,8,6,9,4,1,2

a\) a, e

b\) b, c

[c) d,h]{.mark}

d\) g, j

e\) f,i

**Partea I:**

1.  În algoritmii genetici, **rerezentarea prin șiruri de numere
    întregi**

<!-- -->

1.  Este preferabila pentru probleme de optimizare

2.  Este doar un exercitiu de implementare, nefiind necesara

3.  E preferabila atunci cand pentru fiecare gena sunt posibile mai mult
    de doua valori distincte

4.  nu este utilizata in algoritmi genetici

5.  Nu poate fi utilizata in cazul atributelor ordinale

<!-- -->

2.  In algoritmii genetici, **reprezentarea prin permutări**

<!-- -->

1.  Nu permite utilizarea de operatori de mutatie

2.  Nu este utilizata

3.  Are nevoie de operatori special definiti **(Vezi cursul II: - Slide
    19)**

4.  Nu permite utilizarea de operatori de recombinare

5.  Nu permite mai mult de doua gene cu aceeasi valoare intr-un cromozom

<!-- -->

3.  **Tipurile de probleme care pot fi rezolvate pe baza calculului
    evolutiv **sînt: 1. Problemele de optimizare; 2.Probleme de cautare
    in spatiul solutilor; 3. Prelucrarea datelor de dimensiune
    mare(big-data); 4. Probleme de modelare; 5.Probleme de validare a
    datelor; 6. Probleme de simulare; 7 Alocarea dinamica a datelor in
    memoria calculatorului; 8. Deplasarea autonoma a vechiculelor

<!-- -->

1.  2,4,6

2.  1,4,6**(Vezi cursul I: Introducere: - Slide 9 si 10)**

3.  2,4,6,8

4.  1,3,5,7

5.  2,3,4

<!-- -->

4.  **Intr-un algoritm evolutiv**, functia de tip calitate: 1. Evalueaza
    calitatea algoritmului, 2. Evalueaza calitatea fiecarui candidat; 3.
    Evalueaza viteza de gasire a solutiei fata de consumul de
    resurse; 4. Trebuie maximizata; 5. Stabileste daca un descendent
    este acceptabil; 6. Selecteaza indivizii care se vor reproduce; 7.
    Selecteaza indivizii care trec in generatia urmatoare; 8. Contine un
    factor aleator; 9. Evalueaza calitatea populatiei curente; 10.
    Evalueaza calitatea populatiei curente fata de cea din generatia
    anterioara;

<!-- -->

1.  6,7,8

2.  5

3.  2,4**(Vezi cursul I: Introducere - Slide 11)**

4.  1,3

5.  9,10

<!-- -->

5.  **In algoritmii genetici, reprezentarea binara**

<!-- -->

1.  Este cea mai utilizata varianta de reprezentare a genotipurilor

2.  Nu e utilizata pentru algoritmi genetici

3.  A fost primul tip de reprezentare a cromozomilor in algoritmi
    genetici**(Vezi cursul 2: Slide 14)**

4.  Duce mereu la rezultate optime

5.  Nu depinde de problema rezolvata

<!-- -->

6.  **Componentele algoritmilor evolutivi sunt: **1. Reprezentarea; 2.
    Probabilitatea de mutatie; 3. Functia de evaluare; 4. Probabilitatea
    de recombinare; 5. Populatia; 6. Generarea de numere aleatoare; 7.
    Mecanismul de selectie a parintilor; 8. Generarea de permutari; 9.
    Reprezentarea grafica a evolutiei calitatii; 10; Operatorii de
    variatie; 11. Stabilirea diversitatii genetice a populatiei; 12.
    Mecanismul de inlocuire a populatiei curente; 13. Hillclimbing; 14;
    Initializarea populatiei; 15. Conditia de terminare;

<!-- -->

1.  1,2,5,6,7,14,15

2.  1,3,5,7,10,12,14,15

3.  2,4,6,8,11,13

4.  2,4,5,9,15

5.  1,3,5,6,10,13,14,15

<!-- -->

7.  **Calculul evolutiv este inspirat din**

<!-- -->

1.  Revolutia industriata

2.  Societatea cunoasterii

3.  Societatea informationala

4.  Noua revolutie agrara

5.  Evolutia naturala biologica**(Vezi cursul I: Introducere - Slide
    6)**

<!-- -->

8.  **Algoritmul Hillclimbing**: 1. Se aplica asupra unui singur punct
    din spatiul de cautare; 2. Aplicarea se poate repeta pentru mai
    multe puncte pentru a creste performantele; 3. Este inspirat din
    tehnicilie de alpinism; 4. Gaseste intotdeauna solutia optima; 5.
    Gaseste uneori solutia optima; 6. Calculele se incheie atunci cand
    temperatura sistemului devine 0; 7. De obicei gaseste un punct de
    optim local; 8. Se utilizeaza numai pentru reprezentarea cu siruri
    de numere reale;

<!-- -->

1.  1,2,5,7

2.  1,5,7,8

3.  1,2,4,7

4.  1,4,6,7

5.  3,4,6,8

<!-- -->

9.  **Caracteristicile unui algoritm genetic clasic(canonic) sunt**: 1.
    Reprezentarea populatiei este realizata prin intermediul sirurilor
    binare; 2. Reprezentarea populatiei este realizata prin intermediul
    sirurilor de numere naturale; 3. Probabilitatea de selectie a unui
    individ in multisetul parintilor este proportionala cu valoarea
    functiei de evaluare pentu el; 4. Probabilitatea de selectie a unui
    individ in multisetul parintilor este data de pozitia individului in
    erarhia populatiei, determinata pe baza functiei de evaluare; 5.
    Probabilitatea efectuarii unei mutatii este mica; 6. Probabilitatea
    efectuarii unei mutatii este mare; 7. Probabilitatea efectuarii
    recombinarii este mica; 8. Probabilitatea efectuarii recombinarii
    este mare; 9. Inlocuirea populatiei curente se face pe baza de
    varsta.

<!-- -->

1.  Nu exista algoritm genetic canonic

2.  2,4,6,7

3.  1,3,5,8(Speram, doamne ajuta)

4.  Nici una din variantele A,B,C,E

5.  2,3,6,7,9

<!-- -->

10. **Care din urmatorii operatori** pot fi utilizati intr-un algoritm
    genetic care foloseste reprezentarea prin siruri de numere reale: 1.
    Negarea; 2. Negarea Fuzzy; 3. Resetarea aleatoare; 4. Fluaj; 5.
    Mutatia uniforma; 6. Mutatia neuniforma cu distributie fixata; 7.
    Mutatia locala; 8. Interschimbarea; 9. Inserarea; 10. Mutatia
    Rapida; 11. Amestecu; 12. Mutatia globala; 13. Inversiunea; 14.
    Unipunct; 15; Multipunct; 16. Uniforma; 17. Recombinarea
    radacinilor; 18; Aritmetica simpla; 19. Aritmetica singulara; 20
    Aritmetica totala; 21. Recombinarea sirurilor maxima; 22. PMC; 23.
    Recombinare de ordine; 24. Recombinarea muchilor; 25. Recombinarea
    Ciclica

<!-- -->

1.  Toti operatorii de mai sus

2.  2,7,10,12,17,21

3.  1,3,4,7,10,13,16,17,20

4.  3,4,5,6,7,12,18,19,21

5.  5,6,14,15,16,18,19,20

**Partea II:**

1.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de mutatie:**

<!-- -->

1.  Este utilizata doar in probleme cu constringeri

2.  Este realizata cu probabilitate mica

3.  Utilizeaza populatia curenta

4.  Utilizeaza populatia de copii

5.  Determina structura cromozomiala

6.  Este de tip neuniform

7.  Alege pentru mutatie in medie jumatate de indivizi

8.  Este efectuata o singura data pe parcursul unui algoritm

9.  Este efectuata iterativ

10. Este efectuata imediat ce este disponibila o populatie de copii

<!-- -->

2.  **In cadrul unui algoritm genetic operatia de recombinare:**

<!-- -->

1.  Este efectuata o singura data dupa prima etapa de selectie a
    parintilor

2.  Este utilizata cu probabilitate mica

3.  In general probabilitatea de recombinare nu conteaza in rezolvarea
    problemelor prin algoritmi genetici

4.  Este efectuata o singura data pe parcursul unui algoritm genetic

5.  Este efectuata imediat inaintea fiecare proceduri de mutatie

6.  Este efectuata imediat dupa fiecare etapa de selectie a parintilor

7.  Este utilziata cu probabilitate mare

8.  Este efectuata iterativ

9.  Este utilizata doar in probleme fara constrangeri

10. Utilizeaza populatia de parinti

<!-- -->

3.  **In cadrul unui algoritm evolutiv populatia initiala**

<!-- -->

1.  Este generata la inceputul fiecarui ciclu evolutiv

2.  Este generata utilizand distributia pe probabilitate normala

3.  Este generata inaintea inceperii evolutiei propriu-zise

4.  Este generata dupa fiecare ciclu evolutiv

5.  Este generata utilizand distributia de probabilitate uniforma

6.  Este generata aleator (Vezi cursul I: Introducere - Slide 11)

7.  Este setata pe multimea vida

<!-- -->

4.  **Fie urmatorii doi cromozomi de tip permutare {6, 3, 11,7, 14, 8,
    5, 15, 1, 2, 4, 13, 9 ,10 ,12 } si {7, 1, 15,13,2,
    14,6,10,12,11,4,8,3,9, 5}. Aplicand operatorul de recombinare PMX,
    cu pozitile 4 si 8 se obtin descendentii.**

<!-- -->

1.  Siruri de numere

> x2 = {13,1,10,7,14,8,5,15,12,11,4,2,3,9,6}
>
> y2 = {5,3,11,13,2,14,6,10,1,8,4,7,9,15,12}

5.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de recombinare:**

<!-- -->

1.  Este de tip local sau global

2.  Este efectuata o singura data pe parcursul unui algoritm

3.  Alege pentru recombinare in medie jumatate de indivizi

4.  Este realizata cu probabilitate mica

5.  Determina structura cromozomiala

6.  Utilizeaza poplatia curenta

7.  Este efectuata o singura data, dupa prima etapa de generare a unei
    populatii

8.  Determina obtinerea unui multiset de copii in ...

9.  Este utilizata doar in probleme cu constrangeri

10. Este efectuata iterativ

<!-- -->

6.  **In cadrul unui algoritm din clasa strategiilor evolutive,
    reprezentarea cromozomilor**

<!-- -->

1.  Influenteaza tipul de recombinare folosit

2.  Se alege in functie de problema care se rezolva

3.  Poate fi numai de tip siruri de numere intregi sau reale

4.  Poate fi oricare dintre: siruri binare, siruri de numere intregi,
    siruri de numere reale, permutari

5.  Are influenta asupra mecanismului de  selectie a generatiei
    urmatoare

6.  Nu influenteaza tipul de mutatie folosit(discreta/ nediscreta)

7.  Poate fi numai de siruri de numere reale

8.  Contine atat descrierea individului candidat cat si parametrii care
    ..

<!-- -->

7.  **In cadrul unui algoritm genetic operatia de selectie a
    parintilor**

<!-- -->

1.  Intotdeauna este bazata pe o distributie de probabilitate de
    selectie

2.  Utilizeaza populatia curenta

3.  Este efectuata o singura data pe parcursul unui algoritm genetic

4.  Este utilizata doar in probleme cu constringeri

5.  Este efectuata imediat inaintea fiecarei proceduri de mutatie

6.  Este efectuata imediat ce este disponibila o populatie curenta
    evaluata

7.  Este efectuata o singura data dupa prima etapa de generare a unei
    populatii

8.  Alege in general indivizi pe baza factorului varsta

9.  Utilizeaza populatia de copii mutati

10. Utilizeaza populatia de copii

11. Este efectuata iterativ

12. Poate fi realizata prin utilizarea unei distributii de probabilitate
    de selectie

<!-- -->

8.  **Fie urmatorul cromozom de tip permutare {7, 6, 12, 14, 3, 10, 8,
    15, 11, 5, 4, 1, 13, 2, 9} In urma aplicarii operatorului de mutatie
    prin amestec s-a obitnut cromozomul {7, 14, 13, 12, 1, 15, 2, 8, 6,
    3, 11, 5, 10, 4, 9 }. Cele doua pozitii utilizate pentru amestesc
    sunt:**

<!-- -->

1.  3 si 13

2.  1 si 15

3.  1 si 14

4.  4 si 8

5.  1 si 12

6.  4 si 15

7.  3 si 15

8.  2 si 13

9.  2 si 14

10. 2 si 15

11. 1 si 13

<!-- -->

9.  **In cadrul unui algoritm genetic operatia de mutatie**

<!-- -->

1.  Are probabilitate mica

2.  Se aplica doar daca divesitatea genetica scade sub un prag x dat

3.  Intotdeauna produce indivizi fezabili

4.  Se aplica asupra descendentilor produsi de operatia de recombinare

5.  Se aplica asupra mutlisetului de parinti

6.  Se aplica asupra populatiei curente

7.  Se utilizeaza doar in probleme cu constrangeri

8.  Poate sa produca indivizi nefezabili

9.  Se efectueaza o singura data, dupa generarea populatiei initiale

10. Se aplica imediat inaintea fiecarei etape de selectie a generatiei
    urmatoare

11. Se utilizeaza doar in problemele fara constrangeri

12. Nu foloseste factori aleatori.

<!-- -->

10. **In cadrul unui algoritm genetic operatia de selectie a
    supravietuitorilor**

<!-- -->

1.  Utilizeaza intotdeauna factori aleatori

2.  In unele variante necesita calcularea unei distributii de
    probabilitate de selectie

3.  Indivizii alesi sunt intotdeauna fezabili

4.  Duce la cresterea calitatii medii a populatiei curente

5.  Se aplica la inceputul fiecarei iteratii

6.  Uneori utilizeaza factori aleatori

7.  Se aplica asupra populatiei curente

8.  Garanteaza obtinerea unei generatii cu calitate medie superioara.
    Daca foloseste selectia bazata pe varsta.

9.  Asigura perpetuarea individului cu calitate maxima din populatia
    curenta

10. Alege generatia urmatoare dintre indivizii disponibili dupa operatia
    de mutatie

11. Se aplica asupra descendentilor obtinuti din populatia curenta

Grile PEAG:

1\. Pentru pastrarea relatiilor comune din cromozomii parinti se
foloseste operatorul de recombinare:

a\) PMX (Partially Mapped crossover)

b\) nu exista un operator pebntru acest scop

[c) ECX (Edge crossover)]{.mark}

d\) incrusisare de tip turneu

e\) incrucisare binara

2\. Care din urmatoarele este un dezavantaj al utilizatii distributiei
de probabilitate de selectie de tip FPS?

a\) Convergenta asimptomatica

b\) convergenta lenta

[c) convergenta prematura]{.mark}

d\) eliminarea indivizilor slabi

e\) selectarea celor mai buni indivizi

3\. Pentru problemele in care reprezentarea prin permutari semnifica
ordiea de aparitie a unor evenimente, operatorul de recombinare folosit
este:

a\) incrucisarea aritmetica singulara

b\) incrucisarea unipunct

c\) IPX

[d) OCX (Order crossover)]{.mark}

e\) incrucisare uniforma

4\. Mecanismul de selectie turnir:

a\) este intotdeauna de tip determinist

b\) acorda o sansa si celui mai slab inidvid

c\) nu exista un astfel de mecanism. Turniul este o competitie medievala

[d) nu respecta distributia de probabilitate de selectie]{.mark}

e\) este cel mai des folosit mecanism de selectie

5\. Pentru problemele cu dependenta de adiacente se foloseste operatorul
de recombinare:

a\) OCX

b\) niciunul din celelalte raspunsuri

c\) ECX

[d) PMX]{.mark}

e\) incrucisare aritmetica singulara

6\. Care din urmatoarele nu este un mecanism de selectie?

[a) Ruleta complicata]{.mark}

b\) genitor

c\) ruleta simpla

d\) ruleta multi-brat

e\) turnir

7\. Recombinarea multipla:

a\) nu se poate baza pe frecventa alelelor

b\) este o generealizare a operatiilor de recombinare pentru
reprezentarea cu permutari

c\) are echivalent bilogic

d\) este cea mai bun optiune pentru algoritmii genetici

[e) produce rezultate mai bune doar in unele cazuri particulare]{.mark}

8\. In cazul reprezentarii cu siruri de numere intregi, recombinarile
aritmetice:

[a) se pot aplica daca se face rotunjirea rezultatelor]{.mark}

b\) produc intotdeauna rezultate aberante

c\) nu exista notiunea de recombinare aritmetica

d\) sunt interzise

e\) se pot aplica numai daca toate perechile de alele de pe pozitii
identice sunt fie pare, fie impare

9\. Care din urmatoarele este un dezavantaj al utilizatii distributiei
de probabilitate de selectie tip FPS?

[a) Convergenta prematura]{.mark}

b\) convergenta asimptotica

c\) eliminarea indivizilor slabi

d\) selectarea celor mai buni indivizi

e\) convergenta lenta

10\. Schema generala de recombinare depinde de:

a\) numarul de indivizi din populatia initiala

b\) ooperatorul de recombinare folosit

[c) existenta constrangerilor in problema de rezolvat]{.mark}

d\) reprezentarea cromozomilor

e\) alegerea utilizatorului

11\. Recombinarea multipla:

a\) nu se poate baza pe frecventa alelelor

b\) este o generealizare a operatiilor de recombinare pentru
reprezentarea cu permutari

c\) are echivalent bilogic

d\) este cea mai buna optiune pentru algoritmii genetici

[e) produce rezultate mai bune doar in unele cazuri particulare]{.mark}

12\. In cadrul algoritmilor genetici, generatia urmatoare este selectata
dintre:

a\) parintii selectati

[b) indivizii generatiei curente si descndentii obtinuti dupa etape de
mutatie]{.mark}

c\) decendentii generatiei curente

d\) indivizii generatiei curente

e\) descendentii obtinuti din etapa de recombinare

13\. Care din urmatoarele este un model de populatie?

a\) cu dimensiune fixa

b\) cu dimensiune variabila

c\) cu generatii

d\) cu stari instabile

[e) cu stari stabile]{.mark}

14\. Care din urmatoarele nu este un model de distributie de
probabilitate folosit pentru etapa de selectie:

a\) FPS cu ferestre

b\) FPS

[c) FPS cu alfla scalare]{.mark}

d\) ranguri liniare

e\) FPS cu sigma scalare

15\. Care mecanism de selectie prroduce rezultate mai apropiate de
distributia de probabilitate de selectie calculata?

a\) toate produc rezultate la fel de apropiate

[b) SUS]{.mark}

c\) niciunul

d\) ruleta cu un brat

e\) turnirul

16\. Daca aplicarea unui operator de recombinare produce indivizi
aberanti atunci:

[a) se folosesc parintii ca descendenti]{.mark}

b\) se produce eroare la executie

c\) algoritmul produce totusi rezultate corecte, ca urmare a
autoreglarii prin selectie

d\) rezultatele sunt imprevizibile

e\) problema nu se poate rezolva prin algoritm genetic

17\. De cate ori trebuie rotit bratul ruletei multi-brat pentru a
executa intregul proces de selectie a parintilor, pentru o populatie cu
k indivizi?

a\) de 2\*k ori

b\) de k ori

[c) o data]{.mark}

d\) de k/2 ori

e\) nu este ruleta multi-brat

18\. Ce aritate are operatorul de recombinare in algorimtii genetici
(cati operazi utilizeaza)

a\) unar (un operand)

b\) depinde de problema dee rezolvat

c\) ternar (trei operanzi)

d\) nu exista operatori de recombinare in algoritmii genetici

[e) binar (doi operanzi)]{.mark}

19\. Pentru a pastra cat mai bine informatia referioare la pozitiile
absolute ale alelelor in cromozomi parinti se foloseste operatul:\
a) incrucisare multipunct

[b) CX]{.mark}

c\) ECX

d\) OCX

e\) PMX

20\. Care din urmatoarele afirmatii nu e adevarata petru modelul
generational?

a\) poate inlocui un singur cromozom din populatia curenta

[b) necesita urmarirea mai multor generatii consecutive]{.mark}

c\) nu tine cont de calitatea cromozomilor

d\) poate inlocui parial generatia curenta

e\) poate inlocui complet generatia curenta

Grile PEAG:

97. Fie X = \[6 1 8 10 5 7 9 3 4 2\] si Y = \[9 8 7 3 6 1 5 10 4 2\]
    permutari. Care urmasi sunt generati prin utilizarea operatorului
    CX?

Raspuns corect:

C1=\[6 8 7 10 5 1 9 3 4 2\], C2=\[9 1 8 3 6 7 5 10 4 2\]

98. Intr-un algoritm evolutiv, functia de tip calitate:

<!-- -->

u.  Evalueaza calitatea algoritmului

v.  Evalueaza calitatea fiecarui candidat

w.  Evalueaza viteza de gasire a solutiei fata de consumul de resurse

x.  Trebuie maximizata

y.  Stabileste daca un descendent este acceptabil

z.  Selecteaza indivizii care se vor reproduce

a.  Selecteaza indivizii care trec in generatia urmatoare

b.  Contine un factor aleator

c.  Evalueaza calitatea populatiei curente

d.  Evalueaza calitatea populatiei curente fata de cea din generatia
    anterioara

> Raspuns corect:
>
> b, d

99. In cadrul unui algoritm genetic operatia de selectia a parintilor

- Este efectuata iterative

- Utilizeaza populatia curenta

- Este efectuata imediat ce este disponibila o populatie curenta
  evaluate

- Poate fi realizata prin utilizarea unei distributii de probabilitate
  de selectie

100. Componentele algortmilor evolutivi sunt:

<!-- -->

e.  Reprezentarea

f.  Probabilitatea de mutatie

g.  Functia de evaluare

h.  Probabilitatea de recombinare

i.  Populatia

j.  Generarea de numere aleatoare

k.  Mecanismul de selectie a parintilor

l.  Generarea de permutari

m.  Reprezentarea grafica a evolutiei calitatii

n.  Operatorii de variatie

o.  Stabilirea diversitatii genetice a populatiei

p.  Mecanismul de inlocuire a populatiei curente

q.  Hillclimbing

r.  Initializarea populatiei

s.  Conditia de terminare

> Raspuns corect:
>
> a, c, e, g, j, l, n, o

101. Calculul evolutiv este inspirat din:

\-\--evolutia naturala biologica

102. Fie urmatorii doi cromozomi de tip permutare {6, 3, 11 , 7, 14, 8,
     5, 15, 1, 2, 4, 13, 9, 10, 12} si {7, 1, 15, 13, 2, 14, 6, 10, 12,
     11, 4, 8, 3, 9, 5}. Aplicand operatorul de recombinare PMX, cu
     pozitiile 4 si 8 se obtin descendentii:

Raspuns corect:

h\. 13 1 10 7 14 8 5 15 12 11 4 2 3 9 6

i\. 5 3 11 13 2 14 6 10 1 8 4 7 9 15 12

103. In cadrul uni algoritm genetic operatia de selectie a
     supravietuitorilor

- Se aplica asupra populatiei curente

- Indivizii alesi sunt intotdeauna fezabili

- Uneori utilizeaza factori aleatori

- In unele variante necesita calcularea unei distributii de
  probabilitate de selectie

- Se aplica asupra descendentilor obtinuti din populatia curenta

104. Caracteristicile unui algoritm genetic clasic(canonic) sunt:

- Reprezentarea populatiei initiale este realizata prin intermediul
  sirurilor binare

- Probabilitatea de selectie a unui individ in multisetul parintilor
  este proportional cu valoarea functiei de evaluare pentru ei

- Probabilitatea efectuarii unei mutatii este mica

- Probabilitatea efectuarii recombinarii este mare

105. In cadrul unui algoritm evolutiv populatia initiala

- Este generata aleator

- Este generata inaintea inceperii evolutiei propriu-zise

106. In cadrul unui algoritm din clasa strategiilor evolutive, operatia
     de recombinare:

- Este efectuata iterative

- Determina obtinerea unui multiset de copii in ..

- Utilizeaza populatia curenta

- Este de tip local sau global

107. Care dintre urmatorii operatori pot fi utilizati intr-un algoritm
     genetic care foloseste reprezentarea prin siruri de numere reale:

- Mutatia uniforma

- Mutatia neuniforma cu distributie fixata

- Unipunct

- Multipunct

- Uniforma

- Aritmetica simpla

- Aritmetica singulara

- Aritmetica totala

108. In cadrul unui algoritm genetic operatia de recombinare:

- Utilizeaza populatia de parinti

- Este efectuata imediat dupa fiecare etapa de selectie a parintilor

- Este efectuata imediat inaintea fiecarei procedure de mutatie

- Este efectuata iterative

- Este utilizata cu probabilitate mare

109. In algoritmii genetici, reprezentarea prin siruri de numere intregi

- E preferabila atunci cand pentru fiecare gena sunt posibile mai mult
  de doua valori distincte

110. In cadrul unui algoritm din clasa strategiilor evolutive,
     reprezentarea cromozomilor

- Poate fi numai de siruri de numere reale

- Nu influenteaza tipul de mutatie folosit(discrete/nediscreta)

- Contine atat descrierea individului candidat cat si parametrii care...

111. In cadrul unui algoritm genetic operatia de selectie a
     supravietuitorilor

- In unele variante necesita calcularea unei distributii de
  probabilitate de selectie

- Alege generatia urmatoare dintre indivizii disponibili dupa operatia
  de mutatie

- Indivizii alesi sunt intotdeauna fezabili

- Uneori utilizeaza factori aleatori

- Se aplica asupra populatiei curente si asupra descendentilor obtinuti
  din populatia curenta

112. Tipurile de probleme care pot fi rezolvate pe baza calculului
     evolutiv sunt:

- Probleme de cautare in spatial solutiilor

- Probleme de modelare

- Probleme de simulare

- Deplasarea autonoma a autovehiculelor

113. In algoritmii genetici, reprezentarea prin permutari

- Necesita operatori de variatie special definite

114. Intr-un algoritm evolutiv, functia fitness:

- Evalueaza calitatea fiecarui candidat

115. Fie urmatorul cromozom de tip permutare {7, 6, 12, 14, 3, 10, 8,
     15, 11, 5, 4, 1, 13, 2, 9}. In urma aplicarii operatorului de
     mutatie prin amestec s-a obtinut cromozomul {7, 14, 13, 12, 1, 15,
     2, 8, 6, 3, 11, 5, 10, 4, 9}. Cele doua pozitii utilizate pentru
     amestec sunt:

- 2 si 14

- 1 si 14

- 2 si 15

- 1 si 15

116. In algoritmii genetici, reprezentarea binara

- A fost primul tip de reprezentare a cromozomilor in algoritmi genetici

117. In cadrul unui algoritm genetic operatia de mutatie:

- Se aplica asupra descendetilor produsi de operatia de recombinare

- Poate sa produca indivizi refezabili

- Are probabilitate mica

118. In algorimii genetici, reprezentarea prin permutari

- Are nevoie de operatori speciali definite

119. In cadrul unui algoritm din clasa strategiilor evolutive, operatia
     de mutatie

- Utilizeaza populatia de copii

- Este efectuata iterative

- Este de tip neuniform

120. Algoritmul Hillclimbing

- Se aplica asupra unui singur punct din spatiul de cautare

- Aplicarea se poate repeat pentru mai multe puncte pentru a creste
  performantele

- Gaseste uneori solutia optima

- De obicei geseste un punct de optim local

121. care nu este un mecanism de selectie: -\> ruleta complicata

122. Ruleta multi-brat trebuie rotita doar o data pentru a executa
     intregul proces de selectie al parintilor

123. Care mecanism de selectie reproduce rezultate cat mai apropiate de
     distributia de probabilitate? -\> SUS(\...)

124. Mecanismul de selectie turnir -\> nu respecta distributia de
     probabilitate de selectie

125. Care din urmatoarele nu sunt modele de populatie? -\> cu generatii,
     cu dimensiune fixa, cu dimensiune variata, cu stari instabile

126. Care sunt modele de populatie? -\> cu stari stabile

127. In cadrul algoritmilor genetici, urmatoarea generatie este
     selectata dintre:

> -\> indivizii generatiei curente si descendentii obtinuti dupa etapa
> de mutatie

128. Care din urmatoarele este un dezavantaj pt distributia de
     probabilitate FPS? -\> convergenta premature

129. De cate ori tre rotit bratul ruletei simple pentru a executa
     intregul proces de selectie al parintilor pt o populatie cu tz
     cromozomi-\> de tz ori

130. In cadrul algoritmilor genetici, generatia urmatoare este selectata
     dintre:

-\> indivizii generatiei curente si descendentii obtinuti dupa etapa de
mutatie

131. Care din urmatoarele nu este un model de distributie folosit pt
     etapa de selectie:

-\> FPS cu alfa scalare

132. Care dintre urmatoarele este falsa pt modelul generational?

-\> nu tine cont de calitatea cromozomilor

133. Daca aplicarea unui operator de recombinare produce indivizi
     aberanti, atunci:

-\> se folosesc parintii ca descendenti

SAU

-\> algoritmul produce totusi rezultate corecte, ca urmare a
autoreglarii prin selectie

134. Mecanismul de selectie turnir -\> este intotdeauna un tip
     determinist

135. Pt pastrarea relatiilor comune din cromozomii parinti se foloseste
     operatorul de recombinare

-\> EXC (Edge crossover)

136. Recombinarea multipla

-\> produce rezultate mai bune doar in unele cazuri particulare

137. Schema generala de recombinare depinde de: -\> operatorul de
     recombinare folosit

138. In cazul reprezentarii cu siruri de numere intregi, recombinarile
     aritmetice:

-\> se pot aplica numai daca toate perechile de alele de pe pozitii
identice sunt fie pare, fie impare

139. Pt a pastra cat mai bine informatia referitoare la pozitiile
     absolute ale alelelor in cromozomii parinti se foloseste
     operatorul:

-\> CX (Cycle crossover)

140. Pentru problemele in care reprezentarea prin permutari semnifica
     ordinea de aparitie a unor evenimente, operatorul de recombinare
     folosit este

-\> OCX (Order crossover)

141. In algoritmii genetici, reprezentarea prin permutari:

-\> Necesita operatori de variatie special definite

142. Intr-un algoritm evolutiv, functia fitness: -\> Evalueaza calitatea
     fiecarui individ

143. In cadrul strategiilor evolutive: -\> Mutatia este aplicata cu
     probabilitate

144. In cadrul unui algoritm genetic, operatia de selectie a
     supravietuitorilor:

> -\>In unele variante necesita calcularea unei distributii de selectie
>
> -\>Alege generatia urmatoare dintre indivizii disponibili dupa
> operatia de mutatie
>
> -\>Indivizii alesi sunt intotdeauna fezabili (ce plm inseamna
> fezabil?)
>
> -\> Uneori utilizeaza factori aleatori
>
> -\> Se aplica asupra populatiei curente si asupra descendentilor
> obtinuti din populatia curenta

PEAG

1.  Care din urmatoarele nu este un model de distributie de
    probabilitate folosit pt etapa de selectie:

<!-- -->

a)  FPS cu ferestre

b)  FPS

c)  [FPS cu alfa scalare]{.mark}

d)  Ranguri liniare

e)  FPS cu sigma scalare

<!-- -->

2.  Pentru a pastra cat mai bine informatia referitoare la pozitiile
    absolute ale alelelor in cromozomii parinti se foloseste operatorul:

<!-- -->

a.  Incrucisare multipunct

b.  [CX (Cycle crossover)]{.mark}

c.  ECX (Edge crossover)

d.  OCX (Order crossover)

e.  PMX (Partally Mapped crossover)

<!-- -->

3.  Pentru problemele in care reprezentarea prin permutari semnifica
    ordinea de aparitie a unor evenimente, operatorul de recombinare
    folosit este:

<!-- -->

a.  Incrucisare aritmetica singulara

b.  Incrucisare unipunct

c.  IPX

d.  [OCX]{.mark}

e.  Incrucisare uniforma

<!-- -->

4.  Care dintre urmatoarele este un dezavantaj al utilizarii
    distributiei de probabiliate de selectie tip FPS?

<!-- -->

a.  Convergenta asimptomatica

b.  Convergenta lenta

c.  [Convergenta prematura]{.mark}

d.  Eliminarea indivizilor slabi

e.  Selectarea celor mai buni indivizi

<!-- -->

5.  De cate ori trebuie rotit bratul ruletei simple pentru a executa
    intregul process de selectie a parintilor, pentru o populatie cu tz
    cromozomi?

<!-- -->

a.  O data

b.  De 2\*tz ori

c.  De tz ori

d.  De 10 ori

e.  De tz/2 ori

<!-- -->

6.  In cazul GA generatia urmatoare este selectata dintre:

<!-- -->

a.  Descendentii obtinuti din etapa de recombinare

b.  [Indivizii generatiei curente si descendentii obtinuti dupa etapa de
    mutatie]{.mark}

c.  Descendentii generatiei curente

d.  Indivizii generatiei curente

e.  Parintii selectati

<!-- -->

7.  Schema generala de recombinare depinde de:

<!-- -->

a.  Existenta constrangerilor in problema de rezolvat

b.  Operatorul de recombinare folosit

c.  Reprezentarea cromozomilor

d.  Alegerea utilizatorului

e.  Numarul de indivizi din pop initiala

<!-- -->

8.  Ce aritate are operatorul de recombinare in GA (cati operanzi
    utilizeaza) ?

<!-- -->

a.  Tenar (trei operanzi)

b.  Binr (doi operanzi)

c.  [Depinde de pb de rezolvat]{.mark}

d.  Nu exista operatori de recombinare in algoritmi genetici

e.  Unar (un operand)

<!-- -->

9.  Pentru pastrarea relatiilor comune din cromozomii parinti se
    foloseste operatorul de recombinare:

<!-- -->

a.  PMX

b.  Nu exista un operator pentru acest scop

c.  [ECX]{.mark}

d.  Incrucisare de tip turneu

e.  Incrucisarea binara

<!-- -->

10. Care mecanism de selectie produce rezultate mai apropiate de
    distributia de probabilitate de selectia calculate?

<!-- -->

a.  Toate produc rezultate la fel de apropiate

b.  SUS (Sochastic Universal Sampling)

c.  [Nici unul]{.mark}

d.  Ruleta cu brat

e.  Turnirul

<!-- -->

11. Mecanismul de selectie turnir:

<!-- -->

a.  Este intotdeauna de tip determinist

b.  Acorda o sansa si celui mai slab individ

c.  Nu exista un astfel de mechanism.

d.  [Nu respecta distributia de probabilitate de selectie]{.mark}

e.  Este cel mai des folosit mecansim de selectie

<!-- -->

12. Daca aplicarea unui operator de recombinare produce indivizi
    aberanti atunci:

<!-- -->

a.  [Algoritmul produce totusi rezultate corecte, ca urmare a
    autoreglarii prin selectie]{.mark}

b.  Problema nu se poate rezolva prin GA

c.  Rezultatele sunt imprevizibile

d.  Se produce erore la executie

e.  Se folosesc parinti ca descendenti

<!-- -->

13. Care dintre urmatoarele NU este mechanism de selectie?

<!-- -->

a.  [Ruleta complicate]{.mark}

b.  Turnir

c.  Genitor

d.  Ruleta multi-brat

e.  Ruleta simpla

<!-- -->

14. In cazul recombinarii cu nr intregi, recombinarile aritmetice:

<!-- -->

a.  Produc intotdeauna rezultate aberante

b.  Sunt interzise

c.  [Se pot aplica daca se face rotunjirea rezultatelor]{.mark}

d.  Nu exista notiunea de recombinare aritmetica

e.  Se pot aplica numai daca toate perechiile de allele de pe pozitii
    identice sunt fie pare, fie impare

<!-- -->

15. De cate ori trebuie rotit bratul ruletei multi-brat pt a executa
    intregul process de selectie a parintilor pt o populatie de k
    indivizi?

<!-- -->

a.  De k ori

b.  [O data]{.mark}

c.  Nu exista ruleta multi-brat

d.  De k/2 ori

e.  De k\*2 ori

<!-- -->

16. Recombinarea multipla:

<!-- -->

a.  Nu se poate baza pe frecventa alelelor

b.  Este o generalizare a operatiilor de recombinare pentru
    reprezentarea cu permutari

c.  Are echivalent biologic

d.  Este cea mai buna optiune pt GA

e.  [Produce rezultate mai bune in unele cazuri particulare.]{.mark}

<!-- -->

17. Care dintre urmatoarele afirmatii **nu** e adevarata pt modelul
    generational?

<!-- -->

a.  Poate inlocui un singur cromozom in populatia curenta

b.  Necesita urmarirea mai multor generatii consecutive

c.  Nu tine cont de calitatea cromozomilor

d.  [Poate inlocui partial generatia curenta]{.mark}

e.  Poate inlocui complet generatia curenta.

<!-- -->

18. Pentru problemele de dependenta de adiacente se foloseste operatorul
    de recombinare:

<!-- -->

a.  OCX

b.  Nici unul din celalalte raspunsuri

c.  ECX

d.  [PMX]{.mark}

e.  Incrucisare aritmetica singulara

<!-- -->

19. Care dintre urmatoarele este un model de populatie?

<!-- -->

a.  Cu dimensiune fixa

b.  Cu dimensiune variabila

c.  Cu generatii

d.  Cu stari instabile

e.  [Cu stari stabile]{.mark}

<!-- -->

20. Pentru problemele in care reprezentarea prin permutari semnifica
    ordinea de aparitie a unor evenimente, operatorul de recombinare:

<!-- -->

a.  [OCX]{.mark}

b.  Incrucisare unipunct

c.  Incrucisare uniforma

d.  Incrucisare aritmetica singulara

e.  IPX

În algoritmii genetici, reprezentarea prin permutări

23\.

Alegeți o opțiune:

![](media/image2.wmf)A. Necesită operatori de variație special definiți

![](media/image3.wmf)B.\
Nu permite utilizarea de operatori de mutație 

![](media/image3.wmf)C. Nu este utilizată

![](media/image3.wmf)D.\
Nu permite utilizarea de operatori de recombinare

![](media/image3.wmf)E.\
Nu permite mai mult de două gene cu aceeași valoare într-un cromozom

24\. Într-un algoritm evolutiv, funcția fitness: 1. Evaluează calitatea
algoritmului; 2. Trebuie selectată aleator; 3. Evaluează viteza de
găsire a soluției față de consumul de resurse; 4. Trebuie modificată la
fiecare iterație; 5. Selectează indivizii care se vor reproduce; 6.
Selectează indivizii care trec în generația următoare; 7. Evaluează
calitatea populației curente față de cea a populației inițiale; 8.
Evaluează calitatea populației curente față de cea din generația
anterioară; 9. Evaluează calitatea fiecărui candidat.

Alegeți o opțiune:

![](media/image3.wmf)a. 6,7,8

![](media/image3.wmf)b. 1,3

![](media/image3.wmf)c. 4,5

![](media/image2.wmf)d. 9 

![](media/image3.wmf)e. 2,3

Fie X=\[ 6 1 8 10 5 7 9 3 4 2 \] și Y=\[ 9 8 7 3 6 1 5 10 4 2 \]
permutări. Care urmași sunt generați prin utilizarea operatorului CX?

25.Alegeți o opțiune:

![](media/image3.wmf)a. C1=\[ 6 7 8 10 5 1 9 3 4 2 \], C2=\[ 9 8 1 3 6 7
5 10 4 2 \]

![](media/image3.wmf)b. C1=\[ 8 7 10 5 1 9 3 4 2 6 \], C2=\[ 2 9 1 8 3 6
7 5 10 4 \] 

![](media/image3.wmf)c. C1=Y, C2=X

![](media/image3.wmf)d. C1=\[ 2 6 7 8 10 5 1 9 3 4 \], C2=\[ 2 8 1 3 6 7
5 10 4 9 \]

![](media/image2.wmf)e. C1=\[ 6 8 7 10 5 1 9 3 4 2 \], C2=\[ 9 1 8 3 6 7
5 10 4 2 \]

26\. În cadrul unui algoritm genetic operația de selecție a
supraviețuitorilor: 1. Se aplică asupra populației curente; 2. În unele
variante necesită calcularea unei distribuții de probabilitate de
selecție; 3. Utilizează întotdeauna factori aleatori; 4. Alege generația
următoare dintre indivizii disponibili după operația de mutație; 5.
Indivizii aleși sînt întotdeauna fezabili; 6. Uneori utilizează factori
aleatori; 7. Asigură perpetuarea individului cu calitate maximă din
populația curentă; 8. Duce la creșterea calității medii a populației
curente; 9. Garantează obținerea unei generații cu calitate medie
superioară, dacă folosește selecția bazată pe vîrstă; 10.Se aplică la
începutul fiecărei iterații; 11. Se aplică asupra descendenților
obținuți din populația curentă; 12. Se aplică asupra populației curente
și asupra descendenților obținuți din populația curentă.

Alegeți o opțiune:

![](media/image3.wmf)a. 2, 3, 4, 5, 6, 11

![](media/image3.wmf)b. 4, 8, 11

![](media/image3.wmf)c. 1,7

![](media/image3.wmf)d. 6, 8, 11

![](media/image2.wmf)e. 2, 4, 5, 6, 12 

27\. În cadrul strategiilor evolutive

Alegeți o opțiune:

![](media/image3.wmf)a. Operatorul de mutație cel mai utilizat este
mutația prin interschimbare

![](media/image3.wmf)b. Sunt utilizați operatori de recombinare OCX

![](media/image3.wmf)c. Nu se permite utilizarea de operatori de mutație

![](media/image2.wmf)d. Mutația este aplicată cu probabilitate 1 

![](media/image3.wmf)e. Reprezentarea este prin vectori binari

**1.** În algoritmii genetici, reprezentarea prin permutări

A. Nu permite utilizarea de operatori de recombinare

B. Nu permite utilizarea de operatori de mutație

C. Nu permite mai mult de două gene cu aceeași valoare într-un cromozom

D. Necesită operatori de variație special definiți

E. Nu este utilizată

**2.** Într-un algoritm evolutiv, funcția fitness: 1. Evaluează
calitatea algoritmului; 2. Trebuie selectată aleator; 3. Evaluează
viteza de găsire a soluției față de consumul de resurse; 4. Trebuie
modificată la fiecare iterație; 5. Selectează indivizii care se vor
reproduce; 6. Selectează indivizii care trec în generația următoare; 7.
Evaluează calitatea populației curente față de cea a populației
inițiale; 8. Evaluează calitatea populației curente față de cea din
generația anterioară; 9. Evaluează calitatea fiecărui candidat.

A. 1, 3

B. 2,3

C. 9

D. 4,5

E. 6, 7, 8

**3.** Fie X=\[ 6 1 8 10 5 7 9 3 4 2 \] și Y=\[ 9 8 7 3 6 1 5 10 4 2 \]
permutări. Care urmași sînt generați prin utilizarea operatorului CX?

A. C1=\[ 2 6 7 8 10 5 1 9 3 4 \], C2=\[ 2 8 1 3 6 7 5 10 4 9 \]

B. C1=\[ 6 8 7 10 5 1 9 3 4 2 \], C2=\[ 9 1 8 3 6 7 5 10 4 2 \]

C. C1=\[ 6 7 8 10 5 1 9 3 4 2 \], C2=\[ 9 8 1 3 6 7 5 10 4 2 \]

D. C1=\[ 8 7 10 5 1 9 3 4 2 6 \], C2=\[ 2 9 1 8 3 6 7 5 10 4 \]

E. C1=Y, C2=X

**4.** Fie următorii doi cromozomi de tip permutare: {6, 3, 11, 7, 14,
8, 5, 15, 1, 2, 4, 13, 9, 10, 12 } și {7, 1, 15, 13, 2, 14, 6, 10, 12,
11, 4, 8, 3, 9, 5}. Aplicînd operatorul de recombinare PMX, cu pozițiile
4 și 8 se obțin descendenții: a. 5 3 15 13 2 14 6 10 12 8 4 7 9 11 1; b.
13 1 11 7 14 8 5 15 12 10 4 2 3 9 6; c. 13 12 11 7 14 8 5 15 1 10 4 2 3
9 6; d. 5 3 11 13 2 14 6 15 1 8 4 7 9 10 12; e. 5 3 15 13 2 14 6 10 1 8
4 7 9 11 12; f. 13 12 11 7 14 8 5 15 1 10 4 2 3 9 6; g. 13 1 15 7 14 8 5
10 12 11 4 2 3 9 6; h. 13 1 10 7 14 8 5 15 12 11 4 2 3 9 6; i. 5 3 11 13
2 14 6 10 1 8 4 7 9 15 12.

A. a, b

B. e, f

C. a, c

D. h, i

E. f, i

**5.** În cadrul unui algoritm genetic operația de selecție a
supraviețuitorilor: 1. Se aplică asupra populației curente; 2. În unele
variante necesită calcularea unei distribuții de probabilitate de
selecție; 3. Utilizează întotdeauna factori aleatori; 4. Alege generația
următoare dintre indivizii disponibili după operația de mutație; 5.
Indivizii aleși sînt întotdeauna fezabili; 6. Uneori utilizează factori
aleatori; 7. Asigură perpetuarea individului cu calitate maximă din
populația curentă; 8. Duce la creșterea calității medii a populației
curente; 9. Garantează obținerea unei generații cu calitate medie
superioară, dacă folosește selecția bazată pe vîrstă; 10.Se aplică la
începutul fiecărei iterații; 11. Se aplică asupra descendenților
obținuți din populația curentă; 12. Se aplică asupra populației curente
și asupra descendenților obținuți din populația curentă.

A. 2, 3, 4, 5, 6, 11

B. 4, 8, 11

C. 2, 4, 5, 6, 12

D. 6, 8, 11

E. 1, 7

E. Nu este utilizată

x pt x intre -10 si 10

-8 4 6 -5 2 10 7 -3 -\> -8 4 6 -5 1 10 7 -3

MUTATIE UNIFORMA

Asemanatoare cu resetare aleatoare

Modifica o alela cu o valoare aleatoare: distributie uniforma

0.4 0.1 0.7 0.9 1.0 0.2 0.3 0.5 -\> 0.4 0.7 0.7 0.9 1.0 0.2 0.3 0.5

MUTATIE NEUNIFORMA

Asemanantoare cu fluaj

Modifica valoarea unei gene cu o valoare mica: distributie gaussiana de
medie 0, deviatie standard

Domenii modificare: \[-t,t\]

INTERSCHIMBARE

Alege aleator 2 gene i, j si le interschimba

\- Se foloseste la regine, lideri

\[4 3 6 5 7 2 1 8\] -\> \[4 3 1 5 7 2 6 8\]

INSERARE

Alege aleator 2 gene i\<j si insereaza xj pe pozitia i+1, iar alelele
i+1, i+2, ..., j-1 se deplaseaza la dreapta cu 1 pozitie

\[ 4 3 6 5 7 2 1 8\] -\> \[4 3 6 1 5 7 2 8\]

AMESTEC

Alege aleator 2 gene i\<j si repozitioneaza aleator alelele I, i+1, ...,
j-1, j in acelasi interval

\[4 3 6 5 7 2 1 8\] -\> \[4 3 7 2 5 1 6 8\]

INVERSIUNE

Alege aleator 2 gene i\<j, inverseaza ordinea alelelor I,i+1,..j-1,j in
acelasi interval

\[4 3 6 5 7 2 1 8\] - \> \[4 3 1 2 7 5 6 8\]

**RECOMBINARE**

**Pt. reprezentare BINARA:** INCRUCISARE UNIPUNCT, MULTIPUNCT, UNIFORMA

**Pt. reprezentare nr. INTREGI:** INCRUCISARE UNIPUNCT, MULTIPUNCT,
UNIFORMA

**Pt. reprezentare nr. REALE:** INCRUCISARE UNIPUNCT, MULTIPUNCT,
UNIFORMA, DE TIP DISCRET, ARITMETICA SIMPLA, SINGULARA, TOTALA

**Pt. reprezentare PERMUTARI:** PMX, OCX, CX, ECX

Grile Irina

1\. In cadrul unui algoritm evolutive conditia de terminare: 1. este
obligatorie; 2.nu este indicata; 3. include obligatoriu, direct sau
indirect, controlul numarului de iteratii (nr pop generate), 4. nu poate
fi implementata 5. este utilizata doar in GA, nu si in cadrul ES

[b. 1,3]{.mark}

1.  Algoritmii genetici:

    a.  Utilizeaza la fiecare moment de timp o varianta de solutie ...
        prin perturbare normala

    b.  Sunt tehnici de cautare stochastica bazate pe populatii

    c.  Folosesc exclusive selectii deterministe

    d.  Sunt modele deterministe de cautare in spatial solutiilor

    e.  Rezolva exclusive probleme definite pe spatii continue

2.  In algoritmii genetici, alegerea unei anumite reprezentari:

    a.  Este independenta de problema de rezolvat

    b.  Nu vad raspunsul

    c.  Poate fi facuta aleatory

    d.  Este imposibila, fiind folosita doar reprezentarea prin numere
        reale

    e.  Influenteaza calitatea solutiei furnizate

> a.4; b.1,3; c.2,5; d.2,3 e.3,5

4\. Algoritmul ES2M:

a\. nu este un algoritm auto-adaptiv

b\. nu este un algoritm evolutive

c\. nici una din celelalte variante

d\. este un algoritm determinist

e\. este algoritmul auto-adaptiv primar

**Partea I:**

1.  În algoritmii genetici, **rerezentarea prin șiruri de numere
    întregi**

<!-- -->

1.  Este preferabila pentru probleme de optimizare

2.  Este doar un exercitiu de implementare, nefiind necesara

3.  E preferabila atunci cand pentru fiecare gena sunt posibile mai mult
    de doua valori distincte

4.  nu este utilizata in algoritmi genetici

5.  Nu poate fi utilizata in cazul atributelor ordinale

<!-- -->

2.  In algoritmii genetici, **reprezentarea prin permutări**

<!-- -->

1.  Nu permite utilizarea de operatori de mutatie

2.  Nu este utilizata

3.  Are nevoie de operatori special definiti **(Vezi cursul II: - Slide
    19)**

4.  Nu permite utilizarea de operatori de recombinare

5.  Nu permite mai mult de doua gene cu aceeasi valoare intr-un cromozom

<!-- -->

3.  **Tipurile de probleme care pot fi rezolvate pe baza calculului
    evolutiv **sînt: 1. Problemele de optimizare; 2.Probleme de cautare
    in spatiul solutilor; 3. Prelucrarea datelor de dimensiune
    mare(big-data); 4. Probleme de modelare; 5.Probleme de validare a
    datelor; 6. Probleme de simulare; 7 Alocarea dinamica a datelor in
    memoria calculatorului; 8. Deplasarea autonoma a vechiculelor

<!-- -->

1.  2,4,6

2.  1,4,6**(Vezi cursul I: Introducere: - Slide 9 si 10)**

3.  2,4,6,8

4.  1,3,5,7

5.  2,3,4

<!-- -->

4.  **Intr-un algoritm evolutiv**, functia de tip calitate: 1. Evalueaza
    calitatea algoritmului, 2. Evalueaza calitatea fiecarui candidat; 3.
    Evalueaza viteza de gasire a solutiei fata de consumul de
    resurse; 4. Trebuie maximizata; 5. Stabileste daca un descendent
    este acceptabil; 6. Selecteaza indivizii care se vor reproduce; 7.
    Selecteaza indivizii care trec in generatia urmatoare; 8. Contine un
    factor aleator; 9. Evalueaza calitatea populatiei curente; 10.
    Evalueaza calitatea populatiei curente fata de cea din generatia
    anterioara;

<!-- -->

1.  6,7,8

2.  5

3.  2,4**(Vezi cursul I: Introducere - Slide 11)**

4.  1,3

5.  9,10

<!-- -->

5.  **In algoritmii genetici, reprezentarea binara**

<!-- -->

1.  Este cea mai utilizata varianta de reprezentare a genotipurilor

2.  Nu e utilizata pentru algoritmi genetici

3.  A fost primul tip de reprezentare a cromozomilor in algoritmi
    genetici**(Vezi cursul 2: Slide 14)**

4.  Duce mereu la rezultate optime

5.  Nu depinde de problema rezolvata

<!-- -->

6.  **Componentele algoritmilor evolutivi sunt[: ]{.mark}**[1.
    Reprezentarea]{.mark}; 2. Probabilitatea de mutatie; [3. Functia de
    evaluare]{.mark}; 4. Probabilitatea de recombinare; [5.
    Populatia]{.mark}; 6. Generarea de numere aleatoare[; 7. Mecanismul
    de selectie a parintilor]{.mark}; 8. Generarea de permutari; 9.
    Reprezentarea grafica a evolutiei calitatii; [10; Operatorii de
    variatie]{.mark}; 11. Stabilirea diversitatii genetice a populatiei;
    [12. Mecanismul de inlocuire a populatiei curente]{.mark}; 13.
    Hillclimbing; [14; Initializarea populatiei; 15. Conditia de
    terminare]{.mark};

<!-- -->

1.  1,2,5,6,7,14,15

2.  1,3,5,7,10,12,14,15

3.  2,4,6,8,11,13

4.  2,4,5,9,15

5.  1,3,5,6,10,13,14,15

<!-- -->

7.  **Calculul evolutiv este inspirat din**

<!-- -->

1.  Revolutia industriata

2.  Societatea cunoasterii

3.  Societatea informationala

4.  Noua revolutie agrara

5.  Evolutia naturala biologica**(Vezi cursul I: Introducere - Slide
    6)**

<!-- -->

8.  **Algoritmul Hillclimbing**: 1. Se aplica asupra unui singur punct
    din spatiul de cautare; 2. Aplicarea se poate repeta pentru mai
    multe puncte pentru a creste performantele; 3. Este inspirat din
    tehnicilie de alpinism; 4. Gaseste intotdeauna solutia optima; 5.
    Gaseste uneori solutia optima; 6. Calculele se incheie atunci cand
    temperatura sistemului devine 0; 7. De obicei gaseste un punct de
    optim local; 8. Se utilizeaza numai pentru reprezentarea cu siruri
    de numere reale;

<!-- -->

1.  1,2,5,7

2.  1,5,7,8

3.  1,2,4,7

4.  1,4,6,7

5.  3,4,6,8

<!-- -->

9.  **Caracteristicile unui algoritm genetic clasic(canonic) sunt**: [1.
    Reprezentarea populatiei este realizata prin intermediul sirurilor
    binare;]{.mark} 2. Reprezentarea populatiei este realizata prin
    intermediul sirurilor de numere naturale; [3. Probabilitatea de
    selectie a unui individ in multisetul parintilor este proportionala
    cu valoarea functiei de evaluare pentu el;]{.mark} 4. Probabilitatea
    de selectie a unui individ in multisetul parintilor este data de
    pozitia individului in erarhia populatiei, determinata pe baza
    functiei de evaluare[; 5. Probabilitatea efectuarii unei mutatii
    este mica;]{.mark} 6. Probabilitatea efectuarii unei mutatii este
    mare; 7. Probabilitatea efectuarii recombinarii este mica[; 8.
    Probabilitatea efectuarii recombinarii este mare;]{.mark} 9.
    Inlocuirea populatiei curente se face pe baza de varsta.

<!-- -->

1.  Nu exista algoritm genetic canonic

2.  2,4,6,7

3.  1,3,5,8(Speram, doamne ajuta)

4.  Nici una din variantele A,B,C,E

5.  2,3,6,7,9

<!-- -->

10. **Care din urmatorii operatori** pot fi utilizati intr-un algoritm
    genetic care foloseste reprezentarea prin siruri de numere reale: 1.
    Negarea; 2. Negarea Fuzzy; 3. Resetarea aleatoare; 4. Fluaj[; 5.
    Mutatia uniforma; 6. Mutatia neuniforma cu distributie
    fixata;]{.mark} 7. Mutatia locala; 8. Interschimbarea; 9.
    Inserarea; 10. Mutatia Rapida; 11. Amestecu; 12. Mutatia
    globala; 13. Inversiunea; [14. Unipunct; 15; Multipunct; 16.
    Uniforma;]{.mark} 17. Recombinarea radacinilor; [18; Aritmetica
    simpla; 19. Aritmetica singulara; 20 Aritmetica totala;]{.mark} 21.
    Recombinarea sirurilor maxima; 22. PMC; 23. Recombinare de
    ordine; 24. Recombinarea muchilor; 25. Recombinarea Ciclica

<!-- -->

1.  Toti operatorii de mai sus

2.  2,7,10,12,17,21

3.  1,3,4,7,10,13,16,17,20

4.  3,4,5,6,7,12,18,19,21

5.  5,6,14,15,16,18,19,20

**Partea II:**

1.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de mutatie:**

<!-- -->

1.  Este utilizata doar in probleme cu constringeri

2.  Este realizata cu probabilitate mica

3.  Utilizeaza populatia curenta

4.  Utilizeaza populatia de copii

5.  [Determina structura cromozomiala]{.mark}

6.  Este de tip neuniform

7.  Alege pentru mutatie in medie jumatate de indivizi

8.  Este efectuata o singura data pe parcursul unui algoritm

9.  Este efectuata iterativ

10. Este efectuata imediat ce este disponibila o populatie de copii

<!-- -->

2.  **In cadrul unui algoritm genetic operatia de recombinare:**

<!-- -->

1.  Este efectuata o singura data dupa prima etapa de selectie a
    parintilor

2.  Este utilizata cu probabilitate mica

3.  In general probabilitatea de recombinare nu conteaza in rezolvarea
    problemelor prin algoritmi genetici

4.  Este efectuata o singura data pe parcursul unui algoritm genetic

5.  Este efectuata imediat inaintea fiecare proceduri de mutatie

6.  Este efectuata imediat dupa fiecare etapa de selectie a parintilor

7.  Este utilziata cu probabilitate mare

8.  Este efectuata iterativ

9.  Este utilizata doar in probleme fara constrangeri

10. Utilizeaza populatia de parinti

<!-- -->

3.  **In cadrul unui algoritm evolutiv populatia initiala**

<!-- -->

1.  Este generata la inceputul fiecarui ciclu evolutiv

2.  Este generata utilizand distributia pe probabilitate normala

3.  Este generata inaintea inceperii evolutiei propriu-zise

4.  Este generata dupa fiecare ciclu evolutiv

5.  [Este generata utilizand distributia de probabilitate
    uniforma]{.mark}

6.  Este generata aleator (Vezi cursul I: Introducere - Slide 11)

7.  Este setata pe multimea vida

<!-- -->

4.  **Fie urmatorii doi cromozomi de tip permutare {6, 3, 11,7, 14, 8,
    5, 15, 1, 2, 4, 13, 9 ,10 ,12 } si {7, 1, 15,13,2,
    14,6,10,12,11,4,8,3,9, 5}. Aplicand operatorul de recombinare PMX,
    cu pozitile 4 si 8 se obtin descendentii.**

<!-- -->

1.  Siruri de numere

> x2 = {13,1,10,7,14,8,5,15,12,11,4,2,3,9,6}
>
> y2 = {5,3,11,13,2,14,6,10,1,8,4,7,9,15,12}

5.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de recombinare:**

<!-- -->

1.  Este de tip local sau global

2.  Este efectuata o singura data pe parcursul unui algoritm

3.  Alege pentru recombinare in medie jumatate de indivizi

4.  Este realizata cu probabilitate mica

5.  Determina structura cromozomiala

6.  Utilizeaza poplatia curenta

7.  Este efectuata o singura data, dupa prima etapa de generare a unei
    populatii

8.  Determina obtinerea unui multiset de copii in ...

9.  Este utilizata doar in probleme cu constrangeri

10. Este efectuata iterativ

<!-- -->

6.  **In cadrul unui algoritm din clasa strategiilor evolutive,
    reprezentarea cromozomilor**

<!-- -->

1.  Influenteaza tipul de recombinare folosit

2.  Se alege in functie de problema care se rezolva

3.  Poate fi numai de tip siruri de numere intregi sau reale

4.  Poate fi oricare dintre: siruri binare, siruri de numere intregi,
    siruri de numere reale, permutari

5.  Are influenta asupra mecanismului de  selectie a generatiei
    urmatoare

6.  Nu influenteaza tipul de mutatie folosit(discreta/ nediscreta)

7.  Poate fi numai de siruri de numere reale

8.  Contine atat descrierea individului candidat cat si parametrii care
    ..

<!-- -->

7.  **In cadrul unui algoritm genetic operatia de selectie a
    parintilor**

<!-- -->

1.  Intotdeauna este bazata pe o distributie de probabilitate de
    selectie

2.  Utilizeaza populatia curenta

3.  Este efectuata o singura data pe parcursul unui algoritm genetic

4.  Este utilizata doar in probleme cu constringeri

5.  Este efectuata imediat inaintea fiecarei proceduri de mutatie

6.  Este efectuata imediat ce este disponibila o populatie curenta
    evaluata

7.  Este efectuata o singura data dupa prima etapa de generare a unei
    populatii

8.  Alege in general indivizi pe baza factorului varsta

9.  Utilizeaza populatia de copii mutati

10. Utilizeaza populatia de copii

11. Este efectuata iterativ

12. Poate fi realizata prin utilizarea unei distributii de probabilitate
    de selectie

<!-- -->

8.  **Fie urmatorul cromozom de tip permutare {7, 6, 12, 14, 3, 10, 8,
    15, 11, 5, 4, 1, 13, 2, 9} In urma aplicarii operatorului de mutatie
    prin amestec s-a obitnut cromozomul {7, 14, 13, 12, 1, 15, 2, 8, 6,
    3, 11, 5, 10, 4, 9 }. Cele doua pozitii utilizate pentru amestesc
    sunt:**

<!-- -->

1.  3 si 13

2.  1 si 15

3.  1 si 14

4.  4 si 8

5.  1 si 12

6.  4 si 15

7.  3 si 15

8.  2 si 13

9.  2 si 14

10. 2 si 15

11. 1 si 13

<!-- -->

9.  **In cadrul unui algoritm genetic operatia de mutatie**

<!-- -->

1.  Are probabilitate mica

2.  Se aplica doar daca divesitatea genetica scade sub un prag x dat

3.  Intotdeauna produce indivizi fezabili

4.  Se aplica asupra descendentilor produsi de operatia de recombinare

5.  Se aplica asupra mutlisetului de parinti

6.  Se aplica asupra populatiei curente

7.  Se utilizeaza doar in probleme cu constrangeri

8.  Poate sa produca indivizi nefezabili

9.  Se efectueaza o singura data, dupa generarea populatiei initiale

10. Se aplica imediat inaintea fiecarei etape de selectie a generatiei
    urmatoare

11. Se utilizeaza doar in problemele fara constrangeri

12. Nu foloseste factori aleatori.

<!-- -->

10. **In cadrul unui algoritm genetic operatia de selectie a
    supravietuitorilor**

<!-- -->

1.  Utilizeaza intotdeauna factori aleatori

2.  In unele variante necesita calcularea unei distributii de
    probabilitate de selectie

3.  Indivizii alesi sunt intotdeauna fezabili

4.  Duce la cresterea calitatii medii a populatiei curente

5.  Se aplica la inceputul fiecarei iteratii

6.  Uneori utilizeaza factori aleatori

7.  Se aplica asupra populatiei curente

8.  Garanteaza obtinerea unei generatii cu calitate medie superioara.
    Daca foloseste selectia bazata pe varsta.

9.  Asigura perpetuarea individului cu calitate maxima din populatia
    curenta

10. Alege generatia urmatoare dintre indivizii disponibili dupa operatia
    de mutatie

11. Se aplica asupra descendentilor obtinuti din populatia curenta

**Partea lll(2019)**

1\. În algoritmii genetici, **reprezentarea prin permutări**

A. Nu permite utilizarea de operatori de recombinare

B. Nu permite utilizarea de operatori de mutație

C. Nu permite mai mult de două gene cu aceeași valoare într-un cromozom

[D. Necesită operatori de variație special definiți]{.mark}

E. Nu este utilizată

2\. Într-un algoritm evolutiv, funcția fitness:

1\. Evaluează calitatea algoritmului;

2\. Trebuie selectată aleator;

3\. Evaluează viteza de găsire a soluției față de consumul de resurse;

4\. Trebuie modificată la fiecare iterație;

5\. Selectează indivizii care se vor reproduce;

6\. Selectează indivizii care trec în generația următoare;

7\. Evaluează calitatea populației curente față de cea a populației
inițiale;

8\. Evaluează calitatea populației curente față de cea din generația
anterioară;

[9. Evaluează calitatea fiecărui candidat.]{.mark}

> A. 1, 3
>
> B. 2,3
>
> [C. 9]{.mark}
>
> D. 4,5
>
> E. 6, 7, 8

3\. Fie X=\[ 6 1 8 10 5 7 9 3 4 2 \] și Y=\[ 9 8 7 3 6 1 5 10 4 2 \]
permutări. Care urmași sunt generați prin utilizarea operatorului CX?

A. C1=\[ 2 6 7 8 10 5 1 9 3 4 \], C2=\[ 2 8 1 3 6 7 5 10 4 9 \]

[B. C1=\[ 6 8 7 10 5 1 9 3 4 2 \], C2=\[ 9 1 8 3 6 7 5 10 4 2 \]]{.mark}

C. C1=\[ 6 7 8 10 5 1 9 3 4 2 \], C2=\[ 9 8 1 3 6 7 5 10 4 2 \]

D. C1=\[ 8 7 10 5 1 9 3 4 2 6 \], C2=\[ 2 9 1 8 3 6 7 5 10 4 \]

4\. Fie următorii doi cromozomi de tip permutare: {6, 3, 11, 7, 14, 8,
5, 15, 1, 2, 4, 13, 9, 10, 12 } și {7, 1, 15, 13, 2, 14, 6, 10, 12, 11,
4, 8, 3, 9, 5}. Aplicand operatorul de recombinare PMX, cu pozițiile 4
și 8 se obțin descendenții:

a\. 5 3 15 13 2 14 6 10 12 8 4 7 9 11 1;

b\. 13 1 11 7 14 8 5 15 12 10 4 2 3 9 6;

c\. 13 12 11 7 14 8 5 15 1 10 4 2 3 9 6;

d\. 5 3 11 13 2 14 6 15 1 8 4 7 9 10 12;

e\. 5 3 15 13 2 14 6 10 1 8 4 7 9 11 12;

f\. 13 12 11 7 14 8 5 15 1 10 4 2 3 9 6;

g\. 13 1 15 7 14 8 5 10 12 11 4 2 3 9 6;

[h. 13 1 10 7 14 8 5 15 12 11 4 2 3 9 6;]{.mark}

[i. 5 3 11 13 2 14 6 10 1 8 4 7 9 15 12.]{.mark}

> A. a, b
>
> B. e, f
>
> C. a, c
>
> [D. h, i]{.mark}
>
> E. f, i

5\. În cadrul unui algoritm **genetic** **operația de selecție a
supraviețuitorilor**:

> 1\. Se aplică asupra populației curente;
>
> [2. În unele variante necesită calcularea unei distribuții de
> probabilitate de selecție;]{.mark}
>
> 3\. Utilizează întotdeauna factori aleatori;
>
> [4. Alege generația următoare dintre indivizii disponibili după
> operația de mutație;]{.mark}
>
> [5. Indivizii aleși sînt întotdeauna fezabili;]{.mark}
>
> [6. Uneori utilizează factori aleatori;]{.mark}
>
> 7\. Asigură perpetuarea individului cu calitate maximă din populația
> curentă;
>
> 8\. Duce la creșterea calității medii a populației curente;
>
> 9\. Garantează obținerea unei generații cu calitate medie superioară,
> dacă folosește selecția bazată pe vîrstă;
>
> 10.Se aplică la începutul fiecărei iterații;
>
> 11\. Se aplică asupra descendenților obținuți din populația curentă;
>
> [12. Se aplică asupra populației curente și asupra descendenților
> obținuți din populația]{.mark} [curentă.]{.mark}
>
> A. 2, 3, 4, 5, 6, 11
>
> B. 4, 8, 11
>
> [C. 2, 4, 5, 6, 12]{.mark}
>
> D. 6,8,11
>
> E.1,7

**Partea lV(2019)**

**1**.In cadrul unui algoritm genetic ce maximizeaza o functie
(fitness):

1.Selectia generatiei urmatoare este obligatoriu bazata pe varsta;

2\. Sunt rezolvate probleme cu constrangeri;

[3. Selectia parintilor este efectuata iterativ;]{.mark}

[4. Mutatia este realizata cu probabilitate mica;]{.mark}

5\. nu este recomandata utilizarea functiei FPS;

6\. multisetul copiilor este fara duplicate.

[7. Selectia supravietuitorilor este determinata de calitate si/sau
factorul varsta;]{.mark}

8\. Recombinarea este realizata rareori;

[9. Este intentionata determinarea unui pct maxim global;]{.mark}

10. Structura cromozomiala difera daca functia este translatata

11. [Se urmareste determianarea unui punct de maxim global]{.mark}

[A. 3,4,7,9]{.mark}

B. 2,3,5,9

C.1,3,5,7

D.4,7,9,10

E.1,2,3,4,7

**2**.In cadrul unui algoritm genetic operatia de **mutatie**:

1\. Nu folosete factori aleatori;

2.Se aplica doar daca diversitatea genetica scade sub un prag dat;

3.Se aplica asupra populatiei curenta;

[4. Poate sa produca indivizi nefezabili;]{.mark}

5\. Intodeauna produce indivizi fezabili;

6\. Se utilizeaza in probleme cu constrangeri;

7\. Se utilizeaza doar in probleme fara constrangeri;

[8. se aplica imediat inaintea fiecarei etape de selectie a generatiei
urmatoare;]{.mark}

9\. Se aplica asupra multisetului de parinti;

[10. Are probabilitatea mica;]{.mark}

11\. Se efectueaza o singura data, dupa generarea populatiei initiale;

[12. Se aplica asupra descendentilor produsi de operatia de
recombinare;]{.mark}

A.3,5,7,12

B.1,4,5,8

C.6,7,8,10,11

D.2,4,5,6,7

[E.4,8,10,12]{.mark}

**3.In cadrul unui algoritm genetic operatia de recombinare:**

1\. Este efectuata o singura data pe parcursul unui algoritm genetic;

[2. este efectuata imediat dupa fiecare etapa de selectie a
parintilor;]{.mark}

3\. In general, probabilitatea de recombinare nu conteaza in rezolvarea
problemelor prin algoritmi genetici

[4. Este efectuata imediat inaintea fiecarei proceduri de
mutatie;]{.mark}

5\. este efectuata inaintea fiecarei etape de selectie a parintilor;

[6. Utilizeaza populatia de parinti;]{.mark}

7\. Este utilizata doar in probleme fara constrangeri;

[8. Este utilizata cu probabilitate mare;]{.mark}

9\. Este utilizata cu probabilitate mica;

[10. Este efectuata iterativ]{.mark}

11\. Este efectuata o singura data, dupa prima etapa de selectie a
parintilor

[A.2,4,6,8,10;]{.mark}

B.2,6,7,8,9;

C.3,4,5,8,9

D.1,3,5,7,9;

E.2,4,5

**4. In cadrul unui algoritm genetic, reprezentarea cromozomilor:**

[1. Poate fi oricare dintre: siruri binare, siruri de numere intregi,
siruri de numere relae,]{.mark} [permutari;]{.mark}

2\. Poate fi numai de tip sir de numere intregi sau reale

3\. poate fi numai tip siruri de numere reale

4.Nu influenteaza tipul de recombinare folosit

[5. Se alege in functie de problema care se rezolva]{.mark}

[6. Influenteaza tipul de recombinare folosit;]{.mark}

> A.1,2,4,5
>
> B.1,3,4,6
>
> C.4,5,6
>
> [D.1,5,6]{.mark}
>
> E.2,4,5

**5. In algoritmii genetici, reprezentarea prin siruri de numere
intregi:**

A. Este preferabila pentru problemele de optimizare

B. Este doar un exercitiu de implementare, nefiind necesara

C. Nu poate si utilizata in cazul atributelor ordinale

[D. E preferabila atunci cand pentru fiecare gena sunt posibile mai mult
de doua valori distincte]{.mark}

E. Nu este utilizata in algoritmi genetici

**6. In cadrul unui algoritm din clasa strategiilor evolutive,
reprezentarea cromozomilor:**

1\. Poate fi oricare dintre : siruri binare, siruri de numere intregi,
siruri de numere reale, permutari

2\. Poate fi numai de tip sir de numere intregi sau reale

[3. poate fi numai tip siruri de numere reale]{.mark}

[4. Nu influenteaza tipul de recombinare
folosit(discreta/intermediara);]{.mark}

5\. Se alege in functie de problema care se rezolva;

6\. Influenteaza tipul de recombinare folosit;

7\. Are influenta asupra mecanismului de selectie a generatiei
urmatoare;

A.1,7; B.1,3,4; C.2,4,5; [D. 3,4;]{.mark} E.2,4,5,6

**7. Componentele algoritmilor evolutivi sunt:**

[1.Reprezentarea]{.mark}

2.Probabilitatea de mutatie

[3.Functia de evaluare]{.mark}

4.Probabilitatea de recombinare

[5.Populatia]{.mark}

6.Generarea de numere aleatoare

[7.Mecanismul de selectie a parintilor]{.mark}

8.Generarea de permutari

9.Reprezentarea grafica a evolutiei calitatii

[10.Operatorii de variatie]{.mark}

11.Stabilirea diversitatii genetice a populatiei

[12. Mecanismul de inlocuire a populatiei curente;]{.mark}

13.Hillclimbing

[14.Initializarea populatiei;]{.mark}

[15.Conditia de terminare]{.mark}

[A.1,3,5,7,10,12,14,15]{.mark}

B.1,3,5,6,10,13,14,15

C.2,4,6,8,11,13

D.1,2,5,6,7,14,15

E.2,4,5,9,15

**8. In cadrul unui algoritm genetic operatia de selectie a
parintilor:**

1\. Este utilizata doar in probleme de constrangeri

2\. Este efectuata o singura data

[3. Este efectuata imediat ce este disponibila]{.mark}

4\. Intodeauna este bazata pe o distributie de probabilitate de selectie

5\. Utilizeaza populatia de copii mutati

[6. Poate fi realizata prin utilizarea unei distributii de probabilitate
de selectie]{.mark}

7\. Utilizeaza populatia de copii

[8. Utilizeaza populatia curenta]{.mark}

9\. este efectuata o singura data pe parcursul unui algoritm genetic

10\. Alege in general indivizi pe baza factorului varsta

11\. Este efectuata imediat inaintea fiecarei proceduri de mutatie

[12. este efectuata iterativ]{.mark}

[A.3,6,8,12;]{.mark} B.3,6,7,8; C.2,5,8,12; D.1,2,4,5; E.4,6,7,8;

**9. Intr-un algoritm evolutiv, functia de tip calitate:**

1\. Evalueaza caliatea algoritmului;

[2. Evaluueaza calitatea fiecarui candidat;]{.mark}

3\. Evalueaza viteza de gasire a solutiei fata de consumul de resurse

[4. Trebuie maximizata]{.mark}

5\. Stabileste daca un descendent este acceptabil

6\. Selecteza indivizii care se vor reproduce

7\. Selecteza indivizii care trec in generatia urmatoare

8\. Contine un factor aleator

9\. Evalueaza calitatea populatiei curente;

10\. Evalueaza caliatea populatie curente fata de cea din generatia
anterioara.

A.5;

B.1,3;

C.6,7,8;

D.9,10;

[E.2,4;]{.mark}

**10. Fie urmatorul cromozom de numere intregi: \....**

B.1,2,3,5?

1.  **Calculul evolutiv este:**

A. Similar metodelor de cautare directa

[B. Tehnica de rezolvare a problemelor este de tip
experiment-eroare]{.mark}

C. Concept ce confirma teoria relativitatii

D. Similar algoritmului de sortare;

E. Concept ce concretizeaza teoria evolutiei;

2.  **In cadrul unui algoritm genetic, operatia de mutatie:**

1\. Este utilizata doar in probleme cu constrangeri

> [2. Este efectuata imediat ce este disponibila o populatie de
> copii]{.mark}

3\. Alege pentru mutatie in medie jumatate din indivizi

4\. Utilizeaza doua multiseturi distincte de copii

5\. Este intodeauna de tip neuniform(fluaj)

6\. Este efectuata o singura data, dupa prima etapa de generare a unei
populatii

7\. Este realizata cu probalilitate 1

8\. Este efectuata o singua data pe parcursul unui algoritm

9\. Utilizeaza populatia curenta

[10. este efectuata iterativ]{.mark}

> [A.2,10]{.mark}
>
> B.3,4,7
>
> C.2,5
>
> D.6,9
>
> E.7,8,10

3.  **Care din urmatorii operatori pot fi utilizati intr-un algoritm
    genetic care foloosete reprezentarea prin siruri de numere reale?**

1.Negarea

2.Negarea fuzzy

3.resetarea pseudo-aleatoare

4.Resetarea determinista;

[5.Mutatia uniforma;]{.mark}

[6.mutatia neuniforma cu distributie fixata;]{.mark}

7.mutatia locala;

8.Interschimbarea;

9.Inserarea

10;Mutatia rapida;

11.Amestecul;

12.Mutatia globala;

13.Inversiunea;

[14.Unipunct]{.mark}

[15.Multi-punct]{.mark}

[16.Uniforma]{.mark}

17.Recombinarea radacinilor;

[18.Aritmetica simpla;]{.mark}

[19.Aritmetica singulara;]{.mark}

[20.Aritmetica totala;]{.mark}

21.Recombinarea sirurilor maxime;

22.Partially mapped crossover;

23.Recombinarea in oridine;

24.Recombinarea muchiilor;

25.recombinarea ciclica

A.1,3,4,7,10,13,16,17,20

B. Toti operatorii de mai sus

C.3,4,5,6,7,12,18,19,21

D.2,7,10,12,17,21

[E.5,6,14,15,16,18,19,20]{.mark}

4.  **Fie urmatorii doi cromozomi de tip
    permutare:{6,3,11,7,14,8,5,15,1,2,4,13,9,10,12}**

**si {7,1,15,13,2,14,6,10,12,11,4,8,3,9,5}. Aplicand operatorul de
recombinare OCX, cu pozitiile 4 si 8 se obtin descententii:**

a\. 5 3 15 13 2 14 6 10 12 8 4 7 9 11 1

b\. 13 1 11 7 14 8 5 15 12 10 4 2 3 9 6

c\. 13 12 11 7 14 8 5 15 1 10 4 2 3 9 6

d\. 5 3 11 13 2 14 6 15 1 8 4 7 9 10 12

e\. 5 3 15 13 2 14 6 10 1 8 4 7 9 11 12

f\. 13 12 11 7 14 8 5 15 1 10 4 2 3 9 6

g\. 13 1 15 7 14 5 10 12 11 4 2 3 9 6

[h. 13 1 10 7 14 8 5 15 12 11 4 2 3 9 6]{.mark}

[i. 5 3 11 13 2 14 6 10 1 8 4 7 9 15 12]{.mark}

j\. 5 3 15 13 2 14 6 10 12 8 4 7 9 11 1

> A. c,d
>
> B. f,i
>
> [C. h,i]{.mark}
>
> D. c,j
>
> E. a,b

**15. Tipurile de probleme care pot fi rezolvate pe baza calculului
evolutiv sunt:**

[1. Probleme de optimizare]{.mark}

2\. Probleme de geometrie.

3\. Prelucrarea datelor de dimensiune mare(big-data)

[4. probleme de modelare]{.mark}

5\. Probleme de validare a datelor

[6. Probleme de simulare]{.mark}

7\. Alocarea dinamica a datelor in memoria calculatorului;

8\. Deplasarea automata a vehiculelor

> A.2,3,4
>
> [B.1,4,6]{.mark}
>
> C.1,3,5,7
>
> D.2,4,6
>
> E.2,4,6,8

**16. In cadrul unui algoritm genetic, conditia de oprire:**

1\. Poate lipsi

[2. Include in general controlul numarului de generatii simulate]{.mark}

3\. Utilizeaza intodeauna factori aleatori

[4. Poate include controlul variabilitatii in cadrul populatiei nou
calculate]{.mark}

5\. Duce la cresterea calitatii medii a populatiei curente

6\. Garanteaza obtinerea unei generatii cu calitate medie superioara,
daca foloseste selectia bazata pe varsta

[7. Nu depinde de reprezentarea cromozomiala]{.mark}

8\. Depinde de reprezentarea cromozomiala

> [A.2,4,7.]{.mark}
>
> B.1,5,8
>
> C.3,5,6
>
> D.2,3,4,5
>
> E.1,4,7,8

**17. Fie permutarile x=\[10 2 3 9 1 7 6 4 8 5\] si y=\[5 4 7 2 1 9 3 6
8 10\], un cromozom copil rezultat prin PMX este c=\[5 2 3 9 1 4 7 6 8
10\]. Atunci ordinea considerarii parintilor si respectiv
[punctele]{.mark} [crossover]{.mark} sunt:**

A.  (x,y) si (1,4)

B.  [(x,y) si (2,5)]{.mark}

C.  (y,x) si (1,4)

D.  (y,x) si (2,5)

E.  (y,x) si (1,5)

**18. In algoritmii genetici, reprezentarea binara:**

A.  Nu e utilizata pentru algoritmii genetici

B.  [Istoric este primul tip de reprezentare in spatiul
    genotipurilor]{.mark}

C.  Este ce mai utilizata varinata de reprezentare a genotipurilor

D.  Duce mereu la rezultate optime

E.  Nu depinde de problema rezolvata

**19. In algoritmii genetici, reprezentarea binara:**

A. Nu permite utilizarea de operatori de recombinare

B. Nu permite utilizarea de operatori de mutatie

[C. Necesita operatori de variatie special definiti]{.mark}

D. nu permite mai mult de doua gene cu aceeasi valoare intr-un cromozom

E. nu este utilizata

**20. Fie urmatorul cromozom de tip permutare {7, 6, 12, 14, 3 10, 8,
15, 11, 5, 4, 1, 13, 2, 9}**

**In urma aplicarii operatorului de mutatie prin amestec s-a obtinut
cromozomul**

**{7, 14, 13, 12, 1, 15, 2,8,6, 3, 11, 5, 10, 4, 9}. Cele doua pozitii
utilizate pentru amestec sunt:**

1.  1 si 14;

2.  4 si 15

3.  3 si 15

4.  4 si 8

5.  2 si 15

6.  1 si 12

7.  2 si 14

8.  2 si 13

9.  1 si 15

10. 1 si 13

11. 3 si 13

<!-- -->

A.  5,10

B.  1,5,7,9

C.  6,7,9

D.  6,2

E.  2

**21. In cadrul unui algoritm genetic operatia de selectie a
supravietuitorilor:**

1\. este intodeauna determinista

[2. Poate fi determinista sau cu factori aleatori]{.mark}

3\. utilizeaza intodeauna factori aleatori

4\. Indivizii alesi nu sunt intodeauna fezabili

5\. Duce la cresterea calitatii medii a populatiei curente

6\. Garanteaza obtinerea unei generatii cu claitate medie superioara,
daca foloseste selectia bazata pe varsta

7\. Se aplica la inceputul fiecarei iteratii

8\. Se aplica asupra descendentilor obtinuti din populatia curenta

[9. este aplicata pentru inlocuirea generatiei curente]{.mark}

A.  4,8

B.  1,6

C.  3,7

D.  2,5

E.  [2,9]{.mark}

**22. In cadrul unui algoritm evolutiv, populatia initiala:**

[1. Este generata inaintea inceperii evolutiei propriu-zise]{.mark}

2\. Este generat dupa fiecare ciclu evolutiv (care presupune efectuarea
operatiilor de selectie, recombinare, mutatie, evaluare)

3\. Este generata la inceputul ficarui ciclu evolutiv

[4. este generata aleator]{.mark}

[5. Este generata utilizand distributia de probabilitate
uniforma]{.mark}

6\. Este generata utilizand distributia de probabilitati

7\. este setata pe multimea vida

A.1,2,3,4,5,6; B. 5,7; C.1,2,4,7; D.2,5,7; [E.1,4,5;]{.mark}

**23. In algoritmii genetici, reprezentarea binara:**

[1. Este eficienta in probleme in care solutia este un vector cu
componente logice]{.mark}

2\. Trebuie folosita in orice GA

3\. Nu trebuie utilizata in GA

4\. Nu poate fi utilizata in probleme de optimizare

[5. Determina ce tip de operatori de variatie trebuie folositi]{.mark}

6\. Impune folosirea selectiei ruleta;

7\. Este eficienta exclusiv in probleme cu restrictii

> [A.1,5]{.mark}
>
> B.1,4,5
>
> C.1,3,5
>
> D.2,3,6
>
> E.2,4,6

**24.Algiritmul Hillclimbing:**

[1. Se aplica asupra unui singur punct din spatiul cautat]{.mark}

[2. Aplicarea se poate repeta pentru mai multe puncte pentru a creste
performantele]{.mark}

3\. Este inspirat din tehnicile de alpinism

4\. Gaseste intodeauna solutia optima

[5. Gaseste uneori solutia optima]{.mark}

6\. Calculele se incheie atunci cand temperatura sistemului devine 0

[7. De obicei gaseste un punct de optim local]{.mark}

8\. Se utilizeaza numai pentru reprezentare cu siruri de numere reale

> A.1,4,6,7
>
> B.3,4,6,8
>
> C.1,2,4,6
>
> D.1,5,7,8
>
> [E.1,2,5,7]{.mark}

**25. In cadrul unui algoritm din clasa strategiilor evolutive,
autoadaptibilitatea se refera la:**

A. Functia fitness

B. Distributia de probabilitate de selectie;

C. Modelul de selectie

[D. Spatiul parametrilor]{.mark}

E. Modelul de selectie al parintilor

**Partea V (2020)**

**1.În cadrul strategiilor evolutive:**

Alegeți o opțiune:

a\. Operatorul de mutație cel mai utilizat este mutația prin
interschimbare

b\. Nu se permite utilizarea de operatori de mutație

c\. Sunt utilizați operatori de recombinare OCX

[d. Mutația este aplicată cu probabilitate 1]{.mark}

e\. Reprezentarea este prin vectori binari

2E-8.5-25.5

Partea I: un singur raspuns corect

1.  Tipurile de probleme care pot fi rezolvate pe baza calcului evolutiv
    sunt:

> Probleme de optimizare (1), Probleme de modelare (4), Probleme de
> simulare (6) -\> 1,4,6 (B).

2.  Care din urmatorii operatori pot fi utilizati intr-un algoritm
    genetic care foloseste reprezentarea prin siruri reale?

> Mutatia uniforma (5), Mutatia neuniforma cu distributie fixata (6),
> Aritmetica simpla (18), Aritmetica singulara (19), Aritmetica totala
> (20), Unipunct (14), Multipunct(15), Uniforma(16) -\> (A)

3.  In algoritmii genetici, reprezentarea prin siruri de numere intregi:

> e preferabila atunci cand pentru fiecare gena sunt posibile mai mult
> de doua valori distincte (D).

4\. In algoritmii genetici, reprezentarea prin permutari: necesita
operatori de variatie special definiti (D). 5. Calculul evolutiv este
inspirat de: evolutia naturala biologica (A).

6\. Algoritmul Hillclimbing: se aplica asupra unui singur punct din
spatiul de cautare (1), Aplicarea de poate repeta pentru mai multe
puncte pentru a creste performantele (2), De obicei gaseste un punct de
optim local (7), Gaseste uneori solutia optima (5) Later edit: nu
gaseste mereu solutia optima.(closed) -- Cezar

7\. In algoritmii genetici, reprezentarea binara: (B) A fost primul tip
de reprezentare a cromozomilor in algoritmii genetici

8\. Caracteristicile unui algoritm genetic clasic: (E)1,3,5,8 --

1.Reprezentarea populatiei este realizata prin intermediul sirurilor
binare, 3.Probabilitatea de selectie a unui individ in multisetul
parintilor este proportionala cu valoarea functiei de evaluare pentru
el; 5. Probabilitatea efectuarii unei mutatii este mica;
8.Probabilitatea efectuarii recombinarii este mare

9\. Intr-un algoritm evolutiv, functia de tip calitate: Evalueaza
calitatea fiecarui candidat (2), Trebuie maximizata(4) (B)

10\. Componentele algoritmilor evolutivi sunt: reprezentarea, functia de
evaluare, populatia, mecanismul de selectare a parintilor, operatorii de
variatie, mecanismul de selectare a membrilor generatiei urmatoare,
definirea modului de initializare(populatia initiala) si definirea
conditiei terminale =\> raspuns corect: (B)

1\. In cadrul unui algoritm din clasa strategiilor evolutive, operatia
de mutatie:

a\. Este utilizata doar in probleme cu constringeri

[b. Este realizata cu probabilitate mica (\*)]{.mark}

c\. Utilizeaza populatia curenta

[d. Utilizeaza populatia de copii (\*)]{.mark}

[e. Determina structura cromozomiala(\*)]{.mark}

[f. Este de tip neuniform (\*)]{.mark}

g\. Alege pentru mutatie in medie jumatate de indivizi

h\. Este efectuata o singura data pe parcursul unui algoritm

i\. Este efectuata iterative(\*)

j\. Este efectuata imediat ce este disponibila o populatie de copii(\*)

2\. In cadrul unui algoritm genetic operatia de recombinare:

a\. Este efectuata o singura data dupa prima etapa de selectie a
parintilor

b\. Este utilizata cu probabilitate mica

c\. In general probabilitatea de recombinare nu conteaza in rezolvarea
problemelor prin algoritmi genetici

d\. Este efectuata o singura data pe parcursul unui algoritm genetic

e\. Este efectuata imediat inaintea fiecare proceduri de mutatie

f[. Este efectuata imediat dupa fiecare etapa de selectie a
parintilor(\*)]{.mark}

g\. [Este utilizata cu probabilitate mare (intre 0.5 si 1, pag.
79)(\*)]{.mark}

h[. Este efectuata iterativ (\*)]{.mark}

i\. Este utilizata doar in probleme fara constrangeri

j[. Utilizeaza populatia de parinti (recombinarea celor doi parinti)
(\*)]{.mark}

3\. In cadrul unui algoritm evolutiv populatia initiala

a\. Este generata la inceputul fiecarui ciclu evolutiv-nu, pentru ca
ciclu evolutiv inseamna fiecare generatie si nu e adevarat.

b\. Este generata utilizand distributia pe probabilitate normala

c\. [Este generata inaintea inceperii evolutiei propriu-zise
(\*)]{.mark}

d\. Este generata dupa fiecare ciclu evolutiv

[e. Este generata utilizant distributia de probabilitate
uniforma(\*)]{.mark}

[f. Este generata aleator (setul initial de candidati este generat
aleator, curs 1) (\*)]{.mark}

g\. Este setata pe multimea vida

4\. Fie urmatorii doi cromozomi de tip permutare {6, 3, 11,7, 14, 8, 5,
15, 1, 2, 4, 13, 9 ,10 ,12 } si {7, 1, 15,13,2, 14,6,10,12,11,4,8,3,9,
5}. Aplicand operatorul de recombinare PMX, cu pozitile 4 si 8 se obtin
descendentii. .

a\. 5 3 15 13 2 14 6 10 12 8 4 7 9 11 1

b\. 5 3 11 13 2 14 6 15 1 8 4 7 9 10 12

c\. 5 3 11 13 2 14 6 15 1 8 4 7 9 15 12 - al doilea copil (\*)

d.13 1 10 7 14 8 5 15 12 11 4 2 3 9 6 - primul copil (\*)

e\. 5 3 15 13 2 14 6 10 1 8 4 7 9 11 12

f\. 13 1 15 7 14 8 5 10 12 11 4 2 3 9 6

g\. 13 12 11 7 14 8 5 15 1 10 4 2 3 9 6

h\. 13 1 11 7 14 8 5 15 12 10 4 2 3 9 6

i\. 13 12 11 7 14 8 5 15 1 10 4 2 3 9 6

j\. 5 3 15 13 2 14 6 10 12 8 4 7 9 11 1

5\. In cadrul unui algoritm din clasa strategiilor evolutive, operatia
de recombinare:

a\. Este de tip local sau global (\*)

b\. Este efectuata o singura data pe parcursul unui algoritm

c\. Alege pentru recombinare in medie jumatate de indivizi

d\. Este realizata cu probabilitate mica

e\. Determina structura cromozomiala

f\. Utilizeaza poplatia curenta (\*)

g\. Este efectuata o singura data, dupa prima etapa de generare a unei
populatii

h\. Determina obtinerea unui multiset de copii in general de dimensiuni
mai mari comparativ cu populatia curenta.(\*)

i\. Este utilizata doar in probleme cu constrangeri

j\. Este efectuata iterative(\*)

6\. In cadrul unui algoritm din clasa strategiilor evolutive,
reprezentarea cromozomilor

a\. Influenteaza tipul de recombinare folosit

b\. Se alege in functie de problema care se rezolva

c\. Poate fi numai de tip siruri de numere intregi sau reale

d\. Poate fi oricare dintre: siruri binare, siruri de numere intregi,
siruri de numere reale, permutari

e\. Are influenta asupra mecanismului de selectie a generatiei urmatoare

f\. Nu influenteaza tipul de mutatie folosit(discreta/ nediscreta) (\*)

g\. Poate fi numai de siruri de numere reale (\*)

h\. Contine atat descrierea individului candidat cat si parametrii care
controleaza evolutia sa. (\*)

7\. In cadrul unui algoritm genetic operatia de selectie a parintilor

a\. Intotdeauna este bazata pe o distributie de probabilitate de
selectie

b\. Utilizeaza populatia curenta (\*)

c\. Este efectuata o singura data pe parcursul unui algoritm genetic

d\. Este utilizata doar in probleme cu constringeri

e\. Este efectuata imediat inaintea fiecarei proceduri de mutatie

f\. Este efectuata imediat ce este disponibila o populatie curenta eva
luata(\*)

g\. Este efectuata o singura data dupa prima etapa de generare a unei
populatii

h\. Alege in general indivizi pe baza factorului varsta

i\. Utilizeaza populatia de copii mutate

j\. Utilizeaza populatia de copii

k\. Este efectuata iterativ (\*)

l\. Poate fi realizata prin utilizarea unei distributii de probabilitate
de selectie(\*)

8\. Fie urmatorul cromozom de tip permutare {7, 6, 12, 14, 3, 10, 8, 15,
11, 5, 4, 1, 13, 2, 9} In urma aplicarii operatorului de mutatie prin
amestec s-a obitnut cromozomul {7, 14, 13, 12, 1, 15, 2, 8, 6, 3, 11, 5,
10, 4, 9 }. Cele doua pozitii utilizate pentru amestesc sunt: 7, 6, 12,
14, 3, 10, 8, 15, 11, 5, 4, 1, 13, 2, 9 7, 14, 13, 12, 1, 15, 2, 8, 6,
3, 11, 5, 10, 4, 9

a\. 3 si 13

b\. 1 si 15 (\*)

c\. 1 si 14 (\*)

d\. 4 si 8

e\. 1 si 12

f\. 4 si 15

g\. 3 si 15

h\. 2 si 13

i\. 2 si 14 (\*)

j\. 2 si 15 (\*)

k\. 1 si 13

9\. In cadrul unui algoritm genetic operatia de mutatie

[a. Are probabilitate mica(\*)]{.mark}

b\. Se aplica doar daca divesitatea genetica scade sub un prag x dat

c\. Intotdeauna produce indivizi fezabili

[d. Se aplica asupra descendentilor produsi de operatia de recombinare
(\*)]{.mark}

e\. Se aplica asupra mutlisetului de parinti

f\. Se aplica asupra populatiei curente

g\. Se utilizeaza doar in probleme cu constrangeri

[h. Poate sa produca indivizi nefezabili (\*)]{.mark}

i\. Se efectueaza o singura data, dupa generarea populatiei initiale
(mutatia se face de mai multe ori; in cazul unui algoritm genetic,
mutatia se face in fiecare era)

j\. Se aplica imediat inaintea fiecarei etape de selectie a generatiei
urmatoare (cred ca dupa mutatie urmeaza evaluare si dupa aceea
selectia.- deci asta nu ar fi)

k\. Se utilizeaza doar in problemele fara constrangeri

l\. Nu foloseste factori aleatori.

10\. In cadrul unui algoritm genetic operatia de seleXCCCCCCSCC

g\. Se aplica asupra populatiei curente si asupra descendentilor
obtinuti(\*)

h\. Garanteaza obtinerea unei generatii cu calitate medie superioara.
Daca foloseste selectia bazata pe varsta. (ASTA ESTE GENITOR, NU VARSTA)

i\. Se aplica asupra descendentilor. Asigura perpetuarea individului cu
calitate maxima din populatia curenta

j\. Alege generatia urmatoare dintre indivizii disponibili dupa operatia
de mutatie (\*)

k\. Se aplica asupra descendentilor obtinuti din populatia curenta

11.In cadrul algoritmilor genetici,generatie urmatoare este selectat
dintre:

R: c.indivizii generatiei curente si descendentii obtinuti dupa etapa de
mutatie

11.Care din urmatoarele nu este un model de distributie de probabilitate
folosit pentru etapa de selectie:

Alegeti o optiune: R:e.FPS cu alfa scalar

12.Care din urmatoarele este un model de populatie?

[Alegeti o optiune: R: c.Cu stari stabile]{.mark}

13.In cadrul algoritmilor genetici,generatia urmatoare este selectata
dintre:

[Alegeti o optiune: a.Indivizii generatiei curente si descendentii
obtinuti dupa etapa de mutatie]{.mark}

13. Mecanismul de selectie turnir:

[Alegeti o optiune:a.Nu respecta distributia de probabilitate de
selectie.]{.mark}

14.Care din urmatoarele afirmatii nu e adevarata pentru modelul
generational?

[Alegeti o optiune:e.Necesita urmarirea mai multor generatii
consecutive(Sau d.Nu tine cont de calitatea cromozomilor)]{.mark}

15.Care din urmatoarele este un dezavantaj al utilizarii distributiei de
probabilitate de selectie tip FPS?

[Alegeti o optiune:c.Convergenta prematur]{.mark}a

16.De cite ori trebuie rotit bratul ruletei simple pentru a executa
intregul proces de selectie a parintilor,pentru o populatie cu tz
cromozomi?

[Alegeti o optiune:d.De tz ori.]{.mark}

17.Care din urmatoarele nu este un mecanism de selectie?

[Alegeti o optiune:a.Ruleta complicata]{.mark}

18.De cite ori trebuie rotit bratul ruletei multi-brat pentru a execut
intregul proces de selectie a parintilor,pentru o populatie cu k
indivizi?

[Alegeti o optiune:b.O data]{.mark}

19.Care mecanism de selectie produce rezultate mai apropiate de
distributia de probabilitate de selectie calculate?

[Alegeti o optiune:R. b.SUS(Stochastic Universal )]{.mark}

20.Care din urmatoarele este un model de populatie?

[Alegeti o optiune:a.Cu generatii c.Cu stari stabile]{.mark}

22.Componentele algoritmilor evolutivi
sunt:1.Reprezentarea;2.Probabilitatea de mutatie;3.Functia de
evaluare;4.Probabilitatea de recombinare;5.Populatia;6.Generarea de
numere aleatoare;7.Mecanismul de selectie a parintilor;8.Generarea de
permutari;9.Reprezentarea grafica a evolutiei calitatii;10.Operatii de
variatie;11.Stabilirea diversitatii genetice a populatiei;12.Mecanismul
de inlocuire a populatiei curente;13.Hillclimbing;14.Initializarea
populatie;15.Conditia de terminare;

Raspuns:1,3,5,7,10,12,14,15

23.Intr-un algoritm evolutiv,functia de tip calitate:1.Evalueaza
calitatea algoritmului,2.Evalueaza calitatea fiecarui
candidat,3.Evalueaza viteza de gasire a solutiei fata de consumul de
resurse,4.Trebuie maximizata;5.Stabileste daca un descendent este
acceptabil;6.Selecteaza indivizii care se vor reproduce;7.Selecteaza
indivizii care trec in generatia urmatoare;8.Contine un factor
aleatory;9.Evalueaza calitatea populatiei curente;10.Evalueaza calitatea
populatiei curente fata de cea din generatia anterioara;

R:2,4

24.In cadrul unui algoritm genetic operatia de selectie a parintilor:

[R.Este efectuata iterative,Utilizeaza populatia curenta,Este efectuata
imediat ce este disponibila o populatie curenta evaluate,Poate fi
realizata prin utilizarea unei distributii de probabilitate de
selectie.]{.mark}

25.Fie urmatorii doi cromozomi de tip permutare:
{6,3,11,7,14,8,5,15,1,2,4,13,9,10,12} si
{7,1,15,13,2,14,6,10,12,11,4,8,3,9,5}.Aplicind operatorul de recombinare
PMX,cu pozitiile 4 si 8 se obtin descendentii:

R:h,i

26.Fie X=\[6 1 8 10 5 7 9 3 4 2\] si Y=\[ 9 8 7 3 6 1 5 10 4 2\]
permutari.Care urmasi sint generate prin utilizarea operatorului CX?

R: C1=\[ 6 8 7 10 5 1 9 3 4 2 \] , C2=\[ 9 1 8 3 6 7 5 10 4 2 \]

27\. Calculul evolutiv este inspirit din:

R: Evolutia naturala biologica.

28.In cadrul unui algoritm genetic operatia de selectie a
supravietuitorilor:

R[: Se aplica populatiei curente,Indivizii alesi sunt intotdeauna
fezabili,Uneori utilizeaza factori aleatori,In unele variante necesita
calcularea unei distributii de probabilitate de selectie,Se aplica
asupra descendentilor obtinuti din populatia curenta.]{.mark}

28.Care din urmatorii operatori pot fi utilizati intr-un algoritm
genetic care foloseste reprezentarea prin siruri de numere
reale:1.Negarea;2.Negarea Fuzzy;3.Resetarea aleatoare;4.Fluaj;5.Mutatia
uniforma;6.Mutatia neuniforma;7.Mutatia
locala;8.Interschimbarea;9.Inserarea;10.Mutatia
Rapida;11.Amestecu;12.Mutatia
globala;13.Inversiunea;14.Unipunct;15.Multipunct;16.Uniforma;17.Recombinarea
radacinilor;18.Aritmetica simpla;19.Aritmetica singular;20.Aritmetica
totala;21.Recombinarea sirurilor maxima;22.PMC;23.Recombinare de
ordine;24.Recombinarea muchiilor;25.Recombinarea Ciclica.

R:5,6,14,15,16,18,19,20

29.Caracteristicile unui algoritm genetic classic(canonic)
sunt:1.Reprezentarea populatiei este realizata prin intermediul sirului
binare;2.Reprezentarea populatiei este realizata prin intermediul
sirurilor de numere natural;3.Probabilitatea de selectie a unui indiv in
multisetul parintilor este proportional cu valoarea functiei de evaluare
pentru el;4.Probabilitatea de selectie a unui individ in multisetul
parintilor este data de pozitia individului in erahiei
populatiei,determinate pe baza functiei de evaluare;5.Probabilitatea
efectuarii unei mutatii este mica;6.Probabilitatea efectuarii unei
mutatii este mare;7.Probabilitatea efectuarii recombinarii este
mica;8.Probabilitatea efectuarii recombinarii este mare;9.Inlocuirea
populatiei curente se face pe baza de varsta.

R:1,3,5,8

30.In cadrul unui algoritm evolutiv populatia initiala:

[R:Este generate aleatory,Este generate inaintea inceperii evolutiei
propriu-zise, Este generate utilizand distribuita de prob
uniforma]{.mark}

31.In algoritmii genetici,reprezentarea prin siruri de numere intregi:

R:E [preferabila atunci cand pentru fiecare gen sunt posibile mai mult
de doua valori distincte.]{.mark}

32.In cadrul unui algoritm din clasa strategiilor
evolutive,reprezentarea cromozilor:

R:Poate fi numai de siruri de numere reale,Nu influenteaza tipul de
mutatie folosit(discrete/nediscreta),Contine atat descrierea individului
candidat cat si prim parametrii care...

33.In cadrul unui algoritm din clasa strategiilor evolutive,operatia de
recombinare:

R:Este efectiv iterative,Determina obtinerea unui multiset de copii
in...,Utilizeaza populatia curenta,Este de tip loca sau global.

34.In cadrul unui algoritm operatia de selectie a
supravietuitorilor:1.Se aplica asupra populatiei curente;2.In unele
variante necesita calcularea unei distributii de probabilitate de
selectie;3.Utilizeaza intotdeauna factori aleatory;4.Alege generatia
urmatoare dintre indivizii disponibili dupa operatia de
mutatie;5.Indivizii alesi sint intotdeauna fezabili;6.Uneori utilizeaza
factori aleatory;7.Asigura perpetuarea individului cu calitate maxima
din populatia curenta;8.Duce la cresterea calitatii medii a populatiei
curente;9.Garanteaza obtinerea unei generatii cu calitate medie
superioara,daca foloseste selectia bazata pe virsta;10.Se aplica la
inceputul fiecari iteratii;11.Se aplica descendentilor obtinuti prin
populatia curenta;12.Se aplica asupra populatiei curente si asupra
descendentilor obtinuti din populatia curenta.

R:2,4,5,6,12

35.Fie urmatorul cromozom de tip permutare
{7,6,12,14,3,10,8,15,11,5,4,1,13,2,9} In urma aplicarii operatorului de
mutatie prin amestec s-a obtinut cromozomul
{7,14,13,12,1,15,2,8,6,3,11,5,10,4,9}.Cele doua pozitii utilizate pentru
amestesc sunt:

R:2 si 14,1 si 14 , 2 si 15 , 1 si 15 .

36.In algoritmii genetici,reprezentarea binara:

R:A fost primul tip de reprezentare a cromomilor in algoritmi genetici

37.Tipuri de problem care pot fi rezolvate pe baza calcului evolutiv
sint:1.Probleme de optimizare;2.Probleme de cautare in spatial
solutilor;3.Prelucrarea datelor de dimensiune mare(big-data);4.Probleme
de modelare;5.Probleme de validare a datelor;6.Probleme de
simulare;7.Alocarea dinamica a datelor in memoria
calculatorului;8.Deplasarea autonoma a vehiculelor

R:1,4,6

38.Intru-un algoritm evolutiv,functia fitness;1.Evalueaza calitatea
algoritmului;2.Trebuie selectata aleatory;3.Evalueaza viteza de gasire a
solutiei fata de consumul de resurse;4.Trebuie modificata la fiecare
iteratie;5.Selecteaza indivizii care se vor reproduce;6.Selecteaza
indivizii care trec in generatia urmatoare;7.Evalueaza calitatea
populatiei curente fata de cea a populatiei initiale;8.Evalueaza
calitatea populatiei curente fata de cea din generatia
anterioara;9.Evalueaza calitatea fiecarui candidat:

R:9.

39.In algoritmii genetici,reprezentarea prin permutari

R:Necesita operatori de variatie special definiti

40.In cadrul unui algoritm genetic operatia de mutatie:

R:Se aplica descendentilor produsi operatia de recombinare,Poate sa
produca indivizi nefezabili,

Are probabilitate mica

41.In algoritmii genetici,reprezentarea prin permutari:

R:Are nevoie de operatori special definiti

41.Algoritmul Hillclimbing:1.Se aplica asupra unui singur punct din
spatial de cautare;2.Aplicarea se poate repeat pentru mai multe puncta
pentru a creste performantele;3.Este inspirit din tehniciile de
alpinism;4.Gasesti intotdeauna Solutia optima;5.Gaseste uneori Solutia
optima;6.Calculele se incheie atunci cand temperature sistemului devine
0;7.De obicei un punct de optim local;8.Se utilizeaza numai pentru
reprezentarea cu siruri de numere reale.

R:1,2,5,7

42.In cadrul unui algoritm din clasa strategiilor evolutive,operatia de
mutatie:

[R:Este efectuata imediat ce este disponibila populatia de copii,Este
efectuata iterative,Este de tip neuniform,Determina structura
cromozomiala]{.mark}

43.Pt pastrarea relatiilor commune din cromozomii parinti se foloseste
operatorul de recombinare.

R: E C X (Edge Crossover)

44.Care din urm deste un dezavantaj al utilizarii distributiei de
probabilitate de selectie tip FPS?

R:Convergenta premature

45.Schema generale de recombinare depinde de:

R:a)existent constrangerilor cu probleme de rezolvat

46.Care din urma f nu e adevarata pentru modelul generational?

[R:Necesita urmarirea mai multor generatii cunoscute.]{.mark}

47.Daca aplicarea unui operator de recombinare produce indivizi aberanti
atunci:

[R:se folosesc parinti ca descendenti.]{.mark}

48.Mecanismul de selectie turnir:

[R:Nu respecta distributia de probabilitate de selectie.]{.mark}

49.In cadrul algoritmilor genetiei,generatia urmatoare este selectata
dintre:

[R:Indivizii generatiei curente si descendenti obtinuti dupa etapa de
mutatie.]{.mark}

50.De cate ori trebuie rolul bratul ruletei simple pentru a executa
intregul process de selectie a parintilor,pt o populatiei cu cromozomi?

[R:De tz ori]{.mark}

51.Pentru problemele in care reprezentarea prin permutari semnif.
Ordinea de aparitie a unor evenimente,operatorul de recombinare folosit
este:

[R:OCX(Order Crossover)]{.mark}

52.De cate ori trb rotit bratul ruletei multi-brat pt a executa intregul
process de selectie a parintilor,pt o populatie cu K indivizi

R:b)O data

53.Care din urmatoarele nu este un model de distributie de probabilitate
folosit pt etapa de selectie

R:FPS cu alfa scalare

54.In cazul reprezentarii cu siruri de nr intregi,recombinarile
aritmetice:

[R:d)se pot aplica desc se face rotunjirea rezultatelor.]{.mark}

55.Operatorul de recombinare unipunct se poate folosi in cazul reprez
prin:

[R:e)siruri de nr intregi,siruri de nr. Reale,siruri binari.]{.mark}

56.Care dintre urmatoarele nu este un model de distributie de
probabiliate folosit pentru etapa de selectie:

a.FPS

b.Ranguri liniare

c.FPS cu ferestre

d.FPS cu sigma scalare

[e.Fps cu alfa scalare]{.mark}

57.Care dintre urmatoarele afirmatii nu e adevarata pentru modelul
generational?

a.Poate inlocui complet generatia curenta

b.Nu tine cont de calitatea cromozomilor

c.Poate inlocui partial generatia curenta

d.Poate inlocui un singur cromozom din populatia curenta

[e.Necesita urmarirea mai multor generatii consecutive]{.mark}

58.Pentru a pastra cat mai bine info. Referitoare la .... Absolute ale
datelor in cromozomii parinti se foloseste operatorul: [CX]{.mark}

59.Pentru problemele cu dependenta de adiacenta se foloseste operatorul
de recombinare:

[PMX]{.mark}

60.In cadrul unui algoritm evolutive conditia de terminare:[1.Este
obligatorie]{.mark};2.Nu este indicate;[3.Include obligatoriu,direct sau
indirect, controlul numarului de interatii;]{.mark}4.Nu poate fi
implementata;5.Este utilizata doar in cadrul GA, nu si in cadrul ES.

61.Algoritmii genetici:

a.Utilizeaza la fiecare moment de timp o varianta de solutie...

[b.Sunt tehnici de cautare stohastica bazate pe populatii]{.mark}

c.Folosesc exclusiv selectii determinisiste

d.Sunt metode deterministe de cautare in spatiul solutiilor

e.Rezolva exclusiv probleme definite de spatii continue

62.In algoritmii genetici, alegerea unei anumite reprezentari:

a.Este independenta de problema de rezolvat

[bDepinde de problema rezolvata;]{.mark}

c.Poate fi facuta aleator

d.Este imposibila,fiind folosita doar reprezentarea prin numere reale

[e.Influenteaza calitatea solutiei furnizate]{.mark}

63.Algoritmul ES2M:

a.Nu este un algotim auto-adaptiv

b.Nu este un algoritm evloutiv

c.Nici una din celelalte varinate

d.Este un algoritm determinist

[e.Este un algoritm auto-adaptiv primar]{.mark}

64.In cadrul strategiei evolutive cu 2 membri(ES-2M): 1.Este generata o
populatie intiala aleator, din distributia normala;[2.La fiecare moment
al evolutiei algoritmului este mentinut un singur candidat la
solutie]{.mark};3.Populatiile sunt de dimenisiuni mari;[4.Calculul unui
termen nou este realizat prin mutatie gaussiana pentru fiecare
componenta a vectorului curent;5.Sunt rezolvate probleme pe spatii
continue;6.Fiecare termen este calculate in maniera stohastica]{.mark};
7.Calculul unui termen nou este realizat prin mutatie gaussiana pentru o
componenta selectata aleatory din vectorul current;8.Este intentionata
cresterea calitatii medii a populatiei curente;9.Este garntata obtinerea
unui optim global;10.La inceputul fiecarei interatii este testata
dimensiunea populatiei curente; 11.Sunt create descendenti obtinuti din
populatia curenta prin recombinare locala

R:2,4,5,6

65.In algoritmii genetici, operatia de selectie a parintilor:

[a.Este utilizata in general in maniera nedeterminista]{.mark}

b.Este doar un exercitiu de implementare,nefiind necesara

c.Nu este utilizata

d.Este utilizata determinist

e.Este utilizata in functie de reprezentarea cromozimiala

66.Intr-un algoritm evolutive, functia de evaluare:

[R:estimeaza nivelul de adaptare a individului]{.mark}

67.Fie X=\[6 1 8 10 5 7 12 43 9 3 4 2\] o secventa de numere intregi.In
urma aplicarii mutatiei fluaj poate fi obtinuta urmatoarea varianta
mutata : r: 2 4 5 6

R:\[6 1 8 10 5 7 12 43 9 4 3 2\];

\[7 1 8 10 5 7 12 43 9 3 4 2\];

\[6 1 8 10 5 7 12 43 9 4 3 2\]

\[6 1 8 10 5 7 12 43 9 4 3 2\]

68.Algoritmii genetici:

[e.Sunt tehnici de cautare stohastica bazate pe populatii]{.mark}

68.Care dintre urmatoarele metode pot fi folosite in cadrul algoritmilor
memetici pentru a imbunatati informatia in interiorul unei
populatii:1.recursivitate [2.hillclimbing]{.mark}, 3.divide et impera;
[4.startegie evolutive cu 2 membri;]{.mark} 5.backtracking[; 6.metode
exacte; 7.metode euristice]{.mark}; 8.validarea datelor;[9.metoda
gradientului]{.mark};10.ECX

R:2,4,6,7,9

69.Fie perumtari x=\[10 2 3 9 1 7 6 4 8 5\] si y=\[5 4 7 2 1 9 3 6 8
10\], un cromozom copil rezultat prin PMX este c=\[5 2 3 9 1 4 7 6 8
10\].Atunci ordinea considerarii parintilor si respective punctelor de
incrucisare sunt:

[(x,y) (2,5)]{.mark}

70\. .Fie X=\[6 1 8 10 5 7 12 43 9 3 4 2\] o permutare. In urma
aplicarii muatiei prin inversiune pentru pozitiile(2,7) poate fi
obtinuta urmatoarea varianta mutata: Y: 1.Y=\[2 6 7 8 10 15 5 1 9 3
4[\], 2.y=\[6 9 7 5 10 8 1 3 4 2\];]{.mark}3. y=\[7 6 8 10 5 1 9 3 4 2
\];4. Y=\[6 7 10 8 5 9 1 3 4 2\];5. Y=\[6 8 7 5 10 1 9 3 4 2\];6.Y=\[6 2
8 10 5 1 9 3 4 7\]

[b.2]{.mark}

71.Decodificarea trebuie realizata:

[Obligatoriu dupa extragerea celui mai bun individ din populatia
finala]{.mark}

72\. Fie X=\[6 1 8 10 5 7 12 43 9 3 4 2\] o permutare.In urma aplicarii
mutatiei prin amestesc pentru pozitiile(2,7) poate fi obtinuta
urmatoarea varianta mutata:

[Y=\[6 7 8 10 5 1 9 3 4 2\]]{.mark}

[Y=\[6 7 10 8 5 9 1 3 4 2\]]{.mark}

[Y=\[6 9 7 5 10 8 1 3 4 2\]]{.mark}

73.Fie urmatorii doi cromozomi de tip permutare:{6,3,7,8,5,1,2,4,9}
si{7,2,8,5,6,9,4,1,3}.Aplicand opertaorul de recombinare PMX, cu
pozitiile 3 si 6 se obtin decendetii:

[d.6,2,7,8,5,1,4,9,3]{.mark}

[h.7,3,8,5,6,9,2,4,1]{.mark}

74.Intr-un algoritm genetic, populatia initiala:2,5,7

[2.Este construita o singura data]{.mark}

[5.Contine exclusive indivizi fezabili]{.mark}

[7.Este genearata uitlizand distributia de probabilitate
uniforma]{.mark}

75.Algoritmul ES2M:

[Este algoritm auto-adaptiv prima]{.mark}
