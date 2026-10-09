# Python Email Validator

An entry-level Python project that validates an email address against simple email formatting conventions.

The program will take an email address as input, perform validity checks using conditional statements and string methods, and output whether the email address is valid/invalide based on the checks performed.

## Features

- Takes an email address as input

- Checks if input is null

- Rejects email addresses with spaces

- Makes sure the email address has one '@' symbol

- Checks if the email address has an empty local part

- Makes sure the email address has a dot in the domain

- Rejects email addresses with domains that start or end with a dot

- Outputs Valid/Invalid depending on the result

## Technologies Used

- Python

## How It Works

The program utilizes a function called `mail_val()` that validates the email address.

The function performs the following operations:

1. Checks if the email address is empty.

2. Checks if the email address has spaces in it.

3. Checks if the email address has more than one '@'

4. Checks if the email address's local part is empty.

5. Checks if the email address's domain has a dot.

6. Check if the email's domain starts or ends with a dot.

If all the tests above return true, the function returns `True`. If any of the tests above fail, the function will return `False`

Please note that this project only validates an email address against simple formatting conventions. It does not guarantee the existence of the email or that it can receive emails.

## Project Structure

python-email-validator/

│

└── Email validator.py

## How To Run

1. Make sure you have Python installed in your machine.

2. Clone this repo.

3. Navigate into the project's directory in your terminal

4. Run the command below:

python "Email validator.py"

5. Provide the email address to check.

6. View results

## Example Output

Enter the Email Address to Check : user@example.com

user@example.com: Valid

## What I Learned

Throughout this project, I was able to practice:

- Python functions

- If-else conditions

- String methods

- User input

- Boolean values

- Simple input validation

- Conditional expressions

## Project Background

I created this project as part of my Python learning journey to practice string manipulation, conditional statements, and validation.

## Future Improvements

- Better email address formatting validation

- More extensive domain validation

- Multiple email validation

- Graphical user interface

## Author

Made as part of my python learning journey.
