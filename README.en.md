# Enigma

🌐 Language: [Česká verze](README.md) | English

A console application written in Python for deterministic password generation from keyword inputs.

The project serves as an example of a smaller object-oriented application
with a separated generator, terminal interface, algorithm selection, and
multilingual support. Passwords are never stored — the application recalculates
them from the same inputs every time.

## Project Description

Enigma allows the user to create passwords using three keyword inputs:
a platform name, a memorable phrase, and any additional word or number.
For each combination of inputs the application generates ten password variants.
The same inputs always return the same passwords — passwords are not stored,
but recalculated on demand.

The project mainly focuses on practicing these areas:

- object-oriented programming in Python,
- separation of responsibilities between multiple classes, each in its own file,
- deterministic password derivation using hash functions,
- class inheritance in Python,
- multilingual support and separation of texts from application logic,
- creating a console interface with colored output.

## Application Features

- three-step guided wizard for password generation (platform, phrase, extra),
- hashing algorithm selection before each generation,
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
- deterministic password derivation (SHA-256, SHA-512, MD5, SHA-1, Caesar),
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
│   ├── generator_screen.py
│   ├── terminal.py
│   ├── language_pack.py
│   └── language_texts.py
├── README.md
└── README.en.md
```

## Main Parts of the Application

### `PasswordGenerator`

The base generator class. It stores password variants (length, character set)
and handles deterministic password derivation from a seed composed of the inputs
and the variant index using SHA-256. Each variant index produces a different password.

### `PasswordGeneratorSHA512`, `PasswordGeneratorMD5`, `PasswordGeneratorSHA1`

Each of these classes inherits from the base generator and overrides only one
property — the name of the algorithm used. The derivation logic remains the same.

### `PasswordGeneratorCaesar`

Inherits from the base generator and overrides the password derivation method.
Before mapping bytes to characters, it rotates the output alphabet by a shift
calculated from the inputs — that is the essence of the Caesar cipher applied
to the output alphabet.

### `GeneratorScreen`

Handles communication with the user during password generation.
It guides the user through algorithm selection and the three keyword inputs.
It displays the generated passwords and allows showing a specific password
by its number.

### `Terminal`

Manages the console interface of the application. It contains the colored output
system, a universal menu, language switching, and connection to screens.

### `LanguagePack`

Handles multilingual support. It allows switching between Czech and English
while the application is running. No text is hardcoded in the logic — everything
is loaded through a language dictionary in `language_texts.py`.

## Application Startup

### 1. Language selection

After launching the application, a menu for selecting the interface language
is displayed:

```text
Main menu
1: Czech
2: English
Choose an option:
```

### 2. Algorithm selection

Before each password generation the user selects a hashing algorithm:

```text
Hashing algorithm
1: SHA-256  (recommended)
2: SHA-512
3: MD5
4: SHA-1
5: Caesar
Choose an option:
```

### 3. Keyword inputs

The wizard asks for three inputs one by one:

```text
Step 2 of 4
Platform
(e.g. Gmail, Facebook, Bank...)

Which platform is this password for?
```

```text
Step 3 of 4
Phrase
(e.g. ILoveDogs, FavoritePlaces...)

Enter a sentence or phrase you will remember:
```

```text
Step 4 of 4
Extra
(e.g. birth year, favourite number, nickname...)

Enter a number or word as extra:
```

### 4. Results

The application displays ten password variants. The user picks one
and notes down the algorithm number and the password number:

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

Select a password and copy it.
Note down: algorithm no.1 + password number!
```

## Show Password by Number

If the user noted the algorithm number and password number,
they can display the same password again at any time without searching:

```text
Main menu
1: Generate password
2: Show password by number
3: Change language
5: Exit program
Choose an option:
```

The wizard asks for the same inputs as during generation and at the end
also for the password number. The application returns exactly the same password.

## How the Passwords Work

Passwords are not generated randomly — each password is deterministically
calculated from the provided inputs using a hash function. The same combination
of inputs always returns the same password. The platform, phrase, and extra input
are never directly visible in the password.

The user does not need to store the password anywhere. It is enough to remember
the keyword inputs and note down the algorithm number and password number.

## Installation and Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/DanielRakusan/Password_Generate.git
```

### 2. Open the project folder

```bash
cd Password_Generate
```

### 3. Run the application

On Windows, macOS, or Linux, run:

```bash
python main.py
```

If your system uses the `python3` command, run:

```bash
python3 main.py
```

### 4. Run with uv

The project uses `uv` for dependency management. If you have `uv` installed:

```bash
uv run python main.py
```

### 5. Run in PyCharm

1. Open the project in PyCharm.
2. Open the `main.py` file.
3. Right-click inside the file.
4. Select `Run 'main'`.

The application will start in the PyCharm console.

## Possible Future Improvements

- master password protection for generation,
- export of notes to an encrypted file,
- adding stronger algorithms such as PBKDF2 or bcrypt,
- web version, for example in Flask or Django.

## Project Goal

The goal of the project is to demonstrate basic Python knowledge in a smaller,
clear application. The project demonstrates working with classes, inheritance,
hash functions, deterministic data derivation, multi-color console navigation,
multilingual support, and separation of logic from the user interface.

## Author

Daniel Rakušan
