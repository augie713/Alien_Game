import tkinter as tk
from tkinter import PhotoImage

M = ""
RAR = 0  # Red Alien Relations score
GAR = 0  # Green Alien Relations score
MONEY = 100  # Starting money score
CHAOS = 50  # Starting chaos score (custom resource)

C = ""

# === EVENTS ===
Event1 = "Hey! We just came to visit Spain from our home planet! Hope we have a great time! Are you the king by any chance? "
Event2 = "Cool! We’ll be around the place. Thank you for your service! Our green friends are on their way by the way, they will arrive soon. "
Event3 = "Hey! Would you like to flip a coin? If it’s tails, you’ll get x coins, if not, you’ll give me x coins. Deal? "
Event4 = "Alright then! Good luck to the both of us!"
Event5 = "Coin Flip!"
Event6 = "No? Aw that’s sad... See you soon!"
Event7 = "Hello! We were wondering if we could decorate the city to celebrate our holiday. the UFOurth of July. but setting up all the decorations will cost money, also, the greens don't really like this holiday, as it's very loud. Would you help us?"
Event8 = "Thank you! We'll try to keep it quiet, but no promises!"
Event9 = "Thank you for stopping their 'celebration'. We like the reds, but they can get a bit rowdy when it comes to parties, we’ll be sure to invite them to our own holiday! If you can spare some cash... we don’t need much, and the reds will join in!"
Event10 = "Thanks! Sorry about the cost, but I'm sure the reds will love this!"
Event11 = "Oh, okay, no worries then! Maybe next time!"
Event12 = "We have more schools than the Greens, but our schools are full. So, we're wondering if you could have our students go to the Green schools too? But they might be a little stuffed."
Event13 = "Thank you! We appreciate it,"
Event14 = "Hey, it is nice of you to want us to share schools and all, but what if we want to learn too? We would greatly appreciate it if you could build another school for us, since ours are a bit full now."
Event15 = "Thanks! We really appreciate it!"
Event16 = "I understand, it's not exactly cheap and there is enough room for now."
Event17 = "Oh okay, well I guess those poor starving children didn't deserve a future anyway did they, let them rot in a lonely uneducated life of sadness... are you sure?"
Event18 = "Fine then, it's okay, but in that case could we build some more schools? It might be costly though."
Event19 = "Thank you so much, we appreciate this gesture we'll have more access to education now!"
Event20 = "Oh okay, it's quite expensive anyway."
Event21 = "One hundred Reds could beat one hundred Greens, right?"
Event22 = "Oh! See you never then."
Event23 = "The aliens left."
Event24 = "I knew it! You know, you should make it an event no? Have an audience, we could throw one hundred of each into a pit and make ‘em battle it out! What do you say?"
Event25 = "Oh? Are you sure? Why don't we test it? Have a game? We can throw one hundred of each into a pit and make ‘em battle it out! What do you say?"
Event26 = "YES!!! Thank you! Our glorious king! I always knew you were a good one, the people will love you for this!"
Event27 = "The people did not take kindly to their king asking people to fight to the death in a pit, and quit following you."
Event28 = "N-No? What do you mean no! I knew it all along, you are no king! Just a dictator who wants to take our rights and freedom!!"
Event29 = "Sorry, the game isn't finished yet, we'll continue working on it soon. See you!"
Event30 = "We have a new proposal! How about a trade agreement? It could benefit both our species!"
Event31 = "If you agree, we can exchange resources that will help us both thrive!"
Event32 = "If you decline, we might have to reconsider our relationship."
Event33 = "We heard about a festival happening soon. Would you like to join us in the celebrations?"
Event34 = "It could be a great way to strengthen our bonds!"
Event35 = "If you choose not to participate, it might upset the Greens."

Event = [Event1, Event2, Event3, Event4, Event5, Event6, Event7, Event8, Event9, Event10, Event11, Event12, Event13, Event14, Event15, Event16, Event17, Event18, Event19, Event20, Event21, Event22, Event23, Event24, Event25, Event26, Event27, Event28, Event29, Event30, Event31, Event32, Event33, Event34, Event35]

# === GUI SETUP ===
root = tk.Tk()
root.title("CorteRoom")
canvas = tk.Canvas(root, width=1000, height=600)
canvas.pack()

def safe_photo(path, subsample=(1, 1)):
    try:
        img = PhotoImage(file=path)
        return img.subsample(*subsample)
    except:
        print(f"Image not found: {path}")
        return None

background_img = safe_photo("corute room.png")
human_img = safe_photo("king.png", subsample=(2, 2))
alien_img_1 = safe_photo("alien_image_1.png", subsample=(3, 1))
alien_img_2 = safe_photo("alien_image_2.png", subsample=(3, 1))
extra_alien_img = safe_photo("alin.png", subsample=(3, 3))  # Optional
box_boc = safe_photo("box.png")

# === PLACE BACKGROUND ===
if background_img:
    canvas.create_image(500, 300, image=background_img)

# === PLACE CHARACTERS ===
if human_img:
    canvas.create_image(200, 400, image=human_img)  

