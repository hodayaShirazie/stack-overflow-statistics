# import pandas as pd
# import networkx as nx
# import matplotlib.pyplot as plt
# #
#
# # hodaya first try
# # # נתיב הקובץ
# # file_path = "sx-stackoverflow.txt"
# #
# # # טעינה של דגימה אקראית של 1000 שורות בלבד
# # data = pd.read_csv(file_path, delimiter=' ', header=None, names=['SRC', 'DST', 'UNIXTS'], nrows=1000)
# #
# # # יצירת גרף ריק
# # G = nx.DiGraph()
# #
# # # הוספת הצלעות (Edges) לגרף
# # for _, row in data.iterrows():
# #     G.add_edge(row['SRC'], row['DST'], timestamp=row['UNIXTS'])
# #
# # # הצגת גרף קטן לדוגמה (כדי לא להעמיס)
# # plt.figure(figsize=(10, 10))
# # nx.draw(G, node_size=50, node_color='blue', alpha=0.6, with_labels=False)
# # plt.title("Graph of interactions on Stack Overflow")
# # plt.show()
#
#
# # tha all interactions full graph - dont try at home
#
# # import networkx as nx
# # import matplotlib.pyplot as plt
# #
# # # קריאת הנתונים מהקובץ
# # edges = []
# # with open("sx-stackoverflow.txt", "r") as file:
# #     for line in file:
# #         data = line.strip().split()
# #         if len(data) >= 2:  # לוודא שיש לפחות שני מספרים (קודקודים)
# #             node1, node2 = int(data[0]), int(data[1])
# #             edges.append((node1, node2))
# #
# # # יצירת גרף
# # graph = nx.Graph()
# # graph.add_edges_from(edges)
# #
# # # ציור הגרף
# # plt.figure(figsize=(12, 8))
# # pos = nx.spring_layout(graph, seed=42)  # פריסה יציבה
# # nx.draw(graph, pos, node_size=50, node_color="lightblue", edge_color="gray", alpha=0.6)
# # plt.title("רשת אינטראקציות ב-Stack Overflow", fontsize=14)
# # plt.show()
#
#
#
#
#
# #all interactions  - 1000 centerlaize nodes
# # import networkx as nx
# # import matplotlib.pyplot as plt
# #
# # # קריאת הנתונים מהקובץ
# # edges = []
# # with open("sx-stackoverflow.txt", "r") as file:
# #     for line in file:
# #         data = line.strip().split()
# #         if len(data) >= 2:
# #             node1, node2 = int(data[0]), int(data[1])
# #             edges.append((node1, node2))
# #
# # # יצירת גרף מלא
# # graph = nx.Graph()
# # graph.add_edges_from(edges)
# #
# # # חישוב מדד Degree Centrality
# # degree_centrality = nx.degree_centrality(graph)
# #
# # # מיון הקודקודים לפי המרכזיות ובחירת 5000 המרכזיים ביותר
# # top_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:1000]
# #
# # # יצירת תת-גרף עם 5000 הקודקודים המרכזיים ביותר
# # subgraph = graph.subgraph(top_nodes)
# #
# # # ציור הגרף
# # plt.figure(figsize=(12, 8))
# # pos = nx.spring_layout(subgraph, seed=42)  # פריסה יציבה
# # nx.draw(subgraph, pos, node_size=30, node_color="lightblue", edge_color="gray", alpha=0.6)
# # plt.title("רשת Stack Overflow - 5000 הקודקודים המרכזיים ביותר", fontsize=14)
# # plt.show()
#
#
#
# # a2q - all graph - not good
#
# # import networkx as nx
# # import matplotlib.pyplot as plt
# #
# # # קריאת הנתונים מהקובץ
# # edges = []
# # with open("sx-stackoverflow-a2q.txt", "r") as file:
# #     for line in file:
# #         data = line.strip().split()
# #         if len(data) >= 2:  # לוודא שיש לפחות שני מספרים (קודקודים)
# #             node1, node2 = int(data[0]), int(data[1])
# #             edges.append((node1, node2))
# #
# # # יצירת גרף
# # graph = nx.Graph()
# # graph.add_edges_from(edges)
# #
# # # ציור הגרף
# # plt.figure(figsize=(12, 8))
# # pos = nx.spring_layout(graph, seed=42)  # פריסה יציבה
# # nx.draw(graph, pos, node_size=50, node_color="lightblue", edge_color="gray", alpha=0.6)
# # plt.title("רשת אינטראקציות ב-Stack Overflow", fontsize=14)
# # plt.show()
# #
# #
#
# # c2q - all graph - not good
#
#
# # import networkx as nx
# # import matplotlib.pyplot as plt
# #
# # # קריאת הנתונים מהקובץ
# # edges = []
# # with open("sx-stackoverflow-c2q.txt", "r") as file:
# #     for line in file:
# #         data = line.strip().split()
# #         if len(data) >= 2:  # לוודא שיש לפחות שני מספרים (קודקודים)
# #             node1, node2 = int(data[0]), int(data[1])
# #             edges.append((node1, node2))
# #
# # # יצירת גרף
# # graph = nx.Graph()
# # graph.add_edges_from(edges)
# #
# # # ציור הגרף
# # plt.figure(figsize=(12, 8))
# # pos = nx.spring_layout(graph, seed=42)  # פריסה יציבה
# # nx.draw(graph, pos, node_size=50, node_color="lightblue", edge_color="gray", alpha=0.6)
# # plt.title("רשת אינטראקציות ב-Stack Overflow", fontsize=14)
# # plt.show()
#
#
#
#
#
# # a2a - all graph - not good
#
# # import networkx as nx
# # import matplotlib.pyplot as plt
# #
# # # קריאת הנתונים מהקובץ
# # edges = []
# # with open("sx-stackoverflow-c2a.txt", "r") as file:
# #     for line in file:
# #         data = line.strip().split()
# #         if len(data) >= 2:  # לוודא שיש לפחות שני מספרים (קודקודים)
# #             node1, node2 = int(data[0]), int(data[1])
# #             edges.append((node1, node2))
# #
# # # יצירת גרף
# # graph = nx.Graph()
# # graph.add_edges_from(edges)
# #
# # # ציור הגרף
# # plt.figure(figsize=(12, 8))
# # pos = nx.spring_layout(graph, seed=42)  # פריסה יציבה
# # nx.draw(graph, pos, node_size=50, node_color="lightblue", edge_color="gray", alpha=0.6)
# # plt.title("רשת אינטראקציות ב-Stack Overflow", fontsize=14)
# # plt.show()
# #
# #
# #
# #
#
#
# # c2a - 1500  centerlize nodes
#
# # import networkx as nx
# # import matplotlib.pyplot as plt
# #
# # # קריאת הנתונים מהקובץ
# # edges = []
# # with open("sx-stackoverflow-c2a.txt", "r") as file:
# #     for line in file:
# #         data = line.strip().split()
# #         if len(data) >= 2:
# #             node1, node2 = int(data[0]), int(data[1])
# #             edges.append((node1, node2))
# #
# # # יצירת גרף מלא
# # graph = nx.Graph()
# # graph.add_edges_from(edges)
# #
# # # חישוב מדד Degree Centrality
# # degree_centrality = nx.degree_centrality(graph)
# #
# # # מיון הקודקודים לפי המרכזיות ובחירת 5000 המרכזיים ביותר
# # top_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:1500]
# #
# # # יצירת תת-גרף עם 5000 הקודקודים המרכזיים ביותר
# # subgraph = graph.subgraph(top_nodes)
# #
# # # ציור הגרף
# # plt.figure(figsize=(12, 8))
# # pos = nx.spring_layout(subgraph, seed=42)  # פריסה יציבה
# # nx.draw(subgraph, pos, node_size=30, node_color="lightblue", edge_color="gray", alpha=0.6)
# # plt.title("רשת Stack Overflow - 5000 הקודקודים המרכזיים ביותר", fontsize=14)
# # plt.show()
# #
# #
# #
# #
# #
# # c2q - 1500  centerlize nodes
#
# #
# # # קריאת הנתונים מהקובץ
# # edges = []
# # with open("sx-stackoverflow-c2q.txt", "r") as file:
# #     for line in file:
# #         data = line.strip().split()
# #         if len(data) >= 2:
# #             node1, node2 = int(data[0]), int(data[1])
# #             edges.append((node1, node2))
# #
# # # יצירת גרף מלא
# # graph = nx.Graph()
# # graph.add_edges_from(edges)
# #
# # # חישוב מדד Degree Centrality
# # degree_centrality = nx.degree_centrality(graph)
# #
# # # מיון הקודקודים לפי המרכזיות ובחירת 5000 המרכזיים ביותר
# # top_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:1500]
# #
# # # יצירת תת-גרף עם 5000 הקודקודים המרכזיים ביותר
# # subgraph = graph.subgraph(top_nodes)
# #
# # # ציור הגרף
# # plt.figure(figsize=(12, 8))
# # pos = nx.spring_layout(subgraph, seed=42)  # פריסה יציבה
# # nx.draw(subgraph, pos, node_size=30, node_color="lightblue", edge_color="gray", alpha=0.6)
# # plt.title("רשת Stack Overflow - 5000 הקודקודים המרכזיים ביותר", fontsize=14)
# # plt.show()
# #
# #
# #
# #
# #
#
#
# # a2q - 1500  centerlize nodes
#
# #
# # # קריאת הנתונים מהקובץ
# # edges = []
# # with open("sx-stackoverflow-a2q.txt", "r") as file:
# #     for line in file:
# #         data = line.strip().split()
# #         if len(data) >= 2:
# #             node1, node2 = int(data[0]), int(data[1])
# #             edges.append((node1, node2))
# #
# # # יצירת גרף מלא
# # graph = nx.Graph()
# # graph.add_edges_from(edges)
# #
# # # חישוב מדד Degree Centrality
# # degree_centrality = nx.degree_centrality(graph)
# #
# # # מיון הקודקודים לפי המרכזיות ובחירת 5000 המרכזיים ביותר
# # top_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:1500]
# #
# # # יצירת תת-גרף עם 5000 הקודקודים המרכזיים ביותר
# # subgraph = graph.subgraph(top_nodes)
# #
# # # ציור הגרף
# # plt.figure(figsize=(12, 8))
# # pos = nx.spring_layout(subgraph, seed=42)  # פריסה יציבה
# # nx.draw(subgraph, pos, node_size=30, node_color="lightblue", edge_color="gray", alpha=0.6)
# # plt.title("רשת Stack Overflow - 5000 הקודקודים המרכזיים ביותר", fontsize=14)
# # plt.show()
# #
# #
#
#
#
#
#
#
# # colored nodes
#
# import networkx as nx
# import matplotlib.pyplot as plt
# import numpy as np
# import random
#
# # פונקציה לקריאת קובץ ולבחירת 1500 קודקודים רנדומליים
# def load_graph_data(filename, sample_size=1500):
#     edges = []
#     response_times = {}
#
#     with open(filename, "r") as file:
#         for line in file:
#             data = line.strip().split()
#             if len(data) == 3:  # לוודא שיש שלושה ערכים (משתמש1, משתמש2, זמן תגובה)
#                 user1, user2, response_time = int(data[0]), int(data[1]), int(data[2])
#                 edges.append((user1, user2))
#
#                 # שמירת זמן תגובה ממוצע לכל משתמש
#                 if user1 not in response_times:
#                     response_times[user1] = []
#                 response_times[user1].append(response_time)
#
#     # חישוב ממוצע זמן תגובה לכל משתמש
#     avg_response_time = {user: np.mean(times) for user, times in response_times.items()}
#
#     # בחירת תת-קבוצה אקראית של קודקודים
#     sampled_nodes = set(random.sample(list(response_times.keys()), min(sample_size, len(response_times))))
#     sampled_edges = [(u, v) for u, v in edges if u in sampled_nodes and v in sampled_nodes]
#
#     return sampled_edges, avg_response_time
#
# # קריאת הנתונים משלושת הקבצים
# edges_a2q, response_time_a2q = load_graph_data("sx-stackoverflow-a2q.txt")
# edges_c2q, response_time_c2q = load_graph_data("sx-stackoverflow-c2q.txt")
# edges_c2a, response_time_c2a = load_graph_data("sx-stackoverflow-c2a.txt")
#
# # פונקציה לציור גרף
# def draw_graph(edges, avg_response_time, title):
#     graph = nx.Graph()
#     graph.add_edges_from(edges)
#
#     # חישוב צבעים לפי זמן תגובה ממוצע
#     node_colors = []
#     for node in graph.nodes():
#         avg_time = avg_response_time.get(node, 0)  # אם אין מידע, ברירת מחדל 0
#         node_colors.append(avg_time)
#
#     # נורמליזציה של הצבעים
#     norm_colors = np.array(node_colors)
#     if len(norm_colors) > 0:
#         norm_colors = (norm_colors - norm_colors.min()) / (norm_colors.max() - norm_colors.min() + 1e-5)
#
#     # ציור הגרף
#     plt.figure(figsize=(10, 7))
#     pos = nx.spring_layout(graph, seed=42)
#
#     # ציור הקשתות
#     nx.draw_networkx_edges(graph, pos, edge_color="gray", alpha=0.6)
#
#     # ציור הקודקודים עם צבעים
#     nodes = nx.draw_networkx_nodes(graph, pos, node_size=50, node_color=norm_colors, cmap="coolwarm")
#
#     # הוספת colorbar עם מפתח צבעים
#     plt.colorbar(nodes, label="Average Response Time")
#
#     # הוספת כותרת עם מספר קודקודים וקשתות
#     plt.title(f"{title}\nNodes: {graph.number_of_nodes()}, Edges: {graph.number_of_edges()}", fontsize=14)
#     plt.axis("off")  # להוריד צירים
#     plt.show()
#
# # ציור שלושת הגרפים
# draw_graph(edges_a2q, response_time_a2q, "Answer to Question")
# draw_graph(edges_c2q, response_time_c2q, "Comment to Question")
# draw_graph(edges_c2a, response_time_c2a, "Comment to Answer")













