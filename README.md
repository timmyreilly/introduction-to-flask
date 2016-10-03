#Intro to Flask 

Supporting slides can be found [here](https://doc.co/E7UnqU)

### Before we get started buildling with flask we need to setup our development environment. 

1. Install Python
2. Install virtualenv
3. Install virtualenvwrapper or virtualenvwrapper-win
4. Create a virtual environment 
5. Install flask 
6. Run our flask project
7. Checkout the next bit of code  

## 1. Install Python

[Windows](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/)

[Mac](http://docs.python-guide.org/en/latest/starting/install/osx/)

## 2. Install virtualenv

```
$ pip install virtualenv
```

## 3. Install virtualenvwrapper or virtualenvwrapper-win

virtualenv wrappers make it easy to manage multiple environments and can make iterating on project easy. 


[Windows](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/)

``` 
C:\ pip install virtualenvwrapper-win  
```


[Mac](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

```
$ pip install virtualenvwrapper 
$ export WORKON_HOME=~/Envs 
$ source /usr/local/bin/virtualenvwrapper.sh 
```

## 4. Create a virtual environment

```
$ mkvirtualenv venv
```
deavtivate environment
```
$ deavtivate 
```
workon that environment
```
$workon venv
```

EXTRA: link directory to virtualenv 
```
$ setprojectdir .

$ deactivate

$ workon helloworld
```

Before moving forward -  Make sure you're virtualenv is activated. Should look like this: 

```
(venv) path\to\something\like\your\project$ 
```


## 5. Install flask

Now we need [flask](http://flask.pocoo.org/) for our first website!

```
$ pip install flask
```

## 6. Clone the repo 
```
$ git clone https://github.com/timmyreilly/introduction-to-flask.git 
```

## 7. Checkout our first section
```
$ git checkout a 
```

## 8. Run our flask project
```
$ python hello.py
 * Running on http://localhost:5000/
```