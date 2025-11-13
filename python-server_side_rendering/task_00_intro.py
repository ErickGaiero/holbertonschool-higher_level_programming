#!/usr/bin/python3
"""
Module that defines a function to generate personalized invitations
from a given template and list of attendees.
"""

import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files based on a template and a list of attendees.
    """

    if not isinstance(template, str):
        print("Invalid input: template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees should be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        personalized = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if not value:
                value = "N/A"
            personalized = personalized.replace(f"{{{key}}}", str(value))

        output_filename = f"output_{i}.txt"
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(personalized)
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")
