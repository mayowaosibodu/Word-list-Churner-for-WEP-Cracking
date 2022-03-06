# Wordlist-Churner-for-WEP-Cracking
I spent the year 2017 on a gap year from college in the US. I spent it on an island in Cape Verde called Sal.
I had practically no money for upkeep. As one would expect, I needed free internet access since I didn't have the stable funds for regular subscriptions.

I used to connect to the Wifi networks available at different locations on the island. A good number of them were restaurants.

For some of them, the restaurant managers changed their passwords periodically. There was a very clear pattern to these changes however.

One in particular was in the form "Name of restaurant" + "3 digit number".

For this specific case, cracking the password involved figuring out what new 3-digit number had been appended to the restaurant name.

With the attached Python script I could generate a list of words containing a given restaurant name, along with all possible 3-digit combinations.

The Aircrack-Ng password cracking tool can take in this wordlist and try out every given combination until it finds the password which enables a successful connection to the network (if it exists in the wordlist).

Very useful, relevant information on Aircrack-Ng: https://gist.github.com/victorreyesh/6532800
