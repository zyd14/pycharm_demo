# PyCharm for (mostly) python engineering

Pycharm is an incredibly powerful IDE created by JetBrains.  It comes in a free, open-source community edition,
and a paid-for subscription edition.  To be honest, I tried the professional edition just to try out
some of the Flask support, but didn't find the cost was worth it so I stuck with the community edition.

##Getting Started

1. Get Pycham CE [here](https://www.jetbrains.com/pycharm/download/#section=mac)

##Basics

- VCS integration: while many of you are command-line git ninjas, I find myself pulling my hair out paging 
through merge conflicts or diffing various commits from a history.  The VCS integration in Pycharm makes it
easy to see what branches you're working on, whether any of those branches contain changes others don't,
and contains a beautiful diff viewer comparing files, whether it be do resolve a merge conflict, or while 
comparing a file to how it may have looked 6 months ago.

Files which have been modified since the last commit will be highlighted in blue, making it obvious what 
files you've touched.

##Key shortcuts: 
- **⌘-k** will bring up a commit dialog box, listing all the files that have been modified.  You can 
uncheck the checkbox next to each file that you don't want included in the commit

- **fn+⇧+k** will bring up the push menu, and will include all the commits which will be pushed as a result of
this action.

- **⌘-b** will take you to the closest (scope-wise) definition of a variable you have high-lighted, whether that's
in the current function or deep in some third-party library in your virtual environment.  I find this one
to be invaluable when trying to trace back clues as to why an object isn't behaving the way I think it should,
and overall better understand how those objects work.

- **⌥⇧E** will allow you to execute any highlighted code in an IPython console which will automatically appear.
The console will contain the state of any state from previous code executions in that console, but can be easily 
reset using the 'return' button along the Python Console toolbar


##Testing
Pycharm's testing abilities really help make this project shine.  From within the Prefences menu you have can select
Tools \> Python Integrated Tools.  From here you can choose your favorite test runner (mine happens to be pytest), which
will tell PyCharm what tool to use when detecting and running tests in your project.  

(test_ex.png)


##README writing