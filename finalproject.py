from flask import flask
app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    print "This page will show all my restaurants"

@app.route('/restaurants/new')
def newRestaurant():
    print "This page will be for making a new restaurant"

@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    print "This page will be for editing restauran %s"%restaurant_id

@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    print "This page will be for deleting restauran %s"%restaurant_id

@app.route('/restaurants/<int:restaurant_id>')
@app.route('/restaurants/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    print "This page is the menu for restaurant %s"%restaurant_id

@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    print "This page is for making a new menu item for restaurant %s"%restaurant_id

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    print "This page is for editing menu item %s"%menu_id

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    print "This page is for deleting menu item %s"%menu_id



if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)