# Use an official Python runtime as a base image
FROM python:3.6.0b4-alpine

# set file maintainer
LABEL org.opencontainers.image.authors="Aaron Bowden"

# Set the working directory to /autocomplete
WORKDIR /autocomplete

# Copy the current directory contents into the container at /autocomplete
ADD . /autocomplete

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Define environment variable
ENV TEST World
ENV PYTHONUNBUFFERED 1

#Port to expose
EXPOSE 8080

#Run development server when the container launches
CMD ["python","autocomplete/manage.py","runserver","0.0.0.0:8080"]

