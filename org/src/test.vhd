library ieee;
use ieee.std_logic_1164.all;

entity tb is
end tb;

architecture sim of tb is
    signal i_tb: std_logic_vector(15 downto 0);
    signal q_tb: std_logic_vector(31 downto 0);
    -- signal clk_tb: std_logic;

    constant PERIOD : time := 100 ns;

begin
  dut: entity work.sign_extend
    port map (
      i => i_tb,
      q => q_tb
    );

    -- clk_process : process
    -- begin
    --     while (true) loop
    --         clk_tb <= '0';
    --         wait for PERIOD / 2;
    --         clk_tb <= '1';
    --         wait for PERIOD / 2;
    --     end loop;
    -- end process;

    -- Stimulus process
    stimulus_process: process
    begin
        i_tb <= X"FF00"; wait for PERIOD;
        i_tb <= X"00FF"; wait for PERIOD;
        i_tb <= X"FF00"; wait for PERIOD;
        i_tb <= X"00FF"; wait for PERIOD;


        wait;
    end process;
end sim;
