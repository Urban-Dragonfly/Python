from faker import Faker
import random
class VisitCard:
    def __init__(self, name, family_name, phone_number, email):
        self.name = name
        self.family_name = family_name
        self.phone_number = phone_number
        self.email = email

        # Variable to store length of the name and family name
        self._full_name_length = ""

    @property
    def full_name_length(self):
        self._full_name_length = f"{len(self.name)} {len(self.family_name)}"
        return self._full_name_length
    def __str__(self):
        return (f"{self.name} {self.family_name}, phone: {self.phone_number}, email: {self.email}")
    def __repr__(self):
        return f"VisitCard(name={self.name}, family_name={self.family_name}, phone_number={self.phone_number}, email={self.email}, full_name_length={self.full_name_length})"
    def contact(self):
        print(f"Kontaktuję się z {self.name} {self.family_name} pod numerem {self.phone_number}")

class BusinessCard(VisitCard):
    def __init__(self, position, company_name, work_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.work_phone_number = work_phone_number
        
    def contact(self):
        print(f"Kontaktuję się z {self.name} {self.family_name} pod numerem {self.work_phone_number} w {self.company_name}")

# Test selection of random visit cards
card_type = random.choice([True, False])
card_id = random.randint(0, 9)

# Function to generate fake visit cards
def generate_fake_visitcards(card_type, n=10):
    fake = Faker('pl_PL')
    fake_visitcards = []
    if card_type:
        for _ in range(n):
            fake_visitcards.append(VisitCard(
                name=fake.first_name(),
                family_name=fake.last_name(),
                phone_number=fake.phone_number(),
                email=fake.email(),))
        return fake_visitcards
    else:
        for _ in range(n):
            fake_visitcards.append(BusinessCard(
                name=fake.first_name(),
                family_name=fake.last_name(),
                phone_number=fake.phone_number(),
                email=fake.email(),
                position=fake.job(),
                company_name=fake.company(),
                work_phone_number=fake.phone_number(),))
        return fake_visitcards

# Generate 10 fake visit cards
visitcards = generate_fake_visitcards(card_type)

# Display the visit cards
for card in visitcards:
    print(card)
print()

# Contact the selected visit card
card = visitcards[card_id]
card.contact()
print(card.full_name_length)

# # Sort the visit cards by name, family name and email
# by_name = sorted(visitcards, key=lambda x: x.name)
# by_family_name = sorted(visitcards, key=lambda x: x.family_name)
# by_email = sorted(visitcards, key=lambda x: x.email)
# print("\nSorted by name:\n" + "\n".join(map(str, by_name)))
# print("\nSorted by family name:\n" + "\n".join(map(str, by_family_name)))
# print("\nSorted by email:\n" + "\n".join(map(str, by_email)))
