# My python notes and collection
***
## Python classes
### Two version of python on Pi, how to make python 3 the default interpreter

Find out which python version is used per default. 
```
pi@raspberrypi:~ $ which python
/usr/bin/python

pi@raspberrypi:~ $ ls -al /usr/bin/python
lrwxrwxrwx 1 root staff 16 May 29 19:01 /usr/bin/python -> python2 
```

At the moment is python2 the default version on Linux, and we have to change the default to python 3. Since the file starts with an `l` in its attributes, and security permissions, it indicates that it is a `link where /usr/bin/python is linked to Python 2`. 

While I easily could change this link to Python 3, it is probably not the best choice! Upon updating Python, I would find that the link would have been updated back to the original link location pointing to Python 2. 

**A better solution**, is to possibly create your own link in a directory that's listed in the path prior to the usr/bin path, or /usr/bin path. In this case below, `the /usr/local/bin path is listed prior /usr/bin`. 
```
pi@raspberrypi:~ $ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games
```
I create a link to Python 3 in the directory /usr/local/bin, it will be found before the link in the directory /usr/bin pointing to Pyhton 2.  
```
sudo ln -s /usr/bin/python3 /usr/local/bin/python
```

To make sure I clear my hash, cache, of any paths like typing python, I type ``hash –r `.
If I enter now `python` on the command line, I will have the pyhton 3 interpreter available! 
```
pi@raspberrypi:~ $ python
Python 3.5.3 (default, Jan 19 2017, 14:11:04)
[GCC 6.3.0 20170124] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Basic class 1
The class did not provided the option to download the presented code samples. I took my own notes and a created the source code files for a subset of the covered code by myself, which is stored here: https://github.com/kapahnke-iot/python/tree/master/basic-class-1

**Covered topic**
* `Read input from keyboard` and `print a text message concatenated` with the input message. https://github.com/kapahnke-iot/python/blob/master/basic-class-1/input_print.py

### Basic class 2
The complete source code will be stored here: https://github.com/kapahnke-iot/python/tree/master/basic-class-2
