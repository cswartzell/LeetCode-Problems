# Neat. Now... how to do it? My instinct is that I need a literal Dictionary
# of words, mapped to... maybe #### Alphanumeric Chars? That'd still be a lot
# Wait, how DO these work? The URLs they give are impossibly small to actually
# encode all the data that generates them. They've just got to be storing a
# hashed version on a server right?

# Well this is bullshit for a "medium". I just read three articles on this
# high level problem: of course you want to hash it, but... hash what?
# In all three cases they start by building a database and use an AutoIncremented
# (ie, "take a number") int each time a url is added to the DB, and hash this
# int ID. They do not at all hash the URL directly. They dont even use it as
# part of the Hash as its length would necessarily correspond direcctly to the
# hash length. I guess I will just use a dict and auto incrementer here and
# replicate this behaviour, but the question is terrible: It sort of implies
# one is just creating the hashing portion, but at least given the solution, the
# DB and autoincrementer ID are interagal parts of this. You arent just making
# the Hashing part, you are making the whole damned thing.

# Wait... using a new, effectively randomly generated ID and encoding that each
# time means nothing checks if the URL is ALREADY in the DB, it just gets added
# again. Is this how these work? Duplicated entries could become a massive drain
# right? I guess its not that common a use case but it is interesting that the
# articles I read didnt even bother to mention this fact. YOLO I guess, one article
# said there were only 677x10^6 URLs at the time, so if our database holds 5000
# times this amount then its pretty safe to just accept dupes. [a-z+A-Z+0-9] = 62
# 62^7 = 3,521,614,606,208/677x10^6 = 5201. Every URL could be copied over 5000 times


class Codec:
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.decode(codec.encode(url))
    tiny_url_db = {}
    INT_ID = 56800235584  # Sure, lets skip 56.8 billion possible entries, its only 1.5% of our space
    # Since we have SOOOOO much room, why not start the ID at such a place
    # that hashing it automatically produces 7 chars, rather than figuring
    # out how to pad values. We have so few test cases, the hashing is going
    # to end up just being a sequence of ints from 100000000 to 100001000
    # Well what a stupid excercise.

    # NOTE, as this is an int, we need to skip leading zeros anyhow

    map = list(string.digits) + list(string.ascii_letters)
    # map = [chr(i) for i in range(48,58)] + [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
    # Create a map for 0-9 A-Z a-z

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        new_id = self.INT_ID
        self.INT_ID += 1
        # assign a new ID to our incoming URL, ignoring that we may have encoded it many times

        short_url = []

        while new_id:
            short_url.append(self.map[new_id % 62])
            new_id = new_id // 62
        short_url.reverse()
        short_url = "".join(short_url)
        # Simple modulo map base62 to our id

        self.tiny_url_db[short_url] = longUrl
        # lazybones use built in dict for our DB using short_url as the key (instead of ID)
        return short_url  # Oh. It doesnt just want it saved, it wants it returened. Duh... its in the prompt
        # What was NOT clear was the way they are calling decode NEEDS to have encode return
        # as its actually calling decode(encode(longurl))

    def decode(self, shortUrl: str) -> str:
        return self.tiny_url_db[shortUrl] if self.tiny_url_db[shortUrl] else None

        # I'm being lazy as I don't want to write a full DB
        # In my lazybones version I would just store the short
        # URL as the key in a dict, with the full URL as the val
        # The "real" answer might want you to instead store by the
        # ID number so it can be stored in a BST for instance, so youd
        # actually need to invert the encoding to retrieve the ID number,
        # then use THAT to do the lookup. Faster?
