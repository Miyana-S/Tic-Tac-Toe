import tkinter as tk
from tkinter import messagebox
import random
from tkinter import PhotoImage
import pygame
pygame.mixer.init()


import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



# === Global Variables ===
theme = "star" 
game_mode = "pvp"
root = tk.Tk()
root.iconbitmap(resource_path("icon2tab.ico"))
root.resizable(False,False)

ai_difficulty = "easy"  # options: "easy", "medium", "hard"

click_sound = pygame.mixer.Sound(resource_path("Sounds/button-click.wav"))
place_sound = pygame.mixer.Sound(resource_path("Sounds/place-pawn.wav"))
win_sound = pygame.mixer.Sound(resource_path("Sounds/win-game.wav"))
draw_sound = pygame.mixer.Sound(resource_path("Sounds/draw-game.wav"))


# --- Toggle Logic ---
frame_visible = [False]
theop1= PhotoImage(file=resource_path('theop1.png'))
theop2= PhotoImage(file=resource_path('theop2.png'))
theop3= PhotoImage(file=resource_path('theop3.png'))

# === Theme Configurations ===
themes = {
    "star": {
        "bg": "#E4BAF4",
        "fg": "#000000",
        "cell_bg": "#eeeeee",
        "btg":'#B767D7',
        "ftg":'white',
        "walp":resource_path('Star/theme2.png'),
        "po":[resource_path("Star/po.png"),"Saturn"],
        "px":[resource_path("Star/px.png"),'Star'],
        "bd":resource_path('Star/bd.png'),
        "wb":resource_path('Star/mainbg.png')

    },
    "beach": {
        "bg": "#11B7C7",
        "fg": "#000000",
        "cell_bg": "#eeeeee",
        "btg":'#CFEBEE',
        "ftg":'#444444',
        "walp":resource_path("Beach/theme2.png"),
        "po":[resource_path('Beach/po1.png'),'Seashell'],
        "px":[resource_path('Beach/px1.png'),'Turtle'],
        "bd":resource_path('Beach/bd.png'),
        "wb":resource_path('Beach/mainbg.png')
    },
    "forest": {
        "bg": "#4D7A4B",
        "fg": "#ffffff",
        "cell_bg": "#444444",
        "btg":'#C9EAA2',
        "ftg":'#444444',
        "walp":resource_path("Forest/theme2.png"),
        "po":[resource_path('Forest/po.png'),'Robin'],
        "px":[resource_path('Forest/px.png'),'Fawn'],
        "bd":resource_path('Forest/bd.png'),
        "wb":resource_path('Forest/mainbg.png')
    }
}

# === Main Menu ===
def show_main_menu():
    clear_window()
    root.title("Tic-Tac-Toe")
    root.geometry("300x340")
    root.configure(bg=themes[theme]['bg'])

    icon2= PhotoImage(file=resource_path('icon2.png'))
    root.iconphoto(False,icon2)

    bg_image = PhotoImage(file=themes[theme]['wb'])
    # Create a label to hold the image
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0 ,relwidth=1, relheight=1)
    # Keep a reference
    bg_label.image = bg_image
    

    tk.Label(root, text="Tic-Tac-Toe", font=('Courier New',20,"bold"), bg=themes[theme]['bg'], fg=themes[theme]['fg']).place(x=58,y=42)
    
    tk.Button(root, text="Player vs Player",font=('Courier',12),bg=themes[theme]['btg'],fg=themes[theme]['ftg'],command=lambda: (click_sound.play(),start_game("pvp")),padx=16,pady=6).place(x=45,y=125)
    tk.Button(root, text="Player vs Computer", font=('Courier',12),bg=themes[theme]['btg'],fg=themes[theme]['ftg'], command=lambda: (click_sound.play(),start_game("pvc")),padx=6,pady=6).place(x=45,y=193)
    
    # --- Toggle Frame ---
    global toggle_frame
    toggle_frame = tk.Frame(root, bg='#FFFFFF', bd=1, relief='raised')
    
    tk.Button(toggle_frame, image= theop1, command=lambda: (click_sound.play(),select_theme('forest'))).pack(padx=10, pady=5)
    tk.Button(toggle_frame, image= theop2, command=lambda: (click_sound.play(),select_theme('beach'))).pack(padx=10, pady=5)
    tk.Button(toggle_frame, image= theop3, command=lambda: (click_sound.play(),select_theme('star'))).pack(padx=10, pady=5)
    
    thbut=PhotoImage(file=themes[theme]['walp'])
    thbutton= tk.Button(root, image= thbut, relief='flat', borderwidth=0, highlightthickness=0,bg=themes[theme]['bg'], activebackground=themes[theme]['bg'], command=lambda: (click_sound.play(),togthop()))
    thbutton.image = thbut 
    thbutton.place(x=252, y=291)

