# Beaver
Beaver is a utility that automatically edits your .bib files with new papers as they are added to your LaTeX files.

<img align="middle" src="https://i.ibb.co/2FhD1n2/beaver.png" alt="beaver">

<hr>

## Sample Usage - Without GUI
If you have to just use the code ```bib_reader.py``` which scraps the bibtex file from Google scholar, you can do the following.

```diff
  + from bib_reader import Parser
  + paper_name = "" # write the title of the paper you want the bib for
  + bibParser = Parser(paper_name)
  + retrieved_bib = bibParser.recover_bib()
  + print(retrieved_bib)
```

## License
This is covered by the standard MIT License.
