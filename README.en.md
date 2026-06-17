# KeyForge

🌐 Language: [Česká verze](README.md) | English

A console application written in Python for deterministic password generation from keyword inputs.
Passwords are never stored — the application recalculates them from the same inputs every time.

## How It Works

The user provides three things: a platform name, a memorable phrase, and any extra word or number. The application uses the chosen algorithm to calculate ten password variants. The same inputs always return the same passwords — just remember them and the password is available again at any time, without being stored anywhere.

## Algorithms

I started with SHA-256 as the foundation — a standard hash function that reliably produces a fixed set of bytes from the inputs. Adding SHA-512, MD5 and SHA-1 was straightforward after that: each class inherits the base and only changes the algorithm name.

Then I wanted to try something more interesting than yet another hashing variant.

### Caesar Cipher

I got curious about classic ciphers and looked up how the Caesar cipher works. Julius Caesar reportedly used it for military communication — each letter in a message is shifted by a fixed number of positions in the alphabet. A becomes B, B becomes C, and so on. Simple, but effective.

I decided to incorporate this into the generator. Instead of mapping bytes directly to characters, I first rotate the entire output character set by a shift calculated from the inputs. Each combination of platform, phrase and extra word produces a different shift — and therefore a different password than plain hashing would.

### Enigma

While researching more ciphers I came across the Enigma machine. I found out it was an electromechanical encryption device used by the German military in World War II for secret communication. Allied intelligence considered it unbreakable for a long time.

I was fascinated by how it actually worked. Enigma has three rotors — each rotor is essentially a scrambled alphabet, mapping each letter to a different letter. You press a key and the signal passes through all three rotors forward, hits a reflector that bounces it back, and passes through all three rotors again in reverse. The result is a completely different letter than the one you pressed.

What interested me most: after each character is typed, the right rotor advances by one position. Every 26 characters the middle rotor advances, and every 676 characters the left rotor advances. This means that even two identical letters typed in a row get different encodings — the cipher changes with every character.

I looked up the historical rotor wiring tables for the Wehrmacht Enigma I, II and III, including Reflector B, and implemented them exactly as they were in the original machine. The starting rotor positions in the application are derived from the inputs — each combination of keyword inputs sets the rotors to a different starting position, producing a completely different password.

Optionally, a custom Enigma key can be entered — any word that further shifts the rotor starting positions. If you use it, you must write it down, otherwise you won't be able to regenerate the same password.

## Application Features

- three-step guided wizard for password generation (platform, phrase, extra),
- algorithm selection before each generation (SHA-256, SHA-512, MD5, SHA-1, Caesar, Enigma),
- ten password variants for each combination of inputs,
- different lengths and character sets for each variant,
- showing a specific password by its number,
- deterministic output — the same inputs always produce the same password,
- interface language selection (Czech / English),
- colored output in the terminal.

## Technologies Used

- Python 3,
- object-oriented programming and class inheritance,
- console user interface with ANSI colors,
- hash functions via the standard `hashlib` library,
- deterministic password derivation,
- multilingual support — texts separated from application logic.

## Project Structure

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

## Running the Application

### 1. Clone the repository

```bash
git clone https://github.com/DanielRakusan/Password_Generate.git
cd Password_Generate
```

### 2. Run

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

With `uv`:

```bash
uv run python main.py
```

### 3. Run in PyCharm

1. Open the project in PyCharm.
2. Open `main.py`.
3. Right-click → `Run 'main'`.

## Sample Output

```text
Generated passwords

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

Save (exactly as entered):
  Alg. 1 (SHA-256)  ·  Platform: Gmail  ·  Phrase: ILoveDogs  ·  Extra: 1990
  Password no.: ___
```

## Project Goal

The project was built as an example of a smaller object-oriented Python application. I wanted to combine standard hashing with classic cipher techniques while practicing working with classes, inheritance, and console navigation.

## Author

Daniel Rakušan
