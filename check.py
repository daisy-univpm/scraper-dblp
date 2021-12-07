journal = "pr"
keywords = ["cnn", "convolutional neural network",
             "multilayer network", "deep learning", "model compression", "model pruning",
             "knowledge distillation"]

papers = list(set(open("journal/" + journal + ".txt", "r", encoding="utf-8").read().split("\n")))
c = {k: 0 for k in keywords}
for paper in papers:
    for w in keywords:
        if w in paper.lower():
            c[w] = c[w] + 1
print(journal, "# PAPERS: ", len(papers))
print(c)