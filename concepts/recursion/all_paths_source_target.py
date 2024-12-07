def find_all_paths(p, path_list, node, result):
    if node == len(path_list)-1:
        result.append(p[:])
        return

    for next_node in path_list[node]:
        p.append(next_node)
        find_all_paths(p, path_list, next_node, result)
        p.pop()
    return result

print(find_all_paths([0], [[1,2],[3],[3],[]],0,[]))




