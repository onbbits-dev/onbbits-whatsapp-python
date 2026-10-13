# Send WhatsApp Messages Using Python | Onbbits API

Send WhatsApp messages using Python with the Onbbits WhatsApp Business API. This repository provides a Python code example to help developers integrate WhatsApp messaging into their applications using Onbbits.

Create an API Campaign in Onbbits, configure the required API details, and use the Python script to send WhatsApp messages through your application.

## Features

- **WhatsApp Messaging with Python:** Send WhatsApp messages using Python code.
- **Onbbits API Integration:** Integrate WhatsApp messaging into your applications.
- **WhatsApp API Campaigns:** Use API Campaigns configured in Onbbits.
- **Easy Integration:** Use the example code as a starting point for your Python projects.
- **Developer-Friendly:** Follow simple setup instructions to get started.

## How It Works

1. Log in to [Onbbits](https://app.onbbits.io/).
2. Navigate to **Campaigns → Add Campaign → API Campaign**.
3. Configure your campaign and select an approved WhatsApp message template.
4. Click **Test Campaign** to obtain the API request configuration.
5. Add the required API details to `send_whatsapp.py`.
6. Run the Python script to execute the API request.

For detailed instructions, refer to the [Onbbits API Campaign Guide](https://help.onbbits.io/create-api-campaign/).

## Prerequisites

Before getting started, ensure you have:

- An Onbbits account.
- A WhatsApp Business Account connected to Onbbits.
- An API Campaign configured in Onbbits.
- The required API credentials and campaign details.
- Python installed on your system.

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/onbbits-dev/onbbits-whatsapp-python.git
cd onbbits-whatsapp-python
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Create an API Campaign in Onbbits

Log in to [Onbbits](https://app.onbbits.io/) and create an API Campaign.

Configure your campaign and select the appropriate WhatsApp message template.

Follow the [official API Campaign guide](https://help.onbbits.io/create-api-campaign/) to obtain the required API request configuration.

### 4. Configure the Python Script

Open `send_whatsapp.py` and configure the required API details, authentication credentials, recipient information, and campaign parameters according to the Onbbits API documentation.

Use the exact endpoint, authentication format, and request payload required by the API.

**Security:** Never commit API tokens, secret keys, or other sensitive credentials to your public repository.

### 5. Run the Python Script

Execute the script from your terminal:

```bash
python send_whatsapp.py
```

Review the API response to determine whether the request was accepted.

### 6. Verify the Result

Check the campaign status and message delivery information in Onbbits, where available.

An accepted API request does not necessarily mean that the WhatsApp message has been delivered successfully.

## Use Cases

This Python example can help developers who want to:

- Send WhatsApp messages using Python.
- Integrate the Onbbits API into their applications.
- Build WhatsApp messaging integrations.
- Execute API-based WhatsApp campaigns.
- Automate WhatsApp messaging workflows.

## Troubleshooting

If your API request fails, check the following:

- Verify that your API credentials are correct.
- Ensure your API Campaign is configured properly.
- Confirm that the request endpoint and payload match the Onbbits API documentation.
- Review the API response for error details.
- Check that your WhatsApp message template and recipient information meet the applicable requirements.

## Resources

- **Onbbits Platform:** https://app.onbbits.io/
- **API Campaign Documentation:** https://help.onbbits.io/create-api-campaign/
- **GitHub Repository:** https://github.com/onbbits-dev/onbbits-whatsapp-python

## License

See the `LICENSE` file in this repository for the applicable license terms.

## Contact Us

For questions, support, or assistance with Onbbits API integration, contact us:

- **WhatsApp:** +91 97270 77732
- **Website:** [https://onbbits.io/](https://onbbits.io/)
- **Platform:** [https://app.onbbits.io/](https://app.onbbits.io/)
- **Help Center:** [https://help.onbbits.io/](https://help.onbbits.io/)

