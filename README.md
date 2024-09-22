# Covert Channel Example
This is a simple covert channel that works by creating files in a "tmp" like directory, and encodes the message in the filename, utilizng a substiution cipher to obsfuscate the actual message.
I created this on a Windows 11 machine and not a Linux machine, so that is why it lacks certain modulations. 
The receiver reads the message and then deletes the files.

