def merge_lists(my_list, alices_list):
  # Combine the sorted lists into one large sorted list
  # This will be similar to some sorting approach: take a single
  # number from a list and compare it with an item in second list.
  # Maintain cursor to both lists
  n_me = len(my_list)
  n_al = len(alices_list)
  # If my list is empty then just return alices
  if n_me == 0:
    return alices_list
  # If alices list is empty then just return mine
  elif n_al == 0:
    return my_list
  # try to merge
  else:
    merged = []
    i_al = 0
    i_me = 0
    # Run through all my orders
    while i_me < n_me:
      # if alices list is empty, return currently merged and what is left in mine
      if i_al == n_al:
        return merged + my_list[i_me:n_me]
      # add order from my list if it is smaller; and increase cursor to my orders
      if my_list[i_me] < alices_list[i_al]:
        merged.append(my_list[i_me])
        i_me += 1
      # add alices otherwise; and increase cursor to her orders
      else:
        merged.append(alices_list[i_al])
        i_al += 1
    # Return merged and if something is left from alices
    return merged + alices_list[i_al:n_al]

print(merge_lists([2,4,5,6],[1,3,7,8,9]))