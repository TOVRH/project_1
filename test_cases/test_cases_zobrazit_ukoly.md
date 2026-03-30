# TC01: Zobrazení prázdného seznamu úkolů

**Popis:** Ověření, že systém správně informuje uživatele při zobrazení seznamu bez uložených úkolů  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky testu:**
1. Zadej `2` a potvrď Enter  

**Očekávaný výsledek:** Program zobrazí hlášku "Seznam úkolů je prázdný."  
**Skutečný výsledek:** Program zobrazil hlášku "Seznam úkolů je prázdný."  
**Stav:** Pass  
**Poznámky:** Test ověřuje správnou hlášku při prázdném seznamu úkolů  

---

# TC02: Zobrazení seznamu po přidání jednoho úkolu

**Popis:** Ověření, že se po přidání jednoho úkolu správně zobrazí jeho název a popis  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky testu:**
1. Zadej `1` a potvrď Enter  
2. Zadej název úkolu `Úkol 1` a potvrď Enter  
3. Zadej popis úkolu `Popis 1` a potvrď Enter  
4. Zadej `2` a potvrď Enter  

**Očekávaný výsledek:**  
Program zobrazí:  
Seznam úkolů:  
1. Úkol 1 - Popis 1  

**Skutečný výsledek:** Program zobrazil seznam úkolů  
**Stav:** Pass  
**Poznámky:** Test ověřuje správné zobrazení jednoho úkolu v seznamu  

---

# TC03: Zobrazení seznamu po přidání více úkolů

**Popis:** Ověření, že systém správně zobrazí více úkolů v seznamu ve správném pořadí  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky testu:**
1. Zadej `1` a potvrď Enter  
2. Zadej název úkolu `Úkol 1` a potvrď Enter  
3. Zadej popis úkolu `Popis 1` a potvrď Enter  
4. Zadej `1` a potvrď Enter  
5. Zadej název úkolu `Úkol 2` a potvrď Enter  
6. Zadej popis úkolu `Popis 2` a potvrď Enter  
7. Zadej `2` a potvrď Enter  

**Očekávaný výsledek:**  
Program zobrazí:  
Seznam úkolů:  
1. Úkol 1 - Popis 1  
2. Úkol 2 - Popis 2  

**Skutečný výsledek:** Program zobrazil seznam úkolů  
**Stav:** Pass  
**Poznámky:** Test ověřuje zobrazení více úkolů v seznamu  

---

# TC04: Zobrazení úkolů se speciálními znaky

**Popis:** Ověření, že systém správně zobrazí úkoly obsahující speciální znaky v názvu i popisu  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky testu:**
1. Zadej `1` a potvrď Enter  
2. Zadej název úkolu `Úkol #&@` a potvrď Enter  
3. Zadej popis úkolu `Popis #&@` a potvrď Enter  
4. Zadej `2` a potvrď Enter  

**Očekávaný výsledek:**  
Program zobrazí:  
Seznam úkolů:  
1. Úkol #&@ - Popis #&@  

**Skutečný výsledek:** Program zobrazil seznam úkolů a správně zobrazil speciální znaky  
**Stav:** Pass  
**Poznámky:** Test ověřuje práci se speciálními znaky ve výstupu  

---

# TC05: Zobrazení úkolu s velmi dlouhým názvem a popisem

**Popis:** Ověření, že systém správně zobrazí úkol s velmi dlouhým textem bez oříznutí nebo chyb  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky testu:**
1. Zadej `1` a potvrď Enter  
2. Zadej název úkolu `aaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAA` a potvrď Enter  
3. Zadej popis úkolu `aaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAA` a potvrď Enter  
4. Zadej `2` a potvrď Enter  

**Očekávaný výsledek:**  
Program zobrazí:  
Seznam úkolů:  
1. aaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAA - aaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAA  

**Skutečný výsledek:** Program zobrazil seznam úkolů bez jakékoliv změny textu  
**Stav:** Pass  
**Poznámky:** Test ověřuje práci s velmi dlouhými vstupy bez ořezání nebo chyb  