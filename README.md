# Olympics-Medal-Table
Get started!

    Fork the django-tutorial repository on GitHub.

    Copy your fork locally:

    $ git clone git@github.com:<your_name_here>/django-tutorial.git

    Make sure your system is up to date:

    $ apt-get update
    $ apt-get upgrade
    $ apt-get install -y build-essential
    $ apt-get install -y python3-dev python3-software-properties  # or
    $ apt-get install -y python2-dev python2-software-properties

    Configure your local copy to work with virtualenv and pip. Assuming you have virtualenv installed, this is how you set up your copy for local development:

    $ cd django-tutorial/
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

    Switch to overview branch to start the tutorial from the first item of the tutorial checklist:

    $ git checkout overview

    Now you can make your changes locally to develop the overview item of checklist.

    When you're done making changes for the item, commit your changes and push the branch of the item to GitHub:

$ git add .
$ git commit -m "Your detailed description of your changes."
$ git push origin <branch-name>

    Now, create a new branch to develop the next item checklist of the tutorial:

    $ git checkout -b <branch-name>

    Back to step 6 until the tutorial checklist is fully completed.

    Switch to master branch and merge it with the last created branch:

    $ git checkout master
    $ git merge reusable-apps
    $ git push origin master

    Run the development server:

    $ python manage.py runserver

