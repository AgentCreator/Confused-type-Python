Confused: type = type('Confused', (), {
    'marriages': {},
    '__init__': (lambda self, *args: setattr(self, "args", [*args])),
    'get_instance_name': lambda self: next((name for name, val in globals().items() if val is self), None).title(),
    'get_conf_lvl': lambda self: "not that confused" if self.args[0] < 4 else "pretty confused" if self.args[0] < 8 else "very confused",
    'set_conf_lvl': lambda self, num: setattr(self, "args", [num, self.args[1:]]),
    'get_info': lambda self: f"{getattr(self, 'get_instance_name')().title()} is {self.get_conf_lvl()} because {self.args[-1]}" + ("\nand because he use linux...\nand because he programs..." if self.args[2] and self.args[1] else "\nand because he uses linux..." if self.args[2] else "\nand because he programs..." if self.args[1] else ''),
    '__str__': lambda self: __import__('cowsay', globals(), locals(), ["get_output_string"], 0).get_output_string('tux' if self.args[2] else 'miki', f'hello, I am a {self.get_conf_lvl()} {self.get_instance_name().title()}!'),
    '__repr__': lambda self: f"Confused( args = [confusion_level = f{self.args[0]}, is_programmer = {self.args[1]}, is_using_linux = {self.args[2]}, cause = \"{self.args[3]}\"])",
    'diconfuse': lambda self, what: f"sorry {self.get_instance_name()}, but you are too confused to understand my explanation.",
    'disband_marriage': lambda self, p1, p2: setattr(Confused, "marriages", dict(list(filter(lambda x: not ((x[0] == p1 and x[1] == p2) or (x[1] == p1 and x[0] == p2)), self.marriages.items())))),
    'update_marriages': lambda self, p1, p2: self.marriages.update({p1 : p2}),
    'switch_is_programmer': lambda self: setattr(self, "args", [self.args[0]]+[not self.args[1]]+self.args[1:]),
    'switch_is_linux_user': lambda self: setattr(self, "args", [*self.args[:1]]+[not self.args[2]]+self.args[2:]),
    '__add__': lambda self, wife_or_husband: self.update_marriages(self.get_instance_name(), wife_or_husband.get_instance_name()) or f"{self.get_instance_name()} + {wife_or_husband.get_instance_name()} = ♥️",
    '__sub__': lambda self, wife_or_husband: (self.disband_marriage(self.get_instance_name(), wife_or_husband.get_instance_name()) or f"{self.get_instance_name()} - {wife_or_husband.get_instance_name()} = 💔"),
    'get_reason': lambda self: self.args[-1]

})
#example
Cody: Confused = Confused(10, True, True, "He doesn't understand what is going on in that snippet beyond that you're importing & then accessing something xd")
