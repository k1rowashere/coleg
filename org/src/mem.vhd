library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity mem_4k is
    port(
        address: in std_logic_vector(31 downto 0);
        data_in: in std_logic_vector(31 downto 0);
        data_out: out std_logic_vector(31 downto 0);
        read, write: in std_logic;
        clk: in std_logic
    );
    type memory is array(1024*4 downto 0) of std_logic_vector(7 downto 0);
end entity;

architecture rtl of mem_4k is
    signal mem: memory;
begin
    process(clk)
        variable addr: integer;
    begin
        addr := to_integer(unsigned(address));
        if rising_edge(clk) then
            if read = '1' then
                data_out <= mem(addr) & mem(addr + 1) & mem(addr + 2) & mem(addr + 3);
            elsif write = '1' then
                mem(addr) <= data_in(7 downto 0);
                mem(addr + 1) <= data_in(15 downto 8);
                mem(addr + 2) <= data_in(23 downto 16);
                mem(addr + 3) <= data_in(31 downto 24);
            end if;
        end if;
    end process;
end rtl;
