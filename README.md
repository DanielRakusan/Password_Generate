# Enigma

🌐 Jazyk: Čeština | [English version](README.en.md)

Konzolová aplikace v Pythonu pro deterministické generování hesel z klíčových vstupů.

Projekt slouží jako ukázka menší objektově orientované aplikace
s odděleným generátorem, terminálovým rozhraním, výběrem algoritmu
a vícejazyčnou podporou. Hesla se nikam neukládají — aplikace je pokaždé
znovu vypočítá ze stejných vstupů.

## Popis projektu

Enigma umožňuje uživateli vytvářet hesla pomocí tří klíčových vstupů:
platformy, zapamatovatelné fráze a libovolného doplňujícího slova nebo čísla.
Pro každou kombinaci vstupů aplikace vygeneruje deset variant hesla.
Stejné vstupy vždy vrátí stejná hesla — hesla se tedy neukládají,
ale kdykoli znovu vypočítají.

Projekt je zaměřený hlavně na procvičení těchto oblastí:

- objektově orientované programování v Pythonu,
- rozdělení odpovědností mezi více tříd, každá v vlastním souboru,
- deterministická derivace hesel pomocí hašovacích funkcí,
- dědičnost tříd v Pythonu,
- vícejazyčnost a oddělení textů od logiky aplikace,
- tvorba konzolového rozhraní s barevným výstupem.

## Funkce aplikace

- průvodce generováním hesla ve třech krocích (platforma, fráze, extra),
- výběr hašovacího algoritmu před každým generováním,
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
- deterministická derivace hesel (SHA-256, SHA-512, MD5, SHA-1, Caesar),
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
│   ├── generator_screen.py
│   ├── terminal.py
│   ├── language_pack.py
│   └── language_texts.py
├── README.md
└── README.en.md
```

## Hlavní části aplikace

### `PasswordGenerator`

Základní třída generátoru. Uchovává varianty hesel (délka, znaková sada)
a zajišťuje deterministickou derivaci hesla ze seedu složeného ze vstupů
a indexu varianty pomocí SHA-256. Každý index varianty dá jiné heslo.

### `PasswordGeneratorSHA512`, `PasswordGeneratorMD5`, `PasswordGeneratorSHA1`

Každá z těchto tříd dědí ze základního generátoru a přepíše pouze jednu
vlastnost — název použitého algoritmu. Logika derivace zůstává stejná.

### `PasswordGeneratorCaesar`

Dědí ze základního generátoru a přepíše metodu derivace hesla.
Před mapováním bajtů na znaky rotuje výstupní abecedu o posun vypočítaný
ze vstupů — to je podstata Caesarovy šifry aplikované na výstupní abecedu.

### `GeneratorScreen`

Zajišťuje komunikaci s uživatelem při generování hesel.
Vede průvodce výběrem algoritmu a zadáváním tří klíčových vstupů.
Zobrazuje vygenerovaná hesla a umožňuje zobrazit konkrétní heslo
podle jeho čísla.

### `Terminal`

Spravuje konzolové rozhraní aplikace. Obsahuje systém barevného výstupu,
univerzální menu, přepínání jazyka a propojení s obrazovkami.

### `LanguagePack`

Zajišťuje vícejazyčnost aplikace. Umožňuje přepínání mezi češtinou
a angličtinou za běhu. Žádný text není v kódu natvrdo — vše se načítá
přes jazykový slovník v souboru `language_texts.py`.

## Spuštění aplikace

### 1. Výběr jazyka

Po spuštění aplikace se zobrazí menu pro výběr jazyka rozhraní:

```text
Hlavní menu
1: Čeština
2: English
Zadejte číslo volby:
```

### 2. Výběr algoritmu

Před každým generováním hesel uživatel zvolí hašovací algoritmus:

```text
Výběr algoritmu hešování
1: SHA-256  (doporučeno)
2: SHA-512
3: MD5
4: SHA-1
5: Caesar
Zadejte číslo volby:
```

### 3. Zadání klíčových vstupů

Průvodce postupně požádá o tři vstupy:

```text
Krok 2 ze 4
Platforma
(např. Gmail, Facebook, Banka...)

Na jaké platformě se heslo používá?
```

```text
Krok 3 ze 4
Fráze
(např. MamRadPsy, OblibenaMista...)

Zadejte větu nebo frázi, kterou si zapamatujete:
```

```text
Krok 4 ze 4
Extra
(např. rok narození, oblíbené číslo, přezdívka...)

Zadejte číslo nebo slovo navíc:
```

### 4. Výsledky

Aplikace zobrazí deset variant hesla. Uživatel si vybere jedno
a poznamená si číslo algoritmu a číslo hesla:

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

Vyberte heslo a zkopírujte jej.
Poznamenejte si: algoritmus č.1 + číslo hesla!
```

## Zobrazení hesla podle čísla

Pokud si uživatel zapamatoval číslo algoritmu a číslo hesla,
může stejné heslo kdykoli znovu zobrazit bez hledání:

```text
Hlavní menu
1: Generovat heslo
2: Zobrazit heslo podle čísla
3: Změnit jazyk
5: Ukončit program
Zadejte číslo volby:
```

Průvodce požádá o stejné vstupy jako při generování a na konci
i o číslo hesla. Aplikace vrátí přesně to samé heslo.

## Jak hesla fungují

Hesla se nevytváří náhodně — každé heslo je deterministicky vypočítáno
ze zadaných vstupů pomocí hašovací funkce. Stejná kombinace vstupů
vždy vrátí stejné heslo. Platforma, fráze a extra vstup nikdy nejsou
v hesle přímo vidět.

Uživatel si nemusí heslo ukládat. Stačí si zapamatovat klíčové vstupy
a poznamenat si číslo algoritmu a číslo hesla.

## Instalace a spuštění projektu

### 1. Naklonování repozitáře

```bash
git clone https://github.com/DanielRakusan/Password_Generate.git
```

### 2. Přechod do složky projektu

```bash
cd Password_Generate
```

### 3. Spuštění aplikace

Na Windows, macOS nebo Linuxu spusťte:

```bash
python main.py
```

Pokud systém používá příkaz `python3`, spusťte:

```bash
python3 main.py
```

### 4. Spuštění přes uv

Projekt používá `uv` pro správu závislostí. Pokud máte `uv` nainstalované:

```bash
uv run python main.py
```

### 5. Spuštění v PyCharmu

1. Otevřete projekt v PyCharmu.
2. Otevřete soubor `main.py`.
3. Klikněte pravým tlačítkem do souboru.
4. Vyberte možnost `Run 'main'`.

Aplikace se spustí v konzoli PyCharmu.

## Možná budoucí rozšíření

- ochrana generování hlavním heslem,
- export poznámek do šifrovaného souboru,
- přidání silnějších algoritmů jako PBKDF2 nebo bcrypt,
- webová verze například ve Flasku nebo Djangu.

## Cíl projektu

Cílem projektu je ukázat základní znalosti Pythonu v menší, přehledné aplikaci.
Projekt demonstruje práci s třídami, dědičností, hašovacími funkcemi,
deterministickou derivací dat, konzolovou vícebarevnou navigací, vícejazyčností
a oddělením logiky od uživatelského rozhraní.

## Autor

Daniel Rakušan
