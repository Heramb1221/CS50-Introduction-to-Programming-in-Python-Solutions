**Unit Conversion Program**

**Video Demo:** https://youtu.be/0A-AH2IcIJs

**Description:**

This Python program allows users to convert between different units of length, temperature, weight, and volume. The program leverages the pint library to handle unit conversions accurately.

**Features**
Convert units of length (e.g., kilometer, meter, centimeter).
Convert units of temperature (e.g., Celsius, Fahrenheit, Kelvin).
Convert units of weight (e.g., kilogram, gram, milligram).
Convert units of volume (e.g., liter, milliliter, kiloliter).
Simple text-based user interface for easy interaction.

**Prerequisites**
Python 3.x
pint library
You can install the pint library using pip:

pip install pint

**Usage**
Run the program using Python:
python unit_conversion.py
Follow the on-screen prompts to select the type of conversion and enter the relevant details.

**Code Overview**
#Imports
python
import sys
import pint

#Supported Units
The following unit lists are defined for conversion:
lunits = ['kilometer', 'hectometer', 'decameter', 'meter', 'decimeter', 'centimeter', 'millimeter']
tunits = ['celsius', 'fahrenheit', 'kelvin', 'rankine']
wunits = ['kilogram', 'hectogram', 'decagram', 'gram', 'decigram', 'centigram', 'milligram']
vunits = ['milliliter', 'centiliter', 'deciliter', 'liter', 'dekaliter', 'hectoliter', 'kiloliter']

#Main Function
The main function drives the user interaction, allowing the selection of conversion types and taking the necessary inputs:
Helper Functions
take_input: Takes user input for selecting the type of conversion.
get_value: Safely takes a numerical input value from the user.
convert_length: Converts length units.
convert_temp: Converts temperature units.
convert_weight: Converts weight units.
convert_volume: Converts volume units.s
