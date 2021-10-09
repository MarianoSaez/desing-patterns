from ConcreteCreators import RandomProductCreator, OnlyLegendaryProductCreator


if __name__ == "__main__":
    print("Iniciando fabricas!")
    random = RandomProductCreator()
    legendary = OnlyLegendaryProductCreator()
    print("Generando un producto...")
    prod = random.factoryMethod()
    print(prod.nombre)
