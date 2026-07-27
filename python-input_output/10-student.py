#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of attribute names to retrieve.
                If None, all attributes are retrieved.

        Returns:
            dict: The (optionally filtered) dictionary representation.
        """
        is_valid = isinstance(attrs, list)
        if is_valid:
            is_valid = all(isinstance(a, str) for a in attrs)
        if is_valid:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
