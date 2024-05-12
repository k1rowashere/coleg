# Systems Programming - Sheet 5

## Question 1:


- Opcode Table:
  Lookup table used to convert assembly nemonics to machine language opcodes.
- Symbol Table:
  Stores the labels and their respective location value.
- Literal Table:
  Stores the literals and their respective location value.
- Location Counter:
  Variable that stores the current location (address) of the line being processed.
- Base indicator:
  Flag that determines if `Base` mode is being used.
- Copy File:
  Intermediate file between pass 1 and pass 2.
- Object File:
  Machine code output of the 2-pass assembler.


---
## Question 2:


a. Special hardware access, handles exceptions, parallel processed and used intensively.

a.
    - Operating Systems: Manage resources and processies running on system.
    - Language facilites: Compilers, interpreters, assemblers, linkers, loaders...
    Translate/run user code to machine language

a. 
    - Manages hw resources and application processies.
    - Helps in developing programs.
        a. It is a program that translates assembly language input to machine code.
        a. i, ii and iii.
        a. Pass 1.
        a. A scan over the source code.
        a. Programs can be developed in reusable modules, code can be loaded anywhere in memory.

a. 
    1.  Loads a program to memory and resolves relocatable addresses to actual addresses.
    1.  Performs linking of modules and loads them to memory.
    1.  Translates assembly to relocatable machine code executable.
    1.  Translates assembly to machine code then loads it directly to memory.
    1.  Translates assembly to machine code executable.
    1.  Links multiple object files (modules) together.

a. Code cannot be reused, must be loaded in the exact location in memory.

a.

| Module Assembler                      | Load and go assembler                                     |
| ------------------------------------- | --------------------------------------------------------- |
| Can create reloacatable code.         | Can only create abosulte code.                            |
| Code only needs to be assembled once. | Code must be assembled each time the program is executed. |
| Can be linked with other code.        | Cannot be linked with other code.                         |

a.
    - \# of Passes: 1-pass or 2-pass
    - Translation: module assembler (generate reloactable code) or laod-and-go assembler (ran immediately)

a. Can't handle forward references, which burdens the programmer.

a. One pass module assebler, load-and-go assembler. (shown in prev question)

a.
    1.  (shown in prev question)
    1.  1-pass module assembler:
        - Forward reference are only allowed for branches.
        - Literals are not allowed.

a. Piece of reloactable code.

<div style="page-break-after: always;"></div>

## Question 3:


a. **Machine Instructions**
    - Pass-1:
        - Read line from source file.
        - Mnemonic is parsed to Machine code according to instruction format.
        - Location counter is incremented.
        - Literal (if exists) is added to literal table.
        - Line is written to copy file.
    - Pass-2
        - Read line from copy file.
        - Operand is parsed according to internal representation.
        - Line is written to object file.

a. **WORD directive**
    - Pass-1:
        - Read line from source file.
        - Symbol is added to symbol table.
        - Location counter is incremented (+3).
    - Pass-2
        - Read line from copy file.
        - Add binary representation to object file

a. **BYTE directive**
    - Pass-1:
        - Read line from source file.
        - Symbol is added to symbol table.
        - Location counter is incremented (+ length of constant).
    - Pass-2
        - Read line from copy file.
        - Add binary representation to object file

