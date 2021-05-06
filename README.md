# Generate Sentences from a Context Free Grammar

This has only been tested on non-recursive grammars, ones in which phrases can't be nodes twice.

## Use

You need to build a tree with the provide tree data structure in this repo. These trees work:

```python
tree1 = Tree("S", 
               [Tree("Sub",
                     [Tree("Bill"), Tree("Tawny Owl"), Tree("Cajun Boss")]), 
                Tree("Verb", 
                     [Tree("cooks"), Tree("fights"), Tree("eats")]),
                Tree("Obj", [Tree("rodents"), Tree("aliens"), Tree("Kentucky Fried Chicken")])])

tree2 = Tree("S",
               [Tree("Sub",
                     [Tree("Det",
                           [Tree("the"), Tree("a")]
                     ), 
                     Tree("Noun",
                          [Tree("Shakespeare"), Tree("Banana")]
                     )]
               ),
                Tree("Verb",
                     [Tree("fights"), Tree("builds")])])
```

Run the line to generate your sentence:

```python
tree1.generate_sentence()
```
