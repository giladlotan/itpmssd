# Setting up your Amazon EC2 Machine

Use the following instructions to setup your Amazon EC2 Machine. We'll spin up a machine using an image specifically configured for this class, so once up and running, we'll have minimal setup. For the purposes of this class (at least it's start), we'll be using Amazon's free tier, which is awesome. Small, and somewhat slow machine, but totally usable given our goal. The process involves multiple steps, so bear with me.

**Create an Amazon AWS account**

First thing we'll do is make an Amazon AWS account (if you have one already, skip this part). Go to [aws.amazon.com] and create an account. Even though you're choosing the basic (free) plan, you'll have to enter a credit card number. Verify your information (easiest via phone). Once you have a verified account, log into the AWS console.

**Spin up a machine**

- Click on EC2 Virtual Servers in the Cloud (upper left)
- Top right-corner drop down, change your region from **Oregon** to **US East (N. Virginia)**
- Launch Instance (big blue button) -> Click on *Community AMIs* in the left sidebar
- Search for the following AMI id:
```sh
ami-2382e346
```
- Select -> Review and Launch -> Edit Security Groups
- Add Rule -> In the new section that comes up, insert 8887 under "Port Range" , and use the drop-down menu bar under "Source" to choose the 'anywhere' option. Leave "Type" as Custom TCP Rule.
(What we're doing here is making sure that port 8887 is open on this machine. We'll use this port to access our iPython notebooks remotely.)

- Click Review and Launch
- Click Launch -> Create a new Key-Pair
  - We need a Key-Pair in order to SSH into the machine. This will come in the form of a .pem file that we will download from Amazon. It is very important to keep this file in a safe folder. We'll need to reference it every time we access our machine.
- Enter key pair name (mine is "gilad_itp") -> and download Key Pair
- Open up your Terminal window and create an ~./ssh directory. Move the .pem file there.
```sh
mkdir ~/.ssh
mv ~/Downloads/gilgul_itp.pem ~/.ssh
```
- Go back to your browser, and click 'Launch Instance'
- Click on the cube in the upper left corner -> then click on EC2 just below it
- Click on 'Running Instances' and you should be able to see the status of your newly created machine. (Hopefully it is GREEN! -> if not... you're fucked...)

**SSH into the machine** 

- Right click on the instance in the dashboard -> click 'Connect'
- Take a look at the instructions for ssh-ing into this machine
  - First you have to run the following on your pem file: (granting permission)
```sh
chmod 400 ~/.ssh/gilad_itp.pem
```
  - Grab the 'Public IP' address that Amazon provides you with, and insert it into the command below (instead of 'PUBLIC_IP_ADDRESS' insert yours -> something like '52.22.14.26'):

```sh
ssh -i ~/.ssh/gilad_itp.pem ubuntu@PUBLIC_IP_ADDRESS
```
- run the following commands in the terminal while SSH'd into your new machine:
```sh
cd /class
sudo bash
git init
git clone https://github.com/giladlotan/itpmssd
```
- this should pull in a folder named 'itpmssd' (you can verify by running the command: 'ls -l')

**Setup an SSH tunnel in order to view IPython notebooks locally**

The iPython notebook helps us interactively develp python code. The iPython server is already running in our remote machine on port 8887. Now we need to create an SSH tunnel that lets us access the server from our local machine. The goal: run ipython notebook on our browsers. Run the following command (with your .pem file name and remote machine IP address) in a terminal window:

```sh
ssh -i ~/.ssh/gilad_itp.pem -N -f -L localhost:8887:localhost:8887 ubuntu@PUBLIC_IP_ADDRESS
```

Now you should be able to see the Jupyter Notebook web interface when you hit the following link on your browser:
[http://localhost:8887]

Finally, make sure to go over [these notes] (https://github.com/giladlotan/itpmssd/blob/master/Week_1/Technical_Setup.md) detailing our class's technical setup.

---

If this doesn't work, your iPython Notebook server may not be running correctly on your EC2 machine. In the terminal window, while SSH'd into your remote machine, try the following:
```sh
ps -aux | grep ipython
```
If one of the resulting prompts looks something like this:
```
sudo /usr/local/bin/ipython notebook --notebook-dir=/class --no-browser --port=8887
```
The server should be running. If you don't see this line, try restarting the Amazon machine, grabbing its new IP address, and trying again. Otherwise, send a message [on our Slack] (https://itpmssd.slack.com). Gilad (or anyone else from class) can help debug.

[aws.amazon.com]:http://aws.amazon.com
[http://localhost:8887]:http://localhost:8887/tree
