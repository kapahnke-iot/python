# My python notes and collection
***
## Python courses

### Two version of python on Pi, how to make python 3 the default interpreter

Find out which python version is specified as default. 
```
pi@raspberrypi:~ $ which python
/usr/bin/python

pi@raspberrypi:~ $ ls -al /usr/bin/python
lrwxrwxrwx 1 root staff 16 May 29 19:01 /usr/bin/python -> python2 
```

At the moment is *python2* the default version on Linux, and we have to change the default to *python3*. 

***
**A quick solution is to change the link to python3, but error prone**

Since the file starts with an `l` in its attributes, it indicates that it is a `link` where /usr/bin/python is linked to *python2*. 

While I easily could change this link to **python3**, it is probably not the best choice! Upon `updating python`, I would find that the link would have been updated back to the original link location which is pointing back to *python2*. 

***
**Another quick solution is to use a shell alias, but still error prone** 

Set up a shell alias, type that at a prompt:

```alias python=/usr/local/bin/python3```

Better to make the change to be persistent put it in `~/.bashrc`, now when I type *python* it runs the chosen *python3*, but when some program on the system tries to run a script with `/usr/bin/python` it runs the linux default *python2*!

***
**A stable solution an my recommendation !!!**

Create your own link in a directory that's listed in the path prior to the usr/bin path, or /usr/bin path. In this case below, the */usr/local/bin path is listed prior /usr/bin*. 

```
pi@raspberrypi:~ $ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games
```
I create a link to *python3* in the directory /usr/local/bin, it will be found before the link in the directory /usr/bin pointing to *pyhton2*.  
```
sudo ln -s /usr/bin/python3 /usr/local/bin/python
```

To make sure I clear my hash, cache, of any paths like typing python, I type `hash –r`.
If I enter now `python` on the command line, I will have the *pyhton3 interpreter* available! 
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
