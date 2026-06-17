# KeyForge

🌐 Jazyk: Čeština | [English version](README.en.md)

Konzolová aplikace v Pythonu pro deterministické generování hesel z klíčových vstupů.
Hesla se nikam neukládají — aplikace je pokaždé znovu vypočítá ze stejných vstupů.

## Jak to funguje

Uživatel zadá tři věci: název platformy, zapamatovatelnou frázi a libovolné extra slovo nebo číslo. Aplikace z toho pomocí zvoleného algoritmu vypočítá deset variant hesla. Stejné vstupy vždy vrátí stejná hesla — stačí si je zapamatovat a heslo je kdykoli znovu k dispozici bez toho, aby bylo někde uložené.

## Algoritmy

Na začátku jsem použil SHA-256 jako základ — standardní hašovací funkce, která ze vstupů spolehlivě vytvoří pevnou sadu bajtů. Přidat SHA-512, MD5 a SHA-1 bylo pak jednoduché, každá třída zdědí základ a změní jen název algoritmu.

Pak mě napadlo zkusit něco zajímavějšího než další hašovací variantu.

### Caesarova šifra

Začal jsem se zajímat o klasické šifry a dohledal jsem si, jak Caesarova šifra funguje. Julius Caesar ji prý používal pro vojenskou komunikaci — každé písmeno zprávy se posune o pevný počet pozic v abecedě. A dostane se B, B dostane C, a tak dál. Jednoduchý, ale funkční princip.

Rozhodl jsem se ho zapojit do generátoru. Místo přímého mapování bajtů na znaky nejdřív celou výstupní znakovou sadu rotuju o posun, který se vypočítá ze vstupů. Každá kombinace platformy, fráze a extra slova dá jiný posun — a tím i jiné heslo, než by dalo čisté hašování.

### Enigma

Při hledání dalších šifer jsem narazil na Enigmu. Zjistil jsem, že to byl elektromechanický šifrovací stroj, který německá armáda používala ve druhé světové válce pro tajnou komunikaci. Spojenecká rozvědka ho dlouho považovala za nerozluštitelný.

Zaujalo mě, jak to celé funguje. Enigma má tři rotory — každý rotor je v podstatě zamíchaná abeceda, kde každé písmeno dostane jiné písmeno. Stisknete klávesu a signál projde přes všechny tři rotory dopředu, narazí na reflektor, který ho odrazí zpátky, a projde všemi třemi rotory znovu v opačném směru. Výsledkem je úplně jiné písmeno než to, které jste stiskli.

Co mě ale zaujalo nejvíc: po každém napsaném znaku se pravý rotor pootočí o jednu pozici. Každých 26 znaků se pootočí prostřední rotor, každých 676 znaků levý. Díky tomu i dvě stejná písmena za sebou dostanou jiné zakódování — šifra se mění s každým znakem.

Dohledal jsem si historické tabulky zapojení rotorů Wehrmacht Enigma I, II a III, včetně reflektoru B, a implementoval je přesně tak, jak byly v originále. Počáteční pozice rotorů se v aplikaci odvozují ze vstupů — každá kombinace klíčových slov nastaví rotory na jinou výchozí polohu a dostanete tak zcela odlišné heslo.

Volitelně lze zadat vlastní klíč Enigmy — libovolné slovo, které nahradí historické tabulky rotorů úplně vlastními. Bez klíče se použijí historické Wehrmacht tabulky, s klíčem se z něj vygenerují nové tabulky zapojení. Pokud klíč použijete, musíte si ho poznamenat — jinak stejné heslo znovu nevygenerujete.

## Funkce aplikace

- průvodce generováním hesla ve třech krocích (platforma, fráze, extra),
- výběr algoritmu před každým generováním (SHA-256, SHA-512, MD5, SHA-1, Caesar, Enigma),
- deset variant hesla pro každou kombinaci vstupů,
- různé délky a znakové sady pro každou variantu,
- zobrazení konkrétního hesla podle jeho čísla,
- deterministický výstup — stejné vstupy vždy vytvoří stejné heslo,
- výběr jazyka rozhraní (čeština / angličtina),
- barevný výstup v terminálu.

## Použité technologie

- Python 3,
- objektově orientované programování a dědičnost,
- konzolové uživatelské rozhraní s ANSI barvami,
- hašovací funkce přes standardní knihovnu `hashlib`,
- deterministická derivace hesel,
- vícejazyčnost — texty odděleny od logiky aplikace.

## Struktura projektu

```text
Password_Generate/
├── main.py
├── password_generator/
│   ├── generator.py
│   ├── generator_sha512.py
│   ├── generator_md5.py
│   ├── generator_sha1.py
│   ├── generator_caesar.py
│   ├── generator_enigma.py
│   ├── generator_screen.py
│   ├── terminal.py
│   ├── language_pack.py
│   └── language_texts.py
├── README.md
└── README.en.md
```

## Spuštění aplikace

### 1. Naklonování repozitáře

```bash
git clone https://github.com/DanielRakusan/Password_Generate.git
cd Password_Generate
```

### 2. Spuštění

```bash
python main.py
```

Pokud systém používá `python3`:

```bash
python3 main.py
```

Přes `uv`:

```bash
uv run python main.py
```

### 3. Spuštění v PyCharmu

1. Otevřete projekt v PyCharmu.
2. Otevřete `main.py`.
3. Pravý klik → `Run 'main'`.

## Ukázka výstupu

```text
Vygenerovaná hesla

   1.  BzzQnS2QGIUW#HT*
   2.  @hl&6*t$WTE9
   3.  v&Vt6aLpO?hrQpsKzUWB
   4.  vrz66u4YnPyScaWj
   5.  5NEg7YeNszB9QB1ME0cN
   6.  j8BiEXYnMtn3
   7.  3JJYCdOPmyjfV1mk
   8.  m4mXXKrdY3Wg1jqoxWaHcZBT
   9.  nORwhxL*q@NXJcQ3CF
  10.  T3E9IKFryZRDZxZZoDqt6RDVdxxlEYs2

Uložte si (přesně jak jste zadali):
  Alg. 1 (SHA-256)  ·  Platforma: Gmail  ·  Fráze: MamRadPsy  ·  Extra: 1990
  Číslo hesla: ___
```

## Cíl projektu

Projekt vznikl jako ukázka menší objektově orientované aplikace v Pythonu. Chtěl jsem zkombinovat standardní hašování s klasickými šifrovacími technikami a zároveň procvičit práci s třídami, dědičností a konzolovou navigací.

## Autor

Daniel Rakušan