if extra_alien_img:
    canvas.create_image(700, 200, image=extra_alien_img)  

alien_id = None
if alien_img_1:
    alien_id = canvas.create_image(900, 300, image=alien_img_1)

text_id = canvas.create_text(700, 180, text="", width=200, font=("Arial", 12), fill="black")

# === STATISTICS BOX (Background Rectangle + Text) ===
stats_box_background = canvas.create_rectangle(10, 10, 300, 150, fill="lightgrey", outline="black", width=2)
stats_box = canvas.create_text(
    20, 20, 
    text="", 
    font=("Arial", 14, "bold"), 
    fill="black", 
    anchor="nw",
    justify="left"
)

yes_button = no_button = None

# Scenes unchanged from original with events and choices, plus new added events
scenes = {
    "start": {
        "text": Event1,
        "choices": {
            "yes": "green_on_the_way",
            "no": "see_u_never"
        }
    },
    "green_on_the_way": {
        "text": Event2,
        "auto": True,
        "next": "coin_flip_request"
    },
    "coin_flip_request": {
        "text": Event3,
        "choices": {
            "yes": "yes_coin_flip",
            "no": "no_coin_flip"
        }
    },
    "yes_coin_flip": {
        "text": Event4,
        "auto": True,
        "next": "flip_coin"
    },
    "flip_coin": {
        "text": Event5,
        "auto": True,
        "next": "decorate_city"
    },
    "no_coin_flip": {
        "text": Event6,
        "auto": True,
        "next": "decorate_city"
    },
    "decorate_city": {
        "text": Event7,
        "choices": {
            "yes": "yes_decoration",
            "no": "green_celebration_request"
        }
    },
    "yes_decoration": {
        "text": Event8,
        "auto": True,
        "next": "full_schools"
    },
    "green_celebration_request": {
        "text": Event9,
        "choices": {
            "yes": "yes_green_celebration",
            "no": "no_green_celebration"
        }
    },
    "yes_green_celebration": {
        "text": Event10,
        "auto": True,
        "next": "full_schools"
    },
    "no_green_celebration": {
        "text": Event11,
        "auto": True,
        "next": "full_schools"
    },
    "full_schools": {
        "text": Event12,
        "choices": {
            "yes": "yes_schools",
            "no": "no_schools"
        }
    },
    "yes_schools": {
        "text": Event13,
        "auto": True,
        "next": "new_school"
    },
    "new_school": {
        "text": Event14,
        "choices": {
            "yes": "yes_new_school",
            "no": "no_new_school"
        }
    },
    "yes_new_school": {
        "text": Event15,
        "auto": True,
        "next": "100v100"
    },
    "no_new_school": {
        "text": Event16,
        "auto": True,
        "next": "100v100"
    },
    "no_schools": {
        "text": Event17,
        "choices": {
            "yes": "yes_schools",
            "no": "def_no_schools"
        }
    },
    "def_no_schools": {
        "text": Event18,
        "choices": {
            "yes": "yes_own_school",
            "no": "no_own_school"
        }
    },
    "yes_own_school": {
        "text": Event19,
        "auto": True,
        "next": "100v100"
    },
    "no_own_school": {
        "text": Event20,
        "auto": True,
        "next": "100v100"
    },
    "100v100": {
        "text": Event21,
        "choices": {
            "yes": "yes100",
            "no": "no100"
        }
    },
    "see_u_never": {
        "text": Event22,
        "auto": True,
        "next": "leaving_ending"
    },
    "leaving_ending": {
        "text": Event23,
        "choices": {}
    },
    "yes100": {
        "text": Event24,
        "choices": {
            "yes": "yes_pit",
            "no": "no_pit"
        }
    },
    "no100": {
        "text": Event25,
        "choices": {
            "yes": "yes_pit",
            "no": "no_pit"
        }
    },
    "yes_pit": {
        "text": Event26,
        "auto": True,
        "next": "yes_pit_ending"
    },
    "yes_pit_ending": {
        "text": Event27,
        "choices": {}
    },
    "no_pit": {
        "text": Event28,
        "auto": True,
        "next": "game_not_finished"
    },
    "game_not_finished": {
        "text": Event29,
        "choices": {}
    },
    "trade_agreement": {
        "text": Event30,
        "choices": {
            "yes": "yes_trade",
            "no": "no_trade"
        }
    },
    "yes_trade": {
        "text": Event31,
        "auto": True,
        "next": "festival_invitation"
    },
    "no_trade": {
        "text": Event32,
        "auto": True,
        "next": "festival_invitation"
    },
    "festival_invitation": {
        "text": Event33,
        "choices": {
            "yes": "yes_festival",
            "no": "no_festival"
        }
    },
    "yes_festival": {
        "text": Event34,
        "auto": True,
        "next": "end_festival"
    },
    "no_festival": {
        "text": Event35,
        "auto": True,
        "next": "end_festival"
    },
    "end_festival": {
        "text": "The festival was a success! Your relations with both aliens improved.",
        "choices": {}
    }
}

current_scene = "start"

