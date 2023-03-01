"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    # Define the constructor method for the class
    def __init__(self, start=0):
        # Initialize the start value and the next value to the start value
        self.start = self.next = start

    # Define a method to return a string representation of the object
    def __repr__(self):
        # Return a formatted string with the start and next values
        return f"<SerialGenerator start={self.start} next={self.next}>"

    # Define a method to generate the next serial number
    def generate(self):
        # increment the value of self.next by 1
        self.next += 1
        # Subtract 1 from the next value and return the result
        return self.next - 1

    # Define a method to reset the next value to the start value
    def reset(self):
        self.next = self.start
