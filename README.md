Welcome to Command Station!
With this program, you can turn your cellphone into a reprogrammable macro keyboard.
In order to get started, download the server script from www.CraigMSirota.com/Command-Station. You can download the mobile app from the website or from the Google Play Store.
Decompress the file, and run AppServer.py.
On the mobile client, make sure to join the same Wi-Fi network that the computer is running on, and then enter the computer’s IP address into the textfield, labeled IP.

In order to change the functions of the keys, on the computer, navigate to the Prog_Files folder. You will see 16 files named prog0.py-prog15.py. The numbers, 0-15, correspond to the buttons in the following pattern:
[ 0][ 1][ 2][ 3]
[ 4][ 5][ 6][ 7]
[ 8][ 9][10][11]
[12][13][14][15]

If you want to change the function of a key, edit the set() function in the prog_.py file corresponding to the button you would like to edit.

To set/change the name of a button, click the "CHANGE TEXT" button, followed by the button you would like to edit. This will bring up a screen where you can type the new name.

