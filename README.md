This is a learning project. It's the first time I have  attempted to query 
an API, the first time I've written my own modules, and the first time
I really dove into git. The code and structure might not be the best, but 
the whole point was to learn, so I don't care. I also realized too late that 
I should have included a config.py file, and there was some sensitive info 
in the program. So, I deleted the couple months commit history and started new.

Anyways, what's this project about? 
This is a Flask app that is supposed to run on my raspberry pi. It makes three
separate requests (for past day/week/month) to the Google Analytics API and 
saves the responses to json files. Then those files are opened up and parsed to get what we really care about: the page views (or whatever metrics and 
dimensions you choose to request). This data now gets displayed on a simple
webpage running from the localhost.

And that's it. Its simple. 
