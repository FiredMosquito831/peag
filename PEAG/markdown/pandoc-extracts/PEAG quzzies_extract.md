**CAP. 1**

1.  În cadrul algoritmilor evolutivi, scopul evoluției este:

> a\. Obținerea unor indivizi mai bine adaptați mediului

2.  În modelul clasic de rezolvare a problemelor, cele trei elemente
    sînt: datele de intrare, modelul de transformare, datele de ieșire.
    Care din următoarele nu este o clasă de probleme:

> b\. Probleme de echilibrare: se cunoaște doar modelul de transformare

3.  Care din următoarele etape ale algoritmilor evolutivi se pot
    desfășura și în mod determinist:

> e\. Selecția generației următoare

4.  Scenariul utilizat simularea proceselor evolutive în cadrul
    algoritmilor evolutivi este:

> c\. Mediu cu resurse limitate, care se mențin la un nivel constant

5.  Care dintre următoarele nu este un element standard al algoritmilor
    evolutivi:

> c\. Resuscitarea

**CAP. 2**

1.  Pentru a garanta obținerea soluției optime, în cadrul algoritmului
    hillclimbing:

> b\. Nu se poate garanta obținerea soluției optime

2.  Care din următoarele afirmații este incorectă:

> **a. Individul evoluează pentru a se adapta mediului (asta e
> corectă)**
>
> b\. Dimensiunea populației trebuie să fie fixă
>
> c\. Operatorii de selecție acționează asupra populației
>
> d\. Populația evoluează pentru a se adapta mediului
>
> e\. Individul este un element static, nu evoluează

3.  În cadrul algoritmului hillclimbing, modul de alegere a punctelor
    vecin luate în considerare: a. influențează calitatea rezultatului
    obținut

4.  Care dintre următoarele nu sînt elemente ale unui algoritm
    evolutiv: 1) reprezentarea, 2) includerea bibliotecilor, 3)
    stabilirea datelor de intrare, 4) funcția de evaluare, 5)
    populația, 6) implementarea, 7) mecanismul de selecție a
    părinților, 8) operatorul de recombinare, 9) sortarea populației
    după calitate, 10) operatorul de mutație, 11) mecanismul de selecție
    a generației următoare, 12) condiția de terminare, 13) extragerea
    celui mai bun individ, 14) lansarea în execuție? d. 2, 3, 6, 9, 13,
    14

5.  În cadrul algoritmului hillclimbing, evoluția de la un punct
    inițial: e. Duce la un punct de extrem (maxim) care poate fi local
    sau global pe domeniul de lucru

6.  în cadrul unui cromozom, o „genă" desemnează: e. Poziția unui
    element din cromozom

**CAP. 3**

1.  Reprezentarea cu șiruri binare în cadrul algoritmilor genetici:

> a\. este naturală pentru problemele a căror soluție reprezintă un șir
> de decizii booleene

2.  Care din următoarele tipuri de reprezentare a indivizilor nu este
    utilizată de algoritmii genetici: d. reprezentarea arborescentă

3.  Care din următoarele nu este element specific algoritmului genetic
    canonic: a. reprezentarea cu șiruri de numere reale; b. utilizarea
    operației de recombinare cu probabilitate mică; c. utilizarea
    operației de mutație cu probabilitate mare; d. selecția celor mai
    buni indivizi pentru a forma generația următoare e. nici unul dintre
    elementele numite nu este specific algoritmului genetic canonic

4.  Tipurile de relații între elementele reprezentate prin șiruri de
    numere reale pot fi: e. ordinale sau cardinale

5.  Alegerea reprezentării pentru rezolvarea unei probleme prin
    intermediul unui algoritm genetic: a. trebuie să țină cont de
    eventualele constrîngeri ale problemei; b. depinde de problema
    rezolvată, unele reprezentări fiind mai potrivite decît altele; c.
    uneori este dificilă; **d. toate celelalte răspunsuri sînt
    corecte**; e. este o etapă obligatorie, foarte importantă.

6.  Care dintre următorii nu este operator de mutație pentru
    reprezentarea prin permutări: e. mutație uniformă

7.  Algoritmul genetic canonic: c. este algoritmul genetic clasic,
    propus de Holland

**CAP. 4**

1.  Ce aritate are operatorul de recombinare în algoritmii genetici
    (cîți operanzi utilizează)?

> a\. binar (doi operanzi)

