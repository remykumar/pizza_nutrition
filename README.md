**Pizza Nutrition** 

A python flask application which displays calorie values for few popular pizzas per slice. 
This application is build via Docker and ran in a python virtual environment inside a python container. 

Steps to run this static web application (using docker): 
1. Pull the docker image from docker hub 

    `docker pull remykumar/pizza_nutrition`
 
2. Run the container image

    `docker run -dt  -p 8899:5000 --name pizza remykumar/pizza_nutrition`
     
      // Run it in detached/background mode
      
   
    `docker run  -p 8899:5000 --name pizza remykumar/pizza_nutrition`
     
      // Run it in console (mostly for debugging purposes)

3. Accessing the static website 

    http://localhost:8899 (or) http://[PublicIP]:8899 
   
   
Steps to run this static web application (without docker): 
1. Clone the repository 

    `git clone https://github.com/remykumar/pizza_nutrition.git`
  
2. Change directory to code directory 

    `cd pizza_nutrition`

3. Run the applicaton 

    `python3 app.py` 
  
4. Accessing the static website

    http://localhost:5000 (or) http://[PublicIP]:5000
   
![Module6_Assignment_Step2](https://user-images.githubusercontent.com/38254327/145840315-6ccd8fe8-6a11-44b3-ad0f-fb96faa0f7fd.png)