import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Load the dataset
file_path = "sx-stackoverflow.txt"
edges = []

with open(file_path, 'r') as file:
    for line in file:
        # Split by whitespace and ensure there are at least two values (source and target)
        parts = line.strip().split()
        if len(parts) >= 2:
            source, target = parts[0], parts[1]  # Assuming first two columns are source and target
            edges.append((source, target))

# Step 2: Create a directed graph
G = nx.DiGraph()
G.add_edges_from(edges)

# Step 3: Calculate centrality (e.g., degree centrality or betweenness centrality)
centrality = nx.degree_centrality(G)  # You can use nx.betweenness_centrality(G) for another option
sorted_nodes = sorted(centrality, key=centrality.get, reverse=True)[:1500]

# Step 4: Create a subgraph with the top 1500 nodes based on centrality
subgraph = G.subgraph(sorted_nodes)

# Step 5: Save the graph in TXT format
with open("centralized_graph.txt", "w") as file:
    for edge in subgraph.edges():
        file.write(f"{edge[0]} {edge[1]}\n")

# Step 6: Visualize the graph
plt.figure(figsize=(12, 12))
nx.draw(subgraph, with_labels=False, node_size=50, node_color='lightblue', edge_color='gray', font_size=8, font_weight='bold')
plt.title("All Interaction Graph (CENTRALIZED)")
plt.show()


