# This Dockerfile sets up the BurgerOrderer container environment:
#   - Uses the "python:3.9-slim" image as the base.
#   - Sets the working directory to "/app".
#   - Installs dependencies from "requirements.txt".
#   - Copies all app files into the container.
#   - Runs the (MenuStore_db.py) script to populate the database, followed by starting the Flask app (app.py).

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "python MenuStore_db.py && python app.py"]
