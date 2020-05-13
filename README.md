# Beaver
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Beaver is a utility that automatically edits your .bib files with new papers as they are added to your LaTeX files.

<img align="middle" src="https://i.ibb.co/2FhD1n2/beaver.png" alt="beaver">

<hr>

## Sample Usage - Without GUI
If you have to just use the code ```bib_reader.py``` which scraps the bibtex file from Google scholar, you can do the following.

```
    from bib_reader import Parser
    paper_name = "" # write the title of the paper you want the bib for
    bibParser = Parser(paper_name)
    retrieved_bib = bibParser.recover_bib()
    print(retrieved_bib)
```

You can also retrieve the bibTex of papers you partially remember the name of. A few keywords (which appear in the title of the paper) and the matching can be done which results in the correct bib retrieval.

```
    # the actual paper name is: Imagenet classification with deep convolutional neural networks
    # so we just type a few keywords we can remember from the top of our head
    paper_name = "ImageNet Deep Classification" 
    # call the recover_bib() method.
    # the output would be: 
    
    @inproceedings{krizhevsky2012imagenet,
          title={Imagenet classification with deep convolutional neural networks},
          author={Krizhevsky, Alex and Sutskever, Ilya and Hinton, Geoffrey E},
          booktitle={Advances in neural information processing systems},
          pages={1097--1105},
          year={2012}
    }

```

## License
This is covered by the standard MIT License.