# === Clear Window ===
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()
    

# === Theme Selection ===
def select_theme(selected_theme):
    global theme
    theme = selected_theme
    togthop()
    show_main_menu()

# === Toggle Theme Options ===
def togthop():
    # Using list to make it mutable inside function
    global frame_visible,toggle_frame
    if frame_visible[0]:
        toggle_frame.place_forget()  # Hide the frame
    else:
        toggle_frame.place(x=50, y=100)  # Show it at specific location
    frame_visible[0] = not frame_visible[0]

# === Level Selection ===
def set_difficulty(level):
    global ai_difficulty
    ai_difficulty = level
    open_game_window()

# === Start Game ===
def start_game(mode):
    global game_mode
    game_mode = mode
    if mode == "pvc":
        show_difficulty_selection()
    else:
        open_game_window()

def show_difficulty_selection():
    clear_window()
    root.title("Select Difficulty")
    root.geometry("300x340")
    root.configure(bg=themes[theme]['bg'])

    bg_image = PhotoImage(file=themes[theme]['wb'])
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0 ,relwidth=1, relheight=1)
    bg_label.image = bg_image

    tk.Label(root, text="Choose Difficulty", font=('Courier New',16,"bold"), bg=themes[theme]['bg'], fg=themes[theme]['fg']).pack(pady=40)

    tk.Button(root, text="Easy", font=('Courier',12), bg=themes[theme]['btg'], fg=themes[theme]['ftg'],
              command=lambda: (click_sound.play(),set_difficulty("easy")),padx=40).pack(pady=5)
    tk.Button(root, text="Medium", font=('Courier',12), bg=themes[theme]['btg'], fg=themes[theme]['ftg'],
              command=lambda: (click_sound.play(),set_difficulty("medium")),padx=30).pack(pady=5)
    tk.Button(root, text="Hard", font=('Courier',12), bg=themes[theme]['btg'], fg=themes[theme]['ftg'],
              command=lambda: (click_sound.play(),set_difficulty("hard")),padx=40).pack(pady=5)

    tk.Button(root, text="Back", font=('Courier',10), bg=themes[theme]['cell_bg'], fg=themes[theme]['fg'],
              command=lambda: (click_sound.play(),show_main_menu()), padx=15).pack(pady=20)



