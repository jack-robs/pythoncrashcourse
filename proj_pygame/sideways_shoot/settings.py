class Settings():
    '''Stores Sideway shooter game settings'''
    def __init__(self):
        #Screen settings
        self.width = 800
        self.height = 600
        self.bg_color = (100, 200, 55)
        
        #Ship settings
        self.ship_speed_factor = 1.5
        
        #Bullet's settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
