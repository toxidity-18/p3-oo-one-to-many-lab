class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []
    
    def pets(self):
        """Returns a full list of the owner's pets."""
        return self.pets_list
    
    def add_pet(self, pet):
        """Adds a pet to the owner's list of pets if the pet is an instance of Pet."""
        if not isinstance(pet, Pet):
            raise TypeError("The pet must be an instance of Pet.")
        if pet not in self.pets_list:
            self.pets_list.append(pet)
            pet.owner = self
    
    def get_sorted_pets(self):
        """Returns a sorted list of pets by their names."""
        return sorted(self.pets_list, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        # Add this pet to the class variable all
        Pet.all.append(self)

    def __repr__(self):
        return f"{self.name} ({self.pet_type})"
