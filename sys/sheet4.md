# System Programming | Sheet 4

Kyrollos Youssef - 8057

# Question 1:

## a.

```
Q   RESW    1
R   RESW    1
U   RESW    1

FUN LDA     Q
    MULR    A, A
    MUL     Q
    MUL     #5
    ADD     R
    STA     U
    RSUB
```

## b.

```
QQ  RESW    1
RR  RESW    1
UU  RESW    1

    LDA     QQ
    STA     Q
    LDA     RR
    STA     R

    JSUB    FUN

    LDA     U
    STA     UU
```

# Question 2:

## a.

```
P   RESW    1
Q   RESW    1
R   RESW    1

FUN LDA     P
    COMP    Q
    JGT     DO

ELS LDA     P
    ADD     #10
    MUL     Q
    ADD     20
    J       OUT

DO  MULR    A, A
    ADD     15

OUT STA     R
    RSUB

```

## b.

```
AP  RESW    1
AQ  RESW    1
AR  RESW    1

    LDA     AP
    STA     P
    LDA     AQ
    STA     Q

    JSUB    FUN

    LDA     R
    STA     AR
```

# Question 3:

```
N   RESW    1
R   RESW    1

FUN LDA     N
    MULR    A, A
    MUL     #10
    SUB     5
    STA     @R
    RSUB
```

# Question 4:

## a.

```
P   RESW    1
Q   RESW    1

FUN LDA     Q
    MUL     #10
    ADD     #20
    MUL     Q
    ADD     #30
    MUL     Q
    ADD     #40
    STA     P
    RSUB
```

## b.

```
AP  RESW    1
AQ  RESW    1

    LDA     AP
    STA     P

    JSUB    FUN

    LDA     Q
    STA     AQ
```

# Question 5:

## a.

```
P1  RESW    1
P2  RESW    1
C   RESW    1

FUN LDA     @P1
    ADD     C
    STA     @P1

    LDA     @P2
    SUB     C
    STA     @P2
    RSUB
```

## b.

```
...
PA1 RESW    1
PA2 RESW    1

    LDA     @PA1
    STA     P1

    LDA     @PA2
    STA     P2

    LDA     #057
    STA     C

    JSUB    FUN
```

# Question 6:

## a.

```
P   RESW    1
Q   RESW    1

FUN LDA     @P
    MUL     #2
    ADD     #3
    MUL     @P
    ADD     #4

    STA     @Q
    RSUB
```

## b.

```
...
PPP RESW    1
QQQ RESW    1

    LDA     @PPP
    STA     P

    LDA     @QQQ
    STA     Q

    JSUB    FUN
```

# Question 7:

## a.

```
P       RESW    1
Q       RESW    1

CUBE    LDA     @P
        MULR    A, A
        MUL     @P

        STA     @Q
        RSUB
```

## b.

```
...
XXX     RESW    1
YYY     RESW    1

        LDA     @XXX
        STA     P

        LDA     @YYY
        STA     Q

        JSUB    CUBE
```

# Question 8:

```
P       RESW    1
Q       RESW    1

U       RESW    1
V       RESW    1


START   LDA     @U
        STA     P

        LDA     @V
        STA     Q

        JSUB    SWAP

SWAP    LDA     @P
        LDS     @Q

        STA     @Q
        STS     @P

        RSUB
```

# Question 9:

> skipped

# Question 10:

1. TRUE
1. FALSE
1. FALSE
1. FALSE
1. FALSE
1. FALSE
1. FALSE

# Question 11:

a. `BASE` directive must be used first.
b. X'ABCDE' is $5 * 4 = 20 bits$ not mutliple of 8 (even # of hex digits).
c. Can't store in a literal.
d. L4 and L6 used before declaration.

# Question 12:

a. _Direct_: TA = 150 Operand = (150) = 20
b. _Indirect_: TA = 150 Operand = ((150)) = (20)
c. _Immediate_: TA = N/A Operand = 150
d. _PC relative_: TA = (PC) + 150 = 853 Operand = (853)
e. _Base relative_: TA = (B) + 150 = 230 Operand = (230)
f. _Indexed_: TA = 150 + (X) = 270 Operand = (270)

# Question 13:

a. The assembler desides based on the `BASE` and `NOBASE` directives.

b. By having a `+` before the mnemonic.

```
X    RESW    1
     ADD     X   format-3
     +ADD    X   format-4
```

# Question 14:

a. 0x0080 + 100 \* 3 = 0x01AC
b. 100 = 0x0064

# Question 15:

|---|---|---|
|Symbol|Value|Absolute / Relocatable|
|---|---|---|
|XXX|0x30|Rel|
|YYY|0x30 + 3 = 0x33 |Rel|
|WWW|0x33 + 2024 = 0x81B |Rel|
|ZZZ|0x17EB - 0x30 = 0x7EB |Abs|
|RRR|_ERROR: cannot add relative locations_| - |
|ZZZ|0x17BB + 0xA = 0x7F2 |Abs|
|---|---|---|
