class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Missle settings 
        self.missile_speed= 0.25
        self.missile_width =6
        self.missile_height = 30
        self.missiles_allowed = 2
        self.missile_color = (255,255,255)

        # Alien settings
        self.alien_speed = 0.8
        self.fleet_drop_speed = 2.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Astroid settings
        self.astroid_speed = 0.5
        self.astroid_direction = 1
        
