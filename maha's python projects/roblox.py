import pygame
import sys

# Initialize Pygame
pygame.init()

# --- Constants ---
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 5
JUMP_STRENGTH = 15
GRAVITY = 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (135, 206, 235) # Sky color
GRASS_GREEN = (34, 139, 34) # Grass color
DIRT_BROWN = (139, 69, 19) # House roof color
WOOD_BROWN = (160, 82, 45) # House wall color
PALE_YELLOW = (250, 235, 215) # Inside house color
ITEM_COLOR_KEY = (255, 223, 0) # Gold color for a key
ITEM_COLOR_BOOK = (139, 69, 19) # Brown for a book
ITEM_COLOR_COIN = (255, 215, 0) # Gold for a coin

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Game Full - Improved")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)
title_font = pygame.font.SysFont("Arial", 30, bold=True)

# --- Game State Variables ---
player_x = 100
player_y = HEIGHT - 200
player_vel_y = 0
on_ground = True
in_house = False

# Player position inside the house
player_x_inside = WIDTH // 2 - 25 # Centered horizontally
player_y_inside = HEIGHT - 150 # On the floor inside the house

# Character customization options
shirt_colors = [(200, 0, 0), (0, 200, 200), (255, 165, 0), (0, 128, 0)]
shirt_styles = ["short", "long"]
pants_colors = [(0, 0, 255), (50, 50, 50), (100, 50, 0), (150, 150, 150)]
pants_styles = ["tight", "wide"]
dress_colors = [(128, 0, 128), (255, 192, 203), (70, 130, 180), (255, 0, 0)]
dress_styles = ["short", "long"]
skirt_colors = [(255, 182, 193), (255, 105, 180), (0, 200, 0), (100, 0, 100)]
skirt_styles = ["mini", "midi"]
hair_styles = [(0, 0, 0), (255, 215, 0), (139, 69, 19), (200, 200, 200)]
face_styles = [":)", ":(", "zzz", ">:(", "XD", "O_O"]

pet_options = ["cat", "dog", "duck", "rabbit"]

# Current selection indices for customization
shirt_color_index = 0
shirt_style_index = 0
pants_color_index = 0
pants_style_index = 0
dress_color_index = 0
dress_style_index = 0
skirt_color_index = 0
skirt_style_index = 0
hair_index = 0
face_index = 0
pet_index = 0

show_custom_menu = False
pet_leg_offset = 0
pet_leg_direction = 1

# UI Elements (Rectangles for buttons and house)
custom_button = pygame.Rect(WIDTH - 150, HEIGHT - 70, 120, 40)
menu_buttons = {
    "Shirt Color": pygame.Rect(70, 70, 120, 30),
    "Shirt Style": pygame.Rect(200, 70, 120, 30),
    "Pants Color": pygame.Rect(330, 70, 120, 30),
    "Pants Style": pygame.Rect(460, 70, 120, 30),
    "Dress Color": pygame.Rect(70, 110, 120, 30),
    "Dress Style": pygame.Rect(200, 110, 120, 30),
    "Skirt Color": pygame.Rect(330, 110, 120, 30),
    "Skirt Style": pygame.Rect(460, 110, 120, 30),
    "Hair": pygame.Rect(70, 150, 100, 30),
    "Face": pygame.Rect(180, 150, 100, 30),
    "Pet": pygame.Rect(290, 150, 100, 30),
}
house_rect = pygame.Rect(600, HEIGHT - 150, 100, 100)

# --- Item System ---
class Item:
    def __init__(self, name, color, x, y, size=20):
        self.name = name
        self.color = color
        self.rect = pygame.Rect(x, y, size, size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=5)
        item_text = font.render(self.name, True, BLACK)
        # Center the text on the item
        text_rect = item_text.get_rect(center=self.rect.center)
        surface.blit(item_text, text_rect)

