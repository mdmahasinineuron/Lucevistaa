class Mamals:
    __limph = 4

    def __init__(self,speacis,lifespan):
        speacis = speacis
        lifespan = lifespan

    def change_limph_to10(self):
        self.limph = 10

    def change_limph_to20(self):
        self.limph = 20




mamals1 = Mamals("dog",12)
mamals1.change_limph_to10()
mamals1.change_limph_to20()

mamals2 = Mamals("human",70)

print(mamals1.limph)