2.  Pentru problemele în care reprezentarea prin permutări semnifică
    ordinea de apariție a unor evenimente, operatorul de recombinare
    folosit este:

> b\. OCX (Order crossover)

3.  Pentru păstrarea relațiilor comune din cromozomii părinți se
    folosește operatorul de recombinare:

> e\. ECX (Edge crossover) Corect

4.  Operatorul de recombinare unipunct se poate folosi în cazul
    reprezentării prin:

> b\. șiruri de numere întregi, șiruri de numere reale, șiruri binare

5.  în cazul reprezentării cu șiruri de numere întregi, recombinările
    aritmetice:

> b\. se pot aplica dacă se face rotunjirea rezultatelor

6.  Dacă aplicarea unui operator de recombinare produce indivizi
    aberanți atunci: a. se folosesc părinții ca descendenți

7.  Pentru problemele cu dependență de adiacențe se folosește operatorul
    de recombinare: a. PMX (Partially Mapped crossover)

8.  Schema generală de recombinare depinde de: c. existența
    constrîngerilor în problema de rezolvat

9.  Recombinarea multiplă: a. produce rezultate mai bune doar în unele
    cazuri particulare

10. Pentru a păstra cît mai bine informația referitoare la pozițiile
    absolute ale alelelor în cromozomii părinți se folosește
    operatorul: e. CX (Cycle crossover)

**CAP. 5**

1.  Care din următoarele afirmații nu e adevărată pentru modelul
    generațional?

> a\. Nu ține cont de calitatea cromozomilor
>
> b\. Poate înlocui parțial generația ciuentă
>
> c\. Poate înlocui complet generația curentă
>
> d\. Poate înlocui un singur cromozom din populația curentă
>
> e\. Necesită urmărirea mai multor generații consecutive **(CORECT)**

2.  Care din următoarele nu este un mecanism de selecție?

> a\. Ruletă simplă
>
> b\. Turnir
>
> c\. Ruletă complicată **Corect**
>
> d\. Ruletă multi-braț
>
> e\. Genitor

3.  Care din următoarele este un dezavantaj al utilizării distribuției
    de probabilitate de selecție tip FPS?

> **b. Convergența prematură**

4.  În cadrul algoritmilor genetici, generația următoare este selectată
    dintre: d. Indvizii generației curente și descendenții obținuți după
    etapa de mutație

5.  Mecanismul de selecție turnir: c. Nu respectă distribuția de
    probabilitate de selecție

6.  Care din următoarele nu este un model de distribuție de
    probabilitate folosit pentru etapa de selecție:

> a\. FPS cu sigma scalare
>
> **b. FPS cu alfa scalare Corect**
>
> c\. Ranguri liniare
>
> d\. FPS
>
> e\. FPS cu ferestre

7.  De cîte ori trebuie rotit brațul ruletei simple pentru a executa
    întregul proces de selecție a părinților, pentru o populație cu tz
    cromozomi? **e. De tz ori**

8.  Care mecanism de selecție produce rezultate mai apropiate de
    distribuția de probabilitate de selecție calculată? **a. SUS
    (Stochastic Universal Sampling)**

9.  De cîte ori trebuie rotit brațul ruletei multi-braț pentru a execut
    întregul proces de selecție a părinților, pentru o populație cu k
    indivizi? **b. O dată**

10. Care din urmatoarele este un model de populație? **b. Cu stări
    stabile**

**DE LA MIHA:**

**Partea I:**

1.  În algoritmii genetici, **rerezentarea prin șiruri de numere
    întregi**

<!-- -->

1.  Este preferabila pentru probleme de optimizare

2.  Este doar un exercitiu de implementare, nefiind necesara

3.  [E preferabila atunci cand pentru fiecare gena sunt posibile mai
    mult de doua valori distincte]{.mark}

4.  nu este utilizata in algoritmi genetici

5.  Nu poate fi utilizata in cazul atributelor ordinale

<!-- -->

2.  In algoritmii genetici, **reprezentarea prin permutări**

<!-- -->

1.  Nu permite utilizarea de operatori de mutatie

2.  Nu este utilizata

3.  [Are nevoie de operatori special definiti **(Vezi cursul II: - Slide
    19)**]{.mark}

4.  Nu permite utilizarea de operatori de recombinare

5.  Nu permite mai mult de doua gene cu aceeasi valoare intr-un cromozom

<!-- -->

