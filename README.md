# CRM Django Project

## Overview
This is the first draft demo of a Customer Relationship Management (CRM) system built using Django. The project integrates essential business tools to streamline lead management, marketing, and customer engagement.

## Repository
[GitHub Repository](https://github.com/shreyash0019/CRM-Django.git)

## Features
✅ Lead Capture Custom Forms  
✅ Google Reviews Manager  
✅ WhatsApp Marketing  
✅ Email & SMS Marketing  
✅ AI Chatbot  
✅ Click-to-Call Feature  
✅ Social Media Scheduler & Insights  
✅ Loyalty & Referral Programs  
✅ Security Services  
✅ Client Billing System  

## Installation & Setup
### Prerequisites
- Python 3.12+
- Django 5.1.4
- Virtual Environment (optional but recommended)
- SQLite (default) or any preferred database

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/shreyash0019/CRM-Django.git
   cd CRM-Django
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # macOS/Linux
   env\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the server:
   ```bash
   python manage.py runserver
   ```
7. Open in browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## User Manual
### Navigation
- **Dashboard:** Overview of CRM features
- **Lead Capture:** Add and manage leads
- **Google Reviews Manager:** Monitor and respond to reviews
- **Marketing Modules:** WhatsApp, Email & SMS campaigns
- **AI Chatbot:** Automate customer interactions
- **Click-to-Call:** Directly connect with clients
- **Social Media Scheduler:** Plan and track social campaigns
- **Loyalty & Referral:** Reward loyal customers
- **Security Services:** Manage security settings
- **Billing System:** Handle invoices and payments

### How to Use
1. **Login:** Use the admin panel to access and manage CRM features.
2. **Create Leads:** Navigate to 'Lead Capture' and add a new lead.
3. **Manage Marketing:** Utilize WhatsApp, Email, and SMS tools.
4. **View Reports:** Analyze customer interactions and marketing performance.
5. **Automate Responses:** Configure the AI Chatbot.
6. **Schedule Social Media Posts:** Plan campaigns directly from the dashboard.
7. **Process Payments:** Use the billing system for client transactions.

## API Endpoints
- **Authentication**
  - `POST /api/token/` - Obtain JWT token
  - `POST /api/token/refresh/` - Refresh JWT token
- **Leads**
  - `GET /api/leads/` - Get all leads
  - `POST /api/leads/` - Create a new lead
  - `PUT /api/leads/{id}/` - Update a lead
  - `DELETE /api/leads/{id}/` - Delete a lead
- **Marketing**
  - `POST /api/email/send/` - Send email campaigns
  - `POST /api/sms/send/` - Send SMS campaigns
- **Billing**
  - `GET /api/invoices/` - View invoices
  - `POST /api/invoices/` - Create an invoice

## Future Enhancements
- 🔹 Expand AI chatbot capabilities with NLP
- 🔹 Enhance dashboard UI with more analytics
- 🔹 Integrate third-party payment gateways
- 🔹 Add automation for lead nurturing workflows
- 🔹 Implement role-based access control (RBAC)
- 🔹 Improve API documentation using Swagger

 

## License
This project is open-source under the [MIT License](LICENSE).

