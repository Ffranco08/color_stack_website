# Docker Image: This is like the skeleton or the blueprint of your container. It includes the basic operating system and any pre-installed software (like Python).
# Packages (Dependencies): These are additional parts that you "add" to the skeleton to make it capable of running your specific application 
# (e.g., Flask, database connectors, etc.).


# Use the official Python 3.12 image from Docker Hub as a base (skeleton)
FROM python:3.12

# Set the working directory inside the container (Virtual Machine)
WORKDIR /color_stack_website

# Copy the entire project into the container's /color_stack_website directory (flesh ontop of skeleton)
COPY . /color_stack_website

# Install the required Python packages inside the container
RUN pip install --no-cache-dir -r /color_stack_website/requirements.txt

# Expose the port your app will run on (default for Flask is 5000)
EXPOSE 5000

# Specify the entry point
CMD ["python", "run.py"]