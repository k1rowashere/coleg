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
