# CS224n
## Assignment implementation
### 1. a1
- Exploring word vectors
### 2. a2
- Sigmoid function
- Implementing word2vec(loss and gradient descent)
- SGD optimizer

We can't remove parsed at the first step otherwise it wll disobey the condition.

$$ \begin{array}{|l|l|l|l} Stack & Buffer & New dependency & Transition \ \hline [Root, parsed] & [this, sentence, correctly] & parsed \rightarrow I & LEFT-ARC \ [Root, parsed, this] & [sentence, correctly] & & SHIFT \ [Root, parsed, this, sentence] & [correctly] & & SHIFT \ [Root, parsed, sentence] & [correctly] & this \rightarrow sentence & LEFT-ARC \ [Root, parsed] & [correctly] & parsed \rightarrow sentence & RIGHT-ARC \ [Root, parsed, correctly] & [] & & SHIFT \ [Root, parsed] & [] & parsed \rightarrow correctly & RIGHT-ARE \ [Root] & [] & Root \rightarrow parsed & RIGHT-ARE \end{array}$$
