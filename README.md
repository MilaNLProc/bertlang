# [BertLang](bertlang.unibocconi.it)

[BertLang](bertlang.unibocconi.it) is a webapp that contains info about BERT models.

![Image description](https://raw.githubusercontent.com/MilaNLProc/bertlang/master/static/img/logo.png)

## How to Contribute

Do you want to add a new model? we currently store all the information in a .json file `static/data/data_example.json`. 
See the following example for the Italian BERT, ALBERTO.

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

We are keeping this structure that is easy to parse and to check. If you find errors or you have something to add, you can modify it and send us a pull requests

## Contributors

+ Debora Nozza - debora.nozza@unibocconi.it
+ Federico Bianchi - federico.bianchi@unibocconi.it
+ Dirk Hovy - dirk.hovy@unibocconi.it

## Copyright and License

Built with [Start Bootstrap](https://startbootstrap.com/template-overviews/bare/).

Start Bootstrap is an open source library of free Bootstrap templates and themes. All of the free templates and themes on Start Bootstrap are released under the MIT license, which means you can use them for any purpose, even for commercial projects.
Copyright 2013-2019 Blackrock Digital LLC. Code released under the [MIT](https://github.com/BlackrockDigital/startbootstrap-bare/blob/gh-pages/LICENSE) license.
