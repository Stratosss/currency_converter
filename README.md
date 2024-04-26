#  Currency converter and Exchange rate table
## Overview
This application utilises an API from https://www.freecurrencyapi.com.
It returns the latest exchange rates, as well as converts the given amount to and from the currencies of interest. It consists of 33 popular currencies.
- First, it asks the user to select the currency they want to exchance from.
- Then prompts them to select the currency they want to exchance to.
- Finally, it asks for the amount to be converted.
  
- The application, checks if the currency given is within the list and proceeds to the next step. Alternatively, if the input is something irrelevant, the application returns and prompts the user to enter a currency from the given list.
- Then, it asks for the amount of interest. If the value is a negative number it returns the results for the equivalent positive number. If the value is string, it prompts the user to input again the correct type.
- Alongside the currency convertion, the application returns a table with the latest exchange rates for all of the popular currencies of the list.
