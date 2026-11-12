"""
Cesar Silguero
CS 313E Project
11/11/26
"""

import csv

class Shoe:
    """
    Stores individual shoe data and processes it to get
    distance and mechanical stress values.
    """

    def __init__(self, model_name):
        self.model_name = model_name
        self.mileage = 0.0
        self.stress = 0.0

    def add_run(self, distance, pace):
        """
        Determines mechanical stress and added mileage
        Stress is determined by a factor of 10/pace so the larger the pace,
        the less stress added.
        Stress is determined directly by the distance.
        """

        stress_factor = 10 / pace
        self.stress += (stress_factor * distance)
        self.mileage += distance

    def __str__(self):
        return (
            f"Shoe: {self.model_name: <18} | "
            f"Total Mileage: {self.mileage: >5.2f} | "
            f"Stress: {self.stress: >6.2f}"
        )

class Fatigue:
    """
    Process the run data from the csv file and creates Shoe objects for each shoe.
    It loops through the different run entries and adds everything to the object.
    """

    def __init__(self):
        self.inventory = {}

    def load_runs(self, filename):
        """
        Receives run data and sends it to the class to process
        """

        with open(filename, mode = 'r', encoding = "utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Model']
                distance = float(row['Distance'])
                pace = float(row['Pace'])

                if name not in self.inventory:
                    self.inventory[name] = Shoe(name)

                self.inventory[name].add_run(distance, pace)

    def sort_stress(self):
        """
        Sorts the shoes by stress levels
        """

        shoes = list(self.inventory.values())
        n = len(shoes)

        for i in range(n):
            for j in range(0, n - i - 1):
                if shoes[j].stress < shoes[j + 1].stress:
                    shoes[j], shoes[j + 1] = shoes[j + 1], shoes[j]

        return shoes

if __name__ == "__main__":
    fatigue_tracker = Fatigue()

    fatigue_tracker.load_runs("running_log.csv")

    print("SHOE REPLACEMENT TRACKER")
    for shoe in fatigue_tracker.sort_stress():
        print(shoe)
