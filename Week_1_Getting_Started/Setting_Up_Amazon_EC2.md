# Setting up your Amazon EC2 Machine

Use the following instructions to setup your Amazon EC2 Machine. We'll spin up a machine using an image specifically configured for this class, so once up and running, we'll have minimal setup. For the purposes of this class (at least it's start), we'll be using Amazon's free tier, which is awesome. Small, and somewhat slow machine, but totally usable given our goal. The process involves multiple steps, so bear with me.

*Create an Amazon AWS account*

1. First thing we'll do is make an Amazon AWS account (if you have one already, skip this part). Go to [aws.amazon.com] and create an account. Even though you're choosing the basic (free) plan, you'll have to enter a credit card number. Verify your information (easiest via phone). Once you have a verified account, log into the AWS console.

2. 




#### Spin up a machine



#### SSH into the machine




Run the following command to start the ipython server on your AWS machine:
```sh
ipython notebook --no-browser --port=8887 2>/dev/null &
```

In this case we're running the iPython Notebook on our remote machine, hence no need for browser locally. We choose port 8887 (opened it on our machine so that we can access it remotely). Finally, we pipe all output from the server to /dev/null (we don't want to see all the output as we make changes and run different iPython Notebook pages.




### iPython Notebook / Server





[aws.amazon.com]:http://aws.amazon.com
