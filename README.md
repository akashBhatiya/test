# Project Setup Guide for EC2 Instance

This guide provides step-by-step instructions to launch this project on a newly created AWS Ubuntu EC2 instance.

## Prerequisites

- AWS Ubuntu EC2 instance
- SSH access to the instance
- GitHub Personal Access Token (for cloning private repositories)

## Installation Steps

### 1. Update System Packages

```bash
sudo apt update
sudo apt install -y \
  git \
  curl \
  poppler-utils \
  tesseract-ocr \
  libgl1 \
  libglib2.0-0 \
  build-essential
```

### 2. Install UV Package Manager

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify the installation:

first reload the ssh
```bash
source ~/.bashrc
```

```bash
uv --version
```

### 3. Configure Git

```bash
git --version
git config --global user.name akashBhatiya
git config --global user.email asbhatiya8888@gmail.com
```

### 4. Clone the Repository

```bash
git clone https://github.com/OrrisCare/unstructured.git
```

> **Note:** When prompted, enter:
> - Username: `akashBhatiya`
> - Password: Your GitHub Personal Access Token

### 5. Navigate to Project Directory

```bash
cd unstructured
```

### 6. Configure Environment Variables

Create and edit the `.env` file:

```bash
nano .env
```

Paste your environment variables into this file and save it (Ctrl+X, then Y, then Enter).

### 7. Install Dependencies and Run

```bash
uv sync
uv run python main.py
```

## Project Structure

- `input/` - Input PDF files
- `output/` - Generated outputs
  - `json_output/` - JSON parsing results
  - `grounding_output/` - Extracted images/tables
- `services/` - Service modules (e.g., S3 upload)
- `main.py` - Main application entry point

## Support

For issues or questions, please contact the development team.