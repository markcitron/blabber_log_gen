# blabber_log_gen
This is for those situations where you need one or more fake logs running for one reason or another.

- [blabber_log_gen.py](blabber_log_gen.py) is the main log generator.  It currently just recites the [Jabberwocky](https://www.poetryfoundation.org/poems/42916/jabberwocky) by Lewis Carroll.  Once it has gone throught the whole poem, it will log and out of range error and then restart.
- [start_blabber.py](start_blabber.py) is a wrapper script that can start one or more of the fake log generators, each is numberred for differentiation.  
## Notes 
- Currently all of the logs are generated with the same log level,  I might change this if needed and time warrants the work.
## TODO
- If something doesn't make sense or you have suggestions, please either send me an email or just propose a code change.  This is just a utility that I made to make things easier and if you can make it better, please do :-)
