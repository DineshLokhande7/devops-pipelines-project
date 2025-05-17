# DevOps Pipelines Project

This project demonstrates a simple DevOps CI/CD pipeline for a Python application. It includes the necessary configurations for continuous integration and continuous deployment using GitHub Actions.

## Project Structure

```
devops-pipelines-project
├── .github
│   └── workflows
│       ├── ci.yml
│       └── cd.yml
├── src
│   ├── app.py
│   └── tests
│       └── test_app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd devops-pipelines-project
   ```

2. **Install dependencies:**
   Make sure you have Python and pip installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   You can run the application using:
   ```bash
   python src/app.py
   ```

4. **Run tests:**
   To run the unit tests, execute:
   ```bash
   python -m unittest discover -s src/tests
   ```

## CI/CD Pipelines

- **Continuous Integration (CI):** The CI pipeline is defined in `.github/workflows/ci.yml`. It builds and tests the application whenever code is pushed to the repository.

- **Continuous Deployment (CD):** The CD pipeline is defined in `.github/workflows/cd.yml`. It deploys the application to a production environment after successful builds.

## Docker

To build the Docker image, run:
```bash
docker build -t your-image-name .
```

To run the Docker container, use:
```bash
docker run -p 5000:5000 your-image-name
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.