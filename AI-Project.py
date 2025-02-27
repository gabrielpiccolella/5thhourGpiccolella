




""""
import tkinter as tk
import math
import random
from PIL import Image, ImageTk
# --------------------------
# Game Constants
# --------------------------
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 20
BULLET_SIZE = 5
ENEMY_SIZE = 25

# --------------------------
# Utility Functions
# --------------------------
def normalize(dx, dy):
    mag = math.hypot(dx, dy)
    return (dx/mag, dy/mag) if mag else (0, 0)

# --------------------------
# Player Class
# --------------------------
class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.health = 100
        self.speed = 5
        # Represent the player as a triangle
        self.id = canvas.create_polygon(self._triangle_coords(), fill="green")

    def _triangle_coords(self):
        # Points of a triangle centered at (self.x, self.y)
        return [self.x, self.y - PLAYER_SIZE,
                self.x - PLAYER_SIZE, self.y + PLAYER_SIZE,
                self.x + PLAYER_SIZE, self.y + PLAYER_SIZE]

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.canvas.move(self.id, dx * self.speed, dy * self.speed)
        # Keep the player on screen
        self.x = max(PLAYER_SIZE, min(WIDTH - PLAYER_SIZE, self.x))
        self.y = max(PLAYER_SIZE, min(HEIGHT - PLAYER_SIZE, self.y))
        # Update triangle coords
        self.canvas.coords(self.id, *self._triangle_coords())

# --------------------------
# Bullet Class
# --------------------------
class Bullet:
    def __init__(self, canvas, x, y, target_x, target_y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.speed = 10
        dx, dy = target_x - x, target_y - y
        self.dx, self.dy = normalize(dx, dy)
        self.id = canvas.create_oval(x - BULLET_SIZE, y - BULLET_SIZE,
                                     x + BULLET_SIZE, y + BULLET_SIZE,
                                     fill="white")

    def update(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        self.canvas.move(self.id, self.dx * self.speed, self.dy * self.speed)
        # Check if bullet is off screen
        if not (0 <= self.x <= WIDTH and 0 <= self.y <= HEIGHT):
            self.destroy()
            return False
        return True

    def destroy(self):
        self.canvas.delete(self.id)

# --------------------------
# Enemy Class
# --------------------------
class Enemy:
    def __init__(self, canvas, player):
        self.canvas = canvas
        self.player = player
        # Spawn enemy at a random edge
        side = random.choice(["top", "bottom", "left", "right"])
        if side == "top":
            self.x = random.randint(0, WIDTH)
            self.y = 0
        elif side == "bottom":
            self.x = random.randint(0, WIDTH)
            self.y = HEIGHT
        elif side == "left":
            self.x = 0
            self.y = random.randint(0, HEIGHT)
        else:
            self.x = WIDTH
            self.y = random.randint(0, HEIGHT)
        self.speed = 2
        self.health = 50
        self.id = canvas.create_rectangle(self.x - ENEMY_SIZE, self.y - ENEMY_SIZE,
                                          self.x + ENEMY_SIZE, self.y + ENEMY_SIZE,
                                          fill="red")

    def update(self):
        # Move toward the player
        dx, dy = self.player.x - self.x, self.player.y - self.y
        dx, dy = normalize(dx, dy)
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.canvas.move(self.id, dx * self.speed, dy * self.speed)

    def destroy(self):
        self.canvas.delete(self.id)

    def collides_with(self, obj_x, obj_y, size):
        # Simple collision detection (circle-rectangle approximation)
        return (abs(self.x - obj_x) < ENEMY_SIZE + size) and (abs(self.y - obj_y) < ENEMY_SIZE + size)

# --------------------------
# Game Class
# --------------------------
class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.player = Player(self.canvas)
        self.bullets = []
        self.enemies = []
        self.score = 0

        # For keeping the game-over meme image in memory
        self.ninja_image = None

        # Bind keys for movement and mouse for shooting
        root.bind("<KeyPress>", self.on_key_press)
        self.canvas.bind("<Button-1>", self.on_mouse_click)

        # Start enemy spawn loop and game update loop
        self.spawn_enemy()
        self.update()

    def on_key_press(self, event):
        key = event.keysym.lower()
        if key in ("w", "up"):
            self.player.move(0, -1)
        elif key in ("s", "down"):
            self.player.move(0, 1)
        elif key in ("a", "left"):
            self.player.move(-1, 0)
        elif key in ("d", "right"):
            self.player.move(1, 0)

    def on_mouse_click(self, event):
        bullet = Bullet(self.canvas, self.player.x, self.player.y, event.x, event.y)
        self.bullets.append(bullet)

    def spawn_enemy(self):
        enemy = Enemy(self.canvas, self.player)
        self.enemies.append(enemy)
        # Spawn a new enemy every 2 seconds
        self.root.after(2000, self.spawn_enemy)

    def update(self):
        # Update bullets; remove if necessary
        for bullet in self.bullets[:]:
            if not bullet.update():
                self.bullets.remove(bullet)

        # Update enemies and check collisions
        for enemy in self.enemies[:]:
            enemy.update()
            # Check collision with player (simple proximity check)
            if enemy.collides_with(self.player.x, self.player.y, PLAYER_SIZE):
                self.player.health -= 1
                if self.player.health <= 0:
                    self.game_over()
                    return

            # Check collision with bullets
            for bullet in self.bullets[:]:
                if enemy.collides_with(bullet.x, bullet.y, BULLET_SIZE):
                    enemy.health -= 25
                    bullet.destroy()
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    if enemy.health <= 0:
                        enemy.destroy()
                        self.enemies.remove(enemy)
                        self.score += 1
                        break

        # Draw HUD
        self.canvas.delete("hud")
        hud_text = f"Health: {self.player.health}    Score: {self.score}"
        self.canvas.create_text(10, 10, anchor="nw", text=hud_text, fill="white", font=("Arial", 16), tag="hud")

        # Schedule next update (~50 FPS)
        self.root.after(20, self.update)

    def game_over(self):
        # Clear the canvas
        self.canvas.delete("all")
        try:
            # Attempt to load the ninja meme image
            self.ninja_image = game_over_image = tk.PhotoImage(file="ninja_low_taper_fade.png")
            # Display the image centered on the canvas.
            # (Ensure your image is large or scaled appropriately to fill the window.)
            self.canvas.create_image(WIDTH//2, HEIGHT//2, image=self.ninja_image)
        except Exception as e:
            # If the image file isn't found, fallback to text
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="Game Over\n(No Meme Image Found)",
                                    fill="white", font=("Arial", 36))

# --------------------------
# Main Program
# --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minimal CS:GO Prototype (Tkinter)")
    game = Game(root)
    root.mainloop()
"""
"""
import random

# Story Elements
titles = ["The Lost Treasure", "The Forbidden Forest", "Space Odyssey", "The Cursed Amulet", "Cyberpunk Heist"]
settings = ["a dark cave", "a mystical castle", "a neon-lit city", "an abandoned spaceship", "a parallel dimension"]
companions = ["a talking cat", "a rogue AI", "a retired knight", "a time traveler", "a disgruntled goblin"]
conflicts = ["an ancient prophecy", "a robot uprising", "a stolen artifact", "a shadowy organization", "an unstable reality rift"]
outcomes = ["become a legend", "find a secret society", "lose all memories", "unleash chaos", "gain immortality"]


def generate_story():
    title = random.choice(titles)
    setting = random.choice(settings)
    companion = random.choice(companions)
    conflict = random.choice(conflicts)
    outcome = random.choice(outcomes)

    print(f"\n--- {title} ---\n")
    print(f"You find yourself in {setting}. With you is {companion}.")
    print(f"Your adventure revolves around {conflict}.")
    print(f"At the end of your journey, you will {outcome}.")
    print("\nPrepare for the unexpected!\n")

def main():
    print("Welcome to the Random Adventure Generator!")
    while True:
        generate_story()
        cont = input("Generate another story? (y/n): ")
        if cont.lower() != 'y':
            break


# Padding with nonsense to make it 1000 lines
for i in range(970):
    if i % 10 == 0:
        print("# Still adding pointless lines")
    else:
        print(f"# Line {i + 1}: This line exists to fill space")

if __name__ == "__main__":
    main()
"""

