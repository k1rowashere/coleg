# Question 1

```
XX      WORD    1,2,3,5,7,9
YY      WORD    2,4,5,6,10
SUM     WORD    0

        LDS     #15
        LDT     #3
        LDX     #0

LOOP    LDA     XX, X
        MUL     YY, X
        ADD     SUM
        STA     SUM

        ADDR    LDT, LDX
        COMP    LDX, LDS
        JEQ     OUT
        J       LOOP

OUT     ...     ...
```

# Question 2

## a.

```
Q       WORD    1
SUM     WORD    0

        LDA     Q
        LDS     #0

LOOP    COMP    #4
        JGT     OUT

        MULR    A, A
        ADD     SUM
        STA     SUM

        LDA     Q
        ADD     #1
        J       LOOP

OUT     ...     ...
```

## b.

```
U       WORD    1, 2, 3, 4, 5, 6, 7, 8
V       RESW    8


        LDS     #21
        LDT     #3
        LDX     #0

LOOP    LDA     U, X
        STA     V, X

        ADDR    LDT, LDX
        COMP    LDX, LDS
        JEQ     OUT
        J       LOOP

OUT     ...     ...
```

## c.

```
Y       RESW    1
Z       RESW    1

LOOP    LDA     Z
        DIV     #3
        STA     Z

        LDA     Y
        ADDR    A, A
        STA     Y

        COMP    #1000
        JLT     LOOP
```

## d.

```
N       WORD    4
Y       WORD    0
Z       RESW    1

LOOP    LDA     N
        COMP    #256
        JGT     OUT

        ADD     Y
        STA     Y

        ADD     #4
        STA     N

        J       LOOP

OUT     LDA     Y
        MULR    A, A
        STA     Z
```

## e.

```
P       RESW    1
Q       RESW    1
R       RESW    1
W       RESW    1

LOOP    LDA     P
        MUL     Q
        COMP    #200
        JGT     OUT

        LDA     P
        SUB     #1
        STA     P

        LDA     Q
        ADD     #3
        STA     Q

        LDA     R
        ADD     P
        STA     R

        J       LOOP

OUT     LDA     R
        MUL     #5
        STA     W
```

## f.

```
LA      RESW    1
AL      RESW    1
BL      RESW    1
CL      RESW    1
DL      RESW    1
EL      RESW    1

        LDA     LA
        COMP    AL
        JEQ     CASEA
        COMP    BL
        JEQ     CASEB
        COMP    CL
        JEQ     CASEC
        COMP    DL
        JEQ     CASED
        J       DEFAULT


CASEA   LDA     AL
        SUB     #1
        STA     AL
        J       OUT

CASEB   LDA     BL
        SUB     #1
        STA     BL
        J       OUT

CASEC   LDA     CL
        SUB     #1
        STA     CL
        J       OUT

CASED   LDA     DL
        SUB     #1
        STA     DL
        J       OUT

DEFAULT LDA     EL
        SUB     #1
        STA     EL
        J       OUT

OUT     ...     ...
```


## g.

```
P       RESW    1
R       RESW    1
Q       RESW    1
SS      RESW    1


LOOP    LDA     P
        COMP    Q
        JLT     OUT

        LDA     R
        ADD     P
        STA     R

        LDA     P
        SUB     #2
        STA     P

        J       LOOP

OUT     LDA     SS
        ADD     R
        STA     SS
```

# Question 3

```
WBASE   RESW    50
UBASE   RESW    50
VBASE   RESW    50

        LDX     #0
        LDS     #3
        LDT     #150

LOOP    LDA     UBASE, X
        MUL     VBASE, X
        STA     WBASE, X

        ADDR    S, X
        COMPR   X, T
        JLT     LOOP
```

# Question 4

```
DATA    RESW     50

        LDX     #0
        LDS     #3
        LDT     #150
LOOP    LDA     DATA,X
        MUL     #2
        STA     DATA,X

        ADDR    S, X
        COMPR   X, T
        JLT     LOOP
```

# Question 5

```
H       BYTE    10
I       BYTE    10

        LDX     #0
LOOP    LDA     H, X
        STA     I, X
        TIX     #10
        JLT     LOOP
```

# Question 6

```
YBASE   RESW 200

        LDX     #0
        LDS     #3
        LDT     #600
LOOP    LDA     YBASE, X
        MUL     #3
        STA     YBASE, X

        ADDR    S, X
        COMPR   X, T
        JLT     LOOP
```

# Question 7

```
N       RESW    100

        LDX     #0
        LDS     #3

        
LOOP    LDA     N, X    A <- N[j - 1]

        ADDR    S, X
        RMO     X, T
        ADDR    S, X
        ADD     N, X    A <- A + N[j + 1]
        RMO     T, S
        STA     N, X    A -> A + N[j]

        ADDR    S, X
        LDT     #300
        COMPR   X, T
        JLT     LOOP
```

# Question 8

```
INDEV   EQU     F1
OUTDEV  EQU     05
        
LOOP    TD      INDEV
        JEQ     LOOP
        RD      INDEV

        TD      OUTDEV
TEST    JEQ     TEST
        WD      OUTDEV

        J       LOOP
```

# Question 9

```
DATA    RESW    100

        LDX     #0
        LDS     #3
        LDT     #300
LOOP    LDA     DATA, X
        MUL     #2
        STA     YBASE, X

        ADDR    S, X
        COMPR   X, T
        JLT     LOOP
```

# Question 10

```
DATA    RESW    150
NZERO   RESW    1

        LDX     #0
        LDS     #3
        LDT     #450

LOOP    LDA     DATA, X
        COMP    #0
        JEQ     SKIP

        LDA     NZERO
        ADD     #1
        STA     NZERO

SKIP    ADDR    S, X
        COMPR   X, T
        JLT     LOOP
```

