# AniTrac Server Sample

Simple overview of the backend code for the Anirac server.

## Description

Anitrac is an anilox inventory and usage tracking system. Recently, production has shifted towards being a server-side application instead of a localized single machine application. This repo serves as a slimmed down sample of how the backend works. 

## Getting Started

### Dependencies

* Python 3.12
* Python packages found in requirements.txt

### Installing

Start by downloading this repo as a zip file and unpack. From the terminal, create a virtual enviroment (details on how to create a virtual enviorment can be found [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)) and activate it.

### Executing program

After activating your virtual enviorment
1. Navigate to the folder with `requirements.txt`
2. Run the command `python -m pip install -r requirements.txt`
3. Navigate to the `src` folder.
4. Run `flask run` to start the server.


## Help

To experince the functionality of the server, start by opening the server via navigating to <a href="http://127.0.0.1:5000" target="_blank">http://127.0.0.1:5000</a>. You should get the message `Anitrac is running`. Navigate to <a href="http://127.0.0.1:5000/anilox_list" target="_blank">http://127.0.0.1:5000/anilox_list</a> to see the list of anilox rollers in the database. 

To add a new anilox, naivate to the data folder in your terminal. Run the command `python add_anilox.py`. This should print `500`, verifying a new (random) anilox was added. Refresh your anilox list to update the screen.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
