**CAP. 1**

1.  În cadrul algoritmilor evolutivi, scopul evoluției este:

a. Obținerea unor indivizi mai bine adaptați mediului

1.  În modelul clasic de rezolvare a problemelor, cele trei elemente sînt: datele de intrare, modelul de transformare, datele de ieșire. Care din următoarele nu este o clasă de probleme:

b. Probleme de echilibrare: se cunoaște doar modelul de transformare

1.  Care din următoarele etape ale algoritmilor evolutivi se pot desfășura și în mod determinist:

e. Selecția generației următoare

1.  Scenariul utilizat simularea proceselor evolutive în cadrul algoritmilor evolutivi este:

c. Mediu cu resurse limitate, care se mențin la un nivel constant

1.  Care dintre următoarele nu este un element standard al algoritmilor evolutivi:

c. Resuscitarea

**CAP. 2**

1.  Pentru a garanta obținerea soluției optime, în cadrul algoritmului hillclimbing:

b. Nu se poate garanta obținerea soluției optime

1.  Care din următoarele afirmații este incorectă:

**a. Individul evoluează pentru a se adapta mediului (asta e corectă)**

b. Dimensiunea populației trebuie să fie fixă

c. Operatorii de selecție acționează asupra populației

d. Populația evoluează pentru a se adapta mediului

e. Individul este un element static, nu evoluează

1.  În cadrul algoritmului hillclimbing, modul de alegere a punctelor vecin luate în considerare: a. influențează calitatea rezultatului obținut
2.  Care dintre următoarele nu sînt elemente ale unui algoritm evolutiv: 1) reprezentarea, 2) includerea bibliotecilor, 3) stabilirea datelor de intrare, 4) funcția de evaluare, 5) populația, 6) implementarea, 7) mecanismul de selecție a părinților, 8) operatorul de recombinare, 9) sortarea populației după calitate, 10) operatorul de mutație, 11) mecanismul de selecție a generației următoare, 12) condiția de terminare, 13) extragerea celui mai bun individ, 14) lansarea în execuție? d. 2, 3, 6, 9, 13, 14
3.  În cadrul algoritmului hillclimbing, evoluția de la un punct inițial: e. Duce la un punct de extrem (maxim) care poate fi local sau global pe domeniul de lucru
4.  în cadrul unui cromozom, o „genă” desemnează: e. Poziția unui element din cromozom

**CAP. 3**

1.  Reprezentarea cu șiruri binare în cadrul algoritmilor genetici:

a. este naturală pentru problemele a căror soluție reprezintă un șir de decizii booleene

1.  Care din următoarele tipuri de reprezentare a indivizilor nu este utilizată de algoritmii genetici: d. reprezentarea arborescentă
2.  Care din următoarele nu este element specific algoritmului genetic canonic: a. reprezentarea cu șiruri de numere reale; b. utilizarea operației de recombinare cu probabilitate mică; c. utilizarea operației de mutație cu probabilitate mare; d. selecția celor mai buni indivizi pentru a forma generația următoare e. nici unul dintre elementele numite nu este specific algoritmului genetic canonic
3.  Tipurile de relații între elementele reprezentate prin șiruri de numere reale pot fi: e. ordinale sau cardinale
4.  Alegerea reprezentării pentru rezolvarea unei probleme prin intermediul unui algoritm genetic: a. trebuie să țină cont de eventualele constrîngeri ale problemei; b. depinde de problema rezolvată, unele reprezentări fiind mai potrivite decît altele; c. uneori este dificilă; **d. toate celelalte răspunsuri sînt corecte**; e. este o etapă obligatorie, foarte importantă.
5.  Care dintre următorii nu este operator de mutație pentru reprezentarea prin permutări: e. mutație uniformă
6.  Algoritmul genetic canonic: c. este algoritmul genetic clasic, propus de Holland

**CAP. 4**

1.  Ce aritate are operatorul de recombinare în algoritmii genetici (cîți operanzi utilizează)?

a. binar (doi operanzi)

1.  Pentru problemele în care reprezentarea prin permutări semnifică ordinea de apariție a unor evenimente, operatorul de recombinare folosit este:

