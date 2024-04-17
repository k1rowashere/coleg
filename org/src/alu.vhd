library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity alu is
    port(
        a, b: in std_logic_vector(31 downto 0);
        op: in std_logic_vector(3 downto 0);
        res: inout std_logic_vector(31 downto 0);
        z: out std_logic
    );
end entity;

-- 32 bit ALU
-- op:
-- 0000: AND
-- 0001: OR
-- 0010: ADD
-- 0011: SUB
-- 0100: MUL
-- 0101: DIV
-- 0110: NOR
-- 0111: SLT (res = a < b)

architecture behaviour of alu is
    signal ia, ib: integer;
    signal temp: std_logic_vector(31 downto 0);
begin
    ia <= to_integer(signed(a));
    ib <= to_integer(signed(b));

    temp <= X"00000001" when ia < ib else X"00000000";

    with op select
    res <= (a and b) when "0000", 
           (a or b)  when "0001", 
           std_logic_vector(to_signed(ia + ib, 32)) when "0010", 
           std_logic_vector(to_signed(ia - ib, 32)) when "0011", 
           std_logic_vector(to_signed(ia * ib, 32)) when "0100", 
           std_logic_vector(to_signed(ia / ib, 32)) when "0101", 
           (not (a or b)) when "0110", 
           temp           when "0111", 
           X"00000000"    when others;

    z <= '1' when res = X"00000000" else '0';
end behaviour;



library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity alu_tb is
end entity;

architecture tb_arch of alu_tb is
    component alu is
        port (
            a, b: in std_logic_vector(31 downto 0);
            op: in std_logic_vector(3 downto 0);
            res: inout std_logic_vector(31 downto 0);
            z: out std_logic
        );
    end component;

    signal a, b, res: std_logic_vector(31 downto 0) := (others => '0');
    signal op: std_logic_vector(3 downto 0);
    signal z: std_logic;

begin
    uut: alu port map (
        a => a,
        b => b,
        op => op,
        res => res,
        z => z
    );

    stimulus: process
    begin
        -- Test 1: AND operation
        a <= x"FFFFFFFF";
        b <= x"0000FFFF";
        op <= "0000";
        wait for 10 ns;


        -- Test 2: OR operation
        a <= x"00000010";
        b <= x"00000020";
        op <= "0001";
        wait for 10 ns;

        -- -- Test 3: ADD operation
        -- a <= x"00000010";
        -- b <= x"00000001";
        -- op <= "0010";
        -- wait for 10 ns;

        -- -- Test 4: SUB operation
        -- a <= x"80000000";
        -- b <= x"00000001";
        -- op <= "0011";
        -- wait for 10 ns;

        -- -- Test 5: MUL operation
        -- a <= x"00000005";
        -- b <= x"00000004";
        -- op <= "0100";
        -- wait for 10 ns;

        -- Test 6: DIV operation
        a <= x"0000FFFF";
        b <= x"0000000F";
        op <= "0101";
        wait for 10 ns;

        -- Test 7: NOR operation
        a <= x"FFFFFFFF";
        b <= x"00000000";
        op <= "0110";
        wait for 10 ns;

        -- Test 8: SLT operation
        a <= x"00000001";
        b <= x"00000002";
        op <= "0111";
        wait for 10 ns;

        wait;
    end process;
end tb_arch;