# Initial items inside the house
current_items_in_house = [
    Item("Key", ITEM_COLOR_KEY, WIDTH // 2 - 100, HEIGHT - 170),
    Item("Book", ITEM_COLOR_BOOK, WIDTH // 2 + 50, HEIGHT - 170),
    Item("Coin", ITEM_COLOR_COIN, WIDTH // 2, HEIGHT - 170),
]

player_inventory = []
INVENTORY_SLOT_SIZE = 40
INVENTORY_SLOT_COUNT = 5 # Number of slots in the inventory

# --- Drawing Functions ---

def draw_rounded_rect(surface, color, rect, radius):
    """Draws a rectangle with rounded corners."""
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def draw_player(x, y):
    """Draws the player character with current customization."""
    # Head and Face
    hair_color = hair_styles[hair_index]
    pygame.draw.circle(screen, hair_color, (x + 25, y - 10), 20) # Hair
    pygame.draw.circle(screen, (255, 224, 189), (x + 25, y), 18) # Skin color for face
    face_text = font.render(face_styles[face_index], True, BLACK)
    screen.blit(face_text, (x + 15, y - 10))

    # Body and Clothing
    if dress_style_index != 0: # If dress is selected
        pygame.draw.rect(screen, dress_colors[dress_color_index], (x + 5, y + 20, 40, 60 if dress_styles[dress_style_index] == "short" else 80))
    elif skirt_style_index != 0: # If skirt is selected
        pygame.draw.rect(screen, shirt_colors[shirt_color_index], (x + 10, y + 20, 30, 30)) # Shirt part
        pygame.draw.rect(screen, skirt_colors[skirt_color_index], (x + 5, y + 50, 40, 30 if skirt_styles[skirt_style_index] == "mini" else 40)) # Skirt part
    else: # Default: shirt and pants
        pygame.draw.rect(screen, shirt_colors[shirt_color_index], (x + 10, y + 20, 30, 40 if shirt_styles[shirt_style_index] == "short" else 50)) # Shirt
        pygame.draw.rect(screen, pants_colors[pants_color_index], (x + 10, y + 60, 10, 20 if pants_styles[pants_style_index] == "tight" else 30))
        pygame.draw.rect(screen, pants_colors[pants_color_index], (x + 30, y + 60, 10, 20 if pants_styles[pants_style_index] == "tight" else 30))

def draw_pet(x, y):
    """Draws the selected pet with simple leg animation."""
    global pet_leg_offset, pet_leg_direction
    kind = pet_options[pet_index]

    if kind == "cat":
        color = (150, 150, 255)
        pygame.draw.ellipse(screen, color, (x, y + 80, 30, 20))
        pygame.draw.circle(screen, color, (x + 35, y + 80), 10)
        pygame.draw.polygon(screen, color, [(x+30, y+70), (x+35, y+75), (x+40, y+70)])
        pygame.draw.polygon(screen, color, [(x+40, y+70), (x+45, y+75), (x+50, y+70)])
    elif kind == "dog":
        color = (160, 100, 60)
        pygame.draw.ellipse(screen, color, (x, y + 80, 35, 22))
        pygame.draw.circle(screen, color, (x + 40, y + 80), 11)
        pygame.draw.polygon(screen, color, [(x+35, y+75), (x+40, y+85), (x+45, y+75)])
    elif kind == "duck":
        color = (255, 255, 0)
        pygame.draw.ellipse(screen, color, (x, y + 85, 28, 18))
        pygame.draw.circle(screen, color, (x + 30, y + 85), 9)
        pygame.draw.rect(screen, (255, 165, 0), (x + 33, y + 87, 6, 4))
    elif kind == "rabbit":
        color = (200, 200, 200)
        pygame.draw.ellipse(screen, color, (x, y + 80, 25, 20))
        pygame.draw.circle(screen, color, (x + 30, y + 80), 10)
        pygame.draw.ellipse(screen, color, (x + 28, y + 65, 5, 15))
        pygame.draw.ellipse(screen, color, (x + 35, y + 65, 5, 15))

    # Legs animation
    leg_y = y + 95 + pet_leg_offset
    for leg_x_offset in [5, 10, 20, 25]:
        pygame.draw.rect(screen, color, (x + leg_x_offset, leg_y, 5, 10))

    pet_leg_offset += pet_leg_direction * 0.5
    if abs(pet_leg_offset) > 2:
        pet_leg_direction *= -1

def draw_house():
    """Draws the house structure."""
    draw_rounded_rect(screen, WOOD_BROWN, house_rect, 10)
    pygame.draw.polygon(screen, DIRT_BROWN, [(house_rect.x, house_rect.y),
                                            (house_rect.x + house_rect.width // 2, house_rect.y - 50),
                                            (house_rect.x + house_rect.width, house_rect.y)])
    pygame.draw.rect(screen, BLACK, (house_rect.x + 35, house_rect.y + 50, 30, 50))
    pygame.draw.circle(screen, (255, 215, 0), (house_rect.x + 60, house_rect.y + 75), 3)

def draw_inside_house():
    """Draws the scene when inside the house, including items and inventory."""
    screen.fill(PALE_YELLOW) # Light background for inside
    # Floor inside the house
    pygame.draw.rect(screen, (100, 100, 100), (0, HEIGHT - 100, WIDTH, 100)) # Gray floor

    text = font.render("Inside the house - Press ESC to leave, E to pick up items", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, 30))
    screen.blit(text, text_rect)

    # Simple furniture
    pygame.draw.rect(screen, (100, 50, 0), (100, HEIGHT - 150, 150, 50)) # Table
    pygame.draw.rect(screen, (100, 50, 0), (120, HEIGHT - 100, 30, 50)) # Table leg 1
    pygame.draw.rect(screen, (100, 50, 0), (200, HEIGHT - 100, 30, 50)) # Table leg 2
    pygame.draw.rect(screen, (80, 40, 0), (300, HEIGHT - 100, 50, 50)) # Chair seat
    pygame.draw.rect(screen, (80, 40, 0), (300, HEIGHT - 150, 10, 50)) # Chair back

    # Draw items currently in the house
    for item in current_items_in_house:
        item.draw(screen)

    # Draw inventory slots
    inventory_start_x = (WIDTH - (INVENTORY_SLOT_COUNT * INVENTORY_SLOT_SIZE + (INVENTORY_SLOT_COUNT - 1) * 5)) // 2
    for i in range(INVENTORY_SLOT_COUNT):
        slot_rect = pygame.Rect(inventory_start_x + i * (INVENTORY_SLOT_SIZE + 5), HEIGHT - INVENTORY_SLOT_SIZE - 10, INVENTORY_SLOT_SIZE, INVENTORY_SLOT_SIZE)
        pygame.draw.rect(screen, GRAY, slot_rect, 2, border_radius=5) # Draw empty slot border
        if i < len(player_inventory):
            # Draw item in slot
            item_in_slot = player_inventory[i]
            # Draw a smaller version of the item centered in the slot
            item_rect_in_slot = pygame.Rect(slot_rect.x + 5, slot_rect.y + 5, INVENTORY_SLOT_SIZE - 10, INVENTORY_SLOT_SIZE - 10)
            pygame.draw.rect(screen, item_in_slot.color, item_rect_in_slot, border_radius=3)
            item_text_in_slot = font.render(item_in_slot.name[0].upper(), True, BLACK) # Just first letter
            text_rect_in_slot = item_text_in_slot.get_rect(center=item_rect_in_slot.center)
            screen.blit(item_text_in_slot, text_rect_in_slot)


def draw_custom_menu():
    """Draws the customization menu panel and buttons."""
    menu_panel_rect = pygame.Rect(40, 10, WIDTH - 80, 200)
    draw_rounded_rect(screen, (50, 50, 50, 200), menu_panel_rect, 15)
    pygame.draw.rect(screen, (70, 70, 70), menu_panel_rect, 3, border_radius=15)

    title_text = title_font.render("Character Customization", True, WHITE)
    title_text_rect = title_text.get_rect(center=(WIDTH // 2, 35))
    screen.blit(title_text, title_text_rect)

    for label, rect in menu_buttons.items():
        draw_rounded_rect(screen, GRAY, rect, 8)
        pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)
        text = font.render(label, True, BLACK)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    instruction_text = font.render("Click options to cycle, ESC to close menu", True, WHITE)
    instruction_text_rect = instruction_text.get_rect(center=(WIDTH // 2, 190))
    screen.blit(instruction_text, instruction_text_rect)

def draw_button(rect, label):
    """Draws a generic button with improved styling."""
    pygame.draw.rect(screen, (50, 50, 50), rect, border_radius=10)
    pygame.draw.rect(screen, (80, 80, 80), rect.inflate(-4, -4), border_radius=8)
    text = font.render(label, True, WHITE)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

def draw_background_elements():
    """Draws additional background elements like clouds and sun."""
    pygame.draw.circle(screen, (255, 255, 0), (700, 80), 40)
    pygame.draw.ellipse(screen, WHITE, (50, 50, 100, 50))
    pygame.draw.ellipse(screen, WHITE, (120, 40, 80, 40))
    pygame.draw.ellipse(screen, WHITE, (600, 100, 120, 60))
    pygame.draw.ellipse(screen, WHITE, (680, 90, 90, 50))


# --- Main Game Loop ---
running = True
while running:
    clock.tick(FPS)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not in_house and custom_button.collidepoint(event.pos):
                show_custom_menu = not show_custom_menu
            elif show_custom_menu:
                # Handle customization menu clicks
                if menu_buttons["Shirt Color"].collidepoint(event.pos):
                    shirt_color_index = (shirt_color_index + 1) % len(shirt_colors)
                elif menu_buttons["Shirt Style"].collidepoint(event.pos):
                    shirt_style_index = (shirt_style_index + 1) % len(shirt_styles)
                elif menu_buttons["Pants Color"].collidepoint(event.pos):
                    pants_color_index = (pants_color_index + 1) % len(pants_colors)
                elif menu_buttons["Pants Style"].collidepoint(event.pos):
                    pants_style_index = (pants_style_index + 1) % len(pants_styles)
                elif menu_buttons["Dress Color"].collidepoint(event.pos):
                    dress_color_index = (dress_color_index + 1) % len(dress_colors)
                    skirt_style_index = 0
                elif menu_buttons["Dress Style"].collidepoint(event.pos):
                    dress_style_index = (dress_style_index + 1) % len(dress_styles)
                    skirt_style_index = 0
                elif menu_buttons["Skirt Color"].collidepoint(event.pos):
                    skirt_color_index = (skirt_color_index + 1) % len(skirt_colors)
                    dress_style_index = 0
                elif menu_buttons["Skirt Style"].collidepoint(event.pos):
                    skirt_style_index = (skirt_style_index + 1) % len(skirt_styles)
                    dress_style_index = 0
                elif menu_buttons["Hair"].collidepoint(event.pos):
                    hair_index = (hair_index + 1) % len(hair_styles)
                elif menu_buttons["Face"].collidepoint(event.pos):
                    face_index = (face_index + 1) % len(face_styles)
                elif menu_buttons["Pet"].collidepoint(event.pos):
                    pet_index = (pet_index + 1) % len(pet_options)

        elif event.type == pygame.KEYDOWN:
            if not in_house:
                if event.key in [pygame.K_SPACE, pygame.K_UP]:
                    player_bottom_center = pygame.Rect(player_x + 20, player_y + 80, 10, 10)
                    if house_rect.colliderect(player_bottom_center):
                        in_house = True
                        show_custom_menu = False
                        # Reset player position to inside house
                        player_x_inside = WIDTH // 2 - 25
                        player_y_inside = HEIGHT - 150 # On the floor
                    elif on_ground:
                        player_vel_y = -JUMP_STRENGTH
                        on_ground = False
            elif in_house: # Inside house controls
                if event.key == pygame.K_ESCAPE:
                    in_house = False
                    # Reset player position to outside house near the door
                    player_x = house_rect.x + house_rect.width // 2 - 25
                    player_y = HEIGHT - 200 # On the ground outside
                elif event.key == pygame.K_e: # Pick up item
                    # Check for collision with items
                    player_rect_inside = pygame.Rect(player_x_inside, player_y_inside, 50, 100) # Approx player rect
                    items_to_remove = []
                    for item in current_items_in_house:
                        if player_rect_inside.colliderect(item.rect) and len(player_inventory) < INVENTORY_SLOT_COUNT:
                            player_inventory.append(item)
                            items_to_remove.append(item)
                    for item in items_to_remove:
                        current_items_in_house.remove(item)

    # Game Logic
    if not in_house:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_x += PLAYER_SPEED

        player_x = max(0, min(player_x, WIDTH - 50))

        player_y += player_vel_y
        player_vel_y += GRAVITY

        if player_y >= HEIGHT - 200:
            player_y = HEIGHT - 200
            player_vel_y = 0
            on_ground = True
    else: # Logic when inside the house
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x_inside -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_x_inside += PLAYER_SPEED

        # Keep player within house boundaries (simple bounds for now)
        player_x_inside = max(50, min(player_x_inside, WIDTH - 100)) # Adjusted for house walls

    # --- Drawing ---
    if not in_house:
        screen.fill(LIGHT_BLUE)
        draw_background_elements()
        pygame.draw.rect(screen, GRASS_GREEN, (0, HEIGHT - 50, WIDTH, 50))
        pygame.draw.rect(screen, DIRT_BROWN, (0, HEIGHT - 20, WIDTH, 20))
        draw_player(player_x, player_y)
        draw_pet(player_x - 30, player_y)
        draw_house()
        draw_button(custom_button, "Customize")
        if show_custom_menu:
            draw_custom_menu()
    else:
        draw_inside_house()
        draw_player(player_x_inside, player_y_inside) # Draw player at inside position
        draw_pet(player_x_inside - 30, player_y_inside) # Draw pet at inside position

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
