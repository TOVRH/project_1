# TC01: Ověření spuštění aplikace a zobrazení hlavního menu

**Popis:** Ověření, že se po spuštění aplikace správně zobrazí hlavní menu s dostupnými možnostmi  
**Předpoklady:** Program je připraven ke spuštění  

**Kroky:**
1. Spusť program  
2. Ověř, že se zobrazí hlavní menu s nabídkou voleb  

**Očekávaný výsledek:**  
Program zobrazí hlavní menu:  
> Správce úkolů - hlavní menu  
> 1. Přidat nový úkol  
> 2. Zobrazit všechny úkoly  
> 3. Odstranit úkol  
> 4. Konec programu  
> Vyberte možnost (1–4):

**Skutečný výsledek:**  
Program zobrazil očekávanou nabídku voleb  

**Stav:** Pass  

**Poznámky:**  
Základní test ověřující spuštění aplikace  

---

# TC02: Reakce na zadání neexistující volby v menu

**Popis:** Ověření chování aplikace při zadání hodnoty, která neodpovídá žádné dostupné možnosti v hlavním menu  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky:**
1. Ověř, že se zobrazuje hlavní menu  
2. Zadej `5` a stiskni Enter  

**Očekávaný výsledek:**  
Zobrazí se chybová hláška:  
> "Neplatná volba, zkuste to prosím znovu."  

**Skutečný výsledek:**  
Chybová hláška se zobrazila  

**Stav:** Pass  

**Poznámky:**  
Test validace vstupu mimo povolený rozsah (1–4)  

---

# TC03: Zadání prázdného vstupu v menu

**Popis:** Ověření, že aplikace správně reaguje na zadání prázného vstupu  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky:**
1. Ověř, že se zobrazuje hlavní menu  
2. Stiskni Enter bez zadání hodnoty  

**Očekávaný výsledek:**  
Zobrazí se chybová hláška:  
> "Neplatná volba, zkuste to prosím znovu."  

**Skutečný výsledek:**  
Chybová hláška se zobrazila  

**Stav:** Pass  

**Poznámky:**  
Test chování při prázdném vstupu  

---

# TC04: Reakce na nečíselný vstup v hlavním menu

**Popis:** Ověření, že aplikace odmítne textový vstup při výběru položky v menu a zobrazí chybovou hlášku  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky:**
1. Ověř, že se zobrazuje hlavní menu  
2. Zadej `abc` a stiskni Enter  

**Očekávaný výsledek:**  
Zobrazí se chybová hláška:  
> "Neplatná volba, zkuste to prosím znovu."  

**Skutečný výsledek:**  
Chybová hláška se zobrazila  

**Stav:** Pass  

**Poznámky:**  
Test validace nečíselného vstupu  

---

# TC05: Zadání hodnoty obsahující mezery v menu

**Popis:** Ověření, že aplikace správně zpracuje vstup obsahující mezery a posoudí jej jako platnou volbu  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky:**
1. Ověř, že se zobrazuje hlavní menu  
2. Zadej ` 1 ` a stiskni Enter  

**Očekávaný výsledek:**  
Program přijme vstup jako platnou volbu `1` a zobrazí:  
> "Zadejte název úkolu:"  

**Skutečný výsledek:**  
Program zobrazil výzvu k zadání názvu úkolu  

**Stav:** Pass  

**Poznámky:**  
Ověření odstranění mezer (např. pomocí `.strip()`)  

---

# TC06: Ošetření záporné hodnoty v menu

**Popis:** Ověření, že aplikace správně odmítne záporné číslo jako neplatnou volbu v menu  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky:**
1. Ověř, že se zobrazuje hlavní menu  
2. Zadej `-1` a stiskni Enter  

**Očekávaný výsledek:**  
Zobrazí se chybová hláška:  
> "Neplatná volba, zkuste to prosím znovu."  

**Skutečný výsledek:**  
Chybová hláška se zobrazila  

**Stav:** Pass  

**Poznámky:**  
Test chování při záporném vstupu  

---

# TC07: Validace desetinného čísla v menu

**Popis:** Ověření, že aplikace odmítne desetinné číslo jako neplatný vstup v hlavním menu  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky:**
1. Ověř, že se zobrazuje hlavní menu  
2. Zadej `1.0` a stiskni Enter  

**Očekávaný výsledek:**  
Zobrazí se chybová hláška:  
> "Neplatná volba, zkuste to prosím znovu."  

**Skutečný výsledek:**  
Chybová hláška se zobrazila  

**Stav:** Pass  

**Poznámky:**  
Ověření validace desetinných čísel  

---

# TC08: Ukončení aplikace z hlavního menu

**Popis:** Ověření správného ukončení aplikace po výběru příslušné volby v hlavním menu  
**Předpoklady:** Program zobrazuje hlavní menu  

**Kroky:**
1. Ověř, že se zobrazuje hlavní menu  
2. Zadej `4` a stiskni Enter  

**Očekávaný výsledek:**  
Program zobrazí:  
> "Konec programu"  
a ukončí se  

**Skutečný výsledek:**  
Program se ukončil správně  

**Stav:** Pass  

**Poznámky:**  
Ověření správného ukončení aplikace  