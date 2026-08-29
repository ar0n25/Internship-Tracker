# Internship Tracker Aron Armas

An Internship tracker built to manage my own internship search across fintech, banking, tech consultancy, defence, automotive, and big tech. This is a simple project build with no user accounts or authentication.

## Why I built this

Spreadsheets get messy fast when you're tracking 50+ applications across different sectors and stages. This replaces that with a proper web app: add a company, set its status, see everything at a glance, update it as things move forward.

## Built with

- Python (Flask)
- HTML / CSS
- SQLite (via Flask-SQLAlchemy)

## Features

- **Add, edit, and delete** applications
- Track **company, role, sector, status, date applied, and notes** for each one
- **Colour-coded status badges** (e.g. green for Offer, red for Rejected) for a quick visual read of where things stand
- Sector and status are fixed dropdown lists rather than free text, so data stays consistent

## How it works

Four routes handle everything:
- `GET /` — lists all applications, newest first
- `POST /add` — inserts a new application from the form
- `GET/POST /edit/<id>` — shows the edit form, then saves changes on submit- `POST /delete/<id>` — removes an application
- `POST /delete/<id>` — removes an application