# Animal Shelter
from collections import deque


class AnimalShelter:

    def __init__(self):
        self.cat_queue = deque()
        self.dog_queue = deque()
        self.increment = 0

    def enqueue(self, animal, type):
        if type == 'dog':
            self.dog_queue.append((animal, self.increment))
        elif type == 'cat':
            self.cat_queue.append((animal, self.increment))
        else:
            raise Exception("The animal must be either a cat or a dog")

        self.increment += 1

    def dequeue_cat(self):
        if len(self.cat_queue) == 0:
            raise Exception("There are currently no cats available")
        return self.cat_queue.popleft()[0]

    def dequeue_dog(self):
        if len(self.dog_queue) == 0:
            raise Exception("There are currently no dogs available")
        return self.dog_queue.popleft()[0]

    def dequeue_any(self):
        if not self.cat_queue and not self.dog_queue:
            raise Exception("There are currently no animals available")
        elif not self.cat_queue:
            return self.dequeue_dog()
        elif not self.dog_queue:
            return self.dequeue_cat()

        if self.cat_queue[0][1] < self.dog_queue[0][1]:
            return self.dequeue_cat()
        else:
            return self.dequeue_dog()


if __name__ == "__main__":

    shelter = AnimalShelter()
    animals = [('cat1', 'cat'), ('cat2', 'cat'), ('dog1', 'dog'), ('cat3', 'cat'), ('dog2', 'dog'),
               ('dog3', 'dog'), ('cat4', 'cat'), ('cat5', 'cat'), ('dog4', 'dog')]

    for animal in animals:
        shelter.enqueue(animal[0], type=animal[1])

    print(shelter.dequeue_dog())
    print(shelter.dequeue_cat())
    print(shelter.dequeue_any())
    print(shelter.dequeue_any())
    print(shelter.dequeue_any())
    print(shelter.dequeue_any())
    print(shelter.dequeue_any())
    print(shelter.dequeue_any())
    print(shelter.dequeue_any())
