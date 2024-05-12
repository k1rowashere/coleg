DAC     EQU     3FD8h

CODE    SEGMENT
        ASSUME  CS:CODE, DS:CODE


START:  mov     dx, DAC

        mov     al, 92h     ; 5.5V
J1:     out     dx, al
        inc     al
        cmp     al, 0F3h    ; 9.5V
        jl      J1

J2:     out     dx, al
        dec     al
        cmp     al, 5Ah     ; 3.5V
        jg      J2

        mov     cx, 0500h
J3:     out     dx, al
        loop    J3
        
        mov     al, 26h     ; 1.5V
        jmp     START

CODE    ENDS
        END     START
