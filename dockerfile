# importing base image (python)
FROM python:3.9.19
# create a working directory
WORKDIR /sentiment
# copy all to working directory
COPY . .
# install dependicies
RUN pip install -r requirements.txt

# export op port 5000
EXPOSE 5000

# CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]

# run the script
CMD ["python" , "./app.py"]

######## comands on terminal ###########

# sudo docker build --tag my_docker1 .  
# sudo docker image ls
