// a
p       WORD    4
q       WORD    3
res     RESW    1

        LDA     p
        MUL     q
        COMP    10
        JGT     THEN

ELSE    LDA     100
        STA     p
        LDA     200
        STA     q
        J       OUT

THEN    LDA     1
        STA     p     
        MUL     2
        STA     q

OUT     LDA     p
        ADD     q
        STA     res

//b
Y       WORD    8
Z       RESW    1
Q       RESW    1

        LDA     Y
        COMP    0
        JEQ     THEN

ELSE    LDA     16
        J       OUT

THEN    LDA     1

OUT     STA     Q
        STA     Z

        
//c

Y       RESW    1
Z       RESW    1
E       RESW    1

        LDA     Y
        ADD     7
        COMP    Z
        JGT     ELSE

THEN    LDA     Z
        RMO     A,S
        MULR    A,A
        MUL     10
        SUB     3
        MULR    S,A
        ADD     6
        STA     E

        RMO     S,A
        ADD     1
        STA     Z
        J       OUT


ELSE    LDA     Y
        SUB     Z
        MUL     5
        STA     E

        LDA     Z
        SUB     1
        STA     Z

OUT     ...     ...

//d

Y       RESW    1
Z       RESW    1
R       RESW    1

        LDA     Y
        ADD     3
        COMP    Z
        JGT     ELSE

THEN    LDA     Z
        MUL     10
        ADD     20
        STA     R

        LDA     Z
        ADD     1
        STA     Z
        J       OUT


ELSE    LDA     Y
        SUB     Z
        MUL     5
        STA     R

        LDA     Z
        SUB     1
        STA     Z

OUT     ...     ...



// e

Y       RESW    1
Z       WORD    15
R       RESW    1

        LDA     Y
        ADD     3
        COMP    Z
        JGT     ELSE

THEN    LDA     Z
        MUL     10
        ADD     20
        STA     R

        LDA     Y
        ADD     1
        STA     Z
        J       OUT


ELSE    LDA     Y
        SUB     Z
        STA     R

        LDA     Z
        SUB     1
        STA     Z

OUT     ...     ...



// f

P       RESW    1
Q       RESW    1
R       RESW    1
S       RESW    1

        LDA     P
        COMP    Q
        JGT     THEN

ELSE    LDA     3
        J       OUT

THEN    LDA     2

OUT     STA     R
        MUL     P
        STA     S


//g


P       RESW    1
Q       RESW    1
R       RESW    1

        LDA     P
        SUB     Q
        COMP    500
        JLT     ELSE

THEN    LDA     P
        SUB     5
        STA     P
        J       OUT

ELSE    LDA     Q
        ADD     2
        STA     Q


OUT     LDA     P
        MUL     Q
        STA     R


// h


P       RESW    1
Q       RESW    1
R       RESW    1
Z       RESW    1

        LDA     500
        SUB     Z
        RMO     A,S
        LDA     P
        SUB     Q
        COMPR   A,S
        JLT     ELSE

THEN    LDA     Z
        MULR    A,A
        MUL     3
        ADD     5
        MUL     Z
        ADD     Q
        STA     P
        J       OUT

ELSE    LDA     Q
        ADD     2
        STA     Q


OUT     LDA     P
        MUL     Q
        MUL     Z
        STA     R
