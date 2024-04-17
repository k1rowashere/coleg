library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity shift_register is
    port(
        i: in std_logic;
        q: out std_logic_vector(3 downto 0);
        rl: in std_logic; -- Right (1)/left
        clk: in std_logic
    );
end shift_register;


architecture rtl of shift_register is
    signal temp: std_logic_vector(3 downto 0) := "0000";
begin
    process(clk)
    begin
        if rising_edge(clk) then
            if (rl = '1') then
                temp <= i & temp(3 downto 1);
            else
                temp <= temp(2 downto 0) & i;
            end if;
            q <= temp;
        end if;
    end process;
end rtl;
