## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <https://github.com/victor90braz/invoice-debugging.git>
   cd <InmaticPart3Debugging>
   ```

2. Run the `setup-windows.bat` Script for Windows:
   ```bash
   ./setup-windows.bat
   ```

3. Run the `setup-linux-mac.sh` Script for Linux or macOS:
   ```bash
   ./setup-linux-mac.sh
   ```

This will:
- Create and activate a virtual environment (`myenv`).
- Install required dependencies such as Django.
- Optionally create a new Django project if it doesn't exist.
- Apply any pending migrations to your database.
- Start the Django development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

Activate a virtual environment (`myenv`)

```bash
.\myenv\Scripts\Activate.ps1
```

## Running a Specific Test 


```bash
coverage run manage.py test inmaticParte3Debugging.tests.service.accounting_invoice_service_test
```

## Generating Test Coverage Report in HTML

Install the `coverage` package if it's not already installed:

   ```bash
   pip install coverage
   ```

Run the tests with coverage:

   ```bash
coverage run manage.py test inmaticParte3Debugging.tests.service.accounting_invoice_service_test
coverage report
coverage html
   ```