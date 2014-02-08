import random
class Word(object):
    def __init__(self,s):
        self.mtext=s #the word itself
        self.etext=s #the word w/ adjectives and adverbs
class Adjective(Word):
    pass
class Noun(Word):
    def __init__(self,s,pronoun=False):
        Word.__init__(self,s)
        self.pronoun=pronoun
    def extend(self,adjective):
        self.etext = adjective.mtext+self.etext
    def get_pronoun(self,prefix="the"):
        if self.pronoun:
            return self.mtext
        else:
            return self.etext.strip(self.mtext)+prefix+" "+self.mtext #add the
class Pronoun(Noun):
    #s is the noun, not the pronoun
    def __init__(self,s):
        Noun.__init__(self,self.get_pronoun(s),pronoun=True)
class Verb(Word):
    def extend(self,adjective):
        self.etext = adjective.mtext+self.etext
class PastVerb(Verb):
    def __init__(self,Initializer):
        "Initializer is either a string, or now verb. ("killed"->"killed")(Verbobj:awkwardly kill->"awkwardly killed")"
        typ = type(Initializer)
        if typ==str:
            self.mtext=Initializer
            self.etext=Initializer
        elif typ==Verb:
            self.mtext=Initializer.etext
            self.etext=Initializer.etext
class SentenceGen(object):
    def __init__(self,l):
        self.instruct=l
    def __call__(self):
        global nouns,verbs,pastverbs,adjectives,adverbs
        adjectives_to_apply=[]
        text=[]
        def apply_adjectives(p,adjectives):
            for adj in adjectives_to_apply:t
                p.extend(adj)
            return p,[]
        for wtype in instruct:
            if wtype == "pronoun":
                p=Pronoun(random.choice(nouns))
                p,adjectives_to_apply=apply_adjectives(p,adjectives_to_apply)
            elif wtype == "a_noun":
                #pronoun!
                p=Pronoun(random.choice(nouns),prefix="a")
                p,adjectives_to_apply=apply_adjectives(p,adjectives_to_apply)
            elif wtype=="noun":
                p=Noun(random.choice(nouns))
                p,adjectives_to_apply=apply_adjectives(p,adjectives_to_apply)
            elif wtype=="adjective":
                adjectives_to_apply.append(Adjective(random.choice(adjectives)))
            elif wtype=="adverb":
                adjectives_to_apply.append(Adjective(random.choice(adverbs)))
            elif wtype=="verb":
                p=Verb(random.choice(verbs))
                p,adjectives_to_apply=apply_adjectives(p,adjectives_to_apply)
            elif wtype=="pastverb":
                p=PastVerb(random.choice(pastverbs))
                p,adjectives_to_apply=apply_adjectives(p,adjectives_to_apply)
            else:
                raise ValueError("Invalid word type:"+wtype)
            text.append(p.mtext)
        return text
class SentenceGenerators:
    "A virtual namespace of sentence generators"
    #Words to use for examples:
    #Pronoun->the orange
    #A_pronoun->a man
    #Pastverb->hugged
    #Noun->speaker
    #Verb->washed
    #Adjective->quickly
    #Adverb->tightly
    did = SentenceGen(["pronoun","pastverb","a_pronoun"]) #The orange hugged a man
    did_disc = SentenceGen(["pronoun","adverb","pastverb","a_pronoun"]) #The orange tightly hugged a man
