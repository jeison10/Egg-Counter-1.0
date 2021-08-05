# Egg-Counter-1.0
Egg counter with Python open CV + modbusTCP + Flask streaming + Node Red

Beta version of an egg counter developed in python using open CV platform. it was made to be used for dayly egg counter on a conveyor for the poultry industry.

![Captura de tela 2021-08-04 200714](https://user-images.githubusercontent.com/43612824/128266766-5c39ea1e-b6ff-4030-a22e-68b5199b7209.png)

The GUI was developed with Pyqt5. Two windows are shown, the main one with the camera and another one with the sytem variables where you can adjust them. 

![Captura de tela 2021-08-04 200805](https://user-images.githubusercontent.com/43612824/128267133-b44da7f2-a1a7-43a4-a587-ff817b5d2733.png)

The software also runs on a local server an interface developed with the node-red platform. This interface shows the total of eggs counted and a real time image of the camera. 
All the information can also be read with an Modbus TCP client.

![Captura de tela 2021-08-04 201301](https://user-images.githubusercontent.com/43612824/128267188-2a54745c-3a3c-47ee-a9f1-b21f5ef04a24.png)

## Requirements and dependencies <h2>

Librarys
cv2
sys
Pyqt5
numpy
pyModbusTCP.server 
streamVideoFlask (Flask)
time
openpyxl



