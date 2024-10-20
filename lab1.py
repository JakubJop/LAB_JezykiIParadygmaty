#Zad1. def podzielpaczki(wagi, max_waga):
#    for waga in wagi:
#        if waga > max_waga:
#            raise ValueError(f"Paczka o wadze {waga} przekracza max dozwoloną wagę {max_waga} kg")
#
#wagi.sorted = sorted(wagi, reverse= True)
#kursy = []
#
#for waga in wagi_sorted:
#    dodano = False
#    for kurs in kursy:
#        if sum(kurs) + waga <= max_waga:
#            kurs.append(waga)
#           dodano = True
#            break
#    if not dodano:
#        kursy.append([waga])
#
#return len(kursy), kursy
#
#
#wagi = [10,15,7,20,5,8,10]
#max_waga = 25
#
#print(podzielPaczki(wagi, max_waga))
#
#for i, kurs in enumerate(kursy, 1):
#    print({f"Kurs {1}: {kurs} - suma wag: {sum(kurs)} kg."})

#Zad2.

# #def bfs(graph, start, goal):
#
#     def bfs_inner(queue, visited, paths):
#         if len(queue) == 0:
#             return []
#
#
#         current_node, path = queue[0]
#         queue = queue[1:]  # Usuwamy pierwszy element (FIFO)
#
#
#         if current_node == goal:
#             return path
#
#
#         neighbors = graph.get(current_node, [])
#         new_paths = list(map(lambda neighbor: (neighbor, path + [neighbor]),
#                              filter(lambda neighbor: neighbor not in visited, neighbors)))
#
#
#         new_queue = queue + new_paths
#         new_visited = visited.union(set(map(lambda x: x[0], new_paths)))
#
#
#         return bfs_inner(new_queue, new_visited, paths)
#
#
#     initial_queue = [(start, [start])]
#     initial_visited = {start}
#     return bfs_inner(initial_queue, initial_visited, [])
#
#
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
#
#
# shortest_path = bfs(graph, 'A', 'F')
# print("Najkrótsza ścieżka:", shortest_path)

#Zad3
# # Proceduralne podejście do optymalizacji rozmieszczenia zadań
# def procedural_task_scheduling(tasks):
#     for i in range(len(tasks)):
#         for j in range(0, len(tasks) - i - 1):
#             if tasks[j]['time'] > tasks[j + 1]['time']:
#
#                 tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]
#
#     total_time = 0
#     waiting_time = 0
#
#
#     for task in tasks:
#         total_time += waiting_time
#         waiting_time += task['time']
#
#     return tasks, total_time
#
#
# def bubble_sort(tasks):
#     n = len(tasks)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if tasks[j]['time'] > tasks[j + 1]['time']:
#
#                 tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]
#     return tasks
#
# def calculate_waiting_time(tasks):
#     total_time = 0
#     waiting_time = 0
#
#
#     def helper(index):
#         nonlocal total_time, waiting_time
#         if index >= len(tasks):
#             return
#         total_time += waiting_time
#         waiting_time += tasks[index]['time']
#         helper(index + 1)
#
#     helper(0)
#     return total_time
#
# def functional_task_scheduling(tasks):
#     sorted_tasks = bubble_sort(tasks)
#     total_time = calculate_waiting_time(sorted_tasks)
#     return sorted_tasks, total_time
#
#
# tasks_procedural = [
#     {'task': 'Task 1', 'time': 3, 'reward': 100},
#     {'task': 'Task 2', 'time': 1, 'reward': 200},
#     {'task': 'Task 3', 'time': 2, 'reward': 150},
#     {'task': 'Task 4', 'time': 5, 'reward': 80}
# ]
#
#
# optimal_tasks, total_waiting_time = procedural_task_scheduling(tasks_procedural)
# print("Proceduralna optymalna kolejność zadań:", [t['task'] for t in optimal_tasks])
# print("Całkowity czas oczekiwania (proceduralnie):", total_waiting_time)
#
#
# tasks_functional = [
#     {'task': 'Task 1', 'time': 3, 'reward': 100},
#     {'task': 'Task 2', 'time': 1, 'reward': 200},
#     {'task': 'Task 3', 'time': 2, 'reward': 150},
#     {'task': 'Task 4', 'time': 5, 'reward': 80}
# ]
#
#
# optimal_tasks_func, total_waiting_time_func = functional_task_scheduling(tasks_functional)
# print("Funkcyjna optymalna kolejność zadań:", [t['task'] for t in optimal_tasks_func])
# print("Całkowity czas oczekiwania (funkcyjnie):", total_waiting_time_func)

