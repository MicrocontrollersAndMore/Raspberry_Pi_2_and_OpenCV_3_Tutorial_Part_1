Welcome to the Raspberry Pi 2 & OpenCV 3 Tutorial - Part 1 !!

If you are unsure where to start I would recommend viewing the video from the beginning and working through "Raspberry Pi 2 + OpenCV 3 Cheat Sheet.txt" to follow along.  The video covers pretty much everything in detail:

(video link here when done)

Note 1: This cheat sheet is intended to be used in conjunction with the above linked YouTube video, NOT necessarily as a standalone document.  If you are unable to follow this cheat sheet at some point please consult the video, all steps are explained and demonstrated.

Note 2: This cheat sheet and accompanying video is intended for an audience that has some  programming, OpenCV, and at least rudimentary electronics hardware knowledge.  If more background in any of these areas would be helpful please see my YouTube Channel as there are other videos that cover all of these topics, or consult another YouTube / website / book as applicable.  No prior Linux knowledge is assumed.

Note 3: In this cheat sheet, unlike previous cheat sheets, I'm using a plain text format.  This is necessary to facilitate copying / pasting into a Linux terminal when using PuTTY (if this does not make sense now, please continue with the tutorial, it will be clear later).

Note 4: This video / cheat sheet is written for the Raspberry Pi 2 model B+, which is currently the only Raspberry Pi 2 model available.  If Raspberry Pi 2 versions other than the B+ are subsequently introduced it may be necessary to make the applicable changes.  Also, the instructions provided would most likely work with a Raspberry Pi 1 model B+, but this has not been tested and the computer vision applications would run unacceptably slowly.  A Raspberry Pi 2 model B+ is the only hardware model recommended, tested with, and supported by these instructions.

Note 5: In these instructions I'm supposing you are using a Windows computer for your desktop.  I've specifically tested these instructions with Windows 10, AFAIK they should work with Windows 7, 8, and 8.1 but I cannot vouch for this first hand as I have only tested on Windows 10.  Mac or Linux desktop users will need to make the applicable adjustments.

Note 6: Microsoft has recently released a free version of Windows 10 for the Raspberry Pi.  After spending a weekend with the Windows 10 Raspberry Pi version, at this time I'm deciding to stick with Raspbian Linux on the RPi for the following reasons:
-Neither USB webcams nor the official Raspberry Pi camera module are yet supported by the Windows 10 Raspberry Pi version and Microsoft has not announced if/when either or both may be supported, this point alone is a show-stopper for anybody interested in computer vision on the RPi
-Raspbian is very developed and far more user friendly now then it was at release 3.5 years ago
-3.5 years of community support (tutorial videos, websites, books, Stack Overflow posts, etc) has accumulated for Raspbian on the RPi, this is only just beginning for Windows 10 on the Raspberry Pi
-The only currently supported wireless adapter for the Windows 10 Raspberry Pi version is the official Raspberry Pi Foundation wireless adapter, which is not widely available
-The Windows 10 Raspberry Pi development environment within Visual Studio is based on the Windows Phone extensions for Visual Studio and therefore not very intuitive for anybody without substantial Windows Phone development experience, which would be a very small number of developers being that Android and Apple are the dominant phone operating systems currently
-A Raspberry Pi with Windows 10 can only be programmed from a desktop with Windows 10 (i.e. desktop computers with Windows 7, 8, or 8.1 cannot be used to program the RPi)

Note 7: In this tutorial we will use Python 2 for all programs as Python 2 support has been thoroughly integrated with OpenCV, whereas support for Python 3 has only been introduced recently and is not yet reliable.  Also, Python 2 is the default Python for Raspbian.
