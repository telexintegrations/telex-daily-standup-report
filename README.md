# Telex Daily Standup Report

## Overview

This project provides a Telex integration that sends scheduled reminders to a channel, prompting team members to submit their daily standup reports. It's built using FastAPI and designed to be deployed as a Telex integration service.

## Screenshots

- [Daily Standup Report on Telex Channel](https://imgur.com/a/6cPT5oe)
- [Description of Telex Daily Standup Report Integration](https://imgur.com/a/eBWMrcE)

## Features

- ⏰ Scheduled reminders for daily standups.
- 📝 Customizable reminder messages with template guidance.
- 🔔 Configurable mention types (@channel, @here).
- ⚙️ Easy configuration via integration settings.
- 🚀 Simple deployment as a Telex integration.
- 🧪 Complete test coverage.

## Project Structure

```
telex-daily-standup-report/
├── api/
│ ├── db/
│ │ ├── __init__.py
│ │ └── schemas.py           # Data models
│ ├── routes/
│ │ ├── __init__.py
│ │ └── remainder.py         # Remainder route handlers
│ └── router.py              # API router configuration
├── core/
│ ├── __init__.py
│ └── config.py              # Application settings
├── tests/
│ ├── __init__.py
│ └── test_remainder.py      # API endpoint tests
├── main.py                  # Application entry point
├── requirements.txt         # Project dependencies
└── README.md
```

## Technologies Used

- Python 3.11+
- FastAPI
- Pydantic
- pytest
- uvicorn
- httpx

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd fastapi-telex-project
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the server:

```bash
uvicorn main:app
```

2. Access the API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Integration Metadata

- `GET /integration.json `- Returns the integration metadata required by Telex.

### Tick Endpoint

- `POST /tick` - Triggers the sending of a standup reminder based on the provided payload.

## Integration Settings

The following settings are configurable via the integration.json endpoint:

- `interval`: The cron-like schedule for sending reminders (e.g., "0 9 * * 1-6").
- `Reminder Message`: The message to be sent in the reminder.
- `Mention Type`: The mention type to use (@channel or @here).

[Screenshot of Daily Standup Report Integration Settings on Telex App](https://imgur.com/a/A2jE386)

## Tick Payload Schema

```json
{
  "channel_id": "channel_id",
  "return_url": "return_url",
  "settings": [
    {
      "label": "interval",
      "type": "text",
      "required": true,
      "default": "0 9 * * 1-6"
    },
    {
      "label": "Reminder Message",
      "type": "text",
      "required": true,
      "default": "Reminder: DAILY STAND-UP REPORT..."
    },
    {
      "label": "Mention Type",
      "type": "dropdown",
      "required": true,
      "default": "@channel",
      "options": ["@channel", "@here"]
    }
  ]
}
```

## Running Tests

```bash
pytest
```

## Error Handling

The API handles errors gracefully and provides appropriate responses.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the GitHub repository.