a. **RESW directive** 
    - Pass-1:
        - Read line from source file.
        - Symbol is added to symbol table.
        - Location counter is incremented (+ 3 * # of elements).
    - Pass-2
        - N/A

a. **RESB directive**
    - Pass-1:
        - Read line from source file.
        - Symbol is added to symbol table.
        - Location counter is incremented (+ 1 * # of elements).
    - Pass-2
        - N/A

a. **EQU directive**
    - Pass-1:
        - Read line from source file.
        - Symbol is added to symbol table (with location value).
    - Pass-2
        - N/A

a. **ORG directive**
    - Pass-1:
        - Read line from source file.
        - Location counter = operand
    - Pass-2
        - N/A

a. **START directive**
    - Pass-1:
        - Read line from source file.
        - Create copy file.
        - Location Counter = operand
        - Write line to copy file
    - Pass-2
        - Read line from copy file.
        - Create object file.

a. **END directive**
    - Pass-1:
        - Read line from source file.
        - Write line to copy file
        - Close copy file.
        - Start pass-2.
    - Pass-2
        - Instert literals to object code
        - Close object file.


## Question 4:


(line is read from source/copy file in all instructions)

answer format:
```
x.  - pass-1
    --------
    - pass-2
```

<style type="text/css">
    ol hr:not(:last-child) {
        height: .2em !important;
        margin: .5em !important;
        opacity: 50%
    }
    @media(print) {
        
    }
</style>

a.
    - Create copy file.
    - $LC := 1000$
    - Insert line in copy file.
    ***
    - Create object file.
    ***

a.
    - `SYMBOL_TABLE` ← `TEXT`,`LC`
    - $LC = LC + 6$
    - Insert line in copy file.
    ***
    - `Object file` ← `'Result'` (according to interal representation)
    ***

a.  
    - `SYMBOL_TABLE` ← `XYZ`,`LC`
    - $LC = LC + 3$ (format-3)
    - Insert line in copy file.
    ***
    - `Object file` ← `opcode`
    - `Object file` ← `ELSE`'s location from `SYMBOL_TABLE`
    ***

a.
    - $LC = LC + 3 * 5$
    - Insert line in copy file.
    ***
    - `Object file` ← `1,2,3,4,5` according to internal representation
    ***

a.
    - Set end address of program to LC
    - Reserve locations to literals
    - Insert line in copy file
    - Close copy file
    - Start pass-2
    ***
    - Insert literals according to internal representation
    - Close object file
    - End assembler
    ***


a.
    - `SYMBOL_TABLE` ← `DONE`,`LC` (if not present)
    - $LC = LC + 4$ (format-4)
    - Insert line in copy file
    ***
    - `Object file` ← `opcode`
    - `Object file` ← `LOOP`'s location from `SYMBOL_TABLE`
    ***

a.
    - `SYMBOL_TABLE` ← `BUFFER`,`#[BUFFEND - BUFFSTART]` (if not present)
    ***
    - N/A
    ***

a. 
    - `SYMBOL_TABLE` ← `STORY` (if not present)
    - $LC = LC + 500 * 3$
    - Insert line in copy file
    ***
    - `Object file` ← `500` according to internal representation
    ***

a.
    - `SYMBOL_TABLE` ← `LABEL` (if not present)
    - $LC = LC + 500$
    - Insert line in copy file
    ***
    - `Object file` ← `500` according to internal representation
    ***

a.
    - `SYMBOL_TABLE` ← `GLOBAL` (if not present)
    - $LC = LC + 3$ (format-3)
    - Insert line in copy file
    ***
    - `Object file` ← `opcode`
    - `Object file` ← `300` according to internal representation
    ***

a.
    - $LC = LC + 3$ (format-3)
    - Insert line in copy file
    ***
    - `Object file` ← `opcode` (with correct addressing mode)
    - `Object file` ← `REFERENCE`'s location from `SYMBOL_TABLE`
    ***

a.
    - `SYMBOL_TABLE` ← `STORE` (if not present)
    - $LC = LC + 4$ (format-4)
    - Insert line in copy file
    ***
    - `Object file` ← `opcode` (with correct addressing mode)
    - `Object file` ← `REFERENCE`'s location from `SYMBOL_TABLE`
    ***

a.
    - $LC = LC - 10$
    ***
    - N/A
    ***

a.
    - `SYMBOL_TABLE` ← `XXX` (if not present)
    - $LC = LC + 3$ (format-3)
    - `Literal Table` ← `10000`
    - Insert line in copy file
    ***
    - `Object file` ← `opcode` (with correct addressing mode)
    - `Object file` ← operand's location from `LITERAL_TABLE`
    ***

a.
    - `SYMBOL_TABLE` ← `TWO` (if not present)
    - $LC = LC + 3$
    - Insert line in copy file
    ***
    - `Object file` ← `2` according to internal representation
    ***

a.
    - `SYMBOL_TABLE` ← `HERE` (if not present)
    - $LC = LC + 3$ (format-3)
    - Insert line in copy file
    ***
    - `Object file` ← `opcode` (with correct addressing mode)
    - `Object file` ← `XXX`'s location from `SYMBOL_TABLE`
    ***

a.
    - `SYMBOL_TABLE` ← `SEVEN` (if not present)
    - $LC = LC + 3$
    - Insert line in copy file
    ***
    - `Object file` ← `7` according to internal representation
    ***


a.
    - `SYMBOL_TABLE` ← `BEGIN` (if not present)
    - $LC = LC + 3$ (format-3)
    - `Literal Table` ← `1000`
    - Insert line in copy file
    ***
    - `Object file` ← `opcode` (with correct addressing mode)
    - `Object file` ← operand's location from `LITERAL_TABLE`
    ***

a.
    - `SYMBOL_TABLE` ← `XXXX` (if not present)
    - $LC = LC + 3$ (format-3)
    - `Literal Table` ← `12345`
    - Insert line in copy file
    ***
    - `Object file` ← `opcode` (with correct addressing mode)
    - `Object file` ← operand's location from `LITERAL_TABLE`

<div style="page-break-after: always;"></div>

## Question 5:


1. False
1. False
1. True
1. False
1. True

