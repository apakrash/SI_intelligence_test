# SI_intelligence_test
#### beta-alpha build

# Using the Python Script

### Libraries needed to run this:

pip install ping3

This code will utilize the files urls.txt and ipAddress.txt to to ping 5 random ip address and send GET request to 5 random URLs.
The objective is to generate events when trying to test Firepower's SI.

  Run using: python SI-diagnostic-1.py
  (since this code uses socket, an elevated priv on linux machines might be needed in which case run using sudo python SI-diagnostic-1.py or sudo python3 SI-diagnostic-1.py)
  The logs will be saved in SI-diagnostic-1.log

# Using the Windows executible file

1. Open cmd.exe on the machine, with ADMIN privilege (else the script will throw errors)
2. navigate to the SI-diagnostic-1 folder inside this repository
3. run the file from the admin cmd prmompt: SI-diagnostic-1.exe
4. The logs will be saved in SI-diagnostic-1.log
