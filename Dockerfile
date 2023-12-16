# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your Discord Bot's source code into the container
COPY . .

# Specify the command to run app
RUN ["chmod", "+x", "./launch.sh"]
CMD ./launch.sh