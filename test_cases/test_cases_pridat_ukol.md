# TC01: Vytvoření úkolu s platným názvem a popisem

**Popis:** Ověření, že je možné úspěšně vytvořit úkol při zadání validního názvu i popisu  
**Předpoklady:** Uživatel je ve funkci Přidat nový úkol  

**Kroky testu:**
1. Zadej název úkolu `Úkol 1` a stiskni Enter  
2. Zadej popis úkolu `Popis 1` a stiskni Enter  

**Očekávaný výsledek:** Zobrazí se hláška "Úkol 'Úkol 1' byl přidán."  
**Skutečný výsledek:** Zobrazila se hláška "Úkol 'Úkol 1' byl přidán."  
**Stav:** Pass  
**Poznámky:** Ověření funkce přidání úkolu s platným názvem a popisem  

---

# TC02: Přidání prázdného názvu úkolu

**Popis:** Ověření, že systém neumožní vytvoření úkolu bez zadání názvu  
**Předpoklady:** Uživatel je ve funkci Přidat nový úkol  

**Kroky testu:**
1. Stiskni Enter  

**Očekávaný výsledek:** Zobrazí se hláška "Název úkolu nesmí být prázdný.", program vyzve k zadání nového názvu úkolu  
**Skutečný výsledek:** Zobrazila se hláška "Název úkolu nesmí být prázdný.", program vyzval k zadání nového názvu úkolu  
**Stav:** Pass  
**Poznámky:** Test validace prázdného názvu  

---

# TC03: Přidání prázdného popisu úkolu

**Popis:** Ověření, že systém neumožní vytvoření úkolu bez zadání popisu  
**Předpoklady:** Uživatel je ve funkci Přidat nový úkol  

**Kroky testu:**
1. Zadej název úkolu `Úkol 1` a stiskni Enter  
2. Stiskni Enter  

**Očekávaný výsledek:** Objeví se hláška "Popis úkolu nesmí být prázdný.", program vyzve k zadání nového popisu úkolu  
**Skutečný výsledek:** Objevila se hláška "Popis úkolu nesmí být prázdný.", program vyzval k zadání nového popisu úkolu  
**Stav:** Pass  
**Poznámky:** Test validace prázdného popisu  

---

# TC04: Přidání úkolu s názvem obsahujícím pouze mezery

**Popis:** Ověření, že název obsahující pouze mezery je vyhodnocen jako prázdný  
**Předpoklady:** Uživatel je ve funkci Přidat nový úkol  

**Kroky testu:**
1. Zadej název úkolu ` ` a stiskni Enter  
2. Stiskni Enter  

**Očekávaný výsledek:** Objeví se hláška "Název úkolu nesmí být prázdný.", program vyzve k zadání nového názvu úkolu  
**Skutečný výsledek:** Objevila se hláška "Název úkolu nesmí být prázdný.", program vyzval k zadání nového názvu úkolu  
**Stav:** Pass  
**Poznámky:** Ověření odstranění mezer v názvu pomocí .strip()  

---

# TC05: Přidání úkolu s popisem obsahujícím pouze mezery

**Popis:** Ověření, že popis obsahující pouze mezery je vyhodnocen jako prázdný  
**Předpoklady:** Uživatel je ve funkci Přidat nový úkol  

**Kroky testu:**
1. Zadej název úkolu `Úkol 1` a stiskni Enter  
2. Zadej popis úkolu ` ` a stiskni Enter  
3. Stiskni Enter  

**Očekávaný výsledek:** Objeví se hláška "Popis úkolu nesmí být prázdný.", program vyzve k zadání nového popisu úkolu  
**Skutečný výsledek:** Objevila se hláška "Popis úkolu nesmí být prázdný.", program vyzval k zadání nového popisu úkolu  
**Stav:** Pass  
**Poznámky:** Ověření odstranění mezer v popisu pomocí .strip()  

---

# TC06: Vytvoření úkolu se speciálními znaky

**Popis:** Ověření, že systém správně uloží a zobrazí úkol obsahující speciální znaky v názvu i popisu  
**Předpoklady:** Uživatel je ve funkci Přidat nový úkol  

**Kroky testu:**
1. Zadej název úkolu `Úkol #&@` a stiskni Enter  
2. Zadej popis úkolu `Popis #&@` a stiskni Enter  

**Očekávaný výsledek:** Zobrazí se hláška "Úkol 'Úkol #&@' byl přidán."  
**Skutečný výsledek:** Zobrazila se hláška "Úkol 'Úkol #&@' byl přidán."  
**Stav:** Pass  
**Poznámky:** Test ověřuje zpracování speciálních znaků  

---

# TC07: Vytvoření úkolu s velmi dlouhým názvem a popisem

**Popis:** Ověření, že systém zvládne uložit a zobrazit úkol s velmi dlouhým textem bez oříznutí nebo chyby  
**Předpoklady:** Uživatel je ve funkci Přidat nový úkol  

**Kroky testu:**
1. Zadej název úkolu `aaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAA` a stiskni Enter  
2. Zadej popis úkolu `aaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAA` a stiskni Enter  

**Očekávaný výsledek:** Zobrazí se hláška "Úkol 'aaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAA' byl přidán."  
**Skutečný výsledek:** Správně se zobrazila hláška s dlouhým názvem úkolu  
**Stav:** Pass  
**Poznámky:** Test ověřuje práci s dlouhými vstupy bez ořezání nebo chyb  