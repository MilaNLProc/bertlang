# [BertLang](https://bertlang.unibocconi.it)

[BertLang](https://bertlang.unibocconi.it) is a webapp that contains info about language-specific BERT models.

![Image description](https://raw.githubusercontent.com/MilaNLProc/bertlang/master/static/img/logo.png)



## How to Contribute

This is a **collaborative** resource to help researchers understand and find the best BERT model for a given dataset, task and language. The numbers here rely on self reported performance (we can give no guarantees for their accuracy. In the future, we hope to independently verify each of the models).

We currently store all the information in a .json file `static/data/data_example.json`. We are keeping this structure that is easy to parse and to check.
*Do you want to add a new model or suggest updates?* Send us a pull request!

See the following example for the Italian BERT model, ALBERTO.

```json
 {
     "name": "ALBERTO",
     "language": "Italian",
     "tasks": [
       {
         "source": "http://ceur-ws.org/Vol-2481/paper57.pdf",
         "code": "https://github.com/marcopoli/AlBERTo-it",
         "name": "SA",
         "dataset": {
           "name": "SENTIPOLC 2016",
           "link": "http://www.di.unito.it/~tutreeb/sentipolc-evalita16/data.html",
           "domain": "twitter"
         },
         "measure": "F1 (test)",
         "performance": 72.23,
         "multi_lingual": "nan",
         "multi_difference": "nan"
       },
       {
         "name": "SC",
         "source": "http://ceur-ws.org/Vol-2481/paper57.pdf",
         "code": "https://github.com/marcopoli/AlBERTo-it",
         "dataset": {
           "name": "SENTIPOLC 2016",
           "link": "http://www.di.unito.it/~tutreeb/sentipolc-evalita16/data.html",
           "domain": "twitter"
         },
         "measure": "F1 (test)",
         "performance": 79.06,
         "multi_lingual": "nan",
         "multi_difference": "nan"
       },
       {
         "name": "ID",
         "source": "http://ceur-ws.org/Vol-2481/paper57.pdf",
         "code": "https://github.com/marcopoli/AlBERTo-it",
         "dataset": {
           "name": "SENTIPOLC 2016",
           "link": "http://www.di.unito.it/~tutreeb/sentipolc-evalita16/data.html",
           "domain": "twitter"
         },
         "measure": "F1 (test)",
         "performance": 60.9,
         "multi_lingual": "nan",
         "multi_difference": "nan"
       }
     ]
   }
```

## Contributors

+ Debora Nozza - [Twitter](http://twitter.com/debora_nozza) | [Personal Website](http://dnozza.github.io/) | debora.nozza@unibocconi.it
+ Federico Bianchi - [Twitter](http://twitter.com/fb_vinid) | [Personal Website](http://vinid.io/) | federico.bianchi@unibocconi.it
+ Dirk Hovy - [Twitter](http://twitter.com/dirk_hovy) | [Personal Website](http://dirkhovy.com/) |  dirk.hovy@unibocconi.it

## Copyright and License

Built with [Start Bootstrap](https://startbootstrap.com/template-overviews/bare/).

Start Bootstrap is an open source library of free Bootstrap templates and themes. All of the free templates and themes on Start Bootstrap are released under the MIT license, which means you can use them for any purpose, even for commercial projects.
Copyright 2013-2019 Blackrock Digital LLC. Code released under the [MIT](https://github.com/BlackrockDigital/startbootstrap-bare/blob/gh-pages/LICENSE) license.
