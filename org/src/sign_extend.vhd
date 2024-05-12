library ieee;
use ieee.std_logic_1164.all;
-- use ieee.numeric_std.all;

entity sign_extend is
    port(
        i: in std_logic_vector(15 downto 0);
        q: out std_logic_vector(31 downto 0)
    );
end entity;


architecture rtl of sign_extend is
begin
    process
    begin
        if i(15) = '0' then
            q <= X"0000" & i;
        else
            q <= X"FFFF" & i;
        end if;
    end process;
end architecture;
