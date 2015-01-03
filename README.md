# Overview


Raspberry Pi files are kept here for references.


# GPIO Pinout Diagram


![GPIO](http://www.element14.com/community/servlet/JiveServlet/previewBody/68203-102-6-294412/GPIO.png)


# Installation

First the image need to be installed to your SD Card. It can be 
downloaded from the raspberry's own web site.
After it is downloaded, insert the SD card (for Mac):


```bash
$ df -h
```


Check where is your SD Card mounted, mine went on disk1s1 for example


```bash
$ sudo diskutil unmount /dev/disk1s1
```


The SD Card should be unmounted. To confirm again df


```bash
$ df -h
```


If you do not see it, you are good. Next, write your image to the file.

> If your disk is found at */dev/disk1s1* then, 
> of should be */dev/rdisk1*. 
> So, dev/disk1... becomes /dev/rdisk1 


```bash
$ sudo dd bs=1m if=2014-09-09-wheezy-raspbian.img of=/dev/rdisk1
```


Now, wait till it is done. If you are bit obssessed like me, 
you can press CTRL+T just to see how many bytes are written.


Finished? great! Now, put the card in rasp, connect monitor, keyboard
mouse and power it on. Credential to login is pi/raspberry. After login
write `startx` to start the xwindows. 


Have fun!
