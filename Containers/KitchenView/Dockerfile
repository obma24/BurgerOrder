# This Dockerfile sets up the KitchenView container environment:
#   - Uses the "python:3.9-slim" image as the base.
#   - Sets the working directory to "/app".
#   - Installs dependencies from "requirements.txt".
#   - Copies all app files into the container.
#   - Runs the Flask app (app.py) to handle kitchen orders.

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
