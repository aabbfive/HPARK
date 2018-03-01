<h1 align="center">
  <br>
  <a href="https://github.com/aabbfive/PPark">
    <img src="PPark.svg" alt="PPark" width="200">
  </a>
  <br>
  PPark
  <br>
  <br>
</h1>

<h4 align="center">The best lexing library available any python version confused (2.x, 3.x, PyPy...)</h4>

## 💾 Install

Download the latest version of PPark from
the [GitHub releases](https://github.com/aabbfive/PPark/releases) page.


## 💬 How to Contribute

### Get the code

```
$ git clone https://github.com/aabbfive/PPark.git
$ cd PPark
```

### Install the library

```
$ pip install PPark
```

#### Or

```
$ pip install git+https://github.com/aabbfive/PPark
```

### Examples

```
from PPark import Lexer
from PPark.constant import Keyword, Keywords

lexer = Lexer()
lexer.addRule('INTEGER', r'([0-9]+)')
lexer.addRule('OP', Keywords([
	Keyword('}'), 
	Keyword('{'),
	Keyword('^'),
	Keyword(']'),
	Keyword('['),
	Keyword('>'),
	Keyword('<'),
	Keyword('='),
	Keyword('.'),
	Keyword('-'),
	Keyword(','),
	Keyword('+'),
	Keyword('**'),
	Keyword('*'),
	Keyword('/'),
	Keyword('//'),
	Keyword('%'),
	Keyword(')'),
	Keyword('(')
	]))
@lexer.on_match(r'"([^"\n]|(\\"))*"')
def STRING(token):
	token.value = token.value[1:][:-1]
@lexer.on_match(r'[a-zA-Z_$]\w*')
def IDENTIFIER(token):
	if keywords.contains(token.value):
		token.type = token.value.upper()
		return token
lexer.input("""
t = 12*2
""")
for token in lexer:
	print(token)
```

## ©️ License

MIT. Copyright (c) [Aabbfive](https://github.com/aabbfive).
