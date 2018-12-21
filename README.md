# Project 1 : Logs Analysis

## Project Details:

You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

Here are the questions the reporting tool should answer.

#### 1. What are the most popular three articles of all time?

#### 2. Who are the most popular article authors of all time?

#### 3. On which days did more than 1% of requests lead to errors?

## Getting Started:

To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

### The virtual machine

1. Install VirtualBox from https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

2. Install Vagrant from https://www.vagrantup.com/downloads.html

3. Download and unzip the VM configuration from https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip

4.  Change to this directory in your terminal with `cd`. Inside, you will find another directory called vagrant. Change directory to the vagrant directory.

### Start the virtual machine

5. From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

6. When vagrant up is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM.

### Running the code

 7. Clone this repository and `cd` to its directory.
 
 8. Run the command `python log_main.py`
 
