CNT3    EQU 3FD6H       ; Define 8255 control word port address
BPORT3  EQU 3FD2H       ; Define 8255 portB address
CODE    SEGMENT
ASSUME  CS:CODE, DS:CODE

START:  MOV     SP, 4000H   ; Setup stack pointer
        MOV     AL, 90H     
        MOV     DX, CNT3    ; Enable 8255 control word
        OUT     DX, AL      ; Output data 90H to 8255 control port

        MOV     DX, BPORT3
        MOV     AL, 01H
J1:     OUT     DX, AL
        ROL     AL, 1
        ADD     AL, 01H

        MOV     CX, 0A00H
        LOOP    $           ; Delay loop
        
        CMP     AL, 0FFH
        JNE     J1

        MOV     AL, 03H
J2:     OUT     DX, AL
        SHL     AL, 1
        SHL     AL, 1

        MOV     CX, 0A00H
        LOOP    $           ; Delay loop

        JNZ     J2
        JMP     J1

CODE    ENDS
        END START