3.  **Tipurile de probleme care pot fi rezolvate pe baza calculului
    evolutiv **sînt: [1. Problemele de optimizare]{.mark}; 2.Probleme de
    cautare in spatiul solutilor; 3. Prelucrarea datelor de dimensiune
    mare(big-data); 4. [Probleme de modelare;]{.mark} 5.Probleme de
    validare a datelor; [6. Probleme de simulare;]{.mark} 7 Alocarea
    dinamica a datelor in memoria calculatorului; 8. Deplasarea autonoma
    a vechiculelor

<!-- -->

1.  2,4,6

2.  [1,4,6**(Vezi cursul I: Introducere: - Slide 9 si 10)**]{.mark}

3.  2,4,6,8

4.  1,3,5,7

5.  2,3,4

<!-- -->

4.  **Intr-un algoritm evolutiv**, functia de tip calitate: 1. Evalueaza
    calitatea algoritmului, [2. Evalueaza calitatea fiecarui
    candidat]{.mark}; 3. Evalueaza viteza de gasire a solutiei fata de
    consumul de resurse; [4. Trebuie maximizata]{.mark}; 5. Stabileste
    daca un descendent este acceptabil; 6. Selecteaza indivizii care se
    vor reproduce; 7. Selecteaza indivizii care trec in generatia
    urmatoare; 8. Contine un factor aleator; 9. Evalueaza calitatea
    populatiei curente; 10. Evalueaza calitatea populatiei curente fata
    de cea din generatia anterioara;

<!-- -->

1.  6,7,8

2.  5

3.  [2,4**(Vezi cursul I: Introducere - Slide 11)**]{.mark}

4.  1,3

5.  9,10

<!-- -->

5.  **In algoritmii genetici, reprezentarea binara**

<!-- -->

1.  Este cea mai utilizata varianta de reprezentare a genotipurilor

2.  Nu e utilizata pentru algoritmi genetici

3.  [A fost primul tip de reprezentare a cromozomilor in algoritmi
    genetici**(Vezi cursul 2: Slide 14)**]{.mark}

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

2.  [1,3,5,7,10,12,14,15]{.mark}

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

5.  [Evolutia naturala biologica**(Vezi cursul I: Introducere - Slide
    6)**]{.mark}

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

1.  [1,2,5,7]{.mark}

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

3.  [1,3,5,8(Speram, doamne ajuta)]{.mark}

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

5.  [5,6,14,15,16,18,19,20]{.mark}

**Partea II:**

1.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de mutatie:**

<!-- -->

1.  Este utilizata doar in probleme cu constringeri

2.  Este realizata cu probabilitate mica

3.  Utilizeaza populatia curenta

4.  [Utilizeaza populatia de copii]{.mark}

5.  Determina structura cromozomiala

6.  [Este de tip neuniform]{.mark}

7.  Alege pentru mutatie in medie jumatate de indivizi

8.  Este efectuata o singura data pe parcursul unui algoritm

9.  [Este efectuata iterativ]{.mark}

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

5.  [Este efectuata imediat inaintea fiecare proceduri de
    mutatie]{.mark}

6.  [Este efectuata imediat dupa fiecare etapa de selectie a
    parintilor]{.mark}

7.  [Este utilziata cu probabilitate mare]{.mark}

8.  [Este efectuata iterativ]{.mark}

9.  Este utilizata doar in probleme fara constrangeri

10. [Utilizeaza populatia de parinti]{.mark}

<!-- -->

3.  **In cadrul unui algoritm evolutiv populatia initiala**

<!-- -->

1.  Este generata la inceputul fiecarui ciclu evolutiv

2.  Este generata utilizand distributia pe probabilitate normala

3.  [Este generata inaintea inceperii evolutiei propriu-zise]{.mark}

4.  Este generata dupa fiecare ciclu evolutiv

5.  Este generata utilizand distributia de probabilitate uniforma

6.  [Este generata aleator (Vezi cursul I: Introducere - Slide
    11)]{.mark}

7.  Este setata pe multimea vida

<!-- -->

4.  **Fie urmatorii doi cromozomi de tip permutare {6, 3, 11,7, 14, 8,
    5, 15, 1, 2, 4, 13, 9 ,10 ,12 } si {7, 1, 15,13,2,
    14,6,10,12,11,4,8,3,9, 5}. Aplicand operatorul de recombinare PMX,
    cu pozitile 4 si 8 se obtin descendentii.**

<!-- -->

