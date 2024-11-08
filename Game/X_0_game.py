g = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"""
             {g[0]} | {g[1]} | {g[2]} 
            -----------
             {g[3]} | {g[4]} | {g[5]}
            -----------
             {g[6]} | {g[7]} | {g[8]} 
"""
      )

while True:

    x = int(input('X = '))
    g[x - 1] = 'X'
    print(f"""
                 {g[0]} | {g[1]} | {g[2]} 
                -----------
                 {g[3]} | {g[4]} | {g[5]}
                -----------
                 {g[6]} | {g[7]} | {g[8]} 
    """
          )
    if g[0] == g[1] and g[1] == g[2] or g[3] == g[4] and g[4] == g[5] or g[6] == g[7] and g[7] == g[8] or g[0] == g[
        3] and g[3] == g[6] or g[1] == g[4] and g[4] == g[7] or g[2] == g[5] and g[5] == g[8] or g[0] == g[4] and g[
        4] == g[8] or g[2] == g[4] and g[4] == g[6]:
        print('X yutdi!')
        break
    o = int(input('0 = '))
    g[o - 1] = 'O'
    print(f"""
                 {g[0]} | {g[1]} | {g[2]} 
                -----------
                 {g[3]} | {g[4]} | {g[5]}
                -----------
                 {g[6]} | {g[7]} | {g[8]} 
    """
          )
    if g[0] == g[1] and g[1] == g[2] or g[3] == g[4] and g[4] == g[5] or g[6] == g[7] and g[7] == g[8] or g[0] == g[
        3] and g[3] == g[6] or g[1] == g[4] and g[4] == g[7] or g[2] == g[5] and g[5] == g[8] or g[0] == g[4] and g[
        4] == g[8] or g[2] == g[4] and g[4] == g[6]:
        print('0 yutdi!')
        break