b. OCX (Order crossover)

1.  Pentru păstrarea relațiilor comune din cromozomii părinți se folosește operatorul de recombinare:

e. ECX (Edge crossover) Corect

1.  Operatorul de recombinare unipunct se poate folosi în cazul reprezentării prin:

b. șiruri de numere întregi, șiruri de numere reale, șiruri binare

1.  în cazul reprezentării cu șiruri de numere întregi, recombinările aritmetice:

b. se pot aplica dacă se face rotunjirea rezultatelor

1.  Dacă aplicarea unui operator de recombinare produce indivizi aberanți atunci: a. se folosesc părinții ca descendenți
2.  Pentru problemele cu dependență de adiacențe se folosește operatorul de recombinare: a. PMX (Partially Mapped crossover)
3.  Schema generală de recombinare depinde de: c. existența constrîngerilor în problema de rezolvat
4.  Recombinarea multiplă: a. produce rezultate mai bune doar în unele cazuri particulare
5.  Pentru a păstra cît mai bine informația referitoare la pozițiile absolute ale alelelor în cromozomii părinți se folosește operatorul: e. CX (Cycle crossover)

**CAP. 5**

1.  Care din următoarele afirmații nu e adevărată pentru modelul generațional?

a. Nu ține cont de calitatea cromozomilor

b. Poate înlocui parțial generația ciuentă

c. Poate înlocui complet generația curentă

d. Poate înlocui un singur cromozom din populația curentă

e. Necesită urmărirea mai multor generații consecutive **(CORECT)**

1.  Care din următoarele nu este un mecanism de selecție?

a. Ruletă simplă

b. Turnir

c. Ruletă complicată **Corect**

d. Ruletă multi-braț

e. Genitor

1.  Care din următoarele este un dezavantaj al utilizării distribuției de probabilitate de selecție tip FPS?

**b. Convergența prematură**

1.  În cadrul algoritmilor genetici, generația următoare este selectată dintre: d. Indvizii generației curente și descendenții obținuți după etapa de mutație
2.  Mecanismul de selecție turnir: c. Nu respectă distribuția de probabilitate de selecție
3.  Care din următoarele nu este un model de distribuție de probabilitate folosit pentru etapa de selecție:

a. FPS cu sigma scalare

**b. FPS cu alfa scalare Corect**

c. Ranguri liniare

d. FPS

e. FPS cu ferestre

1.  De cîte ori trebuie rotit brațul ruletei simple pentru a executa întregul proces de selecție a părinților, pentru o populație cu tz cromozomi? **e. De tz ori**
2.  Care mecanism de selecție produce rezultate mai apropiate de distribuția de probabilitate de selecție calculată? **a. SUS (Stochastic Universal Sampling)**
3.  De cîte ori trebuie rotit brațul ruletei multi-braț pentru a execut întregul proces de selecție a părinților, pentru o populație cu k indivizi? **b. O dată**
4.  Care din urmatoarele este un model de populație? **b. Cu stări stabile**

**DE LA MIHA:**

**Partea I:**

