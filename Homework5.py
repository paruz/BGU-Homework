import random
class Animal:
    def __init__(self, name, size, diet, habitat, lifespan, sex, satiety=100, age=0):
        self.name = name
        self.size = size
        self.diet = diet
        self.habitat = habitat
        self.lifespan = lifespan
        self.sex = sex
        self.satiety = satiety
        self.age = age

    def __str__(self):
        return (f'Вид: {self.name}\n'
                f'Размер: {self.size}\n'
                f'Тип питания: {self.diet}\n'
                f'Среда обитания: {self.habitat}\n'
                f'Срок жизни: {self.lifespan}\n'
                f'Возраст: {self.age}\n'
                f'Сытость: {self.satiety}\n'
                f'Пол: {self.sex}')


class Ecosystem:
    def __init__(self):
        self.animals = []
        self.plant_food = 1000

    def add_animal(self, animal):
        self.animals.append(animal)

    def increase_food(self, amount):
        self.plant_food += amount
        print(f'Текущий запас: {self.plant_food}')

    def reproduce(self, animal1, animal2):
        if animal1.name == animal2.name and animal1.sex != animal2.sex:
            if animal1.habitat == "Вода":
                if animal1.satiety > 50 and animal2.satiety > 50:
                    for i in range(5):
                        self.add_animal(Animal(animal1.name, animal1.size, animal1.diet,
                                               animal1.habitat, animal1.lifespan, animal1.sex, 23))
                        self.add_animal(Animal(animal2.name, animal2.size, animal2.diet,
                                               animal2.habitat, animal2.lifespan, animal2.sex, 23))
                    print(f'Появилось 10 новых животных типа: {animal1.name}')
                else:
                    print('Размножиться не получилось, не хватает сытости')

            elif animal1.habitat == "Воздух":
                if animal1.satiety > 42 and animal2.satiety > 42 and animal1.age > 3 and animal2.age > 3:
                    for i in range(2):
                        self.add_animal(Animal(animal1.name, animal1.size, animal1.diet,
                                               animal1.habitat, animal1.lifespan, animal1.sex, 64))
                        self.add_animal(Animal(animal2.name, animal2.size, animal2.diet,
                                               animal2.habitat, animal2.lifespan, animal2.sex, 64))
                        print(f'Появилось 4 новых животных типа: {animal1.name}')

                else:
                    print('Размножиться не получилось, не хватает сытости или возраста')
            else:
                if animal1.satiety > 20 and animal2.satiety > 20 and animal1.age > 5 and animal2.age > 5:
                    self.add_animal(Animal(animal1.name, animal1.size, animal1.diet,
                                           animal1.habitat, animal1.lifespan, animal1.sex, 73))
                    self.add_animal(Animal(animal2.name, animal2.size, animal2.diet,
                                           animal2.habitat, animal2.lifespan, animal2.sex, 73))
                    print(f'Появилось 2 новых животных типа: {animal1.name}')
                else:
                    print('Размножиться не получилось, не хватает сытости или возраста')
        else:
            print('Эти животные не могут размножаться')

    def simulate_time_step(self):
        new_animals = []
        animals_to_remove = []
        for animal in self.animals:
            animal.age += 1
            if animal.age >= animal.lifespan:
                if animal.size == "Большой":
                    self.increase_food(100)
                elif animal.size == "Средний":
                    self.increase_food(50)
                else:
                    self.increase_food(10)
                continue

            if animal.diet == "Растительная пища":
                if self.plant_food > 0:
                    self.plant_food -= 1
                    animal.satiety += 26
                else:
                    animal.satiety -= 9
            else:
                if random.random() < 0.5:
                    random_animal = random.choice(self.animals)
                    if random_animal != animal and random_animal.habitat == animal.habitat:
                        if random.random() < 0.5:
                            animals_to_remove.append(random_animal)
                            animal.satiety += 53
                        else:
                            animal.satiety -= 16
                else:
                    animal.satiety -= 9

            if animal.satiety < 10:
                if animal.size == "Большой":
                    self.increase_food(100)
                elif animal.size == "Средний":
                    self.increase_food(50)
                else:
                    self.increase_food(10)
            else:
                new_animals.append(animal)

        for animal in animals_to_remove:
            if animal in self.animals:
                self.animals.remove(animal)

        self.animals = new_animals


if __name__ == "__main__":
    ecosystem = Ecosystem()
    animals = [
        Animal("Лев", "Большой", "Мясо", "Земля", 12, "м", 100, 11),
        Animal("Лев", "Большой", "Мясо", "Земля", 12, "ж", 100, 11),
        Animal("Орел", "Средний", "Мясо", "Воздух", 20, "м", 100, 3),
        Animal("Орел", "Средний", "Мясо", "Воздух", 20, "ж", 100, 3),
        Animal("Золотая рыбка", "Маленький", "Растительная пища", "Вода", 10, "м"),
        Animal("Золотая рыбка", "Маленький", "Растительная пища", "Вода", 10, "ж"),
        Animal("Слон", "Большой", "Растительная пища", "Земля", 60, "м"),
        Animal("Слон", "Большой", "Растительная пища", "Земля", 60, "ж"),
        Animal("Кит", "Большой", "Мясо", "Вода", 90, "м"),
        Animal("Кит", "Большой", "Мясо", "Вода", 90, "ж"),
        Animal("Волк", "Средний", "Мясо", "Земля", 14, "м"),
        Animal("Волк", "Средний", "Мясо", "Земля", 14, "ж")
    ]

    for animal in animals:
        ecosystem.add_animal(animal)

    for i in range(len(ecosystem.animals)):
        print(f'\nЖивотное {str(i+1)}\n{ecosystem.animals[i]}')

    while True:
        print('\n\n1. Добавить особь')
        print('2. Увеличить запас растительной пищи')
        print('3. Посмотреть характеристики особи')
        print('4. Посмотреть характеристики всех особей')
        print('5. Размножить особей')
        print('6. Моделировать движение времени на 1 единицу')
        print('0. Выйти')
        choice = input('Введите номер действия: ')

        if choice == '1':
            species = input('Вид животного: ')
            size = input('Размер животного: ')
            diet = input('Тип питания: ')
            habitat = input('Среда обитания: ')
            lifespan = int(input('Срок жизни: '))
            sex = input('Пол: ')
            ecosystem.add_animal(Animal(species, size, diet, habitat, lifespan, sex))

        elif choice == '2':
            amount = int(input("Введите количество растительной пищи для добавления: "))
            ecosystem.increase_food(amount)

        elif choice == '3':
            n = int(input('Введите номер особи: '))
            if 1 <= n <= len(ecosystem.animals):
                print(f'\nЖивотное {str(n)}\n{ecosystem.animals[n-1]}')
            else:
                print('Неверный номер')

        elif choice == '4':
            for i in range(len(ecosystem.animals)):
                print(f'\nЖивотное {str(i + 1)}\n{ecosystem.animals[i]}')

        elif choice == '5':
            n1 = int(input('Введите номер первой особи: '))
            n2 = int(input('Введите номер второй особи: '))
            if 1 <= n1 <= len(ecosystem.animals) and 1 <= n2 <= len(ecosystem.animals):
                ecosystem.reproduce(ecosystem.animals[n1-1], ecosystem.animals[n2-1])
            else:
                print('Неверные номера')

        elif choice == '6':
            ecosystem.simulate_time_step()

        elif choice == '0':
            break

        else:
            print('Данного варианта нет')
