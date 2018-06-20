tekst = """To fully understand the processes occurring in present-day living cells, we need to consider how they arose in evolution. The most fundamental of all such problems is the expression of hereditary information, which today requires extraordinarily complex machinery and proceeds from DNA to protein through an RNA intermediate. How did this machinery arise? One view is that an RNA world existed on Earth before modern cells arose (Figure 6-91). According to this hypothesis, RNA stored both genetic information and catalyzed the chemical reactions in primitive cells. Only later in evolutionary time did DNA take over as the genetic material and proteins become the major catalyst and structural component of cells. If this idea is correct, then the transition out of the RNA world was never complete; as we have seen in this chapter, RNA still catalyzes several fundamental reactions in modern-day cells, which can be viewed as molecular fossils of an earlier world."""
zdania = tekst.replace('\n','')
zdania = zdania.replace('.', '')
zdania = zdania.replace('(', '')
zdania = zdania.replace(')', '')
zdania = zdania.replace(',', '')
lista = zdania.split(' ')
print len(lista)


