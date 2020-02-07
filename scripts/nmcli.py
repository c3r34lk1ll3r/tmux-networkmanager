#!/usr/bin/env python

import sys
import subprocess
from string import ascii_lowercase

def show_menu():
    short=ascii_lowercase
    datas=subprocess.check_output(["nmcli","-t","connection","show"])
    datas=datas.decode('ASCII')
    cmd = ["tmux","display-menu","-T","#[align=centre]Network Manager","-x","R","-y","P"]
    index = 0
    for i in datas.split('\n'):
        if i == "":
            continue
        connection_data = i.split(':')
        UUID = connection_data[1]
        name = connection_data[0]
        typ  = connection_data[2]
        is_o = True if connection_data[3] != "" else False
        line="#[align=left fg="
        line+="green" if is_o else "red"
        line+="]"
        if 'wireless' in typ:
            line+='泌'
        elif 'ethernet' in typ:
            line+=''
        elif 'vpn' in typ or 'tun' in typ:
            line+='嬨'
        elif 'bluetooth' in typ:
            line+=''
        else:
            line+=typ
        line+=' '+name 
        cmd.append(line)
        if index < len(short):
            cmd.append(short[index])
            index+=1
        else:
            cmd.append("")
        if is_o:
            command = "run -b \"nmcli connection down uuid "+UUID+"\""
        else:
            command = "command-prompt -p \"Secret\" \"run -b \\\"echo -n %% | nmcli connection up uuid "+UUID+" --ask\\\"\""
        cmd.append(command)
    cmd.append("")
    cmd.append("#[align=centre]Avaliable network")
    cmd.append("")
    cmd.append("")
    datas=subprocess.check_output(["nmcli","-t","device","wifi","list"])
    datas=datas.decode('UTF-8')
    for i in datas.split('\n'):
        if i == "":
            continue
        wifi_data = i.split(':')
        is_on = True if wifi_data[0] == "*" else False
        name  = wifi_data[7]
        speed = wifi_data[10]
        chan  = wifi_data[9]
        signal= wifi_data[11]
        bars  = wifi_data[12]
        command = "#[align=left fg="
        command+= "green" if is_on else "cyan"
        command+="] "+bars+' '+name+(chan)+'#[align=right]'+speed+' ('+signal+'%)'
        cmd.append(command)
        if index<len(short):
            cmd.append(short[index])
            index+=1
        else:
            cmd.append("")
        command = "" if is_on else "command-prompt -p \"Passphrase\" \"run -b \\\"nmcli dev wifi connect \'"+name+"\' password \'%%\' \\\"\""
        cmd.append(command)
    # Create tmux menu
    subprocess.check_output(cmd)
if __name__ == "__main__":
    show_menu();
