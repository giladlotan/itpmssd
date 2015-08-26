# Setting up your Amazon EC2 Machine


Here we"ll go over all the steps involved with setting up your machine

### Create an Amazon AWS account




### Spin up a machine



### SSH into the machine



Run the following command to start the ipython server on your AWS machine:
`ipython notebook --no-browser --port=8887 2>/dev/null &`

In this case we're running the iPython Notebook on our remote machine, hence no need for browser locally. We choose port 8887 (opened it on our machine so that we can access it remotely). Finally, we pipe all output from the server to /dev/null (we don't want to see all the output as we make changes and run different iPython Notebook pages.




### iPython Notebook / Server





