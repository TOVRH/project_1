# TC01: Odstranění úkolu a kontrola integrity seznamu

**Popis:** Ověření, že po smazání jednoho z více úkolů zůstane seznam konzistentní a obsahuje pouze nesmazané položky se správným pořadím  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky:**
1. Zadej `1` a potvrď Enter  
2. Zadej název úkolu `Úkol 1` a potvrď Enter  
3. Zadej popis úkolu `Popis 1` a potvrď Enter  
4. Zadej `1` a potvrď Enter  
5. Zadej název úkolu `Úkol 2` a potvrď Enter  
6. Zadej popis úkolu `Popis 2` a potvrď Enter  
7. Zadej `3` a potvrď Enter  
8. Zadej `2` a potvrď Enter (odstranění druhého úkolu)  
9. Zadej `2` a potvrď Enter  

**Očekávaný výsledek:**  
Seznam úkolů obsahuje pouze nesmazaný úkol:  
> 1. Úkol 1 - Popis 1  

**Skutečný výsledek:**  
Seznam úkolů zobrazil pouze nesmazaný úkol  

**Stav:** Pass  

**Poznámky:**  
Test ověřuje odstranění úkolu a správné číslování zbylého seznamu  

---

# TC02: Vyprázdnění seznamu po odstranění všech úkolů

**Popis:** Ověření, že po smazání všech existujících úkolů systém správně zobrazuje prázdný seznam  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky:**
1. Zadej `1` a potvrď Enter  
2. Zadej název úkolu `Úkol 1` a potvrď Enter  
3. Zadej popis úkolu `Popis 1` a potvrď Enter  
4. Zadej `3` a potvrď Enter  
5. Zadej `1` a potvrď Enter (smazání úkolu)  
6. Zadej `2` a potvrď Enter  

**Očekávaný výsledek:**  
Zobrazí se hláška:  
> "Seznam úkolů je prázdný."  

**Skutečný výsledek:**  
Program zobrazil hlášku "Seznam úkolů je prázdný."  

**Stav:** Pass  

**Poznámky:**  
Test ověřuje, že se po smazání všech úkolů seznam správně vyprázdní  

---

# TC03: Ověření odstranění úkolu u prázdného seznamu

**Popis:** Ověření chování systému při pokusu o odstranění úkolu, když seznam neobsahuje žádné položky  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky:**
1. Zadej `3` a potvrď Enter  

**Očekávaný výsledek:**  
Zobrazí se hláška:  
> "Seznam úkolů je prázdný."  

**Skutečný výsledek:**  
Program zobrazil hlášku "Seznam úkolů je prázdný."  

**Stav:** Pass  

**Poznámky:**  
Test ověřuje správné chování při pokusu o odstranění z prázdného seznamu  

---

# TC04: Ošetření pokusu o smazání neexistujícího úkolu

**Popis:** Ověření, že systém správně reaguje na pokus o smazání neexistujícího úkolu
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky:**
1. Zadej `1` a potvrď Enter  
2. Zadej název úkolu `Úkol 1` a potvrď Enter  
3. Zadej popis úkolu `Popis 1` a potvrď Enter  
4. Zadej `3` a potvrď Enter  
5. Zadej `2` a potvrď Enter  

**Očekávaný výsledek:**  
Zobrazí se hláška:  
> "Zadané číslo úkolu neexistuje, zkuste to znovu."  
a program vyzve k zadání nového čísla úkolu  

**Skutečný výsledek:**  
Hláška se zobrazila a program vyzval k zadání nového čísla úkolu  

**Stav:** Pass  

**Poznámky:**  
Test ověřuje správnou validaci neexistujícího indexu úkolu  

---

# TC05: Validace nečíselného vstupu při výběru úkolu

**Popis:** Ověření, že systém odmítne nečíselný vstup při výběru úkolu k odstranění a vyzve uživatele k novému zadání  
**Předpoklady:** Program zobrazuje hlavní menu a obsahuje alespoň jeden úkol  

**Kroky:**
1. Zadej `1` a potvrď Enter  
2. Zadej název úkolu `Úkol 1` a potvrď Enter  
3. Zadej popis úkolu `Popis 1` a potvrď Enter  
4. Zadej `3` a potvrď Enter  
5. Zadej `abc` a potvrď Enter  

**Očekávaný výsledek:**  
Zobrazí se chybová hláška:  
> "Zadejte platné číslo."  
a program vyzve k opětovnému zadání  

**Skutečný výsledek:**  
Program zobrazil chybovou hlášku a vyzval k zadání nového vstupu  

**Stav:** Pass  

**Poznámky:**  
Test ověřuje validaci nečíselného vstupu při pokusu o odstranění úkolu 