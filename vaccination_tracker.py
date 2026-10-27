"""
PROG211 - OOP 1 Individual Assignment
Domain  : Health - Vaccination Tracker
DPG     : Open-source, inclusive, privacy-respecting (no names/addresses stored),
          modular and reusable.
"""

from datetime import date


class Vaccine:
    """A vaccine type (Task 1: class #1)."""

    def __init__(self, name, doses_required):
        self.name = name
        self.doses_required = doses_required

    def display_info(self):
        print(f"Vaccine: {self.name} | Doses required: {self.doses_required}")


class Recipient:
    """An ANONYMOUS vaccine recipient (Task 1: class #2).
    Privacy: only a code (e.g. 'R001') and an age group are stored."""

    AGE_GROUPS = ("infant", "child", "adult", "elderly")  # tuple (bonus)
    total_recipients = 0  # class attribute

    def __init__(self, recipient_id, age_group):
        if not Recipient.is_valid_age_group(age_group):
            raise ValueError(f"Age group must be one of {Recipient.AGE_GROUPS}")
        self.recipient_id = recipient_id
        self.age_group = age_group
        self.doses = []  # list of (vaccine_name, date) tuples
        Recipient.total_recipients += 1

    # ---- Instance methods ----
    def add_dose(self, vaccine, dose_date=None):
        """Record a dose, interacting with a Vaccine object."""
        if self.doses_taken(vaccine) >= vaccine.doses_required:
            print(f"{self.recipient_id}: already fully vaccinated for {vaccine.name}.")
            return
        self.doses.append((vaccine.name, dose_date or date.today()))
        print(f"{self.recipient_id}: {vaccine.name} dose recorded.")

    def doses_taken(self, vaccine):
        return sum(1 for name, _ in self.doses if name == vaccine.name)

    def is_fully_vaccinated(self, vaccine):
        return self.doses_taken(vaccine) >= vaccine.doses_required

    def display_info(self):
        print(f"ID: {self.recipient_id} | Age group: {self.age_group}")
        for name, d in self.doses:
            print(f"   - {name} on {d}")

    # ---- Class method ----
    @classmethod
    def get_total_recipients(cls):
        return cls.total_recipients

    # ---- Static method ----
    @staticmethod
    def is_valid_age_group(age_group):
        return age_group in Recipient.AGE_GROUPS


# ---- Task 2: ONE data structure (dictionary keyed by unique ID) ----
registry = {}


def add_recipient(recipient):
    """Add a Recipient object to the registry."""
    if recipient.recipient_id in registry:
        print("ID already exists.")
        return
    registry[recipient.recipient_id] = recipient


def display_all():
    """Display all records in the registry."""
    print("\n=== Vaccination Records ===")
    for recipient in registry.values():
        recipient.display_info()


def main():
    covid = Vaccine("COVID-19", 2)
    polio = Vaccine("Polio", 3)
    covid.display_info()
    polio.display_info()
    print()

    add_recipient(Recipient("R001", "adult"))
    add_recipient(Recipient("R002", "child"))
    add_recipient(Recipient("R003", "elderly"))

    registry["R001"].add_dose(covid)
    registry["R001"].add_dose(covid)
    registry["R001"].add_dose(covid)  # blocked: already complete
    registry["R002"].add_dose(polio)

    display_all()
    print("\nR001 fully vaccinated (COVID-19)?", registry["R001"].is_fully_vaccinated(covid))
    print("Total recipients:", Recipient.get_total_recipients())
    print("Valid age group 'teen'?", Recipient.is_valid_age_group("teen"))


if __name__ == "__main__":
    main()
