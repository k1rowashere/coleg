DAC     EQU     3FD8h

CODE    SEGMENT
        ASSUME  CS:CODE, DS:CODE


START:  mov     dx, DAC
        mov     al, 26h

        mov     cx, 0100h   
J1:     out     dx, al
        loop    J1

        mov     al, 0c0h    ; 7.5V
J2:     out     dx, al
        dec     al
        cmp     al, 80h     ; 5V
        jg      J2

        mov     cx, 0080h
J3:     out     dx, al
        loop    J3
        
J2:     out     dx, al
        inc     al
        cmp     al, 0c0h    ; 7.5V
        jl      J4      
        jmp     START

CODE    ENDS
        END     START
