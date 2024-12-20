import requests
from InquirerPy import prompt

# Function to convert currency using an API
def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    if 'rates' in data:
        rate = data['rates'].get(to_currency)
        if rate:
            return amount * rate
        else:
            return "Currency not found"
    return "Error fetching data"

# Expanded list of currency codes (including more countries)
currencies = [
    "USD", "EUR", "INR", "GBP", "AUD", "CAD", "JPY", "CNY", "NZD", "CHF", "MXN", "SGD",  # Common currencies
    "BRL", "ZAR", "TRY", "PLN", "SEK", "NOK", "DKK", "RUB", "KRW", "SAR", "EGP", "AED",  # More currencies
    "KES", "THB", "PHP", "MYR", "IDR", "HKD", "SGD", "IQD", "COP", "VND", "BHD", "PKR",  # Middle Eastern and Asian currencies
    "MAD", "NGN", "CLP", "HUF", "CZK", "RON", "BGN", "HRK", "SYP", "TND", "KWD", "JOD",  # African and Eastern European currencies
    "COP", "COP", "ILS", "MNT", "PEN", "VND"  # Latin American and Other currencies
]

# Prompt to select 'From' and 'To' currency codes using a dropdown
questions = [
    {
        'type': 'list',
        'name': 'from_currency',
        'message': 'Select the currency you want to convert from:',
        'choices': currencies
    },
    {
        'type': 'list',
        'name': 'to_currency',
        'message': 'Select the currency you want to convert to:',
        'choices': currencies
    },
    {
        'type': 'input',
        'name': 'amount',
        'message': 'Enter the amount to convert:',
        'validate': lambda val: val.isdigit() or "Please enter a valid number"
    }
]

# Getting user input using the dropdown
answers = prompt(questions)

amount = float(answers['amount'])
from_currency = answers['from_currency']
to_currency = answers['to_currency']

# Calling the convert_currency function and displaying the result
result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {result} {to_currency}")
