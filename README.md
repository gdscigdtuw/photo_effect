# photo_effect
A web application that renders an effect on an image uploaded by user using python image processing libraries.

## Techstack:
1. Python 
2. Flask
3. HTML
4. CSS
5. Bootstrap

## Workflow:
1. User uploads image
2. Image processed using image processing libraries like OpenCV
3. User downloads image

## Steps to launch application
NOTE: It is vital that you install Python before moving on to subsequent steps.
1. Go to https://www.python.org/ and install the latest version compatible with your system
2. Fork and clone the repo
3. Create a virtual environment through the following command
    ```
    virtualenv venv
    ```
4. Activate the virtualenv
  * (Windows)
    ```
    venv\Scripts\activate
    ```
  * (Linux)
    ```
    source venv/bin/activate
    ```
    NOTE: After you are done working on the application you can deactivate environment by
    ```
    deactivate
    ```
5. Move to the cloned directory
  ```
  cd photo_effect
  ```
6. Open up the terminal and intall the necessary dependencies by the following command
    ```
    pip install -r requirements.txt
    ```
7. Now that we have the essential dependencies lets launch the application through the following commands.
  * (Windows)
    ```
    set FLASK_APP = start.py
    flask run
    ```
  * (Linux)
    ```
    export FLASK_APP = start.py
    flask run
    ```
8. It is possible that while running the application you run into " pakage not found" error. In this case all you need to do to install the necessary package is
    ```
    pip install package_name
    ```
9. Start contributing to the project, comment on an issue if you want to work on it, you can also suggest new issues that you would like to work on!

## References:
1. Flask documentation https://flask.palletsprojects.com/en/1.1.x/
2. OpenCV documentation https://opencv.org/
3. Flask & OpenCV session recordings:
    * Intro to Flask: https://drive.google.com/file/d/1o0Ju5zeuhFY9unZup6v1eb7aUZy3Y3Mb/view?usp=sharing
    * Intro to OpenCV: https://drive.google.com/file/d/1U8zHgcfnfL1CxMD74sjrM2ZUYU16g6D7/view?usp=sharing
    * Video streaming with Flask: https://drive.google.com/file/d/1cuglmCKhbQg97rGnyHpA1q7kNF2HJ_5t/view?usp=sharing
    * For session codes check out https://github.com/dscigdtuw/WebD/tree/master/Flask
