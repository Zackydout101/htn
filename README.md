# APIcasso 🎨

## Turn any website into a well-defined API with one click

APIcasso is an innovative tool that allows anyone to create an API from any website effortlessly. It combines the power of web scraping, AI-driven schema generation, and a user-friendly interface to democratize API creation.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Components](#components)
3. [Features](#features)
4. [Technology Stack](#technology-stack)
5. [Getting Started](#getting-started)
6. [Usage](#usage)
7. [Architecture](#architecture)
8. [Future Developments](#future-developments)
9. [Contributing](#contributing)
10. [License](#license)

## Project Overview

APIcasso aims to simplify the process of creating APIs from web content. It allows users to input a URL and receive a fully functional API endpoint, complete with a well-defined schema. This tool is perfect for developers, data scientists, and anyone who needs to extract structured data from websites quickly and efficiently.

## Components

APIcasso consists of three main components:

1. **Frontend**: A sleek and intuitive user interface built with Next.js and styled with Tailwind CSS.
2. **Backend**: A robust Flask-based server that handles web scraping, schema generation, and API management.
3. **NomadNet**: A work-in-progress mobile proxy network to enhance data collection capabilities and bypass restrictions.

## Features

- One-click API creation from any website
- AI-powered schema generation
- User authentication and dashboard
- Persistent storage of created APIs
- Real-time progress tracking for API creation
- Responsive design for desktop and mobile use
- Automation capabilities for supported platforms (e.g., Shopify)

## Technology Stack

### Frontend
- Next.js 14.2.11
- React 18
- Tailwind CSS 3.4.1
- Redis 4.7.0 (for caching)

### Backend
- Flask
- Supabase (for authentication and database)
- BeautifulSoup4 (for web scraping)
- Cohere API (for AI-powered schema generation)
- Redis (for caching)

### NomadNet (WIP)
- Python
- AsyncIO
- AIOHTTP

## Getting Started

### Prerequisites
- Node.js (v14 or later)
- Python 3.8+
- Redis server

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/apicasso.git
   cd apicasso
   ```

2. Set up the frontend:
   ```
   cd api-casso-frontend
   npm install
   ```

3. Set up the backend:
   ```
   cd ../backend
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the `backend` directory with the following variables:
     ```
     SUPABASE_URL=your_supabase_url
     SUPABASE_KEY=your_supabase_key
     COHERE_API_KEY=your_cohere_api_key
     ```

5. Start the Redis server:
   ```
   redis-server
   ```

6. Run the backend server:
   ```
   python run.py
   ```

7. Run the frontend development server:
   ```
   cd ../api-casso-frontend
   npm run dev
   ```

8. Open your browser and navigate to `http://localhost:3000`

## Usage

1. Sign up for an account or log in if you already have one.
2. On the dashboard, enter a URL and an empty JSON schema.
3. Click "Create New" to generate an API for the given URL.
4. Once complete, you'll receive an API endpoint that you can use to fetch structured data from the website.
5. For supported platforms like Shopify, you can create automation workflows using the "Automations" tab.

## Architecture

APIcasso follows a client-server architecture:

1. The Next.js frontend serves as the client, providing a responsive and interactive user interface.
2. The Flask backend handles API requests, web scraping, and interacts with the database and AI services.
3. Supabase is used for user authentication and storing API schemas and endpoints.
4. Redis is employed for caching frequently accessed data and improving performance.
5. The Cohere API is utilized for AI-powered schema generation and data extraction.

The NomadNet component (work in progress) will act as a distributed proxy network to enhance data collection capabilities and provide additional IP addresses for web scraping tasks.

## Future Developments

- Integration of NomadNet for improved data collection and bypass capabilities
- Support for more e-commerce platforms in the automation feature
- Advanced customization options for generated APIs
- API usage analytics and monitoring
- Integration with popular API management platforms

## Contributing

We welcome contributions to APIcasso! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

Created by Bhav Grewal, Karolina Dubiel, Kevin Li, and Zachary Levesque for Hack the North 2024.
