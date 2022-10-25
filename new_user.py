
class User():
    def __init__(self, first_name, last_name):
        """ function creates first_name, last_name 

        Args:
            first_name (str): first name
            last_name (str): last name
        """
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name

    def describe_user(self):
        """prints formatted first name and last name
        """
        print(
            f"First name: {self.first_name.title()}.\nLast name: {self.last_name.title()}")

    def greet_user(self):
        """prints greetings of user
        """
        print(f"Greetings {self.full_name.title()}.")


new_user = User("Karola", "Nowak")
new_user.describe_user()
new_user.greet_user()