# #Zad4.
# def knapsack_procedural(weights, values, capacity):
#     n = len(weights)
#     dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
#
#     for i in range(1, n + 1):
#         for w in range(capacity + 1):
#             if weights[i - 1] <= w:
#                 dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
#             else:
#                 dp[i][w] = dp[i - 1][w]
#
#     max_value = dp[n][capacity]
#
#     selected_items = []
#     w = capacity
#     for i in range(n, 0, -1):
#         if dp[i][w] != dp[i - 1][w]:
#             selected_items.append(i - 1)
#             w -= weights[i - 1]
#
#     return max_value, selected_items
#
#
# def knapsack_recursive(weights, values, capacity, n):
#     if n == 0 or capacity == 0:
#         return 0, []
#
#     if weights[n - 1] > capacity:
#         return knapsack_recursive(weights, values, capacity, n - 1)
#
#     without_item, items_without = knapsack_recursive(weights, values, capacity, n - 1)
#     with_item, items_with = knapsack_recursive(weights, values, capacity - weights[n - 1], n - 1)
#
#     with_item += values[n - 1]
#
#     if with_item > without_item:
#         return with_item, items_with + [n - 1]
#     else:
#         return without_item, items_without
#
#
# def knapsack_functional(weights, values, capacity):
#     max_value, selected_items = knapsack_recursive(weights, values, capacity, len(weights))
#     return max_value, selected_items
#
#
# weights = [2, 3, 4, 5]
# values = [3, 4, 5, 6]
# capacity = 5
#
# max_value_proc, selected_items_proc = knapsack_procedural(weights, values, capacity)
# print(f"Proceduralnie: Maksymalna wartość = {max_value_proc}, Wybrane przedmioty = {selected_items_proc}")
#
# max_value_func, selected_items_func = knapsack_functional(weights, values, capacity)
# print(f"Funkcyjnie: Maksymalna wartość = {max_value_func}, Wybrane przedmioty = {selected_items_func}")

#Zad5.

# #def procedural_task_scheduling(tasks):
#     tasks.sort(key=lambda x: x['end'])
#
#     max_reward = 0
#     last_end_time = 0
#     selected_tasks = []
#
#     for task in tasks:
#         if task['start'] >= last_end_time:
#             selected_tasks.append(task)
#             max_reward += task['reward']
#             last_end_time = task['end']
#
#     return max_reward, selected_tasks
#
#
# def functional_task_scheduling(tasks):
#     sorted_tasks = sorted(tasks, key=lambda x: x['end'])
#
#     def select_tasks(remaining_tasks, last_end_time, selected_tasks):
#         if not remaining_tasks:
#             return selected_tasks, 0
#
#         current_task = remaining_tasks[0]
#         if current_task['start'] >= last_end_time:
#             new_selected_tasks = selected_tasks + [current_task]
#             new_last_end_time = current_task['end']
#             remaining_tasks = remaining_tasks[1:]
#             selected_tasks, reward = select_tasks(remaining_tasks, new_last_end_time, new_selected_tasks)
#             return selected_tasks, reward + current_task['reward']
#         else:
#             remaining_tasks = remaining_tasks[1:]
#             return select_tasks(remaining_tasks, last_end_time, selected_tasks)
#
#     optimal_tasks, total_reward = select_tasks(sorted_tasks, 0, [])
#     return total_reward, optimal_tasks
#
#
# tasks = [
#     {'task': 'Task 1', 'start': 1, 'end': 3, 'reward': 100},
#     {'task': 'Task 2', 'start': 2, 'end': 5, 'reward': 200},
#     {'task': 'Task 3', 'start': 4, 'end': 6, 'reward': 150},
#     {'task': 'Task 4', 'start': 5, 'end': 7, 'reward': 80},
#     {'task': 'Task 5', 'start': 3, 'end': 9, 'reward': 300},
# ]
#
# max_reward, selected_tasks = procedural_task_scheduling(tasks)
# print("Proceduralna maksymalna nagroda:", max_reward)
# print("Proceduralny harmonogram zadań:", [t['task'] for t in selected_tasks])
#
# max_reward_func, selected_tasks_func = functional_task_scheduling(tasks)
# print("Funkcyjna maksymalna nagroda:", max_reward_func)
# print("Funkcyjny harmonogram zadań:", [t['task'] for t in selected_tasks_func])