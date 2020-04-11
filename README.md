# PyCharm for (mostly) python engineering

Pycharm is an incredibly powerful IDE created by JetBrains.  It comes in a free, open-source community edition,
and a paid-for subscription edition.  To be honest, I tried the professional edition just to try out
some of the Flask support, but didn't find the cost was worth it so I stuck with the community edition.

## Built-ins
Pycharm hosts a dedicated terminal which automatically detects and invokes any virturl env

## Getting Started

Get Pycham CE [here](https://www.jetbrains.com/pycharm/download/#section=mac)

## Key shortcuts: 
- **⌘k** will bring up a commit dialog box, listing all the files that have been modified.  You can 
uncheck the checkbox next to each file that you don't want included in the commit.  A diff viewer will be present for
each file changed, allowing you to see how the file changed for this commit.

- **fn+⇧+k** will bring up the push menu, and will include a list of all the commits which will be pushed as a result of
this action, as well as the ability to view the diffs that will be applied to each changed file.

- **⌘b** will take you to the closest (scope-wise) definition of a variable you have high-lighted, whether that's
in the current function or deep in some third-party library in your virtual environment.  I find this one
to be invaluable when trying to trace back clues as to why an object isn't behaving the way I think it should,
and overall better understand how those objects work.

- **⌥⇧E** will allow you to execute any highlighted code in an IPython console which will automatically appear.
The console will contain the state of any state from previous code executions in that console, but can be easily 
reset using the 'return' button along the Python Console toolbar. This is super handy for testing small snippets of 
code while you're developing.

- **⇧⌘I**  will open up a small peek window with a view of the definition of an object or class you have highlighted. This
is in contrast to **⌘b**, which will take you directly to the module and location of the declaration of the highlighted object. 

![peek_image](https://github.com/zyd14/pycharm_demo/blob/master/peek.png)

All these hotkeys and tons more can be configured iin the **Preferences > Keymap** menu.

## Object inspection, completion
When working with objects that may have lots of methods on them, it can be easy to forget what methods are available.
By simply typing a variable which has been prior been assigned a type (through just assigning it a value, Py3 method signature type hints,
or in-line type hints) and typing the '.' operator, a list of all properties and methods of that variable will appear in a dropdown.
Furthermore, onces you've selected a method and are beginning to feed it parameters, you can type **⌘p** from within the method parentheses to list all the parameters the function takes.  If you'd like to know more about how the function itself
works, you can jump to its definition by highlighting it and typing **⌘b**


## Testing
Pycharm's testing abilities really help make this project shine.  From within the Prefences menu you have can select
Tools \> Python Integrated Tools.  From here you can choose your favorite test runner (mine happens to be pytest), which
will tell PyCharm what tool to use when detecting and running tests in your project.  

![Test Suite](https://github.com/zyd14/pycharm_demo/blob/master/test_ex.png)

By going to the **Test Configurations** menu under the **Run** menu dropdown you can make custom test
run configurations for particular modules or scripts, with different test runners or runtime parameters.

### Debugging
While debugging doesn't always have to occur during a unittest, they often go hand in hand.  Say you've got a test that
is failing and you just don't know why.  Don't you which you could freeze the test right in the middle, inspect the variables
and see which one contains the erroneous value that is making the test puke?

To drop a breakpoint into a test, simply click on the gutter to the left of the line you want to stop at.  This will place
a red dot where the code will stop when we attach a debugger.  Now when you go to click the 'play' button on the test,
right-click and select 'Debug test_stuff.py'.  This will attach a debugger to the test runner, which will stop the code
every time it sees one of the red dots in the gutter.  When the test stops you'll have a few windows pop up in the bottom
of the IDE, one containing the current stack frames, and on containing any locally-defined variables and their value.  
You can also add variables to a watch list from this window, so that if the test traverses many functions you can
keep track of the value of an interesting variable.  Collections and objects in the **Variables** window will
give you the ability to drill-down through their attributes as well if you would like to further interrogate them.

![File ran with debugger](https://github.com/zyd14/pycharm_demo/blob/master/debugger.png)

## Refactoring
Remember when you though 'xfddssd' would be a funny name for a variable? And then that racoon persisted throughout the project,
leaving its trail everywhere and leaving you and your teammates to try to figure out what a racoon object is in the context
of bioinformatics?  Pycharm makes refactoring of variable / object names extremely easy.  Simply highlight the variable 
or object you want to rename, click >**Refactor**, then click \> **Rename**.  Pycharm will then search for any reference
to that variable and present you with a list of all the places throughout the entire project that the highlighted variable occurs.  If you'd like to rename 
all of them it's as easy as clicking 'Do Refactor'.  I've found this incredibly useful for changing object names to be more
clear about their purpose, without having to hunt through scores of modules to determine where they occur. 

## Find Usages
Sometimes you find a seemingly important variable or method that might need to be changed, but have no idea where it's being used or how it's being used.  By highlighting the object, right-clicking and clicking **Find Usages...** a small pop-up window will show where that varible is referenced throughout the entire project. This is particularly helpful for when you're cleaning up cruft and want to know if you can delete something.  'No Usages Found'? Deleted.

Right-clicking an object opens a menu which contains the 'Find Usages...' button:  
![find usages example](https://github.com/zyd14/pycharm_demo/blob/master/find_usages.png)

After clicking the 'Find Usages' button, a pane will open listing all the usages of that object found throughout the
project, presented in a tree-like fashion.  Double-clicking on any of these usages will take you directly to that location
in the code. 
![found_usages_example](https://github.com/zyd14/pycharm_demo/blob/master/found_usages.png)

## Customized lint-hinting
PyCharm comes with a huge number of different of type and style hints to conform to PEP-8 and avoid some logic errors, particularly if you use the Python 3 type declarations in your code. Missing parentheses, brackets, bad indentation, unused
variable detection, unreachable code, possibly uninitialized variables being used all can be reported with varying levels of severity. Which hints to receive, as well as their presentation attributes, can be set in the **Preferences** menu under the **Editor** tab.

## VCS integrations
While many of you are command-line git ninjas, I find myself pulling my hair out paging 
through merge conflicts or diffing various commits from a history.  The VCS integration in Pycharm makes it
easy to see what branches you're working on, whether any of those branches contain changes others don't,
and contains a beautiful diff viewer comparing files, whether it be do resolve a merge conflict, or while 
comparing a file to how it may have looked 6 months ago.

Files which have been modified since the last commit will be highlighted in blue, making it obvious what 
files you've touched.

Diff window comparing two conflicting files and showing the file resulting from how you merge the conflict.  
![Merge Conflict differ](https://github.com/zyd14/pycharm_demo/blob/master/merge_veiwer.png)

You also have the ability to look through the git revision history of any module or folder by selecting the folder / module,
right-clicking and selecing 'Git > Show history...'

![Show History](https://github.com/zyd14/pycharm_demo/blob/master/show_history.png)

This allows you to see the various concurrent branches of development for the file, as well as a diff viewer showing the 
commit diff at each commit.  This can be super handy when trying to find where a problem was introduced, or if you need to 
roll back to a specific commit before your last merge.

## Jupyter Notebook

Pycharm is capable of running Jupyter Notebooks.  This is far from my area of expertise, but the community edition 
of Pycharm does appear to support it.  A very basic jupyter notebook file is included in this project repo to show that it
can be done.  The kernel running the Jupyter Notebook can be configured similarly to how a test runner is configured.
Go to the **Run** window dropdown, click > **Edit Configurations..** and select an item from the drop down below **Jupter Notebooks**
on the left side of the window that appears.

## README writing
When writing any markdown file (ending with .md), PyCharm automatically picks it up as a markdown file and gives you the
option to view the rendered markdown side-by-side with your markdown file as you create it.

## Extensions
There are lots of various plugins for PyCharm that can be accessed through the **Preferences** tab, for various things like
vim keyboard mappings, SQL highlighting and completion, bash completion, ticketing-service integrations, etc.

I've played with the youtrack extension before, and it was pretty neat once I got it up and running.  It allowed me to create
branches directly from an issue pulled from youtrack, and then commits I made to that branch would show
up in the youtrack ticket.  I could also close the ticket after merging the feature back in.  They have a number of other 
issue tracker integrations, including JIRA, Trello, and GitLab.

There are also various tools to enable easier development in cloud applications.  

## Other languages
Pycharm attempts to provide basic code highlighting and completion (like closing tags in HTML) in various languages,
including HTML, SQL, and Docker.  The professional version provides better syntax highlighting for things like Django and 
Jinja2 templates (and I think some light-weight javascript highlighting?), but
I didn't really find them worth it when I did my 30-day free trial of the professional version.  There are many
active community projects for supporting tons of various languages.
