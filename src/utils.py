import os
import random
from imageio import imread
import requests
import io
import json
import config
def open_waste_slot():

    """
        open the machine so that
        an user can enter the machine

    :return:
    """

    send_command_to_machine("open_waste_slot")
    return True


def close_waste_slot():
    """
    close the waste box for user safety
    :return:
    """

    send_command_to_machine("close_waste_slot")
    return True


def process_waste(waste_type):

    """
    move the good slot and shredd the waste
    :return:
    """

    move_container(waste_type)
    was_sucessful = shred_waste()

    return was_sucessful


def move_container(waste_type):

    BOTTLE_BOX = 0
    GLASS_BOX = 1
    command_name = "move_container"

    if waste_type == "bottle":
        send_command_to_machine(command_name, BOTTLE_BOX)
    elif waste_type == "glass":
        send_command_to_machine(command_name, GLASS_BOX)

    return True


def send_command_to_machine(command_name, value=None):

    """
    simulate command sending to rasberry pi
    do nothing to work even if the machine is not connected

    :param command_name:
    :param value:
    :return:
    """
    return True



def shred_waste():

    send_command_to_machine("shred_waste")

    return True


def take_trash_picture():

    """
        function simulating the picture taking
        inside the machine. 

        Call this function to ask the machine to 
        take picutre of the trash

        return : np array of the picture
    """

    send_command_to_machine("take_picture")

    url = MY_URL
    choice = random.choice(os.listdir("./camera")) #change dir name to whatever
    print(choice)
    # Loads the image into memory
    with io.open('./camera/'+choice, 'rb') as image_file:
        content = image_file.read()
    payload = content

    headers = {
      'Prediction-Key': MY_KEY,
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    print(json.loads(response.text)['predictions'][0]['tagName'])
    image = json.loads(response.text)['predictions'][0]['tagName']
    return image
