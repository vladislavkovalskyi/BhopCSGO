import time

import keyboard
import pymem

from offsets import dwLocalPlayer, dwForceJump, m_fFlags

process = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(process.process_handle, "client.dll").lpBaseOfDll


def main():
    while True:
        if keyboard.is_pressed("space"):
            player_object = process.read_int(client + dwLocalPlayer)
            jump = client + dwForceJump
            player_state = process.read_int(player_object + m_fFlags)

            if player_state == 257 or player_state == 263:
                process.write_int(jump, 5)
                time.sleep(.01)
                process.write_int(jump, 4)

main()
