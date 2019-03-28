from transitions import Machine


class StateHandler(object):
    def __init__(self, *args):
        self.states = args

        def build_on_enter(*args):

            def on_enter():
                if len(args) == 1:
                    print(args[0])
                elif len(args) >= 2:
                    for i in range(len(args)-1):
                        print(str(i + 1) + ". " + args[i+1])
                    user_input = int(input(args[0]))
                    return args[user_input]

            return on_enter

        self.on_enter_awake = build_on_enter("How are you today?\n", "good", "bad")


class NarcolepticSuperhero(object):

    def __init__(self, name):
        self.name = name

        self.machine = Machine(model=self, initial='awake', auto_transitions=False)

        self.machine.add_states(['awake', 'hanging_out', 'stay_at_home'])
        self.machine.add_transition(trigger='good', source='awake', dest='hanging_out')
        self.machine.add_transition(trigger='bad', source="awake", dest='stay_at_home')


my_dict = {
    "awake": "on_enter_awake",
}

batman = NarcolepticSuperhero("Batman")

test = StateHandler('awake', 'hanging_out', 'stay_at_home')

for key in my_dict:
    if batman.state == key:
        trigger = getattr(test, my_dict[key])()
        getattr(batman, trigger)()
        break

print(batman.state)