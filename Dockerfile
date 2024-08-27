# Step 1: Use a base image with Python
FROM python:3.9-slim

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy the app files into the container
COPY . /app

# Step 4: Install necessary Python packages
RUN pip install --no-cache-dir Flask

# Step 5: Expose the port Flask will run on
EXPOSE 5000

# Step 6: Run the Flask application
CMD ["python", "./annotator/app.py"]