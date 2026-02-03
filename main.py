"""
main.py
Entry point for the University Registration System CLI.

This file contains minimal logic: it delegates startup to
`registration_system.start_registration_system()` so that object
creation and program flow are kept inside the module that owns the
application logic.

Running this file directly will start the interactive program; importing
this module (for tests or inspection) will not start the program.
"""

from registration_system import start_registration_system


def main():
    # Minimal logic in main: delegate to the registration_system module
    start_registration_system()


if __name__ == "__main__":
    # When executed as a script, run the application.
    main()