import random
import time


def fear_magneto():
    print("Magneto rises, his power beyond comprehension...")
    time.sleep(1)
    chaos_meter = random.randint(1, 100)
    print(f"The world trembles! Chaos Level: {chaos_meter}%")
    time.sleep(1)

    for _ in range(5):
        event = random.choice([
            "Metallic hurricanes tear through the sky!",
            "Reality bends as Magneto's will warps gravity!",
            "Every compass on Earth spins wildly!",
            "Lightning solidifies into razor-sharp steel bolts!",
            "Time itself distorts, past and future collide!"
        ])
        print(event)
        time.sleep(1)

    print("\nBut then... A booming voice echoes through the chaos...")
    time.sleep(2)
    print("IT'S CLOBBERIN' TIME!")
    time.sleep(1)

    for _ in range(5):
        punch_effect = random.choice([
            "The fabric of space cracks as The Thing lands a blow!",
            "Magneto falters, metal flying in all directions!",
            "The Earth itself shakes from the impact!",
            "An entire city block is reduced to rubble!",
            "A shockwave ripples across the multiverse!"
        ])
        print(punch_effect)
        time.sleep(1)

    print("\nPure chaos. Absolute destruction. And then... silence.")
    time.sleep(2)
    print("Who won? No one knows. Only the echoes of battle remain...")


if __name__ == "__main__":
    fear_magneto()
