from GraphFunctions import Graph, draw_graph

# Create the graph
g = Graph()

# #MRT 
g.add_edge("Taft Avenue", "Magallanes")
g.add_edge("Magallanes", "Ayala")
g.add_edge("Ayala", "Buendia")
g.add_edge("Buendia", "Guadalupe")
g.add_edge("Guadalupe", "Boni")
g.add_edge("Boni", "Shaw Boulevard")
g.add_edge("Shaw Boulevard", "Ortigas")
g.add_edge("Ortigas", "Santolan LRT")
g.add_edge("Santolan LRT","Araneta Center - Cubao")
g.add_edge("Araneta Center - Cubao", "Kamuning")
g.add_edge("Kamuning", "Quezon Avenue")
g.add_edge("Quezon Avenue", "North Avenue")


# LRT 2
g.add_edge("Recto", "Legarda")
g.add_edge("Legarda", "Pureza")
g.add_edge("Pureza", "V. Mapa")
g.add_edge("V. Mapa", "J. Ruiz")
g.add_edge("J. Ruiz", "Gilmore")
g.add_edge("Gilmore", "Betty Go Belmonte")
g.add_edge("Betty Go Belmonte", "Araneta Center - Cubao")
g.add_edge("Araneta Center - Cubao", "Anonas")
g.add_edge("Anonas", "Katipunan")
g.add_edge("Katipunan", "Santolan MRT")


# LRT 1
g.add_edge("Baclaran", "EDSA")
g.add_edge("EDSA", "Libertad")
g.add_edge("Libertad", "Gil Puyat")
g.add_edge("Gil Puyat", "Vito Cruz")
g.add_edge("Vito Cruz", "Quirino")
g.add_edge("Quirino", "Pedro Gil")
g.add_edge("Pedro Gil", "United Nations")
g.add_edge("United Nations", "Central Terminal")
g.add_edge("Central Terminal", "Carriedo")
g.add_edge("Carriedo", "Doroteo Jose")
g.add_edge("Doroteo Jose", "Bambang")
g.add_edge("Bambang", "Tayuman")
g.add_edge("Tayuman", "Blumentrit")
g.add_edge("Blumentrit", "Abad Santos")
g.add_edge("Abad Santos", "R. Papa")
g.add_edge("R. Papa", "5th Avenue")
g.add_edge("5th Avenue", "Monumento")
g.add_edge("Monumento", "Balintawak")
g.add_edge("Balintawak", "Roosevelt")

#Connecting Terminals
g.add_edge("Taft Avenue", "EDSA")
g.add_edge("Doroteo Jose", "Recto")

# Draw the graph
draw_graph(g)
