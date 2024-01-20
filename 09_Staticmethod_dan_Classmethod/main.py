from hero import Hero

"""
    Creating top level code environment
    a top level code environment is an
    entry point to the program and where
    your program needs to get executed
    the script directly not when being
    imported
"""
if __name__ == '__main__':
    gerry = Hero("Gerry",100)
    mogi = Hero("Mogi",-1)

    print(f"Hero's name: {gerry.getName}")
    print(f"Hero's health: {gerry.getHealth}")

    Hero.isLow(mogi.getHealth)
    print(f"Totals objects that are made = {Hero.getTotal()}")