from hero import Hero

if __name__ == '__main__':
    hero1 = Hero("Gerry",100,30,50)
    hero2 = Hero("Mogi",100,70,30)

    hero1.attack(hero2)
    print('\n')
    hero2.attack(hero1)