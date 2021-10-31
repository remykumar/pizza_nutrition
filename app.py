from flask import Flask, render_template
import os

app = Flask(__name__)
class Pizza:
    count = -1
    name = ""

# list of pizza images
images = [
    "/static/bbq_pizza.jpg",
    "/static/cheese_pizza.jpg",
]

# dict of pizza images with names - better approach than multiple lists
names = {
  "/static/bbq_pizza.jpg": "1. BBQ Pizza : Per Large Slice : 350 cal",
  "/static/cheese_pizza.jpg": "2. CHEESE Pizza : Per Large Slice : 270 cal",
  "/static/buffalochicken_pizza.jpg": "3. Buffalo Chicken Pizza : Per Large Slice : 330 cal",
  "/static/sausage_pizza.jpg": "4. Sausage Pizza : Per Large Slice : 330 cal",
  "/static/hawaiian_pizza.jpg": "5. Hawaiian Pizza : Per Large Slice : 340 cal",
  "/static/veggie_pizza.jpg": "6. Veggie Pizza : Per Large Slice : 280 cal",
  "/static/pepperoni_pizza.jpg": "7. Pepperoni Pizza : Per Large Slice : 320 cal",
  "/static/meats_pizza.jpg": "8. Meats Pizza : Per Large Slice : 380 cal",
  "/static/supreme_pizza.jpg": "9. Supreme Pizza : Per Large Slice : 350 cal",
  "/static/fourcheese_pizza.jpg": "10. Four Cheese Pizza : Per Large Slice : 320 cal",

}


@app.route("/")
def index():
    limit = len(names) - 1 
    #print (limit)
    if (Pizza.count < limit): 
        Pizza.count=Pizza.count+1
    else: 
        Pizza.count=0 
    print (f'Front count {Pizza.count}')
    image = list(names)[Pizza.count]
    name = list(names.values())[Pizza.count]
    return render_template("index.html", image=image, name=name)

@app.route("/back")
def index1():
    limit = len(names) - 1
    #print (limit)
    if Pizza.count >= 1:
        Pizza.count=Pizza.count-1
    else:
        Pizza.count=0
    print (f'Back count {Pizza.count}')
    image = list(names)[Pizza.count]
    name = list(names.values())[Pizza.count]
    return render_template("index.html", image=image, name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

