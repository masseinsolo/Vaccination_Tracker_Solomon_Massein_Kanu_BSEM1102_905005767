# Vaccination Tracker (PROG211 – OOP 1)

A simple Python OOP program that records vaccine doses for anonymous recipients.

## How it meets DPG standards
- **Open-source:** hosted publicly on GitHub, MIT-style free reuse.
- **Inclusive & accessible:** plain-text console output, simple language, no special hardware.
- **Privacy-respecting:** no names, addresses or phone numbers; only an anonymous ID (e.g. R001) and an age group.
- **Modular & reusable:** `Vaccine` and `Recipient` classes can be reused for any disease or clinic.

## OOP features
- Classes: `Vaccine`, `Recipient` (attributes + methods, objects interact)
- Data structure: one dictionary (`registry`) keyed by unique ID; `add_recipient()` and `display_all()`
- Instance methods: `add_dose()`, `display_info()`, `is_fully_vaccinated()`
- Class method: `get_total_recipients()` (`@classmethod`)
- Static method: `is_valid_age_group()` (`@staticmethod`)
- Tuples (bonus): `AGE_GROUPS` and `(vaccine, date)` dose records

## Run
1. Open VS Code > File > Open Folder > select the project folder.
2. Open the terminal: Terminal > New Terminal (Ctrl + `).
3. Run `python vaccination_tracker.py` (use `py vaccination_tracker.py` on Windows if `python` is not recognised, or `python3` on Mac/Linux).
4. A menu appears: type `1` for a quick demo, `2`-`5` to add recipients, record doses or view records, and `0` to exit.

## Example output
See `sample_output.txt`.