1.  În algoritmii genetici, **rerezentarea prin șiruri de numere întregi**
2.  Este preferabila pentru probleme de optimizare
3.  Este doar un exercitiu de implementare, nefiind necesara
4.  E preferabila atunci cand pentru fiecare gena sunt posibile mai mult de doua valori distincte
5.  nu este utilizata in algoritmi genetici
6.  Nu poate fi utilizata in cazul atributelor ordinale
7.  In algoritmii genetici, **reprezentarea prin permutări**
8.  Nu permite utilizarea de operatori de mutatie
9.  Nu este utilizata
10. Are nevoie de operatori special definiti **(Vezi cursul II: - Slide 19)**
11. Nu permite utilizarea de operatori de recombinare
12. Nu permite mai mult de doua gene cu aceeasi valoare intr-un cromozom
13. **Tipurile de probleme care pot fi rezolvate pe baza calculului evolutiv** sînt: 1. Problemele de optimizare; 2.Probleme de cautare in spatiul solutilor; 3. Prelucrarea datelor de dimensiune mare(big-data); 4. Probleme de modelare; 5.Probleme de validare a datelor; 6. Probleme de simulare; 7 Alocarea dinamica a datelor in memoria calculatorului; 8. Deplasarea autonoma a vechiculelor
14. 2,4,6
15. 1,4,6**(Vezi cursul I: Introducere: - Slide 9 si 10)**
16. 2,4,6,8
17. 1,3,5,7
18. 2,3,4
19. **Intr-un algoritm evolutiv**, functia de tip calitate: 1. Evalueaza calitatea algoritmului, 2. Evalueaza calitatea fiecarui candidat; 3. Evalueaza viteza de gasire a solutiei fata de consumul de resurse; 4. Trebuie maximizata; 5. Stabileste daca un descendent este acceptabil; 6. Selecteaza indivizii care se vor reproduce; 7. Selecteaza indivizii care trec in generatia urmatoare; 8. Contine un factor aleator; 9. Evalueaza calitatea populatiei curente; 10. Evalueaza calitatea populatiei curente fata de cea din generatia anterioara;
20. 6,7,8
21. 5
22. 2,4**(Vezi cursul I: Introducere - Slide 11)**
23. 1,3
24. 9,10
25. **In algoritmii genetici, reprezentarea binara**
26. Este cea mai utilizata varianta de reprezentare a genotipurilor
27. Nu e utilizata pentru algoritmi genetici
28. A fost primul tip de reprezentare a cromozomilor in algoritmi genetici**(Vezi cursul 2: Slide 14)**
29. Duce mereu la rezultate optime
30. Nu depinde de problema rezolvata
31. **Componentele algoritmilor evolutivi sunt:** 1\. Reprezentarea; 2. Probabilitatea de mutatie; 3. Functia de evaluare; 4. Probabilitatea de recombinare; 5. Populatia; 6. Generarea de numere aleatoare; 7. Mecanismul de selectie a parintilor; 8. Generarea de permutari; 9. Reprezentarea grafica a evolutiei calitatii; 10; Operatorii de variatie; 11. Stabilirea diversitatii genetice a populatiei; 12. Mecanismul de inlocuire a populatiei curente; 13. Hillclimbing; 14; Initializarea populatiei; 15. Conditia de terminare;
32. 1,2,5,6,7,14,15
33. 1,3,5,7,10,12,14,15
34. 2,4,6,8,11,13
35. 2,4,5,9,15
36. 1,3,5,6,10,13,14,15
37. **Calculul evolutiv este inspirat din**
38. Revolutia industriata
39. Societatea cunoasterii
40. Societatea informationala
41. Noua revolutie agrara
42. Evolutia naturala biologica**(Vezi cursul I: Introducere - Slide 6)**
43. **Algoritmul Hillclimbing**: 1. Se aplica asupra unui singur punct din spatiul de cautare; 2. Aplicarea se poate repeta pentru mai multe puncte pentru a creste performantele; 3. Este inspirat din tehnicilie de alpinism; 4. Gaseste intotdeauna solutia optima; 5. Gaseste uneori solutia optima; 6. Calculele se incheie atunci cand temperatura sistemului devine 0; 7. De obicei gaseste un punct de optim local; 8. Se utilizeaza numai pentru reprezentarea cu siruri de numere reale;
44. 1,2,5,7
45. 1,5,7,8
46. 1,2,4,7
47. 1,4,6,7
48. 3,4,6,8
49. **Caracteristicile unui algoritm genetic clasic(canonic) sunt**: 1. Reprezentarea populatiei este realizata prin intermediul sirurilor binare; 2. Reprezentarea populatiei este realizata prin intermediul sirurilor de numere naturale; 3. Probabilitatea de selectie a unui individ in multisetul parintilor este proportionala cu valoarea functiei de evaluare pentu el; 4. Probabilitatea de selectie a unui individ in multisetul parintilor este data de pozitia individului in erarhia populatiei, determinata pe baza functiei de evaluare; 5. Probabilitatea efectuarii unei mutatii este mica; 6. Probabilitatea efectuarii unei mutatii este mare; 7. Probabilitatea efectuarii recombinarii este mica; 8. Probabilitatea efectuarii recombinarii este mare; 9. Inlocuirea populatiei curente se face pe baza de varsta.
50. Nu exista algoritm genetic canonic
51. 2,4,6,7
52. 1,3,5,8(Speram, doamne ajuta)
53. Nici una din variantele A,B,C,E
54. 2,3,6,7,9
55. **Care din urmatorii operatori** pot fi utilizati intr-un algoritm genetic care foloseste reprezentarea prin siruri de numere reale: 1. Negarea; 2. Negarea Fuzzy; 3. Resetarea aleatoare; 4. Fluaj; 5. Mutatia uniforma; 6. Mutatia neuniforma cu distributie fixata; 7. Mutatia locala; 8. Interschimbarea; 9. Inserarea; 10. Mutatia Rapida; 11. Amestecu; 12. Mutatia globala; 13. Inversiunea; 14. Unipunct; 15; Multipunct; 16. Uniforma; 17. Recombinarea radacinilor; 18; Aritmetica simpla; 19. Aritmetica singulara; 20 Aritmetica totala; 21. Recombinarea sirurilor maxima; 22. PMC; 23. Recombinare de ordine; 24. Recombinarea muchilor; 25. Recombinarea Ciclica
56. Toti operatorii de mai sus
57. 2,7,10,12,17,21
58. 1,3,4,7,10,13,16,17,20
59. 3,4,5,6,7,12,18,19,21
60. 5,6,14,15,16,18,19,20

