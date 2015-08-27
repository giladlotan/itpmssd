# Notes on Technical Setup for Class

- If you haven't yet created your Amazon instance, [DO THAT FIRST] (https://github.com/giladlotan/itpmssd/blob/master/Week_1/Setting_Up_Amazon_EC2.md).

- Our remote machine:
    - Amazon's Web Services (AWS) includes a wide array of useful cloud computing services - including computation and storage.
    - For the purposes of this class, we'll be using an Instance running on Amazon's Elastic Compute Cloud (EC2) - one of the many services it offers.
    - We loaded up our machine from an image, created specifically for the purposes of this class (so you all have exactly the same machine, computation, file directories and libraries at the start)
    - It is a "micro" machine, effectively the smallest option possible in terms of computation (CPU) and memory. It is also **FREE** (tx Amazon!).
    - There's an attached Volume (think disk drive) with 20G space under a directory called '/class'. This is where we'll place our files, some data, etc.
        - At any point, you can run the following command to see how much space you have left on your machine:
        ```sh
        df -h
        ```
    - SSH (Secure Shell) is a protocol used to access remote machines from the command line. We'll have to continuously SSH into our machine over time, as we get further into the class.
    - **IMPORTANT**: Every time you reboot the machine, its PUBLIC IP address changes. You'll need to use the new IP address when SSH'ing after a reboot.

- Git: 
    - Our materials live in [this Github repository] (https://github.com/giladlotan/itpmssd/).
    - We'll be continuously updating the materials, so make sure to grab the most recent version, by running the following commands:
    ```sh
    cd /class/itpmssd
    sudo git pull
    ```
    
- IPython Notebook: 
    - This is a great tool that supports interactive computation environments, great for exploratory computation and data analysis. Also a really great way to get familiar with Python.
    - We have an IPython Notebook server running on our Amazon instance.
    - We'll be communicating with it by running an SSH tunnel on our local machine. This gives us the ability to see the notebooks in our browser, by navigating to: [localhost:8887] (http://localhost:8887)
    
- Slack:
    - We have a Slack group for our class: [itpmssd.slack.com] (https://itpmssd.slack.com)
    - If you haven't already ** SIGN UP ** to the slack group (throught the above link)
    - We'll use slack for class-related communications: questions, thoughts, answers. We'll also use it to share content we find - links, interesting articles, etc. 
    - Most importantly, we'll use Slack this semester to build a bunch of Bots! (more on that l8trz)

- Redis:
    - On your Amazon instance, there should be a running Redis Server.
    - This will come in handy later, when we need to save certain data.
