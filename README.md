# Space Beetween Us - Telegram-Based News Delivery Platform

**Purpose:**

- To create a platform that delivers personalized news updates to users via Telegram.
- To allow users to subscribe to specific categories of news and schedule delivery times.

**Key Features:**

- **User Registration and Login:** Users can create accounts, log in, and manage their profile information.
- **Telegram Integration:** Users can connect their Telegram accounts to the platform.
- **Category Subscriptions:** Users can subscribe to different news categories (e.g., Technology, Sports, Politics).
- **Scheduled Notifications:** Users can set the time and frequency of news delivery.
- **Personalized News Feed:** Users will receive news updates tailored to their subscribed categories and preferences.

**Technology Stack:**

- **Backend:** FastAPI (Python web framework)
- **Database:** PostgreSQL
- **Message Broker:** RabbitMQ (for asynchronous communication)
- **Telegram Bot:** Python library for interacting with the Telegram Bot API
- **Cronjob:** For scheduling tasks (e.g., checking for notifications)

## Installation

### Prerequisites
Ensure you have the following installed:

- Python >= 3.10
- PostgreSQL
- Redis


### Project Setup
1. Clone the project repository:
    ```bash
    git clone https://github.com/butterflyforkill/space_between_us.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd space_between_us/
    ```

3. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Create .env file using config

6. Create a database

7. Run redis server

## Running the Application
Start the application:

```bash
fastapi dev src/
```

## To look through api-docs

```
http://127.0.0.1:8000/docs 
```
<img width="1430" alt="Screenshot 2024-11-07 at 16 45 29" src="https://github.com/user-attachments/assets/52a6f291-7857-4cda-b300-20fa236b2313">

