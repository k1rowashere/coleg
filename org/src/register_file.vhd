library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity register_file is
    port(
        rr1, rr2, wr: in std_logic_vector(4 downto 0);
        write: in std_logic;
        data_in: in std_logic_vector(31 downto 0);
        data_out1, data_out2: out std_logic_vector(31 downto 0);
        reset: in std_logic;
        clk: in std_logic
    );
    type registers is array(31 downto 0) of std_logic_vector(31 downto 0);
end register_file;


architecture rtl of register_file is
    signal reg_file: registers;
begin
    process(clk)
    begin
        if (reset = '1') then
            for i in 0 to 31 loop
                reg_file(i) <= (others => '0');
            end loop;
        end if;

        if rising_edge(clk) then
            if (write = '1') then
                reg_file(to_integer(unsigned(wr))) <= data_in;
            end if;
            data_out1 <= reg_file(to_integer(unsigned(rr1)));
            data_out2 <= reg_file(to_integer(unsigned(rr2)));
        end if;
    end process;
end rtl;