def update_stats():
    global RAR, GAR, MONEY, CHAOS
    stats_text = (
        f"Red Alien Relations: {RAR}\n"
        f"Green Alien Relations: {GAR}\n"
        f"Money: ${MONEY}\n"
        f"Chaos: {CHAOS}"
    )
    canvas.itemconfig(stats_box, text=stats_text)

def render_scene(scene_name):
    global current_scene, yes_button, no_button, alien_id, RAR, GAR, MONEY, CHAOS
    current_scene = scene_name
    scene = scenes.get(scene_name, {})
    canvas.itemconfig(text_id, text=scene.get("text", "Scene not found."))

    # Update alien image based on scene ending on 'yes' or not
    if alien_id:
        img = alien_img_1 if str(scene_name).endswith("yes") else alien_img_2
        if img:
            canvas.itemconfig(alien_id, image=img)

    if yes_button:
        yes_button.destroy()
    if no_button:
        no_button.destroy()

    # Update stats display
    update_stats()

    if scene.get("auto"):
        # For automatic transitions, optionally update scores based on scene
        adjust_scores_for_scene(scene_name)
        root.after(1500, lambda: render_scene(scene["next"]))
        return

    choices = scene.get("choices", {})
    if choices:
        def yes_action():
            adjust_scores_for_choice(scene_name, "yes")
            render_scene(choices["yes"])

        def no_action():
            adjust_scores_for_choice(scene_name, "no")
            render_scene(choices["no"])

        yes_button = tk.Button(root, text="Yes", command=yes_action)
        no_button = tk.Button(root, text="No", command=no_action)
        yes_button.place(x=400, y=300, width=150)
        no_button.place(x=600, y=300, width=150)
    else:
        # Clear buttons if no choices
        if yes_button:
            yes_button.destroy()
            yes_button = None
        if no_button:
            no_button.destroy()
            no_button = None

def adjust_scores_for_choice(scene_name, choice):
    global RAR, GAR, MONEY, CHAOS
    # Logic to affect scores per scene choice - customize based on event narrative

    if scene_name == "start":
        if choice == "yes":
            GAR += 1  # Green friends arriving increases green relations
        else:
            GAR -= 1

    elif scene_name == "decorate_city":
        if choice == "yes":
            cost = 20
            if MONEY >= cost:
                MONEY -= cost  # Paying for decorations costs money
                RAR += 2      # Reds happy
                GAR -= 1      # Greens annoyed
            else:
                # Not enough money effects could be added
                pass
        else:
            GAR += 1  # Stopping celebration pleases greens

    elif scene_name == "green_celebration_request":
        if choice == "yes":
            GAR += 2
            MONEY -= 10  # Accepting costs money to support celebration
            CHAOS += 5
        else:
            GAR -= 2
            CHAOS -= 5

    elif scene_name == "full_schools":
        if choice == "yes":
            GAR += 1
            CHAOS += 10
        else:
            RAR -= 1
            CHAOS -= 5

    elif scene_name == "yes_new_school":
        MONEY -= 40
        GAR += 3
        CHAOS += 10

    elif scene_name == "no_new_school":
        RAR -= 2
        GAR -= 1

    elif scene_name == "100v100":
        if choice == "yes":
            RAR += 3
            MONEY += 10
        else:
            GAR += 3
            MONEY += 10

    elif scene_name == "yes_pit":
        RAR += 5
        CHAOS -= 10
        MONEY += 20

    elif scene_name == "no_pit":
        GAR += 5
        CHAOS += 5

    elif scene_name == "yes_coin_flip":
        MONEY += 10  # Winning coin flip (example)

    elif scene_name == "no_coin_flip":
        MONEY -= 5

    elif scene_name == "yes_trade":
        RAR += 2
        GAR += 2
        MONEY += 15

    elif scene_name == "no_trade":
        RAR -= 1
        GAR -= 1

    elif scene_name == "yes_festival":
        RAR += 3
        GAR += 3
        CHAOS -= 5

    elif scene_name == "no_festival":
        RAR -= 1
        GAR -= 1
        CHAOS += 5

def adjust_scores_for_scene(scene_name):
    # Effects for auto-transition scenes (optional)
    global RAR, GAR, MONEY, CHAOS
    if scene_name == "green_on_the_way":
        GAR += 1
    elif scene_name == "yes_decoration":
        RAR += 1
    elif scene_name == "yes_green_celebration":
        GAR += 2
    elif scene_name == "no_green_celebration":
        GAR -= 1
    elif scene_name == "yes_schools":
        GAR += 1
    elif scene_name == "no_schools":
        RAR -= 1
    elif scene_name == "yes100":
        RAR += 1
    elif scene_name == "no100":
        GAR += 1
    elif scene_name == "yes_pit_ending":
        RAR += 1
    elif scene_name == "game_not_finished":
        CHAOS += 1
    elif scene_name == "yes_trade":
        RAR += 1
        GAR += 1
    elif scene_name == "no_trade":
        RAR -= 1
        GAR -= 1
    elif scene_name == "yes_festival":
        GAR += 1
        RAR += 1
    elif scene_name == "no_festival":
        GAR -= 1
        RAR -= 1

render_scene("start")
root.mainloop()

