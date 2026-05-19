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