**Partea II:**

1.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia de mutatie:**
2.  Este utilizata doar in probleme cu constringeri
3.  Este realizata cu probabilitate mica
4.  Utilizeaza populatia curenta
5.  Utilizeaza populatia de copii
6.  Determina structura cromozomiala
7.  Este de tip neuniform
8.  Alege pentru mutatie in medie jumatate de indivizi
9.  Este efectuata o singura data pe parcursul unui algoritm
10. Este efectuata iterativ
11. Este efectuata imediat ce este disponibila o populatie de copii
12. **In cadrul unui algoritm genetic operatia de recombinare:**
13. Este efectuata o singura data dupa prima etapa de selectie a parintilor
14. Este utilizata cu probabilitate mica
15. In general probabilitatea de recombinare nu conteaza in rezolvarea problemelor prin algoritmi genetici
16. Este efectuata o singura data pe parcursul unui algoritm genetic
17. Este efectuata imediat inaintea fiecare proceduri de mutatie
18. Este efectuata imediat dupa fiecare etapa de selectie a parintilor
19. Este utilziata cu probabilitate mare
20. Este efectuata iterativ
21. Este utilizata doar in probleme fara constrangeri
22. Utilizeaza populatia de parinti
23. **In cadrul unui algoritm evolutiv populatia initiala**
24. Este generata la inceputul fiecarui ciclu evolutiv
25. Este generata utilizand distributia pe probabilitate normala
26. Este generata inaintea inceperii evolutiei propriu-zise
27. Este generata dupa fiecare ciclu evolutiv
28. Este generata utilizand distributia de probabilitate uniforma
29. Este generata aleator (Vezi cursul I: Introducere - Slide 11)
30. Este setata pe multimea vida
31. **Fie urmatorii doi cromozomi de tip permutare {6, 3, 11,7, 14, 8, 5, 15, 1, 2, 4, 13, 9 ,10 ,12 } si {7, 1, 15,13,2, 14,6,10,12,11,4,8,3,9, 5}. Aplicand operatorul de recombinare PMX, cu pozitile 4 si 8 se obtin descendentii.**
32. Siruri de numere

x2 = {13,1,10,7,14,8,5,15,12,11,4,2,3,9,6}

y2 = {5,3,11,13,2,14,6,10,1,8,4,7,9,15,12}

