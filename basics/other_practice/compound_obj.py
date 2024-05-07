# # THE MENU

# Define the first level
level1 = {
    '01 - Statistics': None,
    '02 - Economics': None,
    '03 - Machine Learning': None,
    '04 - DashBoards': None
}

# Define the second level (related to Statistics)
Statistics = {
    '01 - Measures of Tendency': None,
    '02 - Measures of Dispersion': None,
    '03 - Probability': None
}

# Define the third level (related to Measures of Tendency)
Measures_of_Tendency = {
    '01 - Mean': None,
    '02 - Mode': None,
    '03 - Median': None
}

# Define the fourth level (related to Mean)
Mean = {
    '01 - Average Height': lambda: print("Calculating Average Height..."),
    '02 - Average Test Score': lambda: print("Calculating Average Test Score..."),
    '03 - Final Score': lambda: print("Calculating Geometric Mean...")
}

# Now let's build a class to manage the structure
class MenuStructure:
    def __init__(self):
        self.levels = {}
    
    def add_level(self, level_name, content):
        self.levels[level_name] = content
    
    def get_level(self, level_name):
        return self.levels.get(level_name, None)
    
    def display_options(self, level_name):
        level = self.get_level(level_name)
        if level:
            for key, value in level.items():
                print(key)
        else:
            print(f"No options for {level_name}")

# Create a menu structure and add levels to it
menu = MenuStructure()
menu.add_level("level1", level1)
menu.add_level("Statistics", Statistics)
menu.add_level("Measures_of_Tendency", Measures_of_Tendency)
menu.add_level("Mean", Mean)

# Test by displaying the first level and then drilling down
print("Main Menu:")
menu.display_options("level1")

print("\nStatistics Sub-Menu:")
menu.display_options("Statistics")

print("\nMeasures of Tendency:")
menu.display_options("Measures_of_Tendency")

print("\nMean Options:")
menu.display_options("Mean")

# Call a specific function from the last level
Mean['01 - Average Height']()
