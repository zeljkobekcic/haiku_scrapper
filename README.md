# Haiku Scrapper

This simple script downloads and parses haikus from
[haikus.somebullshit.net/haikus](haikus.somebullshit.net/haikus). There was no
"proper" dataset containing haikus. Then I looked for websites which provide a
*high* number of haikus. That site has a little less than 350.000 haikus, which
should be more than enough.

The intention for this project was to collect a dataset to train a neural
network to generate poems. It turns out, that the
[project gutenberg](https://www.gutenberg.org/wiki/Poetry_(Bookshelf)) is the
best source for data for this project that I can find. The problem only problem
is with the access of this site in germany. Thereafter I looked for other
interesting things I can do with neural networks and then haikus came to my
mind.

## Usage

I recommend to use a virtual enviroment and then executing the next two
commands.
```
pip3 install -r requirements.txt
python3 haiku_scrapper -path some_dir
```

Otherwise you can use Docker.

```
docker volume create haiku_scrapper_data
docker haiku_scrapper_data:haiku_scrapper/data haiku_scrapper
```

Now you just need to wait until it downloaded ~350.000 haikus.