class Actor:
    def __init__(self, actor_full_name=None):
        self.actor_full_name = actor_full_name
        self.actor_colleague = []

    @property
    def actor_full_name(self):
        return self._actor_full_name

    @property
    def actor_colleague(self):
        return self._actor_colleague

    @actor_colleague.setter
    def actor_colleague(self, listOfActors):
        if type(listOfActors) != list: listOfActors = []
        isFullListActors = True
        for anActor in listOfActors:
            if not isinstance(anActor, Actor):
                isFullListActors = False
        if isFullListActors:
            self._actor_colleague = listOfActors

    @actor_full_name.setter
    def actor_full_name(self, value):
        if type(value) != str: value = "None"
        if value == "": value = "None"
        self._actor_full_name = value

    def add_actor_colleague(self, colleague):
        if isinstance(colleague, Actor): self.actor_colleague.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.actor_colleague

    def __repr__(self):
        return f"<Actor {self.actor_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Actor): return False
        return self.actor_full_name == other.actor_full_name

    def __lt__(self, other):
        return self.actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.actor_full_name)
