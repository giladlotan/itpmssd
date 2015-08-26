# Setting up your Amazon EC2 Machine

Use the following instructions to setup your Amazon EC2 Machine. We'll spin up a machine using an image specifically configured for this class, so once up and running, we'll have minimal setup. For the purposes of this class (at least it's start), we'll be using Amazon's free tier, which is awesome. Small, and somewhat slow machine, but totally usable given our goal. The process involves multiple steps, so bear with me.

**Create an Amazon AWS account**

1. First thing we'll do is make an Amazon AWS account (if you have one already, skip this part). Go to [aws.amazon.com] and create an account. Even though you're choosing the basic (free) plan, you'll have to enter a credit card number. Verify your information (easiest via phone). Once you have a verified account, log into the AWS console.

**Spin up a machine**

2. Click on the EC2 Dashboard 
3. Top right-corner, change your region to **N. Virginia**
4. Launch Instance (top blue button) -> Click on *Community AMIs* in the left sidebar
5. Search for the following AMI id:
```sh
ami-d776cfbc
```
6. Select -> Review and Launch -> Edit Security Groups
7. Add Rule -> Insert 8887 in the port field, and use the drop-down menu bar to choose the 'anywhere' option
- What we're doing here is making sure that port 8887 is open on this machine. We'll use this port to access our iPython notebooks remotely.

8. Launch -> Create a new Key-Pair
- We need a Key-Pair in order to SSH into the machine. This will come in the form of a .pem file that we will download from Amazon. It is very important to keep this file in a safe folder. We'll need to reference it every time we access our machine.
9. Enter key pair name -> and download the .pem file
10. I recommend making a ~./ssh directory and placing the .pem file there.
```sh
cd ~
mkdir .ssh
cd .ssh
cp ~/Downloads/gilgul_itp.pem .
```

11. After a few minutes, you should be able to see the instance in your AWS dashboard (green)

**SSH into the machine** 

12. Right click on the instance in the dashboard. Take a look at the instructions for ssh-ing into this machine:
13. Open a terminal window in your computer, and enter the following:
```sh
ssh -i ~/.ssh/YOUR_PEM_FILE_NAME.pem ubuntu@EC2_INSTANCE_PUBLIC_IP
```
- you can get your public IP address information from the EC2 dashboard

**Setup your IPython Notebook environment**

Run the following command to start the ipython server on your AWS machine. Navigate to the right directory first to start it in the ideal folder:
```sh
cd /class/itpmssd
ipython notebook --no-browser --port=8887 2>/dev/null &
```

In this case we're running the iPython Notebook on our remote machine, hence no need for browser locally. We choose port 8887 (opened it on our machine so that we can access it remotely). Finally, we pipe all output from the server to /dev/null (we don't want to see all the output as we make changes and run different iPython Notebook pages.

In order to open up the interactive notebooks in your browser, you'll need to setup an SSH tunnel from your remote server (on the Amazon machine) to your computer.

```sh
ssh -i ~/.ssh/YOUR_PEM_FILE_NAME.pem -N -f -L localhost:8887:localhost:8887 ubuntu@EC2_INSTANCE_PUBLIC_IP
```

Now you should be able to see the Jupyter Notebook web interface when you hit the following link on your browser:

[http://localhost:8887]






[aws.amazon.com]:http://aws.amazon.com
[http://localhost:8887]:http://localhost:8887/tree