1.  **In cadrul unui algoritm din clasa strategiilor evolutive, operatia de recombinare:**
2.  Este de tip local sau global
3.  Este efectuata o singura data pe parcursul unui algoritm
4.  Alege pentru recombinare in medie jumatate de indivizi
5.  Este realizata cu probabilitate mica
6.  Determina structura cromozomiala
7.  Utilizeaza poplatia curenta
8.  Este efectuata o singura data, dupa prima etapa de generare a unei populatii
9.  Determina obtinerea unui multiset de copii in …
10. Este utilizata doar in probleme cu constrangeri
11. Este efectuata iterativ
12. **In cadrul unui algoritm din clasa strategiilor evolutive, reprezentarea cromozomilor**
13. Influenteaza tipul de recombinare folosit
14. Se alege in functie de problema care se rezolva
15. Poate fi numai de tip siruri de numere intregi sau reale
16. Poate fi oricare dintre: siruri binare, siruri de numere intregi, siruri de numere reale, permutari
17. Are influenta asupra mecanismului de  selectie a generatiei urmatoare
18. Nu influenteaza tipul de mutatie folosit(discreta/ nediscreta)
19. Poate fi numai de siruri de numere reale
20. Contine atat descrierea individului candidat cat si parametrii care ..
21. **In cadrul unui algoritm genetic operatia de selectie a parintilor**
22. Intotdeauna este bazata pe o distributie de probabilitate de selectie
23. Utilizeaza populatia curenta
24. Este efectuata o singura data pe parcursul unui algoritm genetic
25. Este utilizata doar in probleme cu constringeri
26. Este efectuata imediat inaintea fiecarei proceduri de mutatie
27. Este efectuata imediat ce este disponibila o populatie curenta evaluata
28. Este efectuata o singura data dupa prima etapa de generare a unei populatii
29. Alege in general indivizi pe baza factorului varsta
30. Utilizeaza populatia de copii mutati
31. Utilizeaza populatia de copii
32. Este efectuata iterativ
33. Poate fi realizata prin utilizarea unei distributii de probabilitate de selectie
34. **Fie urmatorul cromozom de tip permutare {7, 6, 12, 14, 3, 10, 8, 15, 11, 5, 4, 1, 13, 2, 9} In urma aplicarii operatorului de mutatie prin amestec s-a obitnut cromozomul {7, 14, 13, 12, 1, 15, 2, 8, 6, 3, 11, 5, 10, 4, 9 }. Cele doua pozitii utilizate pentru amestesc sunt:**
35. 3 si 13
36. 1 si 15
37. 1 si 14
38. 4 si 8
39. 1 si 12
40. 4 si 15
41. 3 si 15
42. 2 si 13
43. 2 si 14
44. 2 si 15
45. 1 si 13
46. **In cadrul unui algoritm genetic operatia de mutatie**
47. Are probabilitate mica
48. Se aplica doar daca divesitatea genetica scade sub un prag x dat
49. Intotdeauna produce indivizi fezabili
50. Se aplica asupra descendentilor produsi de operatia de recombinare
51. Se aplica asupra mutlisetului de parinti
52. Se aplica asupra populatiei curente
53. Se utilizeaza doar in probleme cu constrangeri
54. Poate sa produca indivizi nefezabili
55. Se efectueaza o singura data, dupa generarea populatiei initiale
56. Se aplica imediat inaintea fiecarei etape de selectie a generatiei urmatoare
57. Se utilizeaza doar in problemele fara constrangeri
58. Nu foloseste factori aleatori.
59. **In cadrul unui algoritm genetic operatia de selectie a supravietuitorilor**
60. Utilizeaza intotdeauna factori aleatori
61. In unele variante necesita calcularea unei distributii de probabilitate de selectie
62. Indivizii alesi sunt intotdeauna fezabili
63. Duce la cresterea calitatii medii a populatiei curente
64. Se aplica la inceputul fiecarei iteratii
65. Uneori utilizeaza factori aleatori
66. Se aplica asupra populatiei curente
67. Garanteaza obtinerea unei generatii cu calitate medie superioara. Daca foloseste selectia bazata pe varsta.
68. Asigura perpetuarea individului cu calitate maxima din populatia curenta
69. Alege generatia urmatoare dintre indivizii disponibili dupa operatia de mutatie
70. Se aplica asupra descendentilor obtinuti din populatia curenta