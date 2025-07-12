

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

