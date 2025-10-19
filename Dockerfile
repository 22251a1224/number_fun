# Step 1: Use a lightweight Python base image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Step 4: Copy the entire project into the container
COPY . .

# Step 5: Expose Flask’s default port
EXPOSE 5000

# Step 6: Command to run the app
CMD ["python", "app.py"]
