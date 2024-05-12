CNT3    EQU 3FD6H       ; Define 8255 control word port address
BPORT3  EQU 3FD2H       ; Define 8255 portB address
CODE    SEGMENT
ASSUME  CS:CODE, DS:CODE

START:  MOV     SP, 4000H   ; Setup stack pointer
        MOV     AL, 90H     
        MOV     DX, CNT3    ; Enable 8255 control word
        OUT     DX, AL      ; Output data 90H to 8255 control port

        MOV     DX, BPORT3

J1:     MOV     AL, 95H
        OUT     DX, AL
        
        MOV     CX, 0A00H
        LOOP    $           ; Delay loop

        MOV     AL, 7AH
        OUT     DX, AL

        MOV     CX, 0A00H
        LOOP    $           ; Delay loop
        JMP     J1

CODE    ENDS
        END START
