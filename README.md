# [BertLang](bertlang.unibocconi.it)

[BertLang](bertlang.unibocconi.it) is a webapp that contains info about BERT models.

![Image description](https://raw.githubusercontent.com/MilaNLProc/bertlang/master/static/img/logo.png)

## How to Contribute

Do you want to add a new model? we currently store all the information in a .json file `static/data/data_example.json`. 
See the following example for the Spanish BERT, BETO.

```json
 {
    "name": "BETO",
    "language": "Spanish",
    "tasks": [
      {
        "source": "https://github.com/dccuchile/beto",
        "code": "https://github.com/dccuchile/beto",
        "name": "POS",
        "dataset": {
          "name": "Turku Dependency Treebank",
          "link": "https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-1827",
          "domain": "wiki, news, blog, speech, legislative, fiction"
        },
        "measure": "UPOS",
        "performance": 98.97,
        "multi_lingual": 97.1,
        "multi_difference": 1.87
      },
      {
        "name": "NER",
        "source": "https://github.com/dccuchile/beto",
        "code": "https://github.com/dccuchile/beto",
        "dataset": {
          "name": "CoNLL 2000, 2002, 2007",
          "link": "https://www.kaggle.com/nltkdata/conll-corpora",
          "domain": "news"
        },
        "measure": "F1",
        "performance": 88.43,
        "multi_lingual": 87.38,
        "multi_difference": 1.05
      },
      {
        "name": "TC",
        "source": "https://github.com/dccuchile/beto",
        "code": "https://github.com/dccuchile/beto",
        "dataset": {
          "name": "MLDoc",
          "link": "https://github.com/facebookresearch/MLDoc",
          "domain": "news"
        },
        "measure": "Accuracy",
        "performance": 95.6,
        "multi_lingual": 95.7,
        "multi_difference": -0.1
      },
      {
        "name": "PI",
        "source": "https://github.com/dccuchile/beto",
        "code": "https://github.com/dccuchile/beto",
        "dataset": {
          "name": "PAWS-X",
          "link": "https://github.com/google-research-datasets/paws/tree/master/pawsx",
          "domain": "wiki"
        },
        "measure": "Accuracy",
        "performance": 89.05,
        "multi_lingual": 90.7,
        "multi_difference": -1.65
      },
      {
        "name": "NLI",
        "source": "https://github.com/dccuchile/beto",
        "code": "https://github.com/dccuchile/beto",
        "dataset": {
          "name": "XNLI",
          "link": "https://github.com/facebookresearch/XNLI",
          "domain": "transcription, politics, news, literature, misc"
        },
        "measure": "Accuracy",
        "performance": 82.01,
        "multi_lingual": 78.5,
        "multi_difference": 3.51
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
