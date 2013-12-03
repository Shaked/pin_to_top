Description
=================

Pin Pelican's article(s) to top "Sticky article". 

It is useful when you want to publish new articles while keeping one or more articles at the top of your articles list.


## Usage

Check out the plugin to your pelican's plugins directory 

Edit your *pelicanconf.py*: 

    PLUGINS = ['pin_to_top']

In your article(s) meta data you can use: 

    Pin: true 
    
Later you can also use it in your theme, for example you can use the glyphicon-pushpin:

    <span>{% if article.pin %}<i class="glyphicon glyphicon-pushpin"></i>{% endif %}</span>
    
Visual example: 

![Pin to top](https://raw.github.com/Shaked/pin-to-top/master/pelican-pin-to-top-example.png)
