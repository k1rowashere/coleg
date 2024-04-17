library ieee;
use ieee.std_logic_1164.all;

entity tb is
end tb;

architecture sim of tb is
    signal i_tb, rl_tb, clk_tb : std_logic;
    signal q_tb : std_logic_vector(3 downto 0);

    constant PERIOD : time := 50 ns;

begin
  dut: entity work.shift_register
    port map (
      i => i_tb,
      q => q_tb,
      rl => rl_tb,
      clk => clk_tb
    );

    clk_process : process
    begin
        while (true) loop
            clk_tb <= '0';
            wait for PERIOD / 2;
            clk_tb <= '1';
            wait for PERIOD / 2;
        end loop;
    end process;

    -- Stimulus process
    stimulus_process: process
    begin
        -- Initialize inputs
        i_tb <= '0'; 
        rl_tb <= '0';

        -- Wait 100 ns for global reset to finish
        wait for 100 ns;

        -- Test case 1
        i_tb <= '1'; wait for PERIOD;
        i_tb <= '0'; wait for PERIOD;
        i_tb <= '1'; wait for PERIOD;
        i_tb <= '0'; wait for PERIOD;
        i_tb <= '0'; wait for PERIOD;
        i_tb <= '1'; wait for PERIOD;
        i_tb <= '1'; wait for PERIOD;

        wait;
    end process;
end sim;
