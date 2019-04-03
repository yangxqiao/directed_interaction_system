class StateHandler:

    def __init__(self, states, funcs=None):
        self.states_to_func = dict()
        self.add_states(states, funcs)

    def run(self, state):
        if state not in self.states_to_func:
            raise KeyError
        else:
            for func in self.states_to_func[state]:
                func()

    def _add_state(self, state, func=None):
        self.states_to_func[state] = []
        if func is not None:
            self._add_func(state, func)

    def add_states(self, states, funcs=None):

        if type(states) is not list:
            states = [states]
        if funcs is not None and type(funcs) is not list:
            funcs = [funcs]

        if (funcs is not None) and (len(states) != len(funcs)):
            raise IOError("The number of states and functions must be equal")

        for i in range(len(states)):
            if funcs is None:
                self._add_state(states[i])
            else:
                self._add_state(states[i], funcs[i])

    def _add_func(self, state, func):
        if not callable(func):
            raise TypeError("The function is not callable: '%s'" % func)
        elif state in self.states_to_func:
            self.states_to_func[state].append(func)
        else:
            self._add_state(state, func)

    def add_funcs(self, state, funcs):
        if type(funcs) is not list:
            funcs = [funcs]
        for i in range(len(funcs)):
            self._add_func(state, funcs[i])

    def _rm_state(self, state):
        if state not in self.states_to_func:
            raise KeyError
        else:
            del (self.states_to_func[state])

    def rm_states(self, states):
        for i in range(len(states)):
            self._rm_state(states[i])

    def clear_func(self, state):
        if state not in self.states_to_func:
            raise KeyError
        else:
            self.states_to_func[state] = []