1.  Siruri de numere

> [x2 = {13,1,10,7,14,8,5,15,12,11,4,2,3,9,6}]{.mark}
>
> [y2 = {5,3,11,13,2,14,6,10,1,8,4,7,9,15,12}]{.mark}

5.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia
    de recombinare:**

<!-- -->

1.  [Este de tip local sau global]{.mark}

2.  Este efectuata o singura data pe parcursul unui algoritm

3.  Alege pentru recombinare in medie jumatate de indivizi

4.  Este realizata cu probabilitate mica

5.  Determina structura cromozomiala

6.  [Utilizeaza poplatia curenta]{.mark}

7.  Este efectuata o singura data, dupa prima etapa de generare a unei
    populatii

8.  [Determina obtinerea unui multiset de copii in ...]{.mark}

9.  Este utilizata doar in probleme cu constrangeri

10. [Este efectuata iterativ]{.mark}

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

6.  [Nu influenteaza tipul de mutatie folosit(discreta/
    nediscreta)]{.mark}

7.  [Poate fi numai de siruri de numere reale]{.mark}

8.  [Contine atat descrierea individului candidat cat si parametrii care
    ..]{.mark}

<!-- -->

7.  **In cadrul unui algoritm genetic operatia de selectie a
    parintilor**

<!-- -->

1.  Intotdeauna este bazata pe o distributie de probabilitate de
    selectie

2.  [Utilizeaza populatia curenta]{.mark}

3.  Este efectuata o singura data pe parcursul unui algoritm genetic

4.  Este utilizata doar in probleme cu constringeri

5.  Este efectuata imediat inaintea fiecarei proceduri de mutatie

6.  [Este efectuata imediat ce este disponibila o populatie curenta
    evaluata]{.mark}

7.  Este efectuata o singura data dupa prima etapa de generare a unei
    populatii

8.  Alege in general indivizi pe baza factorului varsta

9.  Utilizeaza populatia de copii mutati

10. Utilizeaza populatia de copii

11. [Este efectuata iterativ]{.mark}

12. [Poate fi realizata prin utilizarea unei distributii de
    probabilitate de selectie]{.mark}

<!-- -->

8.  **Fie urmatorul cromozom de tip permutare {7, 6, 12, 14, 3, 10, 8,
    15, 11, 5, 4, 1, 13, 2, 9} In urma aplicarii operatorului de mutatie
    prin amestec s-a obitnut cromozomul {7, 14, 13, 12, 1, 15, 2, 8, 6,
    3, 11, 5, 10, 4, 9 }. Cele doua pozitii utilizate pentru amestesc
    sunt:**

<!-- -->

1.  3 si 13

2.  [1 si 15]{.mark}

3.  [1 si 14]{.mark}

4.  4 si 8

5.  1 si 12

6.  4 si 15

7.  3 si 15

8.  2 si 13

9.  [2 si 14]{.mark}

10. [2 si 15]{.mark}

11. 1 si 13

<!-- -->

9.  **In cadrul unui algoritm genetic operatia de mutatie**

<!-- -->

1.  [Are probabilitate mica]{.mark}

2.  Se aplica doar daca divesitatea genetica scade sub un prag x dat

3.  Intotdeauna produce indivizi fezabili

4.  [Se aplica asupra descendentilor produsi de operatia de
    recombinare]{.mark}

5.  Se aplica asupra mutlisetului de parinti

6.  Se aplica asupra populatiei curente

7.  Se utilizeaza doar in probleme cu constrangeri

8.  [Poate sa produca indivizi nefezabili]{.mark}

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

2.  [In unele variante necesita calcularea unei distributii de
    probabilitate de selectie]{.mark}

3.  [Indivizii alesi sunt intotdeauna fezabili]{.mark}

4.  Duce la cresterea calitatii medii a populatiei curente

5.  Se aplica la inceputul fiecarei iteratii

6.  [Uneori utilizeaza factori aleatori]{.mark}

7.  [Se aplica asupra populatiei curente]{.mark}

8.  Garanteaza obtinerea unei generatii cu calitate medie superioara.
    Daca foloseste selectia bazata pe varsta.

9.  Asigura perpetuarea individului cu calitate maxima din populatia
    curenta

10. Alege generatia urmatoare dintre indivizii disponibili dupa operatia
    de mutatie

11. [Se aplica asupra descendentilor obtinuti din populatia
    curenta]{.mark}
