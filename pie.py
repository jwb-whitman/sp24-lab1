class Pie:
  def __init__(self, name, filling, crust):
    self.name = name
    self.filling = filling
    self.crust = crust

p1 = Pie("Key lime", "lime custard", "graham cracker")
p2 = Pie("Cherry", "cherry compote", "traditional pie dough")

print(p1.name)
print(p1.filling)
print(p1.crust)
