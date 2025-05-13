# Family Finances

Family Finances is a web application built with **Django**, **Vite** and **TailwindCSS** that allows users to manage their fixed and variable expenses, plan shopping lists, and optimize costs based on travel distances and fuel consumption.

## Project Structure

- **expenses**: Manages fixed expenses and variable expenses from the shopping module.
- **shopping**: Stores details of purchased products, including:

  - Price
  - Purchase date
  - Location of purchase
  - Store score
  - Registered home location for distance calculation with Google Maps API
  - Fuel cost estimation based on registered vehicles
  - Price Update via Invoice Upload: Users can upload an invoice or receipt, and an AI-powered OCR (Optical Character Recognition) model will extract the product information and update the prices automatically

## Front-End Features

In the front-end interface, users can:

1. Create and manage shopping lists.
2. Define the city and the vehicle to be used for shopping.
3. Get a list of the cheapest places to buy items, considering:

   - Product prices
   - Distance from home
   - Fuel costs for the selected vehicle

## Technologies Used

- **Django** (Back-end)
- **Vite** (Front-end)
- **TailwindCSS v4.0** (Front-end)
- **Google Maps API** for distance calculations
- **OCR** and **AI Model** for product recognition from invoices

## Getting Started

### Prerequisites

- Python 3.13.3+
- Node.js 18+
- Django 4.0+
- Vite 4.0+
- TailwindCSS 4.0+

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ctedescojr/family_finances.git
   cd family_finances
   ```

2. Install back-end dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install front-end dependencies:

   ```bash
   cd frontend
   npm install
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development servers:

   ```bash
   python manage.py runserver
   cd frontend && npm run dev
   ```

## Usage

Access the application at:

- Django API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Vite Front-end: [http://127.0.0.1:5173](http://127.0.0.1:5173)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
