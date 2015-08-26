# Setting up your Amazon EC2 Machine

Use the following instructions to setup your Amazon EC2 Machine. We'll spin up a machine using an image specifically configured for this class, so once up and running, we'll have minimal setup. For the purposes of this class (at least it's start), we'll be using Amazon's free tier, which is awesome. Small, and somewhat slow machine, but totally usable given our goal. The process involves multiple steps, so bear with me.

**Create an Amazon AWS account**

1. First thing we'll do is make an Amazon AWS account (if you have one already, skip this part). Go to [aws.amazon.com] and create an account. Even though you're choosing the basic (free) plan, you'll have to enter a credit card number. Verify your information (easiest via phone). Once you have a verified account, log into the AWS console.

** Spin up a machine **

2. Click on the EC2

3. Create an instance (from image)

4. Top right-corner, change from Oregon to N. Virginia

5. Launch Instance

6. Create a key-pair in order to SSH into the machine

7. Name it and download, placing in a directory on your computer. I recommend making a ~.ssh/ directory and placing the .pem file there.

8. You should be able to see the instance in your AWS dashboard (green)

** SSH into the machine ** 

9. Right click on the instance in the dashboard, and follow instructions in order to ssh into the machine:

- open a terminal window in your computer, and type the following:
```sh
cd ~./ssh
ssh -i "_YOUR_PEM_FILE_NAME.pem" ubuntu@YOUR_IP_ADDRESS_HERE
```


** Setup your IPython Notebook environment**

Run the following command to start the ipython server on your AWS machine:
```sh
ipython notebook --no-browser --port=8887 2>/dev/null &
```

In this case we're running the iPython Notebook on our remote machine, hence no need for browser locally. We choose port 8887 (opened it on our machine so that we can access it remotely). Finally, we pipe all output from the server to /dev/null (we don't want to see all the output as we make changes and run different iPython Notebook pages.








[aws.amazon.com]:http://aws.amazon.com
