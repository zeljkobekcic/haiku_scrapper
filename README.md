# Haiku Scrapper

This simple script downloads and parses haikus from
[haikus.somebullshit.net/haikus](). Because there was no "proper" dataset
containing haikus. So I looked for websites which providing a high number of
haikus. This site has a little less than 350.000 haikus.

The intention for this project was to collect a dataset to train a neural
network to generate poems. It turns out, that the
[project gutenberg](https://www.gutenberg.org/wiki/Poetry_(Bookshelf)) is the
best source of data for this project. The problem is with the access of this
service in germany. Thereafter I looked for other interesting things I can do
with neural networks and then haikus came to my mind.

## Usage

I recommend to use a virtual enviroment
```
pip3 install -r requirements.txt
python3 haiku_scrapper -path some_dir
```

otherwise you can use the Dockerfile.

```
docker volume create haiku_scrapper_data
docker haiku_scrapper_data:haiku_scrapper/data haiku_scrapper
```

Now you just need to wait until it downloaded ~350.000 haikus.