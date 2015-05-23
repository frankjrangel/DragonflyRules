from dragonfly import *
from BaseRules import *
import BaseGrammars
import inspect
import ctypes
AciAware = ctypes.cdll.LoadLibrary(r"C:\Users\chajadan\git\AciImporter\Release\AciAware.dll");
grammar_context = AppContext(executable="Report32")
grammar = BaseGrammars.GlobalGrammar("ACI", context=grammar_context)

# decorator
def GrammarRule(Rule):
    if inspect.isclass(Rule):
        if issubclass(Rule, BaseQuickRules):
            Rule(grammar)
        else:
            grammar.add_rule(Rule())
    else:
        grammar.add_rule(Rule)

def GoToFirstPage():
    AciAware.GoToFirstPage()
    
def AciImportPics():
    action = Key("a-t, i") + Pause("200") + Mouse("(22,101), left:1") + Pause("100")
    action += Text(r"C:\Users\chajadan\git\AciCompiler\AciCompiler\AciCompiler\pics") + Key("enter")
    action += Pause("50") + Key("s-tab, c-a, enter") + Pause("400") + Key("w-up/50, a-v, 3")
    action.execute()


@GrammarRule
class AciChainedRules(QuickContinuousRules):
    mapping = {
        "to do": Text("??"),
        "next item": Key("end, enter") + Text("- "),
        "new item": Text("- "),
        "next page [<n> [times]]": Key("c-pgdown") * Repeat(extra="n"),
        "previous page [<n> [times]]": Key("c-pgup") * Repeat(extra="n"),
        "launch sketch": Key("a-t, d, 1"),
        "import pics": Function(AciImportPics),
        "import flood map": Key("a-s, a, right, 3"),
        "first page": Key("a-v, 6, enter"),
        "hex": Key("f3"),
        "delete this comp": Key("c-z") + Pause("30") + Key("enter"),
        "import field": Key("a-e, e, f"),
        "import section": Key("a-e, e, s"),
        "view image": Mouse("right:1") + Key("down:2, enter"),
        "delete image": Mouse("right:1") + Key("down:3, enter"),    
        "go to first page": Function(GoToFirstPage),
        "first pick": Key("down:5, tab"),
        "next pick": Key("home, left, down, right, up:10"),
        "go to plat map": Key("a-v, m, d, enter/20, c-pgdown/50, down:4"),
        "save file as": Key("a-f, a, r"),
    }
    extrasDict = {
        "n": IntegerRef("n", 1, 30),
    }
    defaultsDict = {
        "n": 1,
    }

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None