# Use light weight python 3.7 image
FROM python:3.7-slim

# Copy the code to the container image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install the production dependencies
RUN pip install Flask gunicorn

# Run the web service on container startup,here we use gunicorn
# webserver, with one worker process and 8 threads
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