# === Game Logic ===
def open_game_window():
    clear_window()
    root.title("Tic-Tac-Toe")
    root.geometry("300x340")
    root.configure(bg=themes[theme]["bg"])

    bg_image = PhotoImage(file=themes[theme]['wb'])
    # Create a label to hold the image
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0 ,relwidth=1, relheight=1)
    # Keep a reference
    bg_label.image = bg_image

    po=PhotoImage(file=themes[theme]["po"][0])
    px=PhotoImage(file=themes[theme]["px"][0])
    boardpic=PhotoImage(file=themes[theme]["bd"])

    board = [""] * 9
    current_symbol = ["X"]  # Track logical player for winner check
    buttons = []

    def make_move(index):
        if board[index] == "" and not check_winner():
            symbol = current_symbol[0]
            board[index] = symbol
            place_sound.play()
            buttons[index].config(image=px if symbol == "X" else po)
            buttons[index].image = px if symbol == "X" else po  # Keep reference

            if check_winner()=="X":
                winner = themes[theme]["px"][1] 
            elif check_winner() == "O":
                winner = themes[theme]["po"][1]
            else:
                winner = check_winner()

            if winner:
                if winner == "Draw":
                    draw_sound.play()
                else:
                    win_sound.play()
                show_custom_popup("Game Over", f"{winner} wins!" if winner != "Draw" else "It's a draw!")
                return
            current_symbol[0] = "O" if symbol == "X" else "X"

            if game_mode == "pvc" and current_symbol[0] == "O":
                root.after(500, computer_move)

    def show_custom_popup(title, message):
        popup = tk.Toplevel(root)
        popup.title(title)
        popup.geometry("250x150+{}+{}".format(root.winfo_x() + 30, root.winfo_y() + 60))
        popup.configure(bg=themes[theme]["bg"])
        popup.transient(root)
        popup.grab_set()
        icon2= PhotoImage(file=resource_path('icon2.png'))
        popup.iconphoto(False,icon2)

        # Optional: Disable resizing
        popup.resizable(False, False)

        if 'draw' not in message:
            icon_img = tk.PhotoImage(file=resource_path("win-icon.png"))
            tk.Label(popup, image=icon_img, bg=themes[theme]["bg"]).pack()
            popup.icon_image = icon_img
        else:
            icon_img = tk.PhotoImage(file=resource_path("draw-icon.png"))
            tk.Label(popup, image=icon_img, bg=themes[theme]["bg"]).pack()
            popup.icon_image = icon_img

        # Message label
        tk.Label(popup, text=message, font=("Courier", 14), bg=themes[theme]["bg"], fg=themes[theme]["fg"]).pack(pady=5)

        # OK button (only calls show_main_menu after the popup is manually closed)
        def on_ok():
            popup.destroy()
            show_main_menu()

        tk.Button(popup, text="OK", font=("Courier", 10), bg=themes[theme]["btg"], fg=themes[theme]["ftg"],
                command=lambda: (click_sound.play(),on_ok()), padx=30).pack(pady=5)


    def computer_move():
        empty_indices = [i for i, val in enumerate(board) if val == ""]

        if not empty_indices:
            return

        if ai_difficulty == "easy":
            # Random move
            choice = random.choice(empty_indices)

        elif ai_difficulty == "medium":
            # Try to win, else block, else random
            for symbol in ["O", "X"]:
                for i in empty_indices:
                    board[i] = symbol
                    if check_winner() == symbol:
                        board[i] = ""
                        choice = i
                        break
                    board[i] = ""
                else:
                    continue
                break
            else:
                choice = random.choice(empty_indices)

        elif ai_difficulty == "hard":
            # Use Minimax (perfect strategy)
            _, choice = minimax(board, True)

        make_move(choice)

    def minimax(board_state, is_ai):
        winner = check_winner()
        if winner == "O":
            return (1, None)
        elif winner == "X":
            return (-1, None)
        elif winner == "Draw":
            return (0, None)

        scores = []
        for i, cell in enumerate(board_state):
            if cell == "":
                board_state[i] = "O" if is_ai else "X"
                score, _ = minimax(board_state, not is_ai)
                scores.append((score, i))
                board_state[i] = ""

        if is_ai:
            return max(scores)
        else:
            return min(scores)



    def check_winner():
        win_patterns = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in win_patterns:
            if board[a] == board[b] == board[c] != "":
                return board[a]
        if all(cell != "" for cell in board):
            return "Draw"
        return None

    # === Game Board UI ===
    frame = tk.Frame(root, bg=themes[theme]["bg"])
    frame.pack(pady=10)
    for i in range(9):
        btn = tk.Button(frame, image=boardpic, width=80, height=80,  # Set fixed size
                compound='center',  
                command=lambda i=i: make_move(i))
        btn.image = boardpic
        btn.grid(row=i // 3, column=i % 3, padx=1, pady=1)
        buttons.append(btn)
    
    tk.Button(root, text="Back to Menu", command=lambda: (click_sound.play(),show_main_menu()),
              bg=themes[theme]["cell_bg"], fg=themes[theme]["fg"], font=('Courier',11)).pack(pady=10)


# === Start ===
show_main_menu()
root.mainloop()
