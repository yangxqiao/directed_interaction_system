from transitions import Machine


class StateMachine:

    def __init__(self, states, transtions, initial):

        self.machine = Machine(model=self, states=states, transitions=transtions, initial=initial, auto_transitions=False)

    def get_transitions(self):
        return self.machine.get_triggers(self.state)

    def get_state(self):
        return self.state

    def do_transition(self, transition):
        try:
            self.trigger(transition)
            return True
        except AttributeError:
            return False
