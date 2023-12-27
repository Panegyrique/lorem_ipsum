# Encrypted identity generator

## What does it do ?
This software generates a first name, surname and date of birth, which can be copied directly into the clipboard for use on websites when registering.

It's also possible to save used identifiers in encrypted form, without local storage of the key. Saved identifiers can be consulted after decryption using the same key that was used for encryption.

## Tree
``` bash
∟ lorem_ipsum
    ∟ designer
        lorem_ispum.ui
    ∟ lorem_ipsum
        ∟ data
            dictionary_history.csv
            dictionary_latin.csv
            icon.png
        ∟ lib
            gui.py
            process.py
            style.py
        __init__.py
        ac_app.py
   .gitignore
   README.md
```

## Modules required
``` bash
# module for graphics
pip install PyQt5

# module for copying to the clipboard
pip install pyperclip

# module for encryption and decryption
    # ∟ An almost drop-in replacement for the old PyCrypto library. You install it with:
        pip install pycryptodome
    # ∟ A library independent of the old PyCrypto. You install it with:
        pip install pycryptodomex
```