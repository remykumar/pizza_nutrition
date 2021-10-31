FROM python:3.8

# set up a working directory 
WORKDIR /usr/src/pizza_nutrition

# copy code, static assests/templates, artifacts to container
COPY . . 

# start the virtual environment 
RUN python3 -m venv venv && . venv/bin/activate

# install dependencies 
RUN venv/bin/python3 -m pip install --upgrade pip && venv/bin/pip3 install --no-cache-dir -r requirements.txt 

# port the container should expose (this is default port of flask app) 
EXPOSE 5000 

# start the app 
CMD ["venv/bin/python3", "./app.py"] 
