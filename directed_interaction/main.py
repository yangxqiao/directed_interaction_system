from directed_interaction.StateHandler import StateHandler
from directed_interaction.StateMachine import StateMachine

if __name__ == '__main__':
    states = ['solid', 'liquid', 'gas', 'plasma']
    transitions = [
        ['melt', 'solid', 'liquid'],
        ['evaporate', 'liquid', 'gas'],
        ['sublimate', 'solid', 'gas'],
        ['ionize', 'gas', 'plasma'], ]

    initial = states[0]

    state_machine = StateMachine(states, transitions, initial)
    triggers = state_machine.get_transitions()
    print(state_machine.do_transition(triggers[0]))

    state_handler = StateHandler(states)


    def print_word(x):
        print(x)


    state_handler.add_states('a', [lambda: print_word(3)])
    state_handler.add_states(['c', 'd'], [lambda: print_word(2), lambda: print_word(3)])

    state_handler.run('a')
    state_handler.run('c')
    state_handler.run('solid')