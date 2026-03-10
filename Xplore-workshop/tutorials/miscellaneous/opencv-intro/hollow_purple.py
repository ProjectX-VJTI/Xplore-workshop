import cv2
import numpy as np
import math
import random
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

# --- Setup ---
WIDTH, HEIGHT = 1280, 720
FPS = 60
DURATION = 6  # Extended for smoothness
TOTAL_FRAMES = FPS * DURATION
CENTER = (WIDTH // 2, HEIGHT // 2)
PHASE_DURATION = 0.4  # Time until the purple mass appears

# --- Animation Logic ---

# Load Backgrounds (Ensure these files exist in your directory)
# bg_start: Light blue/sea
# bg_end: Dark purple/galaxy
bg_start = cv2.imread(str(SCRIPT_DIR / "bg_start.png"))
bg_end = cv2.imread(str(SCRIPT_DIR / "bg_end.png"))

# Resize backgrounds to match frame size
bg_start = cv2.resize(bg_start, (WIDTH, HEIGHT))
bg_end = cv2.resize(bg_end, (WIDTH, HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(str(SCRIPT_DIR / "hollow_purple_evolution.mp4"), fourcc, FPS, (WIDTH, HEIGHT))

def draw_glowing_orb(img, pos, radius, color, shimmer=True):
    """Draws a multi-layered orb to simulate a liquid/energy drop."""
    # Add a tiny bit of random 'life' to the radius
    if shimmer:
        radius += random.randint(-2, 2)
    
    # Layering for a 'glow' effect (simulating a mesh/depth)
    for r in range(radius, 0, -2):
        alpha = 1.0 - (r / radius)
        overlay = img.copy()
        cv2.circle(overlay, pos, r, color, -1)
        # Apply alpha blending
        cv2.addWeighted(overlay, 0.2, img, 0.8, 0, img)

    # Core highlight to make it look like a sphere/drop
    cv2.circle(img, (pos[0]-int(radius*0.3), pos[1]-int(radius*0.3)), 
               int(radius*0.2), (255, 255, 255), -1)

for frame_num in range(TOTAL_FRAMES):
    t = frame_num / TOTAL_FRAMES
    
    # 1. Background Transition Logic
    # Transition starts halfway through the spiral
    bg_weight = np.clip((t - PHASE_DURATION) * 2, 0, 1) 
    frame = cv2.addWeighted(bg_start, 1 - bg_weight, bg_end, bg_weight, 0)

    # 2. Spiral Physics
    # Slower decay for a smoother 'dance'
    max_dist = 400
    current_dist = max_dist * (1 - t)**1.5
    angle = t * math.pi * 12 # 6 rotations
    
    # Adding a slight 'wobble' to the path for realism
    wobble = math.sin(t * 50) * 5
    
    r_pos = (int(CENTER[0] + (current_dist + wobble) * math.cos(angle)),
             int(CENTER[1] + (current_dist + wobble) * math.sin(angle)))
    
    b_pos = (int(CENTER[0] + (current_dist + wobble) * math.cos(angle + math.pi)),
             int(CENTER[1] + (current_dist + wobble) * math.sin(angle + math.pi)))

    # 3. State Management: Spiral vs Combine
    if t < PHASE_DURATION:
        # Drawing the Orbs (Red and Blue)
        # Red: (BGR: 50, 50, 255), Blue: (BGR: 255, 50, 50)
        draw_glowing_orb(frame, r_pos, 35, (50, 50, 255))
        draw_glowing_orb(frame, b_pos, 35, (255, 50, 50))
        
        # Add a subtle ripple trail
        if frame_num % 5 == 0:
            cv2.circle(frame, r_pos, 45, (100, 100, 255), 1)
            cv2.circle(frame, b_pos, 45, (255, 100, 100), 1)

    else:
        # 4. The Hollow Purple "Imaginary Mass"
        # Combine phase: Rapid expansion
        impact_t = (t - PHASE_DURATION) / 0.15
        purple_radius = int(20 + (impact_t * 100))
        
        # Draw the purple mass with a thick energy border
        draw_glowing_orb(frame, CENTER, purple_radius, (180, 0, 130), shimmer=True)
        
        # Distortion Ripple Effect
        # We simulate a shockwave by drawing thin, high-contrast circles
        for i in range(3):
            rip_r = int(purple_radius * (1 + (i * 0.2)))
            alpha = max(0, 1 - impact_t)
            cv2.circle(frame, CENTER, rip_r, (255, 255, 255), 2)

    out.write(frame)

out.release()
print("Animation complete. 'hollow_purple_evolution.mp4' created.")
