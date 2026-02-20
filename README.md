# Project : Django Web Server 

The project is split in 2 apps for a better maintainability:
- a RESTful API to handle website metadata database
- a dictionnary with the 15min delayed bitcoin market price in EUR, the monthly conversion rate from last month from EUR to GBP from the European Central Bank, and the bitcoin price first value of this dictionnary but converted to GBP according to the official ECB rate

Please refer to the 2 postman collections (JSON-documents). They reflect the API documentation.

Before trying to deploy the code in production, make sure you work under a virtual environment and download all dependencies from requirements.txt
