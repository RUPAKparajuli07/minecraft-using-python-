


# update is run every frame
def update():
	#print('test')
	if held_keys['a']:
		cube.x -= 1 * time.dt

# basic window
app = Ursina()

# basic cube 
cube = Entity(model='quad', color=color.orange, scale = (2,5), position = (5,1))

# quad with texture
#sans_image = load_texture('Sans.png')
#sans = Entity(model = 'quad', texture = sans_image)
#sans = Entity(model = 'quad', texture = 'Sans.png')

# creating a block properly
test = Test_cube()

# creating a button
btn = Test_button()
punch_sound = Audio('assets/punch', loop=False, autoplay=False)

app.run()

