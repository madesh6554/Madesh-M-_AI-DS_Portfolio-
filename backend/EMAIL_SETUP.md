# Email Setup Instructions

To enable email notifications for the contact form, follow these steps:

## Step 1: Install Required Package

Make sure you have installed the `python-dotenv` package:
```bash
cd backend
pip install python-dotenv
```

Or install all requirements:
```bash
pip install -r requirements.txt
```

## Step 2: Create .env File

Create a file named `.env` in the `backend` folder with the following content:

```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=madesh6554@gmail.com
SENDER_PASSWORD=your_app_password_here
RECIPIENT_EMAIL=madesh6554@gmail.com
```

## Step 3: Generate Gmail App Password

Since Gmail requires App Passwords for SMTP (not your regular password):

1. Go to your Google Account: https://myaccount.google.com/
2. Click on **Security** in the left sidebar
3. Under "Signing in to Google", enable **2-Step Verification** (if not already enabled)
4. After enabling 2-Step Verification, go back to Security
5. Click on **App passwords** (you may need to search for it)
6. Select **Mail** as the app and **Other (Custom name)** as the device
7. Enter "Portfolio Contact Form" as the name
8. Click **Generate**
9. Copy the 16-character password (it will look like: `abcd efgh ijkl mnop`)
10. Paste it in your `.env` file as `SENDER_PASSWORD` (remove spaces)

## Step 4: Restart Backend Server

After creating the `.env` file, restart your backend server:
```bash
cd backend
python app.py
```

## How It Works

When someone submits the contact form:
1. The message is saved to the database
2. You receive an email at `RECIPIENT_EMAIL` with the contact form details
3. The sender receives a confirmation email

## Troubleshooting

- **Email not sending?** Check that:
  - `.env` file exists in the `backend` folder
  - `SENDER_PASSWORD` is a valid App Password (not your regular Gmail password)
  - 2-Step Verification is enabled on your Google account
  - Backend server is restarted after creating `.env` file

- **Still not working?** Check the backend console for error messages.

