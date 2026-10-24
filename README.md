# Photo Store

A Flask-based anime image service that provides a dynamic image endpoint, backed by a local image collection and automated repository workflows.

The project combines image management, HTTP image delivery, JSON utilities, and deployment configuration to make anime artwork accessible through a web endpoint.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Framework-Flask-000000?logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Automation-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Deployment-Vercel-000000?logo=vercel&logoColor=white" alt="Vercel">
</p>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Running Locally](#running-locally)
- [Using the Image Endpoint](#using-the-image-endpoint)
- [Automation](#automation)
- [Deployment](#deployment)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [License](#license)

## Overview

Photo Store is a Python-based project for serving anime artwork through a web application.

The repository maintains an image collection and includes application code, supporting scripts, JSON data, and automation workflows. The image endpoint can be embedded in Markdown documents and other environments that support remote images.

The project is intended to provide a simple way to serve anime images without manually updating every document that displays them.

## Features

- **Image collection:** Stores anime artwork in a dedicated directory.
- **Flask application:** Provides the Python web application and HTTP routes.
- **Image delivery:** Supports displaying images through a web endpoint.
- **JSON utilities:** Includes scripts for working with JSON-related image data.
- **Workflow automation:** Uses GitHub Actions workflows for scheduled or automated tasks.
- **Web template:** Includes an HTML template for browser-based presentation.
- **Deployment configuration:** Includes a Vercel configuration file.

> Note: The precise behavior of each endpoint and automation workflow depends on its implementation. Refer to the source files for the authoritative details.

## Project Structure

```text
photo-store-repo/
├── .github/
│   ├── workflows/
│   │   ├── cron_job.yml
│   │   └── json_update.yml
│   └── dependabot.yml
├── anime_women/
│   └── ...                  # Anime image collection
├── destination/
│   └── anime.webp           # Image destination or output asset
├── templates/
│   └── index.html           # HTML template
├── .gitignore
├── apend_json.py            # JSON-related utility
├── app.py                   # Flask application
├── eliminate_json.py        # JSON-related utility
├── image_files.json         # Image metadata or file references
├── README.md
├── requirements.txt         # Python dependencies
├── script.py                # Supporting Python script
└── vercel.json              # Vercel configuration
```

The image directory contains the artwork files and is abbreviated here for readability.

### Key Files and Directories

| Path | Purpose |
|---|---|
| `app.py` | Main Flask application |
| `anime_women/` | Collection of anime images |
| `destination/` | Contains the `anime.webp` asset |
| `templates/index.html` | HTML template |
| `image_files.json` | JSON data associated with image files |
| `apend_json.py` | JSON-related processing script |
| `eliminate_json.py` | JSON-related processing script |
| `script.py` | Supporting Python script |
| `.github/workflows/` | GitHub Actions automation |
| `.github/dependabot.yml` | Dependabot configuration |
| `requirements.txt` | Python package dependencies |
| `vercel.json` | Deployment configuration |

## Getting Started

### Prerequisites

Ensure that you have the following installed:

- Python 3
- pip
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/lonelyH3b/photo-store-repo.git
cd photo-store-repo
```

### 2. Create a Virtual Environment

Creating a virtual environment helps isolate the project's dependencies from other Python applications.

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Running Locally

Start the Flask application:

```bash
python app.py
```

If the application starts using Flask's default development configuration, it may be available at:

```text
http://127.0.0.1:5000/
```

The exact host, port, and available routes depend on the configuration in `app.py`.

For local development, use Flask's development server. For production, use an appropriate deployment configuration.

## Using the Image Endpoint

If the application exposes an image route, you can embed its URL in a Markdown document.

For example:

```markdown
![Anime image](https://your-deployment-domain.example/anime-image)
```

Replace the example URL with the actual deployed endpoint.

### Cache Considerations

Browsers, proxies, and platforms such as GitHub may cache remote images.

If the endpoint supports query parameters for cache-busting, a changing query parameter can help request a fresh URL:

```markdown
![Anime image](https://your-deployment-domain.example/anime-image?t=123456)
```

A changing URL does not guarantee that the underlying image changes. That behavior depends on the application and its caching configuration.

## Automation

The repository includes GitHub Actions workflows under `.github/workflows/`.

| Workflow | Intended area |
|---|---|
| `cron_job.yml` | Scheduled automation |
| `json_update.yml` | JSON-related updates |

The repository also includes `.github/dependabot.yml`, which configures Dependabot behavior.

To understand the exact triggers, permissions, schedules, and actions, inspect the corresponding YAML files.

### Workflow Configuration

Before enabling or modifying automated workflows, verify:

- The configured triggers and schedules.
- Required repository permissions.
- Any secrets or environment variables.
- The files modified by each workflow.
- Whether automated changes are committed or published.

## Deployment

The repository includes a `vercel.json` configuration file, indicating that Vercel deployment is part of the project setup.

### Deploy with Vercel

1. Review `vercel.json` and confirm that the application entry point matches the deployment configuration.
2. Ensure that the required Python dependencies are declared in `requirements.txt`.
3. Import or connect the repository through the Vercel dashboard.
4. Configure any required environment variables.
5. Deploy the project and verify the application's routes.

For CLI-based deployment, install the Vercel CLI and run:

```bash
npm install -g vercel
vercel
```

For a production deployment:

```bash
vercel --prod
```

Refer to the [Vercel documentation](https://vercel.com/docs) for current Python deployment requirements and configuration options.

**Important:** Confirm that the deployed application can access the image assets it needs. Also verify that its routing and file paths work in the deployment environment; a configuration that works locally may require adjustments for serverless hosting.

## Technology Stack

| Technology | Role |
|---|---|
| Python | Application logic and supporting scripts |
| Flask | Web application framework |
| JSON | Structured data for image-related operations |
| GitHub Actions | Workflow automation |
| Dependabot | Dependency update configuration |
| Vercel | Deployment platform |

## Contributing

Contributions, bug reports, and suggestions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the application and any affected scripts.
5. Submit a pull request describing your changes.

For substantial changes, consider opening an issue first to discuss the proposed implementation.

## License

Please refer to the repository's license file for the applicable license and usage terms.

If no license file exists, add an appropriate license before presenting the project as open source.

---

**Photo Store** — an image-serving project built with Python and Flask.

