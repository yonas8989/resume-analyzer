# Resume Analyzer Project

## Setup

1. Copy `.env.example` to `.env` and fill in your values
2. Run `docker-compose up --build`
3. Access services:
   - Backend: http://localhost:8000
   - n8n: http://localhost:5678
   - PGAdmin: http://localhost:5050

## Usage

1. Get JWT token:
   ```bash
   curl -X POST http://localhost:8000/auth/login \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin&password=secret"