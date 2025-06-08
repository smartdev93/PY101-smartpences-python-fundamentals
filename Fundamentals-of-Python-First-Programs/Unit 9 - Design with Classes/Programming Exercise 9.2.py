"""
File: student.py
Project 9.2
Resources to manage a student's name and test scores.
Includes methods for comparisons and testing for equality.
Tests the class by putting students into random order in a list
and then sorting them.
"""
import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __lt__(self, other):
        """Returns self < other, with respect
        to names."""
        return self.name < other.name

    def __ge__(self, other):
        """Returns self >= other, with respect
        to names."""
        return self.name >= other.name

    def __eq__(self, other):
        """Tests for equality."""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name

def main():
    """Tests sorting."""
    # Create the list and put 5 students into it
    lyst = []
    for count in reversed(range(5)):
        s = Student("Name" + str(count + 1), 10)
        lyst.append(s)
    # Complete the definition of the main function

    random.shuffle(lyst)

    for i in lyst:
        print(i)

    lyst.sort()

    for i in lyst:
        print(i)

if __name__ == "__main__":
    main()
